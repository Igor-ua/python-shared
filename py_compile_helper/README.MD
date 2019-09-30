## PY_COMPILE_HELPER

This module is supposed to help with the compilation of all python modules with their actual names.

**Why?**
- Python has no tool that is able to compile, rename and compress all modules including their structure into a separate location 
- Python compileall module does the job but you receive modules including python version with py_cache folders inside the modules

**With py_compile_helper you can:**
- Set input and output folder for the compilation
- Output source will have the same structure as the input source
- Set optimization level for binary files
- Skip or include test modules
- Compress compiled files into one archive
- Clean previously compiled files from the cache    

**Examples (Ubuntu x64):**

Launching without any arguments
```
$ ./py_compile_helper.py 
usage: py_compile_helper.py [-h] [-o OPTIMIZE] [-i] [-z] [-c] input output
py_compile_helper.py: error: the following arguments are required: input, output
```

Listing --help information:
```
$ ./py_compile_helper.py --help
usage: py_compile_helper.py [-h] [-o OPTIMIZE] [-i] [-z] [-c] input output

A helper for recursive compilation of python modules

positional arguments:
  input                 input folder that must be compiled
  output                output folder to save compiled files

optional arguments:
  -h, --help            show this help message and exit
  -o OPTIMIZE, --optimize OPTIMIZE
                        optimization level: -1,0,1,2 for py_compile.compile()
  -i, --include         include the compilation of tests
  -z, --zip             add compiled files to zip archive
  -c, --clean           cleans cache by py3clean in the source folder
```

Successful compilation (output folder: ./out, default zip archive: python-compiled.zip):
```
$ ./py_compile_helper.py ./Python-3.7.1/Lib ./out -z -c -o2
The compilation of the test modules will be skipped. Use -i flag to include tests in case of necessity.
Input location: ./Python-3.7.1/Lib/, output location: ./out/
Compile optimization level: 2

Module: root, files: 171 ()
compile:  ./Python-3.7.1/Lib/doctest.py ---> ./out/doctest.pyc
compile:  ./Python-3.7.1/Lib/pathlib.py ---> ./out/pathlib.pyc
compile:  ./Python-3.7.1/Lib/dis.py ---> ./out/dis.pyc
compile:  ./Python-3.7.1/Lib/_py_abc.py ---> ./out/_py_abc.pyc
compile:  ./Python-3.7.1/Lib/_dummy_thread.py ---> ./out/_dummy_thread.pyc
compile:  ./Python-3.7.1/Lib/uuid.py ---> ./out/uuid.pyc
compile:  ./Python-3.7.1/Lib/cgitb.py ---> ./out/cgitb.pyc
compile:  ./Python-3.7.1/Lib/cmd.py ---> ./out/cmd.pyc
compile:  ./Python-3.7.1/Lib/pickletools.py ---> ./out/pickletools.pyc
compile:  ./Python-3.7.1/Lib/mailcap.py ---> ./out/mailcap.pyc
compile:  ./Python-3.7.1/Lib/quopri.py ---> ./out/quopri.pyc
compile:  ./Python-3.7.1/Lib/typing.py ---> ./out/typing.pyc
compile:  ./Python-3.7.1/Lib/asyncore.py ---> ./out/asyncore.pyc
compile:  ./Python-3.7.1/Lib/stringprep.py ---> ./out/stringprep.pyc
compile:  ./Python-3.7.1/Lib/functools.py ---> ./out/functools.pyc
compile:  ./Python-3.7.1/Lib/colorsys.py ---> ./out/colorsys.pyc
compile:  ./Python-3.7.1/Lib/poplib.py ---> ./out/poplib.pyc
compile:  ./Python-3.7.1/Lib/statistics.py ---> ./out/statistics.pyc
compile:  ./Python-3.7.1/Lib/sre_parse.py ---> ./out/sre_parse.pyc
compile:  ./Python-3.7.1/Lib/os.py ---> ./out/os.pyc
compile:  ./Python-3.7.1/Lib/shlex.py ---> ./out/shlex.pyc
compile:  ./Python-3.7.1/Lib/struct.py ---> ./out/struct.pyc
compile:  ./Python-3.7.1/Lib/tarfile.py ---> ./out/tarfile.pyc
compile:  ./Python-3.7.1/Lib/copyreg.py ---> ./out/copyreg.pyc
compile:  ./Python-3.7.1/Lib/compileall.py ---> ./out/compileall.pyc
compile:  ./Python-3.7.1/Lib/rlcompleter.py ---> ./out/rlcompleter.pyc
compile:  ./Python-3.7.1/Lib/bisect.py ---> ./out/bisect.pyc
compile:  ./Python-3.7.1/Lib/shutil.py ---> ./out/shutil.pyc
compile:  ./Python-3.7.1/Lib/_collections_abc.py ---> ./out/_collections_abc.pyc
compile:  ./Python-3.7.1/Lib/argparse.py ---> ./out/argparse.pyc
compile:  ./Python-3.7.1/Lib/_pyio.py ---> ./out/_pyio.pyc
compile:  ./Python-3.7.1/Lib/ntpath.py ---> ./out/ntpath.pyc
compile:  ./Python-3.7.1/Lib/ftplib.py ---> ./out/ftplib.pyc
compile:  ./Python-3.7.1/Lib/profile.py ---> ./out/profile.pyc
compile:  ./Python-3.7.1/Lib/_compat_pickle.py ---> ./out/_compat_pickle.pyc
compile:  ./Python-3.7.1/Lib/nturl2path.py ---> ./out/nturl2path.pyc
compile:  ./Python-3.7.1/Lib/_sitebuiltins.py ---> ./out/_sitebuiltins.pyc
compile:  ./Python-3.7.1/Lib/traceback.py ---> ./out/traceback.pyc
compile:  ./Python-3.7.1/Lib/imaplib.py ---> ./out/imaplib.pyc
compile:  ./Python-3.7.1/Lib/datetime.py ---> ./out/datetime.pyc
compile:  ./Python-3.7.1/Lib/smtplib.py ---> ./out/smtplib.pyc
compile:  ./Python-3.7.1/Lib/sched.py ---> ./out/sched.pyc
compile:  ./Python-3.7.1/Lib/dataclasses.py ---> ./out/dataclasses.pyc
compile:  ./Python-3.7.1/Lib/copy.py ---> ./out/copy.pyc
compile:  ./Python-3.7.1/Lib/enum.py ---> ./out/enum.pyc
compile:  ./Python-3.7.1/Lib/platform.py ---> ./out/platform.pyc
compile:  ./Python-3.7.1/Lib/tty.py ---> ./out/tty.pyc
compile:  ./Python-3.7.1/Lib/antigravity.py ---> ./out/antigravity.pyc
compile:  ./Python-3.7.1/Lib/getpass.py ---> ./out/getpass.pyc
compile:  ./Python-3.7.1/Lib/_compression.py ---> ./out/_compression.pyc
compile:  ./Python-3.7.1/Lib/smtpd.py ---> ./out/smtpd.pyc
compile:  ./Python-3.7.1/Lib/trace.py ---> ./out/trace.pyc
compile:  ./Python-3.7.1/Lib/hmac.py ---> ./out/hmac.pyc
compile:  ./Python-3.7.1/Lib/posixpath.py ---> ./out/posixpath.pyc
compile:  ./Python-3.7.1/Lib/sysconfig.py ---> ./out/sysconfig.pyc
compile:  ./Python-3.7.1/Lib/mailbox.py ---> ./out/mailbox.pyc
compile:  ./Python-3.7.1/Lib/imp.py ---> ./out/imp.pyc
compile:  ./Python-3.7.1/Lib/symbol.py ---> ./out/symbol.pyc
compile:  ./Python-3.7.1/Lib/decimal.py ---> ./out/decimal.pyc
compile:  ./Python-3.7.1/Lib/uu.py ---> ./out/uu.pyc
compile:  ./Python-3.7.1/Lib/sre_compile.py ---> ./out/sre_compile.pyc
compile:  ./Python-3.7.1/Lib/dummy_threading.py ---> ./out/dummy_threading.pyc
compile:  ./Python-3.7.1/Lib/fnmatch.py ---> ./out/fnmatch.pyc
compile:  ./Python-3.7.1/Lib/warnings.py ---> ./out/warnings.pyc
compile:  ./Python-3.7.1/Lib/calendar.py ---> ./out/calendar.pyc
compile:  ./Python-3.7.1/Lib/gzip.py ---> ./out/gzip.pyc
compile:  ./Python-3.7.1/Lib/contextlib.py ---> ./out/contextlib.pyc
compile:  ./Python-3.7.1/Lib/crypt.py ---> ./out/crypt.pyc
compile:  ./Python-3.7.1/Lib/cProfile.py ---> ./out/cProfile.pyc
compile:  ./Python-3.7.1/Lib/cgi.py ---> ./out/cgi.pyc
compile:  ./Python-3.7.1/Lib/threading.py ---> ./out/threading.pyc
compile:  ./Python-3.7.1/Lib/reprlib.py ---> ./out/reprlib.pyc
compile:  ./Python-3.7.1/Lib/zipfile.py ---> ./out/zipfile.pyc
compile:  ./Python-3.7.1/Lib/gettext.py ---> ./out/gettext.pyc
compile:  ./Python-3.7.1/Lib/hashlib.py ---> ./out/hashlib.pyc
compile:  ./Python-3.7.1/Lib/fileinput.py ---> ./out/fileinput.pyc
compile:  ./Python-3.7.1/Lib/opcode.py ---> ./out/opcode.pyc
compile:  ./Python-3.7.1/Lib/base64.py ---> ./out/base64.pyc
compile:  ./Python-3.7.1/Lib/formatter.py ---> ./out/formatter.pyc
compile:  ./Python-3.7.1/Lib/runpy.py ---> ./out/runpy.pyc
compile:  ./Python-3.7.1/Lib/locale.py ---> ./out/locale.pyc
compile:  ./Python-3.7.1/Lib/filecmp.py ---> ./out/filecmp.pyc
compile:  ./Python-3.7.1/Lib/difflib.py ---> ./out/difflib.pyc
compile:  ./Python-3.7.1/Lib/__phello__.foo.py ---> ./out/__phello__.foo.pyc
compile:  ./Python-3.7.1/Lib/aifc.py ---> ./out/aifc.pyc
compile:  ./Python-3.7.1/Lib/pickle.py ---> ./out/pickle.pyc
compile:  ./Python-3.7.1/Lib/symtable.py ---> ./out/symtable.pyc
compile:  ./Python-3.7.1/Lib/macpath.py ---> ./out/macpath.pyc
compile:  ./Python-3.7.1/Lib/lzma.py ---> ./out/lzma.pyc
compile:  ./Python-3.7.1/Lib/operator.py ---> ./out/operator.pyc
compile:  ./Python-3.7.1/Lib/numbers.py ---> ./out/numbers.pyc
compile:  ./Python-3.7.1/Lib/codecs.py ---> ./out/codecs.pyc
compile:  ./Python-3.7.1/Lib/imghdr.py ---> ./out/imghdr.pyc
compile:  ./Python-3.7.1/Lib/selectors.py ---> ./out/selectors.pyc
compile:  ./Python-3.7.1/Lib/types.py ---> ./out/types.pyc
compile:  ./Python-3.7.1/Lib/heapq.py ---> ./out/heapq.pyc
compile:  ./Python-3.7.1/Lib/socket.py ---> ./out/socket.pyc
compile:  ./Python-3.7.1/Lib/_weakrefset.py ---> ./out/_weakrefset.pyc
compile:  ./Python-3.7.1/Lib/glob.py ---> ./out/glob.pyc
compile:  ./Python-3.7.1/Lib/genericpath.py ---> ./out/genericpath.pyc
compile:  ./Python-3.7.1/Lib/keyword.py ---> ./out/keyword.pyc
compile:  ./Python-3.7.1/Lib/bdb.py ---> ./out/bdb.pyc
compile:  ./Python-3.7.1/Lib/stat.py ---> ./out/stat.pyc
compile:  ./Python-3.7.1/Lib/netrc.py ---> ./out/netrc.pyc
compile:  ./Python-3.7.1/Lib/tokenize.py ---> ./out/tokenize.pyc
compile:  ./Python-3.7.1/Lib/_bootlocale.py ---> ./out/_bootlocale.pyc
compile:  ./Python-3.7.1/Lib/zipapp.py ---> ./out/zipapp.pyc
compile:  ./Python-3.7.1/Lib/sre_constants.py ---> ./out/sre_constants.pyc
compile:  ./Python-3.7.1/Lib/wave.py ---> ./out/wave.pyc
compile:  ./Python-3.7.1/Lib/string.py ---> ./out/string.pyc
compile:  ./Python-3.7.1/Lib/io.py ---> ./out/io.pyc
compile:  ./Python-3.7.1/Lib/modulefinder.py ---> ./out/modulefinder.pyc
compile:  ./Python-3.7.1/Lib/pty.py ---> ./out/pty.pyc
compile:  ./Python-3.7.1/Lib/__future__.py ---> ./out/__future__.pyc
compile:  ./Python-3.7.1/Lib/_pydecimal.py ---> ./out/_pydecimal.pyc
compile:  ./Python-3.7.1/Lib/telnetlib.py ---> ./out/telnetlib.pyc
compile:  ./Python-3.7.1/Lib/secrets.py ---> ./out/secrets.pyc
compile:  ./Python-3.7.1/Lib/signal.py ---> ./out/signal.pyc
compile:  ./Python-3.7.1/Lib/weakref.py ---> ./out/weakref.pyc
compile:  ./Python-3.7.1/Lib/pipes.py ---> ./out/pipes.pyc
compile:  ./Python-3.7.1/Lib/ast.py ---> ./out/ast.pyc
compile:  ./Python-3.7.1/Lib/ssl.py ---> ./out/ssl.pyc
compile:  ./Python-3.7.1/Lib/contextvars.py ---> ./out/contextvars.pyc
compile:  ./Python-3.7.1/Lib/mimetypes.py ---> ./out/mimetypes.pyc
compile:  ./Python-3.7.1/Lib/shelve.py ---> ./out/shelve.pyc
compile:  ./Python-3.7.1/Lib/pydoc.py ---> ./out/pydoc.pyc
compile:  ./Python-3.7.1/Lib/fractions.py ---> ./out/fractions.pyc
compile:  ./Python-3.7.1/Lib/abc.py ---> ./out/abc.pyc
compile:  ./Python-3.7.1/Lib/token.py ---> ./out/token.pyc
compile:  ./Python-3.7.1/Lib/turtle.py ---> ./out/turtle.pyc
compile:  ./Python-3.7.1/Lib/tabnanny.py ---> ./out/tabnanny.pyc
compile:  ./Python-3.7.1/Lib/xdrlib.py ---> ./out/xdrlib.pyc
compile:  ./Python-3.7.1/Lib/subprocess.py ---> ./out/subprocess.pyc
compile:  ./Python-3.7.1/Lib/linecache.py ---> ./out/linecache.pyc
compile:  ./Python-3.7.1/Lib/socketserver.py ---> ./out/socketserver.pyc
compile:  ./Python-3.7.1/Lib/_osx_support.py ---> ./out/_osx_support.pyc
compile:  ./Python-3.7.1/Lib/tempfile.py ---> ./out/tempfile.pyc
compile:  ./Python-3.7.1/Lib/site.py ---> ./out/site.pyc
compile:  ./Python-3.7.1/Lib/codeop.py ---> ./out/codeop.pyc
compile:  ./Python-3.7.1/Lib/asynchat.py ---> ./out/asynchat.pyc
compile:  ./Python-3.7.1/Lib/inspect.py ---> ./out/inspect.pyc
compile:  ./Python-3.7.1/Lib/sndhdr.py ---> ./out/sndhdr.pyc
compile:  ./Python-3.7.1/Lib/chunk.py ---> ./out/chunk.pyc
compile:  ./Python-3.7.1/Lib/pprint.py ---> ./out/pprint.pyc
compile:  ./Python-3.7.1/Lib/plistlib.py ---> ./out/plistlib.pyc
compile:  ./Python-3.7.1/Lib/py_compile.py ---> ./out/py_compile.pyc
compile:  ./Python-3.7.1/Lib/nntplib.py ---> ./out/nntplib.pyc
compile:  ./Python-3.7.1/Lib/pyclbr.py ---> ./out/pyclbr.pyc
compile:  ./Python-3.7.1/Lib/configparser.py ---> ./out/configparser.pyc
compile:  ./Python-3.7.1/Lib/csv.py ---> ./out/csv.pyc
compile:  ./Python-3.7.1/Lib/pstats.py ---> ./out/pstats.pyc
compile:  ./Python-3.7.1/Lib/webbrowser.py ---> ./out/webbrowser.pyc
compile:  ./Python-3.7.1/Lib/pkgutil.py ---> ./out/pkgutil.pyc
compile:  ./Python-3.7.1/Lib/getopt.py ---> ./out/getopt.pyc
compile:  ./Python-3.7.1/Lib/optparse.py ---> ./out/optparse.pyc
compile:  ./Python-3.7.1/Lib/re.py ---> ./out/re.pyc
compile:  ./Python-3.7.1/Lib/_strptime.py ---> ./out/_strptime.pyc
compile:  ./Python-3.7.1/Lib/binhex.py ---> ./out/binhex.pyc
compile:  ./Python-3.7.1/Lib/ipaddress.py ---> ./out/ipaddress.pyc
compile:  ./Python-3.7.1/Lib/queue.py ---> ./out/queue.pyc
compile:  ./Python-3.7.1/Lib/bz2.py ---> ./out/bz2.pyc
compile:  ./Python-3.7.1/Lib/this.py ---> ./out/this.pyc
compile:  ./Python-3.7.1/Lib/random.py ---> ./out/random.pyc
compile:  ./Python-3.7.1/Lib/pdb.py ---> ./out/pdb.pyc
compile:  ./Python-3.7.1/Lib/textwrap.py ---> ./out/textwrap.pyc
compile:  ./Python-3.7.1/Lib/code.py ---> ./out/code.pyc
compile:  ./Python-3.7.1/Lib/_markupbase.py ---> ./out/_markupbase.pyc
compile:  ./Python-3.7.1/Lib/sunau.py ---> ./out/sunau.pyc
compile:  ./Python-3.7.1/Lib/tracemalloc.py ---> ./out/tracemalloc.pyc
compile:  ./Python-3.7.1/Lib/_threading_local.py ---> ./out/_threading_local.pyc
compile:  ./Python-3.7.1/Lib/timeit.py ---> ./out/timeit.pyc

Module: curses, files: 5 (curses)
compile:  ./Python-3.7.1/Lib/curses/has_key.py ---> ./out/curses/has_key.pyc
compile:  ./Python-3.7.1/Lib/curses/panel.py ---> ./out/curses/panel.pyc
compile:  ./Python-3.7.1/Lib/curses/__init__.py ---> ./out/curses/__init__.pyc
compile:  ./Python-3.7.1/Lib/curses/ascii.py ---> ./out/curses/ascii.pyc
compile:  ./Python-3.7.1/Lib/curses/textpad.py ---> ./out/curses/textpad.pyc

Module: wsgiref, files: 6 (wsgiref)
compile:  ./Python-3.7.1/Lib/wsgiref/simple_server.py ---> ./out/wsgiref/simple_server.pyc
compile:  ./Python-3.7.1/Lib/wsgiref/headers.py ---> ./out/wsgiref/headers.pyc
compile:  ./Python-3.7.1/Lib/wsgiref/util.py ---> ./out/wsgiref/util.pyc
compile:  ./Python-3.7.1/Lib/wsgiref/__init__.py ---> ./out/wsgiref/__init__.pyc
compile:  ./Python-3.7.1/Lib/wsgiref/validate.py ---> ./out/wsgiref/validate.pyc
compile:  ./Python-3.7.1/Lib/wsgiref/handlers.py ---> ./out/wsgiref/handlers.pyc

Module: lib2to3, files: 13 (lib2to3)
compile:  ./Python-3.7.1/Lib/lib2to3/main.py ---> ./out/lib2to3/main.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/btm_utils.py ---> ./out/lib2to3/btm_utils.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/__init__.py ---> ./out/lib2to3/__init__.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pygram.py ---> ./out/lib2to3/pygram.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/__main__.py ---> ./out/lib2to3/__main__.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pytree.py ---> ./out/lib2to3/pytree.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/refactor.py ---> ./out/lib2to3/refactor.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixer_util.py ---> ./out/lib2to3/fixer_util.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/btm_matcher.py ---> ./out/lib2to3/btm_matcher.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixer_base.py ---> ./out/lib2to3/fixer_base.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/patcomp.py ---> ./out/lib2to3/patcomp.pyc

Module: fixes, files: 53 (lib2to3/fixes)
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_reload.py ---> ./out/lib2to3/fixes/fix_reload.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_exec.py ---> ./out/lib2to3/fixes/fix_exec.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_buffer.py ---> ./out/lib2to3/fixes/fix_buffer.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_input.py ---> ./out/lib2to3/fixes/fix_input.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_urllib.py ---> ./out/lib2to3/fixes/fix_urllib.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_map.py ---> ./out/lib2to3/fixes/fix_map.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_standarderror.py ---> ./out/lib2to3/fixes/fix_standarderror.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_throw.py ---> ./out/lib2to3/fixes/fix_throw.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_paren.py ---> ./out/lib2to3/fixes/fix_paren.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_zip.py ---> ./out/lib2to3/fixes/fix_zip.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_unicode.py ---> ./out/lib2to3/fixes/fix_unicode.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_isinstance.py ---> ./out/lib2to3/fixes/fix_isinstance.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_apply.py ---> ./out/lib2to3/fixes/fix_apply.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_next.py ---> ./out/lib2to3/fixes/fix_next.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_set_literal.py ---> ./out/lib2to3/fixes/fix_set_literal.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_exitfunc.py ---> ./out/lib2to3/fixes/fix_exitfunc.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_operator.py ---> ./out/lib2to3/fixes/fix_operator.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_imports.py ---> ./out/lib2to3/fixes/fix_imports.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_future.py ---> ./out/lib2to3/fixes/fix_future.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_ws_comma.py ---> ./out/lib2to3/fixes/fix_ws_comma.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_imports2.py ---> ./out/lib2to3/fixes/fix_imports2.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_itertools.py ---> ./out/lib2to3/fixes/fix_itertools.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_types.py ---> ./out/lib2to3/fixes/fix_types.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_ne.py ---> ./out/lib2to3/fixes/fix_ne.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_sys_exc.py ---> ./out/lib2to3/fixes/fix_sys_exc.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/__init__.py ---> ./out/lib2to3/fixes/__init__.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_import.py ---> ./out/lib2to3/fixes/fix_import.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_itertools_imports.py ---> ./out/lib2to3/fixes/fix_itertools_imports.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_asserts.py ---> ./out/lib2to3/fixes/fix_asserts.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_raw_input.py ---> ./out/lib2to3/fixes/fix_raw_input.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_funcattrs.py ---> ./out/lib2to3/fixes/fix_funcattrs.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_raise.py ---> ./out/lib2to3/fixes/fix_raise.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_intern.py ---> ./out/lib2to3/fixes/fix_intern.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_long.py ---> ./out/lib2to3/fixes/fix_long.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_idioms.py ---> ./out/lib2to3/fixes/fix_idioms.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_basestring.py ---> ./out/lib2to3/fixes/fix_basestring.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_xreadlines.py ---> ./out/lib2to3/fixes/fix_xreadlines.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_numliterals.py ---> ./out/lib2to3/fixes/fix_numliterals.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_metaclass.py ---> ./out/lib2to3/fixes/fix_metaclass.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_methodattrs.py ---> ./out/lib2to3/fixes/fix_methodattrs.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_execfile.py ---> ./out/lib2to3/fixes/fix_execfile.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_has_key.py ---> ./out/lib2to3/fixes/fix_has_key.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_nonzero.py ---> ./out/lib2to3/fixes/fix_nonzero.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_xrange.py ---> ./out/lib2to3/fixes/fix_xrange.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_filter.py ---> ./out/lib2to3/fixes/fix_filter.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_print.py ---> ./out/lib2to3/fixes/fix_print.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_tuple_params.py ---> ./out/lib2to3/fixes/fix_tuple_params.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_repr.py ---> ./out/lib2to3/fixes/fix_repr.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_except.py ---> ./out/lib2to3/fixes/fix_except.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_renames.py ---> ./out/lib2to3/fixes/fix_renames.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_getcwdu.py ---> ./out/lib2to3/fixes/fix_getcwdu.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_dict.py ---> ./out/lib2to3/fixes/fix_dict.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/fixes/fix_reduce.py ---> ./out/lib2to3/fixes/fix_reduce.pyc

Module: pgen2, files: 9 (lib2to3/pgen2)
compile:  ./Python-3.7.1/Lib/lib2to3/pgen2/pgen.py ---> ./out/lib2to3/pgen2/pgen.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pgen2/literals.py ---> ./out/lib2to3/pgen2/literals.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pgen2/grammar.py ---> ./out/lib2to3/pgen2/grammar.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pgen2/__init__.py ---> ./out/lib2to3/pgen2/__init__.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pgen2/parse.py ---> ./out/lib2to3/pgen2/parse.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pgen2/driver.py ---> ./out/lib2to3/pgen2/driver.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pgen2/conv.py ---> ./out/lib2to3/pgen2/conv.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pgen2/tokenize.py ---> ./out/lib2to3/pgen2/tokenize.pyc
compile:  ./Python-3.7.1/Lib/lib2to3/pgen2/token.py ---> ./out/lib2to3/pgen2/token.pyc

Module: tests, files: 11 (lib2to3/tests)
skipped

Module: data, files: 8 (lib2to3/tests/data)
skipped

Module: fixers, files: 3 (lib2to3/tests/data/fixers)
skipped

Module: myfixes, files: 6 (lib2to3/tests/data/fixers/myfixes)
skipped

Module: xml, files: 1 (xml)
compile:  ./Python-3.7.1/Lib/xml/__init__.py ---> ./out/xml/__init__.pyc

Module: sax, files: 6 (xml/sax)
compile:  ./Python-3.7.1/Lib/xml/sax/_exceptions.py ---> ./out/xml/sax/_exceptions.pyc
compile:  ./Python-3.7.1/Lib/xml/sax/handler.py ---> ./out/xml/sax/handler.pyc
compile:  ./Python-3.7.1/Lib/xml/sax/__init__.py ---> ./out/xml/sax/__init__.pyc
compile:  ./Python-3.7.1/Lib/xml/sax/xmlreader.py ---> ./out/xml/sax/xmlreader.pyc
compile:  ./Python-3.7.1/Lib/xml/sax/saxutils.py ---> ./out/xml/sax/saxutils.pyc
compile:  ./Python-3.7.1/Lib/xml/sax/expatreader.py ---> ./out/xml/sax/expatreader.pyc

Module: parsers, files: 2 (xml/parsers)
compile:  ./Python-3.7.1/Lib/xml/parsers/__init__.py ---> ./out/xml/parsers/__init__.pyc
compile:  ./Python-3.7.1/Lib/xml/parsers/expat.py ---> ./out/xml/parsers/expat.pyc

Module: etree, files: 5 (xml/etree)
compile:  ./Python-3.7.1/Lib/xml/etree/ElementPath.py ---> ./out/xml/etree/ElementPath.pyc
compile:  ./Python-3.7.1/Lib/xml/etree/ElementInclude.py ---> ./out/xml/etree/ElementInclude.pyc
compile:  ./Python-3.7.1/Lib/xml/etree/__init__.py ---> ./out/xml/etree/__init__.pyc
compile:  ./Python-3.7.1/Lib/xml/etree/ElementTree.py ---> ./out/xml/etree/ElementTree.pyc
compile:  ./Python-3.7.1/Lib/xml/etree/cElementTree.py ---> ./out/xml/etree/cElementTree.pyc

Module: dom, files: 8 (xml/dom)
compile:  ./Python-3.7.1/Lib/xml/dom/expatbuilder.py ---> ./out/xml/dom/expatbuilder.pyc
compile:  ./Python-3.7.1/Lib/xml/dom/minicompat.py ---> ./out/xml/dom/minicompat.pyc
compile:  ./Python-3.7.1/Lib/xml/dom/pulldom.py ---> ./out/xml/dom/pulldom.pyc
compile:  ./Python-3.7.1/Lib/xml/dom/__init__.py ---> ./out/xml/dom/__init__.pyc
compile:  ./Python-3.7.1/Lib/xml/dom/xmlbuilder.py ---> ./out/xml/dom/xmlbuilder.pyc
compile:  ./Python-3.7.1/Lib/xml/dom/minidom.py ---> ./out/xml/dom/minidom.pyc
compile:  ./Python-3.7.1/Lib/xml/dom/NodeFilter.py ---> ./out/xml/dom/NodeFilter.pyc
compile:  ./Python-3.7.1/Lib/xml/dom/domreg.py ---> ./out/xml/dom/domreg.pyc

Module: json, files: 5 (json)
compile:  ./Python-3.7.1/Lib/json/decoder.py ---> ./out/json/decoder.pyc
compile:  ./Python-3.7.1/Lib/json/__init__.py ---> ./out/json/__init__.pyc
compile:  ./Python-3.7.1/Lib/json/scanner.py ---> ./out/json/scanner.pyc
compile:  ./Python-3.7.1/Lib/json/tool.py ---> ./out/json/tool.pyc
compile:  ./Python-3.7.1/Lib/json/encoder.py ---> ./out/json/encoder.pyc

Module: sqlite3, files: 3 (sqlite3)
compile:  ./Python-3.7.1/Lib/sqlite3/dump.py ---> ./out/sqlite3/dump.pyc
compile:  ./Python-3.7.1/Lib/sqlite3/__init__.py ---> ./out/sqlite3/__init__.pyc
compile:  ./Python-3.7.1/Lib/sqlite3/dbapi2.py ---> ./out/sqlite3/dbapi2.pyc

Module: test, files: 10 (sqlite3/test)
skipped

Module: asyncio, files: 25 (asyncio)
compile:  ./Python-3.7.1/Lib/asyncio/constants.py ---> ./out/asyncio/constants.pyc
compile:  ./Python-3.7.1/Lib/asyncio/locks.py ---> ./out/asyncio/locks.pyc
compile:  ./Python-3.7.1/Lib/asyncio/protocols.py ---> ./out/asyncio/protocols.pyc
compile:  ./Python-3.7.1/Lib/asyncio/windows_utils.py ---> ./out/asyncio/windows_utils.pyc
compile:  ./Python-3.7.1/Lib/asyncio/coroutines.py ---> ./out/asyncio/coroutines.pyc
compile:  ./Python-3.7.1/Lib/asyncio/runners.py ---> ./out/asyncio/runners.pyc
compile:  ./Python-3.7.1/Lib/asyncio/unix_events.py ---> ./out/asyncio/unix_events.pyc
compile:  ./Python-3.7.1/Lib/asyncio/format_helpers.py ---> ./out/asyncio/format_helpers.pyc
compile:  ./Python-3.7.1/Lib/asyncio/base_subprocess.py ---> ./out/asyncio/base_subprocess.pyc
compile:  ./Python-3.7.1/Lib/asyncio/proactor_events.py ---> ./out/asyncio/proactor_events.pyc
compile:  ./Python-3.7.1/Lib/asyncio/sslproto.py ---> ./out/asyncio/sslproto.pyc
compile:  ./Python-3.7.1/Lib/asyncio/tasks.py ---> ./out/asyncio/tasks.pyc
compile:  ./Python-3.7.1/Lib/asyncio/events.py ---> ./out/asyncio/events.pyc
compile:  ./Python-3.7.1/Lib/asyncio/__init__.py ---> ./out/asyncio/__init__.pyc
compile:  ./Python-3.7.1/Lib/asyncio/base_tasks.py ---> ./out/asyncio/base_tasks.pyc
compile:  ./Python-3.7.1/Lib/asyncio/futures.py ---> ./out/asyncio/futures.pyc
compile:  ./Python-3.7.1/Lib/asyncio/streams.py ---> ./out/asyncio/streams.pyc
compile:  ./Python-3.7.1/Lib/asyncio/queues.py ---> ./out/asyncio/queues.pyc
compile:  ./Python-3.7.1/Lib/asyncio/transports.py ---> ./out/asyncio/transports.pyc
compile:  ./Python-3.7.1/Lib/asyncio/log.py ---> ./out/asyncio/log.pyc
compile:  ./Python-3.7.1/Lib/asyncio/subprocess.py ---> ./out/asyncio/subprocess.pyc
compile:  ./Python-3.7.1/Lib/asyncio/base_events.py ---> ./out/asyncio/base_events.pyc
compile:  ./Python-3.7.1/Lib/asyncio/selector_events.py ---> ./out/asyncio/selector_events.pyc
compile:  ./Python-3.7.1/Lib/asyncio/windows_events.py ---> ./out/asyncio/windows_events.pyc
compile:  ./Python-3.7.1/Lib/asyncio/base_futures.py ---> ./out/asyncio/base_futures.pyc

Module: ensurepip, files: 3 (ensurepip)
compile:  ./Python-3.7.1/Lib/ensurepip/__init__.py ---> ./out/ensurepip/__init__.pyc
compile:  ./Python-3.7.1/Lib/ensurepip/__main__.py ---> ./out/ensurepip/__main__.pyc
compile:  ./Python-3.7.1/Lib/ensurepip/_uninstall.py ---> ./out/ensurepip/_uninstall.pyc

Module: _bundled, files: 2 (ensurepip/_bundled)

Module: concurrent, files: 1 (concurrent)
compile:  ./Python-3.7.1/Lib/concurrent/__init__.py ---> ./out/concurrent/__init__.pyc

Module: futures, files: 4 (concurrent/futures)
compile:  ./Python-3.7.1/Lib/concurrent/futures/thread.py ---> ./out/concurrent/futures/thread.pyc
compile:  ./Python-3.7.1/Lib/concurrent/futures/__init__.py ---> ./out/concurrent/futures/__init__.pyc
compile:  ./Python-3.7.1/Lib/concurrent/futures/process.py ---> ./out/concurrent/futures/process.pyc
compile:  ./Python-3.7.1/Lib/concurrent/futures/_base.py ---> ./out/concurrent/futures/_base.pyc

Module: xmlrpc, files: 3 (xmlrpc)
compile:  ./Python-3.7.1/Lib/xmlrpc/__init__.py ---> ./out/xmlrpc/__init__.pyc
compile:  ./Python-3.7.1/Lib/xmlrpc/client.py ---> ./out/xmlrpc/client.pyc
compile:  ./Python-3.7.1/Lib/xmlrpc/server.py ---> ./out/xmlrpc/server.pyc

Module: idlelib, files: 74 (idlelib)
compile:  ./Python-3.7.1/Lib/idlelib/idle.py ---> ./out/idlelib/idle.pyc
compile:  ./Python-3.7.1/Lib/idlelib/macosx.py ---> ./out/idlelib/macosx.pyc
compile:  ./Python-3.7.1/Lib/idlelib/grep.py ---> ./out/idlelib/grep.pyc
compile:  ./Python-3.7.1/Lib/idlelib/delegator.py ---> ./out/idlelib/delegator.pyc
compile:  ./Python-3.7.1/Lib/idlelib/dynoption.py ---> ./out/idlelib/dynoption.pyc
compile:  ./Python-3.7.1/Lib/idlelib/tooltip.py ---> ./out/idlelib/tooltip.pyc
compile:  ./Python-3.7.1/Lib/idlelib/debugobj_r.py ---> ./out/idlelib/debugobj_r.pyc
compile:  ./Python-3.7.1/Lib/idlelib/calltip_w.py ---> ./out/idlelib/calltip_w.pyc
compile:  ./Python-3.7.1/Lib/idlelib/autocomplete_w.py ---> ./out/idlelib/autocomplete_w.pyc
compile:  ./Python-3.7.1/Lib/idlelib/searchengine.py ---> ./out/idlelib/searchengine.pyc
compile:  ./Python-3.7.1/Lib/idlelib/pyshell.py ---> ./out/idlelib/pyshell.pyc
compile:  ./Python-3.7.1/Lib/idlelib/hyperparser.py ---> ./out/idlelib/hyperparser.pyc
compile:  ./Python-3.7.1/Lib/idlelib/mainmenu.py ---> ./out/idlelib/mainmenu.pyc
compile:  ./Python-3.7.1/Lib/idlelib/debugger.py ---> ./out/idlelib/debugger.pyc
compile:  ./Python-3.7.1/Lib/idlelib/calltip.py ---> ./out/idlelib/calltip.pyc
compile:  ./Python-3.7.1/Lib/idlelib/undo.py ---> ./out/idlelib/undo.pyc
compile:  ./Python-3.7.1/Lib/idlelib/run.py ---> ./out/idlelib/run.pyc
compile:  ./Python-3.7.1/Lib/idlelib/autoexpand.py ---> ./out/idlelib/autoexpand.pyc
compile:  ./Python-3.7.1/Lib/idlelib/codecontext.py ---> ./out/idlelib/codecontext.pyc
compile:  ./Python-3.7.1/Lib/idlelib/statusbar.py ---> ./out/idlelib/statusbar.pyc
compile:  ./Python-3.7.1/Lib/idlelib/scrolledlist.py ---> ./out/idlelib/scrolledlist.pyc
compile:  ./Python-3.7.1/Lib/idlelib/multicall.py ---> ./out/idlelib/multicall.pyc
compile:  ./Python-3.7.1/Lib/idlelib/iomenu.py ---> ./out/idlelib/iomenu.pyc
compile:  ./Python-3.7.1/Lib/idlelib/configdialog.py ---> ./out/idlelib/configdialog.pyc
compile:  ./Python-3.7.1/Lib/idlelib/runscript.py ---> ./out/idlelib/runscript.pyc
compile:  ./Python-3.7.1/Lib/idlelib/help_about.py ---> ./out/idlelib/help_about.pyc
compile:  ./Python-3.7.1/Lib/idlelib/colorizer.py ---> ./out/idlelib/colorizer.pyc
compile:  ./Python-3.7.1/Lib/idlelib/window.py ---> ./out/idlelib/window.pyc
compile:  ./Python-3.7.1/Lib/idlelib/__init__.py ---> ./out/idlelib/__init__.pyc
compile:  ./Python-3.7.1/Lib/idlelib/squeezer.py ---> ./out/idlelib/squeezer.pyc
compile:  ./Python-3.7.1/Lib/idlelib/__main__.py ---> ./out/idlelib/__main__.pyc
compile:  ./Python-3.7.1/Lib/idlelib/debugobj.py ---> ./out/idlelib/debugobj.pyc
compile:  ./Python-3.7.1/Lib/idlelib/autocomplete.py ---> ./out/idlelib/autocomplete.pyc
compile:  ./Python-3.7.1/Lib/idlelib/paragraph.py ---> ./out/idlelib/paragraph.pyc
compile:  ./Python-3.7.1/Lib/idlelib/tree.py ---> ./out/idlelib/tree.pyc
compile:  ./Python-3.7.1/Lib/idlelib/textview.py ---> ./out/idlelib/textview.pyc
compile:  ./Python-3.7.1/Lib/idlelib/help.py ---> ./out/idlelib/help.pyc
compile:  ./Python-3.7.1/Lib/idlelib/search.py ---> ./out/idlelib/search.pyc
compile:  ./Python-3.7.1/Lib/idlelib/percolator.py ---> ./out/idlelib/percolator.pyc
compile:  ./Python-3.7.1/Lib/idlelib/config.py ---> ./out/idlelib/config.pyc
compile:  ./Python-3.7.1/Lib/idlelib/history.py ---> ./out/idlelib/history.pyc
compile:  ./Python-3.7.1/Lib/idlelib/browser.py ---> ./out/idlelib/browser.pyc
compile:  ./Python-3.7.1/Lib/idlelib/stackviewer.py ---> ./out/idlelib/stackviewer.pyc
compile:  ./Python-3.7.1/Lib/idlelib/parenmatch.py ---> ./out/idlelib/parenmatch.pyc
compile:  ./Python-3.7.1/Lib/idlelib/filelist.py ---> ./out/idlelib/filelist.pyc
compile:  ./Python-3.7.1/Lib/idlelib/rstrip.py ---> ./out/idlelib/rstrip.pyc
compile:  ./Python-3.7.1/Lib/idlelib/editor.py ---> ./out/idlelib/editor.pyc
compile:  ./Python-3.7.1/Lib/idlelib/outwin.py ---> ./out/idlelib/outwin.pyc
compile:  ./Python-3.7.1/Lib/idlelib/zoomheight.py ---> ./out/idlelib/zoomheight.pyc
compile:  ./Python-3.7.1/Lib/idlelib/pathbrowser.py ---> ./out/idlelib/pathbrowser.pyc
compile:  ./Python-3.7.1/Lib/idlelib/searchbase.py ---> ./out/idlelib/searchbase.pyc
compile:  ./Python-3.7.1/Lib/idlelib/rpc.py ---> ./out/idlelib/rpc.pyc
compile:  ./Python-3.7.1/Lib/idlelib/config_key.py ---> ./out/idlelib/config_key.pyc
compile:  ./Python-3.7.1/Lib/idlelib/zzdummy.py ---> ./out/idlelib/zzdummy.pyc
compile:  ./Python-3.7.1/Lib/idlelib/query.py ---> ./out/idlelib/query.pyc
compile:  ./Python-3.7.1/Lib/idlelib/pyparse.py ---> ./out/idlelib/pyparse.pyc
compile:  ./Python-3.7.1/Lib/idlelib/redirector.py ---> ./out/idlelib/redirector.pyc
compile:  ./Python-3.7.1/Lib/idlelib/debugger_r.py ---> ./out/idlelib/debugger_r.pyc
compile:  ./Python-3.7.1/Lib/idlelib/replace.py ---> ./out/idlelib/replace.pyc

Module: idle_test, files: 63 (idlelib/idle_test)
skipped

Module: unittest, files: 11 (unittest)
skipped

Module: test, files: 17 (unittest/test)
skipped

Module: testmock, files: 11 (unittest/test/testmock)
skipped

Module: email, files: 21 (email)
compile:  ./Python-3.7.1/Lib/email/_header_value_parser.py ---> ./out/email/_header_value_parser.pyc
compile:  ./Python-3.7.1/Lib/email/encoders.py ---> ./out/email/encoders.pyc
compile:  ./Python-3.7.1/Lib/email/headerregistry.py ---> ./out/email/headerregistry.pyc
compile:  ./Python-3.7.1/Lib/email/_policybase.py ---> ./out/email/_policybase.pyc
compile:  ./Python-3.7.1/Lib/email/policy.py ---> ./out/email/policy.pyc
compile:  ./Python-3.7.1/Lib/email/utils.py ---> ./out/email/utils.pyc
compile:  ./Python-3.7.1/Lib/email/contentmanager.py ---> ./out/email/contentmanager.pyc
compile:  ./Python-3.7.1/Lib/email/__init__.py ---> ./out/email/__init__.pyc
compile:  ./Python-3.7.1/Lib/email/iterators.py ---> ./out/email/iterators.pyc
compile:  ./Python-3.7.1/Lib/email/message.py ---> ./out/email/message.pyc
compile:  ./Python-3.7.1/Lib/email/charset.py ---> ./out/email/charset.pyc
compile:  ./Python-3.7.1/Lib/email/base64mime.py ---> ./out/email/base64mime.pyc
compile:  ./Python-3.7.1/Lib/email/errors.py ---> ./out/email/errors.pyc
compile:  ./Python-3.7.1/Lib/email/_encoded_words.py ---> ./out/email/_encoded_words.pyc
compile:  ./Python-3.7.1/Lib/email/parser.py ---> ./out/email/parser.pyc
compile:  ./Python-3.7.1/Lib/email/generator.py ---> ./out/email/generator.pyc
compile:  ./Python-3.7.1/Lib/email/header.py ---> ./out/email/header.pyc
compile:  ./Python-3.7.1/Lib/email/_parseaddr.py ---> ./out/email/_parseaddr.pyc
compile:  ./Python-3.7.1/Lib/email/feedparser.py ---> ./out/email/feedparser.pyc
compile:  ./Python-3.7.1/Lib/email/quoprimime.py ---> ./out/email/quoprimime.pyc

Module: mime, files: 9 (email/mime)
compile:  ./Python-3.7.1/Lib/email/mime/text.py ---> ./out/email/mime/text.pyc
compile:  ./Python-3.7.1/Lib/email/mime/__init__.py ---> ./out/email/mime/__init__.pyc
compile:  ./Python-3.7.1/Lib/email/mime/message.py ---> ./out/email/mime/message.pyc
compile:  ./Python-3.7.1/Lib/email/mime/application.py ---> ./out/email/mime/application.pyc
compile:  ./Python-3.7.1/Lib/email/mime/image.py ---> ./out/email/mime/image.pyc
compile:  ./Python-3.7.1/Lib/email/mime/multipart.py ---> ./out/email/mime/multipart.pyc
compile:  ./Python-3.7.1/Lib/email/mime/audio.py ---> ./out/email/mime/audio.pyc
compile:  ./Python-3.7.1/Lib/email/mime/nonmultipart.py ---> ./out/email/mime/nonmultipart.pyc
compile:  ./Python-3.7.1/Lib/email/mime/base.py ---> ./out/email/mime/base.pyc

Module: tkinter, files: 14 (tkinter)
compile:  ./Python-3.7.1/Lib/tkinter/constants.py ---> ./out/tkinter/constants.pyc
compile:  ./Python-3.7.1/Lib/tkinter/dnd.py ---> ./out/tkinter/dnd.pyc
compile:  ./Python-3.7.1/Lib/tkinter/tix.py ---> ./out/tkinter/tix.pyc
compile:  ./Python-3.7.1/Lib/tkinter/scrolledtext.py ---> ./out/tkinter/scrolledtext.pyc
compile:  ./Python-3.7.1/Lib/tkinter/font.py ---> ./out/tkinter/font.pyc
compile:  ./Python-3.7.1/Lib/tkinter/__init__.py ---> ./out/tkinter/__init__.pyc
compile:  ./Python-3.7.1/Lib/tkinter/filedialog.py ---> ./out/tkinter/filedialog.pyc
compile:  ./Python-3.7.1/Lib/tkinter/__main__.py ---> ./out/tkinter/__main__.pyc
compile:  ./Python-3.7.1/Lib/tkinter/commondialog.py ---> ./out/tkinter/commondialog.pyc
compile:  ./Python-3.7.1/Lib/tkinter/colorchooser.py ---> ./out/tkinter/colorchooser.pyc
compile:  ./Python-3.7.1/Lib/tkinter/simpledialog.py ---> ./out/tkinter/simpledialog.pyc
compile:  ./Python-3.7.1/Lib/tkinter/messagebox.py ---> ./out/tkinter/messagebox.pyc
compile:  ./Python-3.7.1/Lib/tkinter/ttk.py ---> ./out/tkinter/ttk.pyc
compile:  ./Python-3.7.1/Lib/tkinter/dialog.py ---> ./out/tkinter/dialog.pyc

Module: test, files: 5 (tkinter/test)
skipped

Module: test_ttk, files: 5 (tkinter/test/test_ttk)
skipped

Module: test_tkinter, files: 9 (tkinter/test/test_tkinter)
skipped

Module: turtledemo, files: 22 (turtledemo)
compile:  ./Python-3.7.1/Lib/turtledemo/yinyang.py ---> ./out/turtledemo/yinyang.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/round_dance.py ---> ./out/turtledemo/round_dance.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/lindenmayer.py ---> ./out/turtledemo/lindenmayer.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/planet_and_moon.py ---> ./out/turtledemo/planet_and_moon.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/two_canvases.py ---> ./out/turtledemo/two_canvases.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/bytedesign.py ---> ./out/turtledemo/bytedesign.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/minimal_hanoi.py ---> ./out/turtledemo/minimal_hanoi.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/nim.py ---> ./out/turtledemo/nim.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/__init__.py ---> ./out/turtledemo/__init__.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/__main__.py ---> ./out/turtledemo/__main__.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/forest.py ---> ./out/turtledemo/forest.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/tree.py ---> ./out/turtledemo/tree.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/clock.py ---> ./out/turtledemo/clock.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/penrose.py ---> ./out/turtledemo/penrose.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/paint.py ---> ./out/turtledemo/paint.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/fractalcurves.py ---> ./out/turtledemo/fractalcurves.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/chaos.py ---> ./out/turtledemo/chaos.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/peace.py ---> ./out/turtledemo/peace.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/sorting_animate.py ---> ./out/turtledemo/sorting_animate.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/rosette.py ---> ./out/turtledemo/rosette.pyc
compile:  ./Python-3.7.1/Lib/turtledemo/colormixer.py ---> ./out/turtledemo/colormixer.pyc

Module: urllib, files: 6 (urllib)
compile:  ./Python-3.7.1/Lib/urllib/robotparser.py ---> ./out/urllib/robotparser.pyc
compile:  ./Python-3.7.1/Lib/urllib/response.py ---> ./out/urllib/response.pyc
compile:  ./Python-3.7.1/Lib/urllib/__init__.py ---> ./out/urllib/__init__.pyc
compile:  ./Python-3.7.1/Lib/urllib/error.py ---> ./out/urllib/error.pyc
compile:  ./Python-3.7.1/Lib/urllib/parse.py ---> ./out/urllib/parse.pyc
compile:  ./Python-3.7.1/Lib/urllib/request.py ---> ./out/urllib/request.pyc

Module: venv, files: 2 (venv)
compile:  ./Python-3.7.1/Lib/venv/__init__.py ---> ./out/venv/__init__.pyc
compile:  ./Python-3.7.1/Lib/venv/__main__.py ---> ./out/venv/__main__.pyc

Module: collections, files: 2 (collections)
compile:  ./Python-3.7.1/Lib/collections/__init__.py ---> ./out/collections/__init__.pyc
compile:  ./Python-3.7.1/Lib/collections/abc.py ---> ./out/collections/abc.pyc

Module: logging, files: 3 (logging)
compile:  ./Python-3.7.1/Lib/logging/__init__.py ---> ./out/logging/__init__.pyc
compile:  ./Python-3.7.1/Lib/logging/config.py ---> ./out/logging/config.pyc
compile:  ./Python-3.7.1/Lib/logging/handlers.py ---> ./out/logging/handlers.pyc

Module: test, files: 544 (test)
skipped

Module: libregrtest, files: 9 (test/libregrtest)
skipped

Module: leakers, files: 4 (test/leakers)
skipped

Module: support, files: 3 (test/support)
skipped

Module: test_import, files: 2 (test/test_import)
skipped

Module: package2, files: 2 (test/test_import/data/package2)
skipped

Module: package, files: 2 (test/test_import/data/package)
skipped

Module: circular_imports, files: 9 (test/test_import/data/circular_imports)
skipped

Module: subpkg, files: 2 (test/test_import/data/circular_imports/subpkg)
skipped

Module: crashers, files: 8 (test/crashers)
skipped

Module: test_tools, files: 11 (test/test_tools)
skipped

Module: subprocessdata, files: 5 (test/subprocessdata)
skipped

Module: eintrdata, files: 1 (test/eintrdata)
skipped

Module: test_asyncio, files: 31 (test/test_asyncio)
skipped

Module: encoded_modules, files: 3 (test/encoded_modules)
skipped

Module: test_json, files: 19 (test/test_json)
skipped

Module: test_importlib, files: 16 (test/test_importlib)
skipped

Module: zipdata01, files: 2 (test/test_importlib/zipdata01)
skipped

Module: zipdata02, files: 2 (test/test_importlib/zipdata02)
skipped

Module: data01, files: 4 (test/test_importlib/data01)
skipped

Module: subdirectory, files: 2 (test/test_importlib/data01/subdirectory)
skipped

Module: data03, files: 1 (test/test_importlib/data03)
skipped

Module: portion1, files: 1 (test/test_importlib/data03/namespace/portion1)
skipped

Module: portion2, files: 1 (test/test_importlib/data03/namespace/portion2)
skipped

Module: source, files: 7 (test/test_importlib/source)
skipped

Module: foo, files: 1 (test/test_importlib/namespace_pkgs/portion1/foo)
skipped

Module: child, files: 1 (test/test_importlib/namespace_pkgs/project2/parent/child)
skipped

Module: foo, files: 1 (test/test_importlib/namespace_pkgs/portion2/foo)
skipped

Module: child, files: 1 (test/test_importlib/namespace_pkgs/project1/parent/child)
skipped

Module: foo, files: 2 (test/test_importlib/namespace_pkgs/not_a_namespace_pkg/foo)
skipped

Module: child, files: 1 (test/test_importlib/namespace_pkgs/project3/parent/child)
skipped

Module: module_and_namespace_package, files: 1 (test/test_importlib/namespace_pkgs/module_and_namespace_package)
skipped

Module: foo, files: 2 (test/test_importlib/namespace_pkgs/both_portions/foo)
skipped

Module: builtin, files: 4 (test/test_importlib/builtin)
skipped

Module: extension, files: 6 (test/test_importlib/extension)
skipped

Module: data02, files: 1 (test/test_importlib/data02)
skipped

Module: one, files: 2 (test/test_importlib/data02/one)
skipped

Module: two, files: 2 (test/test_importlib/data02/two)
skipped

Module: frozen, files: 4 (test/test_importlib/frozen)
skipped

Module: import_, files: 11 (test/test_importlib/import_)
skipped

Module: test_email, files: 17 (test/test_email)
skipped

Module: test_warnings, files: 2 (test/test_warnings)
skipped

Module: data, files: 2 (test/test_warnings/data)
skipped

Module: dtracedata, files: 16 (test/dtracedata)
skipped

Module: tracedmodules, files: 2 (test/tracedmodules)
skipped

Module: http, files: 5 (http)
compile:  ./Python-3.7.1/Lib/http/cookies.py ---> ./out/http/cookies.pyc
compile:  ./Python-3.7.1/Lib/http/__init__.py ---> ./out/http/__init__.pyc
compile:  ./Python-3.7.1/Lib/http/client.py ---> ./out/http/client.pyc
compile:  ./Python-3.7.1/Lib/http/cookiejar.py ---> ./out/http/cookiejar.pyc
compile:  ./Python-3.7.1/Lib/http/server.py ---> ./out/http/server.pyc

Module: html, files: 3 (html)
compile:  ./Python-3.7.1/Lib/html/entities.py ---> ./out/html/entities.pyc
compile:  ./Python-3.7.1/Lib/html/__init__.py ---> ./out/html/__init__.pyc
compile:  ./Python-3.7.1/Lib/html/parser.py ---> ./out/html/parser.pyc

Module: pydoc_data, files: 3 (pydoc_data)
compile:  ./Python-3.7.1/Lib/pydoc_data/topics.py ---> ./out/pydoc_data/topics.pyc
compile:  ./Python-3.7.1/Lib/pydoc_data/__init__.py ---> ./out/pydoc_data/__init__.pyc

Module: encodings, files: 125 (encodings)
compile:  ./Python-3.7.1/Lib/encodings/cp424.py ---> ./out/encodings/cp424.pyc
compile:  ./Python-3.7.1/Lib/encodings/big5hkscs.py ---> ./out/encodings/big5hkscs.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp437.py ---> ./out/encodings/cp437.pyc
compile:  ./Python-3.7.1/Lib/encodings/koi8_u.py ---> ./out/encodings/koi8_u.pyc
compile:  ./Python-3.7.1/Lib/encodings/utf_8_sig.py ---> ./out/encodings/utf_8_sig.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_croatian.py ---> ./out/encodings/mac_croatian.pyc
compile:  ./Python-3.7.1/Lib/encodings/tis_620.py ---> ./out/encodings/tis_620.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp037.py ---> ./out/encodings/cp037.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp850.py ---> ./out/encodings/cp850.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso2022_jp.py ---> ./out/encodings/iso2022_jp.pyc
compile:  ./Python-3.7.1/Lib/encodings/quopri_codec.py ---> ./out/encodings/quopri_codec.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp273.py ---> ./out/encodings/cp273.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso2022_kr.py ---> ./out/encodings/iso2022_kr.pyc
compile:  ./Python-3.7.1/Lib/encodings/gb2312.py ---> ./out/encodings/gb2312.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso2022_jp_1.py ---> ./out/encodings/iso2022_jp_1.pyc
compile:  ./Python-3.7.1/Lib/encodings/shift_jisx0213.py ---> ./out/encodings/shift_jisx0213.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp863.py ---> ./out/encodings/cp863.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp737.py ---> ./out/encodings/cp737.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp856.py ---> ./out/encodings/cp856.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso2022_jp_3.py ---> ./out/encodings/iso2022_jp_3.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1258.py ---> ./out/encodings/cp1258.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_4.py ---> ./out/encodings/iso8859_4.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_farsi.py ---> ./out/encodings/mac_farsi.pyc
compile:  ./Python-3.7.1/Lib/encodings/uu_codec.py ---> ./out/encodings/uu_codec.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp864.py ---> ./out/encodings/cp864.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1125.py ---> ./out/encodings/cp1125.pyc
compile:  ./Python-3.7.1/Lib/encodings/latin_1.py ---> ./out/encodings/latin_1.pyc
compile:  ./Python-3.7.1/Lib/encodings/ptcp154.py ---> ./out/encodings/ptcp154.pyc
compile:  ./Python-3.7.1/Lib/encodings/aliases.py ---> ./out/encodings/aliases.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp855.py ---> ./out/encodings/cp855.pyc
compile:  ./Python-3.7.1/Lib/encodings/shift_jis_2004.py ---> ./out/encodings/shift_jis_2004.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp862.py ---> ./out/encodings/cp862.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp861.py ---> ./out/encodings/cp861.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_9.py ---> ./out/encodings/iso8859_9.pyc
compile:  ./Python-3.7.1/Lib/encodings/unicode_escape.py ---> ./out/encodings/unicode_escape.pyc
compile:  ./Python-3.7.1/Lib/encodings/euc_jis_2004.py ---> ./out/encodings/euc_jis_2004.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1250.py ---> ./out/encodings/cp1250.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_cyrillic.py ---> ./out/encodings/mac_cyrillic.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_15.py ---> ./out/encodings/iso8859_15.pyc
compile:  ./Python-3.7.1/Lib/encodings/big5.py ---> ./out/encodings/big5.pyc
compile:  ./Python-3.7.1/Lib/encodings/__init__.py ---> ./out/encodings/__init__.pyc
compile:  ./Python-3.7.1/Lib/encodings/utf_16.py ---> ./out/encodings/utf_16.pyc
compile:  ./Python-3.7.1/Lib/encodings/koi8_t.py ---> ./out/encodings/koi8_t.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso2022_jp_ext.py ---> ./out/encodings/iso2022_jp_ext.pyc
compile:  ./Python-3.7.1/Lib/encodings/utf_7.py ---> ./out/encodings/utf_7.pyc
compile:  ./Python-3.7.1/Lib/encodings/unicode_internal.py ---> ./out/encodings/unicode_internal.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_16.py ---> ./out/encodings/iso8859_16.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp65001.py ---> ./out/encodings/cp65001.pyc
compile:  ./Python-3.7.1/Lib/encodings/bz2_codec.py ---> ./out/encodings/bz2_codec.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_14.py ---> ./out/encodings/iso8859_14.pyc
compile:  ./Python-3.7.1/Lib/encodings/punycode.py ---> ./out/encodings/punycode.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp852.py ---> ./out/encodings/cp852.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_5.py ---> ./out/encodings/iso8859_5.pyc
compile:  ./Python-3.7.1/Lib/encodings/zlib_codec.py ---> ./out/encodings/zlib_codec.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1026.py ---> ./out/encodings/cp1026.pyc
compile:  ./Python-3.7.1/Lib/encodings/euc_jp.py ---> ./out/encodings/euc_jp.pyc
compile:  ./Python-3.7.1/Lib/encodings/utf_16_be.py ---> ./out/encodings/utf_16_be.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp932.py ---> ./out/encodings/cp932.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1254.py ---> ./out/encodings/cp1254.pyc
compile:  ./Python-3.7.1/Lib/encodings/rot_13.py ---> ./out/encodings/rot_13.pyc
compile:  ./Python-3.7.1/Lib/encodings/charmap.py ---> ./out/encodings/charmap.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp857.py ---> ./out/encodings/cp857.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_3.py ---> ./out/encodings/iso8859_3.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp720.py ---> ./out/encodings/cp720.pyc
compile:  ./Python-3.7.1/Lib/encodings/johab.py ---> ./out/encodings/johab.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1140.py ---> ./out/encodings/cp1140.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_11.py ---> ./out/encodings/iso8859_11.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp865.py ---> ./out/encodings/cp865.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1255.py ---> ./out/encodings/cp1255.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_romanian.py ---> ./out/encodings/mac_romanian.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp775.py ---> ./out/encodings/cp775.pyc
compile:  ./Python-3.7.1/Lib/encodings/ascii.py ---> ./out/encodings/ascii.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp875.py ---> ./out/encodings/cp875.pyc
compile:  ./Python-3.7.1/Lib/encodings/kz1048.py ---> ./out/encodings/kz1048.pyc
compile:  ./Python-3.7.1/Lib/encodings/shift_jis.py ---> ./out/encodings/shift_jis.pyc
compile:  ./Python-3.7.1/Lib/encodings/hp_roman8.py ---> ./out/encodings/hp_roman8.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1006.py ---> ./out/encodings/cp1006.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp874.py ---> ./out/encodings/cp874.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp500.py ---> ./out/encodings/cp500.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1253.py ---> ./out/encodings/cp1253.pyc
compile:  ./Python-3.7.1/Lib/encodings/utf_8.py ---> ./out/encodings/utf_8.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1252.py ---> ./out/encodings/cp1252.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_2.py ---> ./out/encodings/iso8859_2.pyc
compile:  ./Python-3.7.1/Lib/encodings/hz.py ---> ./out/encodings/hz.pyc
compile:  ./Python-3.7.1/Lib/encodings/base64_codec.py ---> ./out/encodings/base64_codec.pyc
compile:  ./Python-3.7.1/Lib/encodings/hex_codec.py ---> ./out/encodings/hex_codec.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_10.py ---> ./out/encodings/iso8859_10.pyc
compile:  ./Python-3.7.1/Lib/encodings/raw_unicode_escape.py ---> ./out/encodings/raw_unicode_escape.pyc
compile:  ./Python-3.7.1/Lib/encodings/gbk.py ---> ./out/encodings/gbk.pyc
compile:  ./Python-3.7.1/Lib/encodings/gb18030.py ---> ./out/encodings/gb18030.pyc
compile:  ./Python-3.7.1/Lib/encodings/oem.py ---> ./out/encodings/oem.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp858.py ---> ./out/encodings/cp858.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_6.py ---> ./out/encodings/iso8859_6.pyc
compile:  ./Python-3.7.1/Lib/encodings/euc_jisx0213.py ---> ./out/encodings/euc_jisx0213.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_arabic.py ---> ./out/encodings/mac_arabic.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_7.py ---> ./out/encodings/iso8859_7.pyc
compile:  ./Python-3.7.1/Lib/encodings/idna.py ---> ./out/encodings/idna.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_latin2.py ---> ./out/encodings/mac_latin2.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1256.py ---> ./out/encodings/cp1256.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_roman.py ---> ./out/encodings/mac_roman.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso2022_jp_2.py ---> ./out/encodings/iso2022_jp_2.pyc
compile:  ./Python-3.7.1/Lib/encodings/euc_kr.py ---> ./out/encodings/euc_kr.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp869.py ---> ./out/encodings/cp869.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso2022_jp_2004.py ---> ./out/encodings/iso2022_jp_2004.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_1.py ---> ./out/encodings/iso8859_1.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_8.py ---> ./out/encodings/iso8859_8.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp950.py ---> ./out/encodings/cp950.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_iceland.py ---> ./out/encodings/mac_iceland.pyc
compile:  ./Python-3.7.1/Lib/encodings/utf_32_be.py ---> ./out/encodings/utf_32_be.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp866.py ---> ./out/encodings/cp866.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_centeuro.py ---> ./out/encodings/mac_centeuro.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_turkish.py ---> ./out/encodings/mac_turkish.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp949.py ---> ./out/encodings/cp949.pyc
compile:  ./Python-3.7.1/Lib/encodings/undefined.py ---> ./out/encodings/undefined.pyc
compile:  ./Python-3.7.1/Lib/encodings/palmos.py ---> ./out/encodings/palmos.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1251.py ---> ./out/encodings/cp1251.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp1257.py ---> ./out/encodings/cp1257.pyc
compile:  ./Python-3.7.1/Lib/encodings/iso8859_13.py ---> ./out/encodings/iso8859_13.pyc
compile:  ./Python-3.7.1/Lib/encodings/cp860.py ---> ./out/encodings/cp860.pyc
compile:  ./Python-3.7.1/Lib/encodings/koi8_r.py ---> ./out/encodings/koi8_r.pyc
compile:  ./Python-3.7.1/Lib/encodings/utf_16_le.py ---> ./out/encodings/utf_16_le.pyc
compile:  ./Python-3.7.1/Lib/encodings/mac_greek.py ---> ./out/encodings/mac_greek.pyc
compile:  ./Python-3.7.1/Lib/encodings/utf_32.py ---> ./out/encodings/utf_32.pyc
compile:  ./Python-3.7.1/Lib/encodings/mbcs.py ---> ./out/encodings/mbcs.pyc
compile:  ./Python-3.7.1/Lib/encodings/utf_32_le.py ---> ./out/encodings/utf_32_le.pyc

Module: dbm, files: 4 (dbm)
compile:  ./Python-3.7.1/Lib/dbm/ndbm.py ---> ./out/dbm/ndbm.pyc
compile:  ./Python-3.7.1/Lib/dbm/dumb.py ---> ./out/dbm/dumb.pyc
compile:  ./Python-3.7.1/Lib/dbm/__init__.py ---> ./out/dbm/__init__.pyc
compile:  ./Python-3.7.1/Lib/dbm/gnu.py ---> ./out/dbm/gnu.pyc

Module: multiprocessing, files: 20 (multiprocessing)
compile:  ./Python-3.7.1/Lib/multiprocessing/popen_spawn_posix.py ---> ./out/multiprocessing/popen_spawn_posix.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/sharedctypes.py ---> ./out/multiprocessing/sharedctypes.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/reduction.py ---> ./out/multiprocessing/reduction.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/popen_spawn_win32.py ---> ./out/multiprocessing/popen_spawn_win32.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/util.py ---> ./out/multiprocessing/util.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/forkserver.py ---> ./out/multiprocessing/forkserver.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/synchronize.py ---> ./out/multiprocessing/synchronize.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/__init__.py ---> ./out/multiprocessing/__init__.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/connection.py ---> ./out/multiprocessing/connection.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/spawn.py ---> ./out/multiprocessing/spawn.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/queues.py ---> ./out/multiprocessing/queues.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/popen_forkserver.py ---> ./out/multiprocessing/popen_forkserver.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/pool.py ---> ./out/multiprocessing/pool.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/heap.py ---> ./out/multiprocessing/heap.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/semaphore_tracker.py ---> ./out/multiprocessing/semaphore_tracker.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/context.py ---> ./out/multiprocessing/context.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/managers.py ---> ./out/multiprocessing/managers.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/resource_sharer.py ---> ./out/multiprocessing/resource_sharer.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/popen_fork.py ---> ./out/multiprocessing/popen_fork.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/process.py ---> ./out/multiprocessing/process.pyc

Module: dummy, files: 2 (multiprocessing/dummy)
compile:  ./Python-3.7.1/Lib/multiprocessing/dummy/__init__.py ---> ./out/multiprocessing/dummy/__init__.pyc
compile:  ./Python-3.7.1/Lib/multiprocessing/dummy/connection.py ---> ./out/multiprocessing/dummy/connection.pyc

Module: importlib, files: 7 (importlib)
compile:  ./Python-3.7.1/Lib/importlib/_bootstrap_external.py ---> ./out/importlib/_bootstrap_external.pyc
compile:  ./Python-3.7.1/Lib/importlib/machinery.py ---> ./out/importlib/machinery.pyc
compile:  ./Python-3.7.1/Lib/importlib/util.py ---> ./out/importlib/util.pyc
compile:  ./Python-3.7.1/Lib/importlib/__init__.py ---> ./out/importlib/__init__.pyc
compile:  ./Python-3.7.1/Lib/importlib/resources.py ---> ./out/importlib/resources.pyc
compile:  ./Python-3.7.1/Lib/importlib/abc.py ---> ./out/importlib/abc.pyc
compile:  ./Python-3.7.1/Lib/importlib/_bootstrap.py ---> ./out/importlib/_bootstrap.pyc

Module: distutils, files: 29 (distutils)
compile:  ./Python-3.7.1/Lib/distutils/cmd.py ---> ./out/distutils/cmd.pyc
compile:  ./Python-3.7.1/Lib/distutils/version.py ---> ./out/distutils/version.pyc
compile:  ./Python-3.7.1/Lib/distutils/unixccompiler.py ---> ./out/distutils/unixccompiler.pyc
compile:  ./Python-3.7.1/Lib/distutils/ccompiler.py ---> ./out/distutils/ccompiler.pyc
compile:  ./Python-3.7.1/Lib/distutils/dist.py ---> ./out/distutils/dist.pyc
compile:  ./Python-3.7.1/Lib/distutils/cygwinccompiler.py ---> ./out/distutils/cygwinccompiler.pyc
compile:  ./Python-3.7.1/Lib/distutils/file_util.py ---> ./out/distutils/file_util.pyc
compile:  ./Python-3.7.1/Lib/distutils/debug.py ---> ./out/distutils/debug.pyc
compile:  ./Python-3.7.1/Lib/distutils/dep_util.py ---> ./out/distutils/dep_util.pyc
compile:  ./Python-3.7.1/Lib/distutils/extension.py ---> ./out/distutils/extension.pyc
compile:  ./Python-3.7.1/Lib/distutils/versionpredicate.py ---> ./out/distutils/versionpredicate.pyc
compile:  ./Python-3.7.1/Lib/distutils/sysconfig.py ---> ./out/distutils/sysconfig.pyc
compile:  ./Python-3.7.1/Lib/distutils/util.py ---> ./out/distutils/util.pyc
compile:  ./Python-3.7.1/Lib/distutils/fancy_getopt.py ---> ./out/distutils/fancy_getopt.pyc
compile:  ./Python-3.7.1/Lib/distutils/__init__.py ---> ./out/distutils/__init__.pyc
compile:  ./Python-3.7.1/Lib/distutils/_msvccompiler.py ---> ./out/distutils/_msvccompiler.pyc
compile:  ./Python-3.7.1/Lib/distutils/spawn.py ---> ./out/distutils/spawn.pyc
compile:  ./Python-3.7.1/Lib/distutils/msvccompiler.py ---> ./out/distutils/msvccompiler.pyc
compile:  ./Python-3.7.1/Lib/distutils/errors.py ---> ./out/distutils/errors.pyc
compile:  ./Python-3.7.1/Lib/distutils/config.py ---> ./out/distutils/config.pyc
compile:  ./Python-3.7.1/Lib/distutils/filelist.py ---> ./out/distutils/filelist.pyc
compile:  ./Python-3.7.1/Lib/distutils/bcppcompiler.py ---> ./out/distutils/bcppcompiler.pyc
compile:  ./Python-3.7.1/Lib/distutils/core.py ---> ./out/distutils/core.pyc
compile:  ./Python-3.7.1/Lib/distutils/archive_util.py ---> ./out/distutils/archive_util.pyc
compile:  ./Python-3.7.1/Lib/distutils/text_file.py ---> ./out/distutils/text_file.pyc
compile:  ./Python-3.7.1/Lib/distutils/dir_util.py ---> ./out/distutils/dir_util.pyc
compile:  ./Python-3.7.1/Lib/distutils/log.py ---> ./out/distutils/log.pyc
compile:  ./Python-3.7.1/Lib/distutils/msvc9compiler.py ---> ./out/distutils/msvc9compiler.pyc

Module: command, files: 33 (distutils/command)
compile:  ./Python-3.7.1/Lib/distutils/command/install_data.py ---> ./out/distutils/command/install_data.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/install_lib.py ---> ./out/distutils/command/install_lib.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/sdist.py ---> ./out/distutils/command/sdist.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/build.py ---> ./out/distutils/command/build.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/bdist_rpm.py ---> ./out/distutils/command/bdist_rpm.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/bdist_wininst.py ---> ./out/distutils/command/bdist_wininst.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/install.py ---> ./out/distutils/command/install.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/install_scripts.py ---> ./out/distutils/command/install_scripts.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/build_clib.py ---> ./out/distutils/command/build_clib.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/install_egg_info.py ---> ./out/distutils/command/install_egg_info.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/clean.py ---> ./out/distutils/command/clean.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/bdist_dumb.py ---> ./out/distutils/command/bdist_dumb.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/upload.py ---> ./out/distutils/command/upload.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/__init__.py ---> ./out/distutils/command/__init__.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/config.py ---> ./out/distutils/command/config.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/bdist.py ---> ./out/distutils/command/bdist.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/check.py ---> ./out/distutils/command/check.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/install_headers.py ---> ./out/distutils/command/install_headers.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/bdist_msi.py ---> ./out/distutils/command/bdist_msi.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/build_scripts.py ---> ./out/distutils/command/build_scripts.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/register.py ---> ./out/distutils/command/register.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/build_py.py ---> ./out/distutils/command/build_py.pyc
compile:  ./Python-3.7.1/Lib/distutils/command/build_ext.py ---> ./out/distutils/command/build_ext.pyc

Module: tests, files: 45 (distutils/tests)
skipped

Module: ctypes, files: 5 (ctypes)
compile:  ./Python-3.7.1/Lib/ctypes/_endian.py ---> ./out/ctypes/_endian.pyc
compile:  ./Python-3.7.1/Lib/ctypes/_aix.py ---> ./out/ctypes/_aix.pyc
compile:  ./Python-3.7.1/Lib/ctypes/util.py ---> ./out/ctypes/util.pyc
compile:  ./Python-3.7.1/Lib/ctypes/__init__.py ---> ./out/ctypes/__init__.pyc
compile:  ./Python-3.7.1/Lib/ctypes/wintypes.py ---> ./out/ctypes/wintypes.pyc

Module: test, files: 53 (ctypes/test)
skipped

Module: macholib, files: 7 (ctypes/macholib)
compile:  ./Python-3.7.1/Lib/ctypes/macholib/__init__.py ---> ./out/ctypes/macholib/__init__.pyc
compile:  ./Python-3.7.1/Lib/ctypes/macholib/framework.py ---> ./out/ctypes/macholib/framework.pyc
compile:  ./Python-3.7.1/Lib/ctypes/macholib/dylib.py ---> ./out/ctypes/macholib/dylib.pyc
compile:  ./Python-3.7.1/Lib/ctypes/macholib/dyld.py ---> ./out/ctypes/macholib/dyld.pyc

Module: msilib, files: 4 (msilib)
compile:  ./Python-3.7.1/Lib/msilib/text.py ---> ./out/msilib/text.pyc
compile:  ./Python-3.7.1/Lib/msilib/__init__.py ---> ./out/msilib/__init__.pyc
compile:  ./Python-3.7.1/Lib/msilib/schema.py ---> ./out/msilib/schema.pyc
compile:  ./Python-3.7.1/Lib/msilib/sequence.py ---> ./out/msilib/sequence.pyc

Adding compiled files to zip archive: ./out/../python-compiled
```