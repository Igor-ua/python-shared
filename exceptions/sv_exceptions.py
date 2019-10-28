# ---------------------------------------------------------------------------
#           Name: sv_exceptions.py
#    Description: utility for catching and formatting exception messages
# ---------------------------------------------------------------------------


import sys
import traceback
import datetime


last_exception = {'file': '', 'line': '', 'traceback_msg': ''}


class ExceptionData:
    # Example: a = 1 / 0
    def __init__(self):
        self.exception = {'file': '', 'line': '', 'traceback_msg': ''}
        try:
            # exception_type:       <class 'ZeroDivisionError'>
            # exception_value:      division by zero
            # exception_traceback:  <traceback object at 0x7f5ff5c55088>
            exception_type, exception_value, exception_traceback = sys.exc_info()

            # [
            #   'Traceback (most recent call last):',
            #   '  File "/../../python/sv_exceptions.py", line 95, in <module>',
            #   '    a = 1 / 0',
            #   'ZeroDivisionError: division by zero'
            # ]
            exception_info = traceback.format_exc().splitlines()

            # [
            # split:
            #   '  File "/../../python/sv_exceptions.py"',
            #   ' line 109',
            #   ' in <module>',
            # append:
            #   '    a = 1 / 0'
            # ]
            root_info = []
            if len(exception_info) > 1:
                root_info = str(exception_info[1]).split(",")
            if len(exception_info) > 2:
                root_info.append(exception_info[2])

            # [
            #   'File "/../../python/sv_exceptions.py"',
            #   'line 109',
            #   'in <module>',
            #   'a = 1 / 0'
            # ]
            for index in range(0, 4):
                if len(root_info) <= index:
                    root_info.append("<empty>")
                else:
                    root_info[index] = root_info[index].strip()

            # ['sv_exceptions.py', 'line 130', 'in <module>', 'a = 1 / 0']
            root_info[0] = root_info[0].split("/")[-1].replace("\"", "")

            # file: [sv_exceptions.py], method: test()
            top_file_name = str(exception_traceback.tb_frame.f_code.co_filename).split("/")[-1]
            top_method_name = str(exception_traceback.tb_frame.f_code.co_name)
            del (exception_type, exception_value, exception_traceback)

            # 2019.10.10 - 22:45:21
            exception_timestamp = datetime.datetime.now().strftime("%Y.%m.%d - %H:%M:%S")

            # 2019.10.10 - 22:45:21:
            #   Top:  file: [sv_exceptions.py], method: test()
            #   Root: file: [sv_exceptions.py], line 110, cause: in test [a = 1 / 0]
            #   ZeroDivisionError: division by zero
            traceback_msg = '\n%s:\n' % exception_timestamp
            traceback_msg += "  Top:  file: [%s], method: %s()\n" % (top_file_name, top_method_name)
            traceback_msg += "  Root: file: [%s], %s, cause: %s [%s]\n" % \
                             (root_info[0], root_info[1], root_info[2], root_info[3])
            traceback_msg += "  " + exception_info[-1] + "\n"

            self.exception['file'] = root_info[0]
            self.exception['line'] = root_info[1]
            self.exception['traceback_msg'] = traceback_msg

        except:
            self.exception['traceback_msg'] = "\nError in resolving exception\n" + traceback.format_exc() + "\n"

    def get_exception(self):
        return self.exception

    def __str__(self):
        return self.exception['traceback_msg']


def get_and_log_exception_info():
    exception = ExceptionData().get_exception()

    global last_exception
    # Escape logging of the same exceptions that can happen inside the loops
    if not (last_exception["file"] == exception['file'] and last_exception["line"] == exception['line']):
        last_exception['traceback_msg'] = exception['traceback_msg']
        last_exception["file"] = exception['file']
        last_exception["line"] = exception['line']

        # Final result:
        #
        # 2019.10.10 - 22:45:21:
        #   Top:  file: [sv_exceptions.py], method: test()
        #   Root: file: [sv_exceptions.py], line 110, cause: in test [a = 1 / 0]
        #   ZeroDivisionError: division by zero
        print(last_exception['traceback_msg'])
