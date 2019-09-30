# Identifier.py
#
# A service that provides universally unique identifier (UUID) for different OS
# UUID is based on hardware and software unique information.
#
# python 2.7


# === Imports ==========================================================================================================
import platform
import hashlib
import uuid
import sys
from subprocess import check_output

# === Variables ========================================================================================================
OS_NAME = {'Windows': 1, 'Linux': 2, 'Darwin': 3}
show_debug = False


# === Public ===========================================================================================================

# Returns an id as an encrypted String
def get_encrypted_id():
    return encode_info(get_info_from_os())


# Returns an id as a concatenated String from the collected sources
def get_raw_id():
    return get_info_from_os()


# === Private ==========================================================================================================
def define_os():
    return OS_NAME[platform.system()]


def get_info_from_os():
    info = ''
    if define_os() == 1:
        info = get_info_from_windows()
    elif define_os() == 2:
        info = get_info_from_linux()
    elif define_os() == 3:
        info = get_info_from_mac()
    if info == '':
        info = get_simple_uuid()
    if show_debug:
        print 'info: [%s]' % info
    return info


# Notice: information is being gathered without admin/root rights
def get_info_from_windows():
    """
    Note:
    Windows Management Instrumentation
    Windows Management Instrumentation (WMI) is the infrastructure for management data and operations on
    Windows-based operating systems. You can write WMI scripts or applications to automate administrative tasks
    on remote computers but WMI also supplies management data to other parts of the operating system and products,
    for example System Center Operations Manager, formerly Microsoft Operations Manager (MOM),
    or Windows Remote Management (WinRM). WMI is fully supported by Microsoft.

    The WMI command-line (WMIC) utility provides a command-line interface for WMI.
    WMIC is compatible with existing shells and utility commands.
    More about WMIC is here:
    https://msdn.microsoft.com/en-us/library/aa394531(v=vs.85).aspx
    """
    info = ''
    template = 'WMIC /FAILFAST:ON /LOCALE:MS_409'
    template_flags = '/VALUE'
    # Note: raw: key=value; parse: value
    # raw: ProcessorId=078BFBFF00020FC2
    info += parse_wmic_output(query_reader('%s cpu get ProcessorId %s' % (template, template_flags)))
    # raw: UUID=14E248AF-1DD9-3248-B3B5-228AB1C771B6
    # Note: Could have this value: UUID=FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF
    info += parse_wmic_output(query_reader('%s CSPRODUCT get UUID %s' %
                                           (template, template_flags)))
    # raw: Name=AMD Athlon(tm) 64 Processor 3000+
    info += parse_wmic_output(query_reader('%s CPU get Name %s' % (template, template_flags)))
    # raw: Product=K8T800-8237
    info += parse_wmic_output(query_reader('%s BASEBOARD get Product %s' % (template, template_flags)))
    # raw: Version=VIAK8 - 42303e31
    info += parse_wmic_output(query_reader('%s BIOS get Version %s' % (template, template_flags)))
    # raw: TotalPhysicalMemory=1610039296
    info += parse_wmic_output(query_reader('%s ComputerSystem get TotalPhysicalMemory %s' % (template, template_flags)))
    return info


# Notice: information is being gathered without admin/root rights
def get_info_from_linux():
    info = ''
    # raw: [    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-45-generic
    #                     root=UUID=1821fbaf-59ff-4908-99c1-87572edf11f2 ro quiet splash
    # parsed: 1821fbaf-59ff-4908-99c1-87572edf11f2
    info += query_reader('dmesg | grep UUID | grep "Kernel" | sed "s/.*UUID=//g" | sed "s/\ ro\ quiet.*//g"')
    # raw: [    0.000000] DMI: ASUS All Series/H87-PLUS, BIOS 0607 09/17/2013
    # parsed: ASUS All Series/H87-PLUS, BIOS 0607 09/17/2013
    info += query_reader('dmesg | grep " DMI:" | sed "s/.*DMI: //g"')
    # raw: [    0.000000] PERCPU: Embedded 33 pages/cpu @ffff88021fa00000 s98008 r8192 d28968 u524288
    # parsed: Embedded 33 pages/cpu @ffff88021fa00000 s98008 r8192 d28968 u524288
    info += query_reader('dmesg | grep " PERCPU:" | sed "s/.*PERCPU: //g"')
    # raw: [    0.000000] Memory: 7827724K/8061156K available (8188K kernel code, 1292K rwdata, 3964K rodata,
    #                     1488K init, 1292K bss, 233432K reserved, 0K cma-reserved)
    # parsed: 7827724K/8061156K available (8188K kernel code, 1292K rwdata, 3964K rodata, 1488K init, 1292K bss,
    #          233432K reserved, 0K cma-reserved)
    info += query_reader('dmesg | grep " Memory:" | sed "s/.*Memory: //g"')
    # [    0.065018] smpboot: CPU0: Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz (family: 0x6, model: 0x3c, stepping: 0x3)
    info += query_reader('dmesg | grep " smpboot: CPU0:" | sed "s/.*smpboot: CPU0: //g"')
    return info


def get_info_from_mac():
    # Since dmesg is also available on mac
    return get_info_from_linux


def encode_info(info):
    # doc: https://docs.python.org/2/library/hashlib.html
    # Possible algorithms md5, sha1, sha224, sha256, sha384, sha512
    return hashlib.sha224(info).hexdigest()


# Returns default python's uuid as a String.
# Supposed to be called if the native methods will not work by the unknown reason.
def get_simple_uuid():
    # doc: https://docs.python.org/2/library/uuid.html
    # makes a UUID using a SHA-1 hash of a namespace UUID and a name
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, 'newerth.com'))


def parse_wmic_output(text):
    info = ''
    try:
        parsed = text.splitlines()
        # Remove blank lines from the array
        parsed = filter(None, parsed)
        # key/value
        kv = parsed[0].split('=')
        info = kv[1]
    except:
        pass
    return info


# Tries to get an info. Returns blank string if it fails
def query_reader(query):
    info = ''
    try:
        parsed = check_output(query, shell=True).splitlines()
        # Remove blank lines from the array
        parsed = filter(None, parsed)
        if show_debug:
            print ('reader: %s' % parsed)
        info = parsed[0]
    except:
        print sys.exc_info()
    return info

if __name__ == '__main__':
    show_debug = True
    print 'result: [%s]\n' % get_encrypted_id()
