# Universally Unique Identifier Service (UUID)

**Basic features**
* Is based on hardware and software unique information.
* Supports Windows/Linux/Mac
* Depends on _(gets information from):_
  * WMI:<br>_Windows Management Instrumentation is the infrastructure for management data and operations on
Windows-based operating systems. You can write WMI scripts or applications to automate administrative tasks
on remote computers but WMI also supplies management data to other parts of the operating system and products,
for example System Center Operations Manager, formerly Microsoft Operations Manager (MOM),
or Windows Remote Management (WinRM). WMI is fully supported by Microsoft.
<br>The WMI command-line (WMIC) utility provides a command-line interface for WMI.
WMIC is compatible with existing shells and utility commands.
<br>[More about WMIC](https://msdn.microsoft.com/en-us/library/aa394531(v=vs.85).aspx)_
  * Linux dmesg _(display/driver message utility)_
* Information is being gathered without admin/root rights
* Information is being encoded with [SHA224](https://docs.python.org/2/library/hashlib.html) algorithm.

**Public API**

```python
import identifier

identifier.get_encrypted_id()
identifier.get_raw_id()
```

**Execution example**

```bash
### Windows output:
uuid> python -c 'import identifier; id = identifier.get_encrypted_id(); print id'
uuid> 8e34ecad5020a9b0407d8540053eebf2930ef91bc865dd97f7bc516a

### Linux output:
uuid$ python -c 'import identifier; id = identifier.get_encrypted_id(); print id'
uuid$ 52fce38ea6cb88894b004e89c9f9b7697e1371d9c223fc44367e3e5a

### Windows output with a debug info:
uuid>python identifier.py
reader: ['ProcessorId=078BFBFF00020FC2']
reader: ['UUID=FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF']
reader: ['Name=AMD Athlon(tm) 64 Processor 3000+']
reader: ['Product=K8T800-8237']
reader: ['Version=VIAK8  - 42302e31']
reader: ['TotalPhysicalMemory=1610039296']
info:   [078BFBFF00020FC2FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFFAMD Athlon(tm) 64 Processor 3000+K8T800-8237VIAK8  - 42302e311610039296]
result: [8e34ecad5020a9b0407d8540053eebf2930ef91bc865dd97f7bc516a]


### Linux output with a debug info:
uuid$ python identifier.py
reader: ['1821fbaf-59ff-4908-99c1-87572edf11f2']
reader: ['ASUS All Series/H87-PLUS, BIOS 0607 09/17/2013']
reader: ['Embedded 33 pages/cpu @ffff88021fa00000 s98008 r8192 d28968 u524288']
reader: ['7827724K/8061156K available (8188K kernel code, 1292K rwdata, 3964K rodata, 1488K init, 1292K bss, 233432K
          reserved, 0K cma-reserved)']
reader: ['Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz (family: 0x6, model: 0x3c, stepping: 0x3)']
info:   [1821fbaf-59ff-4908-99c1-87572edf11f2ASUS All Series/H87-PLUS, BIOS 0607 09/17/2013Embedded 33 pages/cpu
         @ffff88021fa00000 s98008 r8192 d28968 u5242887827724K/8061156K available (8188K kernel code, 1292K rwdata, 3964K
         rodata, 1488K init, 1292K bss, 233432K reserved, 0K cma-reserved)Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz
         (family: 0x6, model: 0x3c, stepping: 0x3)]
result: [52fce38ea6cb88894b004e89c9f9b7697e1371d9c223fc44367e3e5a]
```