'''Wrapper for tox.h

Generated with:
/usr/local/bin/ctypesgen.py -ltoxcore /usr/local/include/tox/tox.h -ltoxdns /usr/local/include/tox/toxdns.h -ltoxav /usr/local/include/tox/toxav.h -ltoxencryptsave /usr/local/include/tox/toxencryptsave.h --compile-libdir /usr/lib

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes
import os
import sys
from ctypes import *

if sys.version_info[0] == 3:
    def cmp(a, b):
        return (a > b) - (a < b)
    sys.maxint = sys.maxsize
    unicode = str
    str = bytes

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del _int_types


class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]


def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x

        p.from_param = classmethod(from_param)

    return p


class UserString:
    def __init__(self, seq):
        if isinstance(1, (str, bytes)):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data)

    def __float__(self):
        return float(self.data)

    def __complex__(self):
        return complex(self.data)

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0);
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(1, (str, bytes)):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))

    def __radd__(self, other):
        if isinstance(1, (str, bytes)):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1:]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index + 1:]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(1, (str, bytes)):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub) + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(1, (str, bytes)):
            self.data += other
        else:
            self.data += str(other)
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):
    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, bytes, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))

# End preamble

_libs = {}
_libdirs = ['/usr/lib']

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError as e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/lib64', '/usr/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu', '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu', '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["toxcore"] = load_library("toxcore")
_libs["toxdns"] = load_library("toxdns")
_libs["toxav"] = load_library("toxav")
_libs["toxencryptsave"] = load_library("toxencryptsave")

# 4 libraries
# End libraries

# No modules

# /usr/local/include/tox/tox.h: 124
class struct_Tox(Structure):
    pass

Tox = struct_Tox # /usr/local/include/tox/tox.h: 124

# /usr/local/include/tox/tox.h: 175
if hasattr(_libs['toxcore'], 'tox_version_major'):
    tox_version_major = _libs['toxcore'].tox_version_major
    tox_version_major.argtypes = []
    tox_version_major.restype = c_uint32

# /usr/local/include/tox/tox.h: 180
if hasattr(_libs['toxcore'], 'tox_version_minor'):
    tox_version_minor = _libs['toxcore'].tox_version_minor
    tox_version_minor.argtypes = []
    tox_version_minor.restype = c_uint32

# /usr/local/include/tox/tox.h: 185
if hasattr(_libs['toxcore'], 'tox_version_patch'):
    tox_version_patch = _libs['toxcore'].tox_version_patch
    tox_version_patch.argtypes = []
    tox_version_patch.restype = c_uint32

# /usr/local/include/tox/tox.h: 191
if hasattr(_libs['toxcore'], 'tox_version_is_compatible'):
    tox_version_is_compatible = _libs['toxcore'].tox_version_is_compatible
    tox_version_is_compatible.argtypes = [c_uint32, c_uint32, c_uint32]
    tox_version_is_compatible.restype = c_bool

enum_TOX_USER_STATUS = c_int # /usr/local/include/tox/tox.h: 293

TOX_USER_STATUS_NONE = 0 # /usr/local/include/tox/tox.h: 293

TOX_USER_STATUS_AWAY = (TOX_USER_STATUS_NONE + 1) # /usr/local/include/tox/tox.h: 293

TOX_USER_STATUS_BUSY = (TOX_USER_STATUS_AWAY + 1) # /usr/local/include/tox/tox.h: 293

TOX_USER_STATUS = enum_TOX_USER_STATUS # /usr/local/include/tox/tox.h: 293

enum_TOX_MESSAGE_TYPE = c_int # /usr/local/include/tox/tox.h: 309

TOX_MESSAGE_TYPE_NORMAL = 0 # /usr/local/include/tox/tox.h: 309

TOX_MESSAGE_TYPE_ACTION = (TOX_MESSAGE_TYPE_NORMAL + 1) # /usr/local/include/tox/tox.h: 309

TOX_MESSAGE_TYPE = enum_TOX_MESSAGE_TYPE # /usr/local/include/tox/tox.h: 309

enum_TOX_PROXY_TYPE = c_int # /usr/local/include/tox/tox.h: 331

TOX_PROXY_TYPE_NONE = 0 # /usr/local/include/tox/tox.h: 331

TOX_PROXY_TYPE_HTTP = (TOX_PROXY_TYPE_NONE + 1) # /usr/local/include/tox/tox.h: 331

TOX_PROXY_TYPE_SOCKS5 = (TOX_PROXY_TYPE_HTTP + 1) # /usr/local/include/tox/tox.h: 331

TOX_PROXY_TYPE = enum_TOX_PROXY_TYPE # /usr/local/include/tox/tox.h: 331

# /usr/local/include/tox/tox.h: 339
class struct_Tox_Options(Structure):
    pass

struct_Tox_Options.__slots__ = [
    'ipv6_enabled',
    'udp_enabled',
    'proxy_type',
    'proxy_host',
    'proxy_port',
    'start_port',
    'end_port',
]
struct_Tox_Options._fields_ = [
    ('ipv6_enabled', c_bool),
    ('udp_enabled', c_bool),
    ('proxy_type', TOX_PROXY_TYPE),
    ('proxy_host', String),
    ('proxy_port', c_uint16),
    ('start_port', c_uint16),
    ('end_port', c_uint16),
]

# /usr/local/include/tox/tox.h: 415
if hasattr(_libs['toxcore'], 'tox_options_default'):
    tox_options_default = _libs['toxcore'].tox_options_default
    tox_options_default.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_default.restype = None

enum_TOX_ERR_OPTIONS_NEW = c_int # /usr/local/include/tox/tox.h: 424

TOX_ERR_OPTIONS_NEW_OK = 0 # /usr/local/include/tox/tox.h: 424

TOX_ERR_OPTIONS_NEW_MALLOC = (TOX_ERR_OPTIONS_NEW_OK + 1) # /usr/local/include/tox/tox.h: 424

TOX_ERR_OPTIONS_NEW = enum_TOX_ERR_OPTIONS_NEW # /usr/local/include/tox/tox.h: 424

# /usr/local/include/tox/tox.h: 436
if hasattr(_libs['toxcore'], 'tox_options_new'):
    tox_options_new = _libs['toxcore'].tox_options_new
    tox_options_new.argtypes = [POINTER(TOX_ERR_OPTIONS_NEW)]
    tox_options_new.restype = POINTER(struct_Tox_Options)

# /usr/local/include/tox/tox.h: 445
if hasattr(_libs['toxcore'], 'tox_options_free'):
    tox_options_free = _libs['toxcore'].tox_options_free
    tox_options_free.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_free.restype = None

enum_TOX_ERR_NEW = c_int # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_OK = 0 # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_NULL = (TOX_ERR_NEW_OK + 1) # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_MALLOC = (TOX_ERR_NEW_NULL + 1) # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_PORT_ALLOC = (TOX_ERR_NEW_MALLOC + 1) # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_PROXY_BAD_TYPE = (TOX_ERR_NEW_PORT_ALLOC + 1) # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_PROXY_BAD_HOST = (TOX_ERR_NEW_PROXY_BAD_TYPE + 1) # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_PROXY_BAD_PORT = (TOX_ERR_NEW_PROXY_BAD_HOST + 1) # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_PROXY_NOT_FOUND = (TOX_ERR_NEW_PROXY_BAD_PORT + 1) # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_LOAD_ENCRYPTED = (TOX_ERR_NEW_PROXY_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW_LOAD_BAD_FORMAT = (TOX_ERR_NEW_LOAD_ENCRYPTED + 1) # /usr/local/include/tox/tox.h: 498

TOX_ERR_NEW = enum_TOX_ERR_NEW # /usr/local/include/tox/tox.h: 498

# /usr/local/include/tox/tox.h: 521
if hasattr(_libs['toxcore'], 'tox_new'):
    tox_new = _libs['toxcore'].tox_new
    tox_new.argtypes = [POINTER(struct_Tox_Options), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_NEW)]
    tox_new.restype = POINTER(Tox)

# /usr/local/include/tox/tox.h: 531
if hasattr(_libs['toxcore'], 'tox_kill'):
    tox_kill = _libs['toxcore'].tox_kill
    tox_kill.argtypes = [POINTER(Tox)]
    tox_kill.restype = None

# /usr/local/include/tox/tox.h: 541
if hasattr(_libs['toxcore'], 'tox_get_savedata_size'):
    tox_get_savedata_size = _libs['toxcore'].tox_get_savedata_size
    tox_get_savedata_size.argtypes = [POINTER(Tox)]
    tox_get_savedata_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 550
if hasattr(_libs['toxcore'], 'tox_get_savedata'):
    tox_get_savedata = _libs['toxcore'].tox_get_savedata
    tox_get_savedata.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_get_savedata.restype = None

enum_TOX_ERR_BOOTSTRAP = c_int # /usr/local/include/tox/tox.h: 572

TOX_ERR_BOOTSTRAP_OK = 0 # /usr/local/include/tox/tox.h: 572

TOX_ERR_BOOTSTRAP_NULL = (TOX_ERR_BOOTSTRAP_OK + 1) # /usr/local/include/tox/tox.h: 572

TOX_ERR_BOOTSTRAP_BAD_HOST = (TOX_ERR_BOOTSTRAP_NULL + 1) # /usr/local/include/tox/tox.h: 572

TOX_ERR_BOOTSTRAP_BAD_PORT = (TOX_ERR_BOOTSTRAP_BAD_HOST + 1) # /usr/local/include/tox/tox.h: 572

TOX_ERR_BOOTSTRAP = enum_TOX_ERR_BOOTSTRAP # /usr/local/include/tox/tox.h: 572

# /usr/local/include/tox/tox.h: 593
if hasattr(_libs['toxcore'], 'tox_bootstrap'):
    tox_bootstrap = _libs['toxcore'].tox_bootstrap
    tox_bootstrap.argtypes = [POINTER(Tox), String, c_uint16, POINTER(c_uint8), POINTER(TOX_ERR_BOOTSTRAP)]
    tox_bootstrap.restype = c_bool

# /usr/local/include/tox/tox.h: 609
if hasattr(_libs['toxcore'], 'tox_add_tcp_relay'):
    tox_add_tcp_relay = _libs['toxcore'].tox_add_tcp_relay
    tox_add_tcp_relay.argtypes = [POINTER(Tox), String, c_uint16, POINTER(c_uint8), POINTER(TOX_ERR_BOOTSTRAP)]
    tox_add_tcp_relay.restype = c_bool

enum_TOX_CONNECTION = c_int # /usr/local/include/tox/tox.h: 632

TOX_CONNECTION_NONE = 0 # /usr/local/include/tox/tox.h: 632

TOX_CONNECTION_TCP = (TOX_CONNECTION_NONE + 1) # /usr/local/include/tox/tox.h: 632

TOX_CONNECTION_UDP = (TOX_CONNECTION_TCP + 1) # /usr/local/include/tox/tox.h: 632

TOX_CONNECTION = enum_TOX_CONNECTION # /usr/local/include/tox/tox.h: 632

# /usr/local/include/tox/tox.h: 639
if hasattr(_libs['toxcore'], 'tox_self_get_connection_status'):
    tox_self_get_connection_status = _libs['toxcore'].tox_self_get_connection_status
    tox_self_get_connection_status.argtypes = [POINTER(Tox)]
    tox_self_get_connection_status.restype = TOX_CONNECTION

tox_self_connection_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), TOX_CONNECTION, POINTER(None)) # /usr/local/include/tox/tox.h: 647

# /usr/local/include/tox/tox.h: 660
if hasattr(_libs['toxcore'], 'tox_callback_self_connection_status'):
    tox_callback_self_connection_status = _libs['toxcore'].tox_callback_self_connection_status
    tox_callback_self_connection_status.argtypes = [POINTER(Tox), POINTER(tox_self_connection_status_cb), POINTER(None)]
    tox_callback_self_connection_status.restype = None

# /usr/local/include/tox/tox.h: 667
if hasattr(_libs['toxcore'], 'tox_iteration_interval'):
    tox_iteration_interval = _libs['toxcore'].tox_iteration_interval
    tox_iteration_interval.argtypes = [POINTER(Tox)]
    tox_iteration_interval.restype = c_uint32

# /usr/local/include/tox/tox.h: 674
if hasattr(_libs['toxcore'], 'tox_iterate'):
    tox_iterate = _libs['toxcore'].tox_iterate
    tox_iterate.argtypes = [POINTER(Tox)]
    tox_iterate.restype = None

# /usr/local/include/tox/tox.h: 693
if hasattr(_libs['toxcore'], 'tox_self_get_address'):
    tox_self_get_address = _libs['toxcore'].tox_self_get_address
    tox_self_get_address.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_address.restype = None

# /usr/local/include/tox/tox.h: 701
if hasattr(_libs['toxcore'], 'tox_self_set_nospam'):
    tox_self_set_nospam = _libs['toxcore'].tox_self_set_nospam
    tox_self_set_nospam.argtypes = [POINTER(Tox), c_uint32]
    tox_self_set_nospam.restype = None

# /usr/local/include/tox/tox.h: 706
if hasattr(_libs['toxcore'], 'tox_self_get_nospam'):
    tox_self_get_nospam = _libs['toxcore'].tox_self_get_nospam
    tox_self_get_nospam.argtypes = [POINTER(Tox)]
    tox_self_get_nospam.restype = c_uint32

# /usr/local/include/tox/tox.h: 714
if hasattr(_libs['toxcore'], 'tox_self_get_public_key'):
    tox_self_get_public_key = _libs['toxcore'].tox_self_get_public_key
    tox_self_get_public_key.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_public_key.restype = None

# /usr/local/include/tox/tox.h: 722
if hasattr(_libs['toxcore'], 'tox_self_get_secret_key'):
    tox_self_get_secret_key = _libs['toxcore'].tox_self_get_secret_key
    tox_self_get_secret_key.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_secret_key.restype = None

enum_TOX_ERR_SET_INFO = c_int # /usr/local/include/tox/tox.h: 743

TOX_ERR_SET_INFO_OK = 0 # /usr/local/include/tox/tox.h: 743

TOX_ERR_SET_INFO_NULL = (TOX_ERR_SET_INFO_OK + 1) # /usr/local/include/tox/tox.h: 743

TOX_ERR_SET_INFO_TOO_LONG = (TOX_ERR_SET_INFO_NULL + 1) # /usr/local/include/tox/tox.h: 743

TOX_ERR_SET_INFO = enum_TOX_ERR_SET_INFO # /usr/local/include/tox/tox.h: 743

# /usr/local/include/tox/tox.h: 757
if hasattr(_libs['toxcore'], 'tox_self_set_name'):
    tox_self_set_name = _libs['toxcore'].tox_self_set_name
    tox_self_set_name.argtypes = [POINTER(Tox), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_SET_INFO)]
    tox_self_set_name.restype = c_bool

# /usr/local/include/tox/tox.h: 767
if hasattr(_libs['toxcore'], 'tox_self_get_name_size'):
    tox_self_get_name_size = _libs['toxcore'].tox_self_get_name_size
    tox_self_get_name_size.argtypes = [POINTER(Tox)]
    tox_self_get_name_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 781
if hasattr(_libs['toxcore'], 'tox_self_get_name'):
    tox_self_get_name = _libs['toxcore'].tox_self_get_name
    tox_self_get_name.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_name.restype = None

# /usr/local/include/tox/tox.h: 790
if hasattr(_libs['toxcore'], 'tox_self_set_status_message'):
    tox_self_set_status_message = _libs['toxcore'].tox_self_set_status_message
    tox_self_set_status_message.argtypes = [POINTER(Tox), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_SET_INFO)]
    tox_self_set_status_message.restype = c_bool

# /usr/local/include/tox/tox.h: 801
if hasattr(_libs['toxcore'], 'tox_self_get_status_message_size'):
    tox_self_get_status_message_size = _libs['toxcore'].tox_self_get_status_message_size
    tox_self_get_status_message_size.argtypes = [POINTER(Tox)]
    tox_self_get_status_message_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 815
if hasattr(_libs['toxcore'], 'tox_self_get_status_message'):
    tox_self_get_status_message = _libs['toxcore'].tox_self_get_status_message
    tox_self_get_status_message.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_status_message.restype = None

# /usr/local/include/tox/tox.h: 823
if hasattr(_libs['toxcore'], 'tox_self_set_status'):
    tox_self_set_status = _libs['toxcore'].tox_self_set_status
    tox_self_set_status.argtypes = [POINTER(Tox), TOX_USER_STATUS]
    tox_self_set_status.restype = None

# /usr/local/include/tox/tox.h: 828
if hasattr(_libs['toxcore'], 'tox_self_get_status'):
    tox_self_get_status = _libs['toxcore'].tox_self_get_status
    tox_self_get_status.argtypes = [POINTER(Tox)]
    tox_self_get_status.restype = TOX_USER_STATUS

enum_TOX_ERR_FRIEND_ADD = c_int # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD_OK = 0 # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD_NULL = (TOX_ERR_FRIEND_ADD_OK + 1) # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD_TOO_LONG = (TOX_ERR_FRIEND_ADD_NULL + 1) # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD_NO_MESSAGE = (TOX_ERR_FRIEND_ADD_TOO_LONG + 1) # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD_OWN_KEY = (TOX_ERR_FRIEND_ADD_NO_MESSAGE + 1) # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD_ALREADY_SENT = (TOX_ERR_FRIEND_ADD_OWN_KEY + 1) # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD_BAD_CHECKSUM = (TOX_ERR_FRIEND_ADD_ALREADY_SENT + 1) # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD_SET_NEW_NOSPAM = (TOX_ERR_FRIEND_ADD_BAD_CHECKSUM + 1) # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD_MALLOC = (TOX_ERR_FRIEND_ADD_SET_NEW_NOSPAM + 1) # /usr/local/include/tox/tox.h: 872

TOX_ERR_FRIEND_ADD = enum_TOX_ERR_FRIEND_ADD # /usr/local/include/tox/tox.h: 872

# /usr/local/include/tox/tox.h: 896
if hasattr(_libs['toxcore'], 'tox_friend_add'):
    tox_friend_add = _libs['toxcore'].tox_friend_add
    tox_friend_add.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_ADD)]
    tox_friend_add.restype = c_uint32

# /usr/local/include/tox/tox.h: 918
if hasattr(_libs['toxcore'], 'tox_friend_add_norequest'):
    tox_friend_add_norequest = _libs['toxcore'].tox_friend_add_norequest
    tox_friend_add_norequest.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_ADD)]
    tox_friend_add_norequest.restype = c_uint32

enum_TOX_ERR_FRIEND_DELETE = c_int # /usr/local/include/tox/tox.h: 927

TOX_ERR_FRIEND_DELETE_OK = 0 # /usr/local/include/tox/tox.h: 927

TOX_ERR_FRIEND_DELETE_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_DELETE_OK + 1) # /usr/local/include/tox/tox.h: 927

TOX_ERR_FRIEND_DELETE = enum_TOX_ERR_FRIEND_DELETE # /usr/local/include/tox/tox.h: 927

# /usr/local/include/tox/tox.h: 940
if hasattr(_libs['toxcore'], 'tox_friend_delete'):
    tox_friend_delete = _libs['toxcore'].tox_friend_delete
    tox_friend_delete.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_DELETE)]
    tox_friend_delete.restype = c_bool

enum_TOX_ERR_FRIEND_BY_PUBLIC_KEY = c_int # /usr/local/include/tox/tox.h: 957

TOX_ERR_FRIEND_BY_PUBLIC_KEY_OK = 0 # /usr/local/include/tox/tox.h: 957

TOX_ERR_FRIEND_BY_PUBLIC_KEY_NULL = (TOX_ERR_FRIEND_BY_PUBLIC_KEY_OK + 1) # /usr/local/include/tox/tox.h: 957

TOX_ERR_FRIEND_BY_PUBLIC_KEY_NOT_FOUND = (TOX_ERR_FRIEND_BY_PUBLIC_KEY_NULL + 1) # /usr/local/include/tox/tox.h: 957

TOX_ERR_FRIEND_BY_PUBLIC_KEY = enum_TOX_ERR_FRIEND_BY_PUBLIC_KEY # /usr/local/include/tox/tox.h: 957

# /usr/local/include/tox/tox.h: 965
if hasattr(_libs['toxcore'], 'tox_friend_by_public_key'):
    tox_friend_by_public_key = _libs['toxcore'].tox_friend_by_public_key
    tox_friend_by_public_key.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_BY_PUBLIC_KEY)]
    tox_friend_by_public_key.restype = c_uint32

enum_TOX_ERR_FRIEND_GET_PUBLIC_KEY = c_int # /usr/local/include/tox/tox.h: 974

TOX_ERR_FRIEND_GET_PUBLIC_KEY_OK = 0 # /usr/local/include/tox/tox.h: 974

TOX_ERR_FRIEND_GET_PUBLIC_KEY_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_GET_PUBLIC_KEY_OK + 1) # /usr/local/include/tox/tox.h: 974

TOX_ERR_FRIEND_GET_PUBLIC_KEY = enum_TOX_ERR_FRIEND_GET_PUBLIC_KEY # /usr/local/include/tox/tox.h: 974

# /usr/local/include/tox/tox.h: 985
if hasattr(_libs['toxcore'], 'tox_friend_get_public_key'):
    tox_friend_get_public_key = _libs['toxcore'].tox_friend_get_public_key
    tox_friend_get_public_key.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_GET_PUBLIC_KEY)]
    tox_friend_get_public_key.restype = c_bool

# /usr/local/include/tox/tox.h: 993
if hasattr(_libs['toxcore'], 'tox_friend_exists'):
    tox_friend_exists = _libs['toxcore'].tox_friend_exists
    tox_friend_exists.argtypes = [POINTER(Tox), c_uint32]
    tox_friend_exists.restype = c_bool

# /usr/local/include/tox/tox.h: 1002
if hasattr(_libs['toxcore'], 'tox_self_get_friend_list_size'):
    tox_self_get_friend_list_size = _libs['toxcore'].tox_self_get_friend_list_size
    tox_self_get_friend_list_size.argtypes = [POINTER(Tox)]
    tox_self_get_friend_list_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 1013
if hasattr(_libs['toxcore'], 'tox_self_get_friend_list'):
    tox_self_get_friend_list = _libs['toxcore'].tox_self_get_friend_list
    tox_self_get_friend_list.argtypes = [POINTER(Tox), POINTER(c_uint32)]
    tox_self_get_friend_list.restype = None

enum_TOX_ERR_FRIEND_QUERY = c_int # /usr/local/include/tox/tox.h: 1039

TOX_ERR_FRIEND_QUERY_OK = 0 # /usr/local/include/tox/tox.h: 1039

TOX_ERR_FRIEND_QUERY_NULL = (TOX_ERR_FRIEND_QUERY_OK + 1) # /usr/local/include/tox/tox.h: 1039

TOX_ERR_FRIEND_QUERY_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_QUERY_NULL + 1) # /usr/local/include/tox/tox.h: 1039

TOX_ERR_FRIEND_QUERY = enum_TOX_ERR_FRIEND_QUERY # /usr/local/include/tox/tox.h: 1039

# /usr/local/include/tox/tox.h: 1049
if hasattr(_libs['toxcore'], 'tox_friend_get_name_size'):
    tox_friend_get_name_size = _libs['toxcore'].tox_friend_get_name_size
    tox_friend_get_name_size.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_name_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 1065
if hasattr(_libs['toxcore'], 'tox_friend_get_name'):
    tox_friend_get_name = _libs['toxcore'].tox_friend_get_name
    tox_friend_get_name.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_name.restype = c_bool

tox_friend_name_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1076

# /usr/local/include/tox/tox.h: 1083
if hasattr(_libs['toxcore'], 'tox_callback_friend_name'):
    tox_callback_friend_name = _libs['toxcore'].tox_callback_friend_name
    tox_callback_friend_name.argtypes = [POINTER(Tox), POINTER(tox_friend_name_cb), POINTER(None)]
    tox_callback_friend_name.restype = None

# /usr/local/include/tox/tox.h: 1090
if hasattr(_libs['toxcore'], 'tox_friend_get_status_message_size'):
    tox_friend_get_status_message_size = _libs['toxcore'].tox_friend_get_status_message_size
    tox_friend_get_status_message_size.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_status_message_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 1104
if hasattr(_libs['toxcore'], 'tox_friend_get_status_message'):
    tox_friend_get_status_message = _libs['toxcore'].tox_friend_get_status_message
    tox_friend_get_status_message.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_status_message.restype = c_bool

tox_friend_status_message_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1117

# /usr/local/include/tox/tox.h: 1125
if hasattr(_libs['toxcore'], 'tox_callback_friend_status_message'):
    tox_callback_friend_status_message = _libs['toxcore'].tox_callback_friend_status_message
    tox_callback_friend_status_message.argtypes = [POINTER(Tox), POINTER(tox_friend_status_message_cb), POINTER(None)]
    tox_callback_friend_status_message.restype = None

# /usr/local/include/tox/tox.h: 1135
if hasattr(_libs['toxcore'], 'tox_friend_get_status'):
    tox_friend_get_status = _libs['toxcore'].tox_friend_get_status
    tox_friend_get_status.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_status.restype = TOX_USER_STATUS

tox_friend_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_USER_STATUS, POINTER(None)) # /usr/local/include/tox/tox.h: 1144

# /usr/local/include/tox/tox.h: 1151
if hasattr(_libs['toxcore'], 'tox_callback_friend_status'):
    tox_callback_friend_status = _libs['toxcore'].tox_callback_friend_status
    tox_callback_friend_status.argtypes = [POINTER(Tox), POINTER(tox_friend_status_cb), POINTER(None)]
    tox_callback_friend_status.restype = None

# /usr/local/include/tox/tox.h: 1166
if hasattr(_libs['toxcore'], 'tox_friend_get_connection_status'):
    tox_friend_get_connection_status = _libs['toxcore'].tox_friend_get_connection_status
    tox_friend_get_connection_status.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_connection_status.restype = TOX_CONNECTION

tox_friend_connection_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_CONNECTION, POINTER(None)) # /usr/local/include/tox/tox.h: 1176

# /usr/local/include/tox/tox.h: 1189
if hasattr(_libs['toxcore'], 'tox_callback_friend_connection_status'):
    tox_callback_friend_connection_status = _libs['toxcore'].tox_callback_friend_connection_status
    tox_callback_friend_connection_status.argtypes = [POINTER(Tox), POINTER(tox_friend_connection_status_cb), POINTER(None)]
    tox_callback_friend_connection_status.restype = None

# /usr/local/include/tox/tox.h: 1201
if hasattr(_libs['toxcore'], 'tox_friend_get_typing'):
    tox_friend_get_typing = _libs['toxcore'].tox_friend_get_typing
    tox_friend_get_typing.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_typing.restype = c_bool

tox_friend_typing_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_bool, POINTER(None)) # /usr/local/include/tox/tox.h: 1211

# /usr/local/include/tox/tox.h: 1218
if hasattr(_libs['toxcore'], 'tox_callback_friend_typing'):
    tox_callback_friend_typing = _libs['toxcore'].tox_callback_friend_typing
    tox_callback_friend_typing.argtypes = [POINTER(Tox), POINTER(tox_friend_typing_cb), POINTER(None)]
    tox_callback_friend_typing.restype = None

enum_TOX_ERR_SET_TYPING = c_int # /usr/local/include/tox/tox.h: 1234

TOX_ERR_SET_TYPING_OK = 0 # /usr/local/include/tox/tox.h: 1234

TOX_ERR_SET_TYPING_FRIEND_NOT_FOUND = (TOX_ERR_SET_TYPING_OK + 1) # /usr/local/include/tox/tox.h: 1234

TOX_ERR_SET_TYPING = enum_TOX_ERR_SET_TYPING # /usr/local/include/tox/tox.h: 1234

# /usr/local/include/tox/tox.h: 1246
if hasattr(_libs['toxcore'], 'tox_self_set_typing'):
    tox_self_set_typing = _libs['toxcore'].tox_self_set_typing
    tox_self_set_typing.argtypes = [POINTER(Tox), c_uint32, c_bool, POINTER(TOX_ERR_SET_TYPING)]
    tox_self_set_typing.restype = c_bool

enum_TOX_ERR_FRIEND_SEND_MESSAGE = c_int # /usr/local/include/tox/tox.h: 1272

TOX_ERR_FRIEND_SEND_MESSAGE_OK = 0 # /usr/local/include/tox/tox.h: 1272

TOX_ERR_FRIEND_SEND_MESSAGE_NULL = (TOX_ERR_FRIEND_SEND_MESSAGE_OK + 1) # /usr/local/include/tox/tox.h: 1272

TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_SEND_MESSAGE_NULL + 1) # /usr/local/include/tox/tox.h: 1272

TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_CONNECTED = (TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1272

TOX_ERR_FRIEND_SEND_MESSAGE_SENDQ = (TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1272

TOX_ERR_FRIEND_SEND_MESSAGE_TOO_LONG = (TOX_ERR_FRIEND_SEND_MESSAGE_SENDQ + 1) # /usr/local/include/tox/tox.h: 1272

TOX_ERR_FRIEND_SEND_MESSAGE_EMPTY = (TOX_ERR_FRIEND_SEND_MESSAGE_TOO_LONG + 1) # /usr/local/include/tox/tox.h: 1272

TOX_ERR_FRIEND_SEND_MESSAGE = enum_TOX_ERR_FRIEND_SEND_MESSAGE # /usr/local/include/tox/tox.h: 1272

# /usr/local/include/tox/tox.h: 1293
if hasattr(_libs['toxcore'], 'tox_friend_send_message'):
    tox_friend_send_message = _libs['toxcore'].tox_friend_send_message
    tox_friend_send_message.argtypes = [POINTER(Tox), c_uint32, TOX_MESSAGE_TYPE, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_SEND_MESSAGE)]
    tox_friend_send_message.restype = c_uint32

tox_friend_read_receipt_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, POINTER(None)) # /usr/local/include/tox/tox.h: 1303

# /usr/local/include/tox/tox.h: 1311
if hasattr(_libs['toxcore'], 'tox_callback_friend_read_receipt'):
    tox_callback_friend_read_receipt = _libs['toxcore'].tox_callback_friend_read_receipt
    tox_callback_friend_read_receipt.argtypes = [POINTER(Tox), POINTER(tox_friend_read_receipt_cb), POINTER(None)]
    tox_callback_friend_read_receipt.restype = None

tox_friend_request_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1328

# /usr/local/include/tox/tox.h: 1336
if hasattr(_libs['toxcore'], 'tox_callback_friend_request'):
    tox_callback_friend_request = _libs['toxcore'].tox_callback_friend_request
    tox_callback_friend_request.argtypes = [POINTER(Tox), POINTER(tox_friend_request_cb), POINTER(None)]
    tox_callback_friend_request.restype = None

tox_friend_message_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_MESSAGE_TYPE, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1347

# /usr/local/include/tox/tox.h: 1355
if hasattr(_libs['toxcore'], 'tox_callback_friend_message'):
    tox_callback_friend_message = _libs['toxcore'].tox_callback_friend_message
    tox_callback_friend_message.argtypes = [POINTER(Tox), POINTER(tox_friend_message_cb), POINTER(None)]
    tox_callback_friend_message.restype = None

enum_TOX_FILE_KIND = c_int # /usr/local/include/tox/tox.h: 1365

TOX_FILE_KIND_DATA = 0 # /usr/local/include/tox/tox.h: 1365

TOX_FILE_KIND_AVATAR = (TOX_FILE_KIND_DATA + 1) # /usr/local/include/tox/tox.h: 1365

# /usr/local/include/tox/tox.h: 1414
if hasattr(_libs['toxcore'], 'tox_hash'):
    tox_hash = _libs['toxcore'].tox_hash
    tox_hash.argtypes = [POINTER(c_uint8), POINTER(c_uint8), c_size_t]
    tox_hash.restype = c_bool

enum_TOX_FILE_CONTROL = c_int # /usr/local/include/tox/tox.h: 1435

TOX_FILE_CONTROL_RESUME = 0 # /usr/local/include/tox/tox.h: 1435

TOX_FILE_CONTROL_PAUSE = (TOX_FILE_CONTROL_RESUME + 1) # /usr/local/include/tox/tox.h: 1435

TOX_FILE_CONTROL_CANCEL = (TOX_FILE_CONTROL_PAUSE + 1) # /usr/local/include/tox/tox.h: 1435

TOX_FILE_CONTROL = enum_TOX_FILE_CONTROL # /usr/local/include/tox/tox.h: 1435

enum_TOX_ERR_FILE_CONTROL = c_int # /usr/local/include/tox/tox.h: 1469

TOX_ERR_FILE_CONTROL_OK = 0 # /usr/local/include/tox/tox.h: 1469

TOX_ERR_FILE_CONTROL_FRIEND_NOT_FOUND = (TOX_ERR_FILE_CONTROL_OK + 1) # /usr/local/include/tox/tox.h: 1469

TOX_ERR_FILE_CONTROL_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_CONTROL_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1469

TOX_ERR_FILE_CONTROL_NOT_FOUND = (TOX_ERR_FILE_CONTROL_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1469

TOX_ERR_FILE_CONTROL_NOT_PAUSED = (TOX_ERR_FILE_CONTROL_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1469

TOX_ERR_FILE_CONTROL_DENIED = (TOX_ERR_FILE_CONTROL_NOT_PAUSED + 1) # /usr/local/include/tox/tox.h: 1469

TOX_ERR_FILE_CONTROL_ALREADY_PAUSED = (TOX_ERR_FILE_CONTROL_DENIED + 1) # /usr/local/include/tox/tox.h: 1469

TOX_ERR_FILE_CONTROL_SENDQ = (TOX_ERR_FILE_CONTROL_ALREADY_PAUSED + 1) # /usr/local/include/tox/tox.h: 1469

TOX_ERR_FILE_CONTROL = enum_TOX_ERR_FILE_CONTROL # /usr/local/include/tox/tox.h: 1469

# /usr/local/include/tox/tox.h: 1481
if hasattr(_libs['toxcore'], 'tox_file_control'):
    tox_file_control = _libs['toxcore'].tox_file_control
    tox_file_control.argtypes = [POINTER(Tox), c_uint32, c_uint32, TOX_FILE_CONTROL, POINTER(TOX_ERR_FILE_CONTROL)]
    tox_file_control.restype = c_bool

tox_file_recv_control_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, TOX_FILE_CONTROL, POINTER(None)) # /usr/local/include/tox/tox.h: 1496

# /usr/local/include/tox/tox.h: 1505
if hasattr(_libs['toxcore'], 'tox_callback_file_recv_control'):
    tox_callback_file_recv_control = _libs['toxcore'].tox_callback_file_recv_control
    tox_callback_file_recv_control.argtypes = [POINTER(Tox), POINTER(tox_file_recv_control_cb), POINTER(None)]
    tox_callback_file_recv_control.restype = None

enum_TOX_ERR_FILE_SEEK = c_int # /usr/local/include/tox/tox.h: 1534

TOX_ERR_FILE_SEEK_OK = 0 # /usr/local/include/tox/tox.h: 1534

TOX_ERR_FILE_SEEK_FRIEND_NOT_FOUND = (TOX_ERR_FILE_SEEK_OK + 1) # /usr/local/include/tox/tox.h: 1534

TOX_ERR_FILE_SEEK_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_SEEK_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1534

TOX_ERR_FILE_SEEK_NOT_FOUND = (TOX_ERR_FILE_SEEK_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1534

TOX_ERR_FILE_SEEK_DENIED = (TOX_ERR_FILE_SEEK_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1534

TOX_ERR_FILE_SEEK_INVALID_POSITION = (TOX_ERR_FILE_SEEK_DENIED + 1) # /usr/local/include/tox/tox.h: 1534

TOX_ERR_FILE_SEEK_SENDQ = (TOX_ERR_FILE_SEEK_INVALID_POSITION + 1) # /usr/local/include/tox/tox.h: 1534

TOX_ERR_FILE_SEEK = enum_TOX_ERR_FILE_SEEK # /usr/local/include/tox/tox.h: 1534

# /usr/local/include/tox/tox.h: 1547
if hasattr(_libs['toxcore'], 'tox_file_seek'):
    tox_file_seek = _libs['toxcore'].tox_file_seek
    tox_file_seek.argtypes = [POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(TOX_ERR_FILE_SEEK)]
    tox_file_seek.restype = c_bool

enum_TOX_ERR_FILE_GET = c_int # /usr/local/include/tox/tox.h: 1560

TOX_ERR_FILE_GET_OK = 0 # /usr/local/include/tox/tox.h: 1560

TOX_ERR_FILE_GET_FRIEND_NOT_FOUND = (TOX_ERR_FILE_GET_OK + 1) # /usr/local/include/tox/tox.h: 1560

TOX_ERR_FILE_GET_NOT_FOUND = (TOX_ERR_FILE_GET_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1560

TOX_ERR_FILE_GET = enum_TOX_ERR_FILE_GET # /usr/local/include/tox/tox.h: 1560

# /usr/local/include/tox/tox.h: 1573
if hasattr(_libs['toxcore'], 'tox_file_get_file_id'):
    tox_file_get_file_id = _libs['toxcore'].tox_file_get_file_id
    tox_file_get_file_id.argtypes = [POINTER(Tox), c_uint32, c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FILE_GET)]
    tox_file_get_file_id.restype = c_bool

enum_TOX_ERR_FILE_SEND = c_int # /usr/local/include/tox/tox.h: 1603

TOX_ERR_FILE_SEND_OK = 0 # /usr/local/include/tox/tox.h: 1603

TOX_ERR_FILE_SEND_NULL = (TOX_ERR_FILE_SEND_OK + 1) # /usr/local/include/tox/tox.h: 1603

TOX_ERR_FILE_SEND_FRIEND_NOT_FOUND = (TOX_ERR_FILE_SEND_NULL + 1) # /usr/local/include/tox/tox.h: 1603

TOX_ERR_FILE_SEND_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_SEND_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1603

TOX_ERR_FILE_SEND_NAME_TOO_LONG = (TOX_ERR_FILE_SEND_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1603

TOX_ERR_FILE_SEND_TOO_MANY = (TOX_ERR_FILE_SEND_NAME_TOO_LONG + 1) # /usr/local/include/tox/tox.h: 1603

TOX_ERR_FILE_SEND = enum_TOX_ERR_FILE_SEND # /usr/local/include/tox/tox.h: 1603

# /usr/local/include/tox/tox.h: 1662
if hasattr(_libs['toxcore'], 'tox_file_send'):
    tox_file_send = _libs['toxcore'].tox_file_send
    tox_file_send.argtypes = [POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FILE_SEND)]
    tox_file_send.restype = c_uint32

enum_TOX_ERR_FILE_SEND_CHUNK = c_int # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK_OK = 0 # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK_NULL = (TOX_ERR_FILE_SEND_CHUNK_OK + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_FOUND = (TOX_ERR_FILE_SEND_CHUNK_NULL + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK_NOT_FOUND = (TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK_NOT_TRANSFERRING = (TOX_ERR_FILE_SEND_CHUNK_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK_INVALID_LENGTH = (TOX_ERR_FILE_SEND_CHUNK_NOT_TRANSFERRING + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK_SENDQ = (TOX_ERR_FILE_SEND_CHUNK_INVALID_LENGTH + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK_WRONG_POSITION = (TOX_ERR_FILE_SEND_CHUNK_SENDQ + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_SEND_CHUNK = enum_TOX_ERR_FILE_SEND_CHUNK # /usr/local/include/tox/tox.h: 1703

# /usr/local/include/tox/tox.h: 1721
if hasattr(_libs['toxcore'], 'tox_file_send_chunk'):
    tox_file_send_chunk = _libs['toxcore'].tox_file_send_chunk
    tox_file_send_chunk.argtypes = [POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FILE_SEND_CHUNK)]
    tox_file_send_chunk.restype = c_bool

tox_file_chunk_request_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, c_uint64, c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1749

# /usr/local/include/tox/tox.h: 1755
if hasattr(_libs['toxcore'], 'tox_callback_file_chunk_request'):
    tox_callback_file_chunk_request = _libs['toxcore'].tox_callback_file_chunk_request
    tox_callback_file_chunk_request.argtypes = [POINTER(Tox), POINTER(tox_file_chunk_request_cb), POINTER(None)]
    tox_callback_file_chunk_request.restype = None

tox_file_recv_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, c_uint32, c_uint64, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1786

# /usr/local/include/tox/tox.h: 1794
if hasattr(_libs['toxcore'], 'tox_callback_file_recv'):
    tox_callback_file_recv = _libs['toxcore'].tox_callback_file_recv
    tox_callback_file_recv.argtypes = [POINTER(Tox), POINTER(tox_file_recv_cb), POINTER(None)]
    tox_callback_file_recv.restype = None

tox_file_recv_chunk_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1818

# /usr/local/include/tox/tox.h: 1824
if hasattr(_libs['toxcore'], 'tox_callback_file_recv_chunk'):
    tox_callback_file_recv_chunk = _libs['toxcore'].tox_callback_file_recv_chunk
    tox_callback_file_recv_chunk.argtypes = [POINTER(Tox), POINTER(tox_file_recv_chunk_cb), POINTER(None)]
    tox_callback_file_recv_chunk.restype = None

enum_TOX_ERR_FRIEND_CUSTOM_PACKET = c_int # /usr/local/include/tox/tox.h: 1877

TOX_ERR_FRIEND_CUSTOM_PACKET_OK = 0 # /usr/local/include/tox/tox.h: 1877

TOX_ERR_FRIEND_CUSTOM_PACKET_NULL = (TOX_ERR_FRIEND_CUSTOM_PACKET_OK + 1) # /usr/local/include/tox/tox.h: 1877

TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_CUSTOM_PACKET_NULL + 1) # /usr/local/include/tox/tox.h: 1877

TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_CONNECTED = (TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1877

TOX_ERR_FRIEND_CUSTOM_PACKET_INVALID = (TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1877

TOX_ERR_FRIEND_CUSTOM_PACKET_EMPTY = (TOX_ERR_FRIEND_CUSTOM_PACKET_INVALID + 1) # /usr/local/include/tox/tox.h: 1877

TOX_ERR_FRIEND_CUSTOM_PACKET_TOO_LONG = (TOX_ERR_FRIEND_CUSTOM_PACKET_EMPTY + 1) # /usr/local/include/tox/tox.h: 1877

TOX_ERR_FRIEND_CUSTOM_PACKET_SENDQ = (TOX_ERR_FRIEND_CUSTOM_PACKET_TOO_LONG + 1) # /usr/local/include/tox/tox.h: 1877

TOX_ERR_FRIEND_CUSTOM_PACKET = enum_TOX_ERR_FRIEND_CUSTOM_PACKET # /usr/local/include/tox/tox.h: 1877

# /usr/local/include/tox/tox.h: 1900
if hasattr(_libs['toxcore'], 'tox_friend_send_lossy_packet'):
    tox_friend_send_lossy_packet = _libs['toxcore'].tox_friend_send_lossy_packet
    tox_friend_send_lossy_packet.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_CUSTOM_PACKET)]
    tox_friend_send_lossy_packet.restype = c_bool

tox_friend_lossy_packet_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1910

# /usr/local/include/tox/tox.h: 1916
if hasattr(_libs['toxcore'], 'tox_callback_friend_lossy_packet'):
    tox_callback_friend_lossy_packet = _libs['toxcore'].tox_callback_friend_lossy_packet
    tox_callback_friend_lossy_packet.argtypes = [POINTER(Tox), POINTER(tox_friend_lossy_packet_cb), POINTER(None)]
    tox_callback_friend_lossy_packet.restype = None

# /usr/local/include/tox/tox.h: 1935
if hasattr(_libs['toxcore'], 'tox_friend_send_lossless_packet'):
    tox_friend_send_lossless_packet = _libs['toxcore'].tox_friend_send_lossless_packet
    tox_friend_send_lossless_packet.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_CUSTOM_PACKET)]
    tox_friend_send_lossless_packet.restype = c_bool

tox_friend_lossless_packet_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1945

# /usr/local/include/tox/tox.h: 1951
if hasattr(_libs['toxcore'], 'tox_callback_friend_lossless_packet'):
    tox_callback_friend_lossless_packet = _libs['toxcore'].tox_callback_friend_lossless_packet
    tox_callback_friend_lossless_packet.argtypes = [POINTER(Tox), POINTER(tox_friend_lossless_packet_cb), POINTER(None)]
    tox_callback_friend_lossless_packet.restype = None

# /usr/local/include/tox/tox.h: 1974
if hasattr(_libs['toxcore'], 'tox_self_get_dht_id'):
    tox_self_get_dht_id = _libs['toxcore'].tox_self_get_dht_id
    tox_self_get_dht_id.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_dht_id.restype = None

enum_TOX_ERR_GET_PORT = c_int # /usr/local/include/tox/tox.h: 1983

TOX_ERR_GET_PORT_OK = 0 # /usr/local/include/tox/tox.h: 1983

TOX_ERR_GET_PORT_NOT_BOUND = (TOX_ERR_GET_PORT_OK + 1) # /usr/local/include/tox/tox.h: 1983

TOX_ERR_GET_PORT = enum_TOX_ERR_GET_PORT # /usr/local/include/tox/tox.h: 1983

# /usr/local/include/tox/tox.h: 1988
if hasattr(_libs['toxcore'], 'tox_self_get_udp_port'):
    tox_self_get_udp_port = _libs['toxcore'].tox_self_get_udp_port
    tox_self_get_udp_port.argtypes = [POINTER(Tox), POINTER(TOX_ERR_GET_PORT)]
    tox_self_get_udp_port.restype = c_uint16

# /usr/local/include/tox/tox.h: 1994
if hasattr(_libs['toxcore'], 'tox_self_get_tcp_port'):
    tox_self_get_tcp_port = _libs['toxcore'].tox_self_get_tcp_port
    tox_self_get_tcp_port.argtypes = [POINTER(Tox), POINTER(TOX_ERR_GET_PORT)]
    tox_self_get_tcp_port.restype = c_uint16

# /usr/local/include/tox/toxdns.h: 56
if hasattr(_libs['toxdns'], 'tox_dns3_new'):
    tox_dns3_new = _libs['toxdns'].tox_dns3_new
    tox_dns3_new.argtypes = [POINTER(c_uint8)]
    tox_dns3_new.restype = POINTER(None)

# /usr/local/include/tox/toxdns.h: 60
if hasattr(_libs['toxdns'], 'tox_dns3_kill'):
    tox_dns3_kill = _libs['toxdns'].tox_dns3_kill
    tox_dns3_kill.argtypes = [POINTER(None)]
    tox_dns3_kill.restype = None

# /usr/local/include/tox/toxdns.h: 74
if hasattr(_libs['toxdns'], 'tox_generate_dns3_string'):
    tox_generate_dns3_string = _libs['toxdns'].tox_generate_dns3_string
    tox_generate_dns3_string.argtypes = [POINTER(None), POINTER(c_uint8), c_uint16, POINTER(c_uint32), POINTER(c_uint8), c_uint8]
    tox_generate_dns3_string.restype = c_int

# /usr/local/include/tox/toxdns.h: 89
if hasattr(_libs['toxdns'], 'tox_decrypt_dns3_TXT'):
    tox_decrypt_dns3_TXT = _libs['toxdns'].tox_decrypt_dns3_TXT
    tox_decrypt_dns3_TXT.argtypes = [POINTER(None), POINTER(c_uint8), POINTER(c_uint8), c_uint32, c_uint32]
    tox_decrypt_dns3_TXT.restype = c_int

# /usr/local/include/tox/toxav.h: 31
class struct__ToxAv(Structure):
    pass

ToxAv = struct__ToxAv # /usr/local/include/tox/toxav.h: 31

enum_vpx_img_fmt = c_int # /usr/include/vpx/vpx_image.h: 62

vpx_img_fmt_t = enum_vpx_img_fmt # /usr/include/vpx/vpx_image.h: 62

# /usr/include/vpx/vpx_image.h: 142
class struct_vpx_image(Structure):
    pass

struct_vpx_image.__slots__ = [
    'fmt',
    'w',
    'h',
    'd_w',
    'd_h',
    'x_chroma_shift',
    'y_chroma_shift',
    'planes',
    'stride',
    'bps',
    'user_priv',
    'img_data',
    'img_data_owner',
    'self_allocd',
]
struct_vpx_image._fields_ = [
    ('fmt', vpx_img_fmt_t),
    ('w', c_uint),
    ('h', c_uint),
    ('d_w', c_uint),
    ('d_h', c_uint),
    ('x_chroma_shift', c_uint),
    ('y_chroma_shift', c_uint),
    ('planes', POINTER(c_ubyte) * 4),
    ('stride', c_int * 4),
    ('bps', c_int),
    ('user_priv', POINTER(None)),
    ('img_data', POINTER(c_ubyte)),
    ('img_data_owner', c_int),
    ('self_allocd', c_int),
]

vpx_image_t = struct_vpx_image # /usr/include/vpx/vpx_image.h: 142

ToxAVCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int32, POINTER(None)) # /usr/local/include/tox/toxav.h: 36

ToxAvAudioCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int32, POINTER(c_int16), c_uint16, POINTER(None)) # /usr/local/include/tox/toxav.h: 37

ToxAvVideoCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int32, POINTER(vpx_image_t), POINTER(None)) # /usr/local/include/tox/toxav.h: 38

enum_anon_4 = c_int # /usr/local/include/tox/toxav.h: 62

av_OnInvite = 0 # /usr/local/include/tox/toxav.h: 62

av_OnRinging = (av_OnInvite + 1) # /usr/local/include/tox/toxav.h: 62

av_OnStart = (av_OnRinging + 1) # /usr/local/include/tox/toxav.h: 62

av_OnCancel = (av_OnStart + 1) # /usr/local/include/tox/toxav.h: 62

av_OnReject = (av_OnCancel + 1) # /usr/local/include/tox/toxav.h: 62

av_OnEnd = (av_OnReject + 1) # /usr/local/include/tox/toxav.h: 62

av_OnRequestTimeout = (av_OnEnd + 1) # /usr/local/include/tox/toxav.h: 62

av_OnPeerTimeout = (av_OnRequestTimeout + 1) # /usr/local/include/tox/toxav.h: 62

av_OnPeerCSChange = (av_OnPeerTimeout + 1) # /usr/local/include/tox/toxav.h: 62

av_OnSelfCSChange = (av_OnPeerCSChange + 1) # /usr/local/include/tox/toxav.h: 62

ToxAvCallbackID = enum_anon_4 # /usr/local/include/tox/toxav.h: 62

enum_anon_5 = c_int # /usr/local/include/tox/toxav.h: 71

av_TypeAudio = 192 # /usr/local/include/tox/toxav.h: 71

av_TypeVideo = (av_TypeAudio + 1) # /usr/local/include/tox/toxav.h: 71

ToxAvCallType = enum_anon_5 # /usr/local/include/tox/toxav.h: 71

enum_anon_6 = c_int # /usr/local/include/tox/toxav.h: 81

av_CallNonExistent = (-1) # /usr/local/include/tox/toxav.h: 81

av_CallInviting = (av_CallNonExistent + 1) # /usr/local/include/tox/toxav.h: 81

av_CallStarting = (av_CallInviting + 1) # /usr/local/include/tox/toxav.h: 81

av_CallActive = (av_CallStarting + 1) # /usr/local/include/tox/toxav.h: 81

av_CallHold = (av_CallActive + 1) # /usr/local/include/tox/toxav.h: 81

av_CallHungUp = (av_CallHold + 1) # /usr/local/include/tox/toxav.h: 81

ToxAvCallState = enum_anon_6 # /usr/local/include/tox/toxav.h: 81

enum_anon_7 = c_int # /usr/local/include/tox/toxav.h: 104

av_ErrorNone = 0 # /usr/local/include/tox/toxav.h: 104

av_ErrorUnknown = (-1) # /usr/local/include/tox/toxav.h: 104

av_ErrorNoCall = (-20) # /usr/local/include/tox/toxav.h: 104

av_ErrorInvalidState = (-21) # /usr/local/include/tox/toxav.h: 104

av_ErrorAlreadyInCallWithPeer = (-22) # /usr/local/include/tox/toxav.h: 104

av_ErrorReachedCallLimit = (-23) # /usr/local/include/tox/toxav.h: 104

av_ErrorInitializingCodecs = (-30) # /usr/local/include/tox/toxav.h: 104

av_ErrorSettingVideoResolution = (-31) # /usr/local/include/tox/toxav.h: 104

av_ErrorSettingVideoBitrate = (-32) # /usr/local/include/tox/toxav.h: 104

av_ErrorSplittingVideoPayload = (-33) # /usr/local/include/tox/toxav.h: 104

av_ErrorEncodingVideo = (-34) # /usr/local/include/tox/toxav.h: 104

av_ErrorEncodingAudio = (-35) # /usr/local/include/tox/toxav.h: 104

av_ErrorSendingPayload = (-40) # /usr/local/include/tox/toxav.h: 104

av_ErrorCreatingRtpSessions = (-41) # /usr/local/include/tox/toxav.h: 104

av_ErrorNoRtpSession = (-50) # /usr/local/include/tox/toxav.h: 104

av_ErrorInvalidCodecState = (-51) # /usr/local/include/tox/toxav.h: 104

av_ErrorPacketTooLarge = (-52) # /usr/local/include/tox/toxav.h: 104

ToxAvError = enum_anon_7 # /usr/local/include/tox/toxav.h: 104

enum_anon_8 = c_int # /usr/local/include/tox/toxav.h: 115

av_AudioEncoding = (1 << 0) # /usr/local/include/tox/toxav.h: 115

av_AudioDecoding = (1 << 1) # /usr/local/include/tox/toxav.h: 115

av_VideoEncoding = (1 << 2) # /usr/local/include/tox/toxav.h: 115

av_VideoDecoding = (1 << 3) # /usr/local/include/tox/toxav.h: 115

ToxAvCapabilities = enum_anon_8 # /usr/local/include/tox/toxav.h: 115

# /usr/local/include/tox/toxav.h: 132
class struct__ToxAvCSettings(Structure):
    pass

struct__ToxAvCSettings.__slots__ = [
    'call_type',
    'video_bitrate',
    'max_video_width',
    'max_video_height',
    'audio_bitrate',
    'audio_frame_duration',
    'audio_sample_rate',
    'audio_channels',
]
struct__ToxAvCSettings._fields_ = [
    ('call_type', ToxAvCallType),
    ('video_bitrate', c_uint32),
    ('max_video_width', c_uint16),
    ('max_video_height', c_uint16),
    ('audio_bitrate', c_uint32),
    ('audio_frame_duration', c_uint16),
    ('audio_sample_rate', c_uint32),
    ('audio_channels', c_uint32),
]

ToxAvCSettings = struct__ToxAvCSettings # /usr/local/include/tox/toxav.h: 132

# /usr/local/include/tox/toxav.h: 134
try:
    av_DefaultSettings = (ToxAvCSettings).in_dll(_libs['toxav'], 'av_DefaultSettings')
except:
    pass

# /usr/local/include/tox/toxav.h: 139
if hasattr(_libs['toxav'], 'toxav_new'):
    toxav_new = _libs['toxav'].toxav_new
    toxav_new.argtypes = [POINTER(Tox), c_int32]
    toxav_new.restype = POINTER(ToxAv)

# /usr/local/include/tox/toxav.h: 144
if hasattr(_libs['toxav'], 'toxav_kill'):
    toxav_kill = _libs['toxav'].toxav_kill
    toxav_kill.argtypes = [POINTER(ToxAv)]
    toxav_kill.restype = None

# /usr/local/include/tox/toxav.h: 150
if hasattr(_libs['toxav'], 'toxav_do_interval'):
    toxav_do_interval = _libs['toxav'].toxav_do_interval
    toxav_do_interval.argtypes = [POINTER(ToxAv)]
    toxav_do_interval.restype = c_uint32

# /usr/local/include/tox/toxav.h: 155
if hasattr(_libs['toxav'], 'toxav_do'):
    toxav_do = _libs['toxav'].toxav_do
    toxav_do.argtypes = [POINTER(ToxAv)]
    toxav_do.restype = None

# /usr/local/include/tox/toxav.h: 160
if hasattr(_libs['toxav'], 'toxav_register_callstate_callback'):
    toxav_register_callstate_callback = _libs['toxav'].toxav_register_callstate_callback
    toxav_register_callstate_callback.argtypes = [POINTER(ToxAv), ToxAVCallback, ToxAvCallbackID, POINTER(None)]
    toxav_register_callstate_callback.restype = None

# /usr/local/include/tox/toxav.h: 165
if hasattr(_libs['toxav'], 'toxav_register_audio_callback'):
    toxav_register_audio_callback = _libs['toxav'].toxav_register_audio_callback
    toxav_register_audio_callback.argtypes = [POINTER(ToxAv), ToxAvAudioCallback, POINTER(None)]
    toxav_register_audio_callback.restype = None

# /usr/local/include/tox/toxav.h: 170
if hasattr(_libs['toxav'], 'toxav_register_video_callback'):
    toxav_register_video_callback = _libs['toxav'].toxav_register_video_callback
    toxav_register_video_callback.argtypes = [POINTER(ToxAv), ToxAvVideoCallback, POINTER(None)]
    toxav_register_video_callback.restype = None

# /usr/local/include/tox/toxav.h: 175
if hasattr(_libs['toxav'], 'toxav_call'):
    toxav_call = _libs['toxav'].toxav_call
    toxav_call.argtypes = [POINTER(ToxAv), POINTER(c_int32), c_int, POINTER(ToxAvCSettings), c_int]
    toxav_call.restype = c_int

# /usr/local/include/tox/toxav.h: 184
if hasattr(_libs['toxav'], 'toxav_hangup'):
    toxav_hangup = _libs['toxav'].toxav_hangup
    toxav_hangup.argtypes = [POINTER(ToxAv), c_int32]
    toxav_hangup.restype = c_int

# /usr/local/include/tox/toxav.h: 189
if hasattr(_libs['toxav'], 'toxav_answer'):
    toxav_answer = _libs['toxav'].toxav_answer
    toxav_answer.argtypes = [POINTER(ToxAv), c_int32, POINTER(ToxAvCSettings)]
    toxav_answer.restype = c_int

# /usr/local/include/tox/toxav.h: 194
if hasattr(_libs['toxav'], 'toxav_reject'):
    toxav_reject = _libs['toxav'].toxav_reject
    toxav_reject.argtypes = [POINTER(ToxAv), c_int32, String]
    toxav_reject.restype = c_int

# /usr/local/include/tox/toxav.h: 199
if hasattr(_libs['toxav'], 'toxav_cancel'):
    toxav_cancel = _libs['toxav'].toxav_cancel
    toxav_cancel.argtypes = [POINTER(ToxAv), c_int32, c_int, String]
    toxav_cancel.restype = c_int

# /usr/local/include/tox/toxav.h: 204
if hasattr(_libs['toxav'], 'toxav_change_settings'):
    toxav_change_settings = _libs['toxav'].toxav_change_settings
    toxav_change_settings.argtypes = [POINTER(ToxAv), c_int32, POINTER(ToxAvCSettings)]
    toxav_change_settings.restype = c_int

# /usr/local/include/tox/toxav.h: 210
if hasattr(_libs['toxav'], 'toxav_stop_call'):
    toxav_stop_call = _libs['toxav'].toxav_stop_call
    toxav_stop_call.argtypes = [POINTER(ToxAv), c_int32]
    toxav_stop_call.restype = c_int

# /usr/local/include/tox/toxav.h: 216
if hasattr(_libs['toxav'], 'toxav_prepare_transmission'):
    toxav_prepare_transmission = _libs['toxav'].toxav_prepare_transmission
    toxav_prepare_transmission.argtypes = [POINTER(ToxAv), c_int32, c_int]
    toxav_prepare_transmission.restype = c_int

# /usr/local/include/tox/toxav.h: 221
if hasattr(_libs['toxav'], 'toxav_kill_transmission'):
    toxav_kill_transmission = _libs['toxav'].toxav_kill_transmission
    toxav_kill_transmission.argtypes = [POINTER(ToxAv), c_int32]
    toxav_kill_transmission.restype = c_int

# /usr/local/include/tox/toxav.h: 226
if hasattr(_libs['toxav'], 'toxav_prepare_video_frame'):
    toxav_prepare_video_frame = _libs['toxav'].toxav_prepare_video_frame
    toxav_prepare_video_frame.argtypes = [POINTER(ToxAv), c_int32, POINTER(c_uint8), c_int, POINTER(vpx_image_t)]
    toxav_prepare_video_frame.restype = c_int

# /usr/local/include/tox/toxav.h: 235
if hasattr(_libs['toxav'], 'toxav_send_video'):
    toxav_send_video = _libs['toxav'].toxav_send_video
    toxav_send_video.argtypes = [POINTER(ToxAv), c_int32, POINTER(c_uint8), c_uint32]
    toxav_send_video.restype = c_int

# /usr/local/include/tox/toxav.h: 240
if hasattr(_libs['toxav'], 'toxav_prepare_audio_frame'):
    toxav_prepare_audio_frame = _libs['toxav'].toxav_prepare_audio_frame
    toxav_prepare_audio_frame.argtypes = [POINTER(ToxAv), c_int32, POINTER(c_uint8), c_int, POINTER(c_int16), c_int]
    toxav_prepare_audio_frame.restype = c_int

# /usr/local/include/tox/toxav.h: 250
if hasattr(_libs['toxav'], 'toxav_send_audio'):
    toxav_send_audio = _libs['toxav'].toxav_send_audio
    toxav_send_audio.argtypes = [POINTER(ToxAv), c_int32, POINTER(c_uint8), c_uint]
    toxav_send_audio.restype = c_int

# /usr/local/include/tox/toxav.h: 256
if hasattr(_libs['toxav'], 'toxav_get_peer_csettings'):
    toxav_get_peer_csettings = _libs['toxav'].toxav_get_peer_csettings
    toxav_get_peer_csettings.argtypes = [POINTER(ToxAv), c_int32, c_int, POINTER(ToxAvCSettings)]
    toxav_get_peer_csettings.restype = c_int

# /usr/local/include/tox/toxav.h: 261
if hasattr(_libs['toxav'], 'toxav_get_peer_id'):
    toxav_get_peer_id = _libs['toxav'].toxav_get_peer_id
    toxav_get_peer_id.argtypes = [POINTER(ToxAv), c_int32, c_int]
    toxav_get_peer_id.restype = c_int

# /usr/local/include/tox/toxav.h: 266
if hasattr(_libs['toxav'], 'toxav_get_call_state'):
    toxav_get_call_state = _libs['toxav'].toxav_get_call_state
    toxav_get_call_state.argtypes = [POINTER(ToxAv), c_int32]
    toxav_get_call_state.restype = ToxAvCallState

# /usr/local/include/tox/toxav.h: 271
if hasattr(_libs['toxav'], 'toxav_capability_supported'):
    toxav_capability_supported = _libs['toxav'].toxav_capability_supported
    toxav_capability_supported.argtypes = [POINTER(ToxAv), c_int32, ToxAvCapabilities]
    toxav_capability_supported.restype = c_int

# /usr/local/include/tox/toxav.h: 276
if hasattr(_libs['toxav'], 'toxav_get_tox'):
    toxav_get_tox = _libs['toxav'].toxav_get_tox
    toxav_get_tox.argtypes = [POINTER(ToxAv)]
    toxav_get_tox.restype = POINTER(Tox)

# /usr/local/include/tox/toxav.h: 281
if hasattr(_libs['toxav'], 'toxav_get_active_count'):
    toxav_get_active_count = _libs['toxav'].toxav_get_active_count
    toxav_get_active_count.argtypes = [POINTER(ToxAv)]
    toxav_get_active_count.restype = c_int

# /usr/local/include/tox/toxav.h: 293
if hasattr(_libs['toxav'], 'toxav_add_av_groupchat'):
    toxav_add_av_groupchat = _libs['toxav'].toxav_add_av_groupchat
    toxav_add_av_groupchat.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int, c_int, POINTER(c_int16), c_uint, c_uint8, c_uint, POINTER(None)), POINTER(None)]
    toxav_add_av_groupchat.restype = c_int

# /usr/local/include/tox/toxav.h: 306
if hasattr(_libs['toxav'], 'toxav_join_av_groupchat'):
    toxav_join_av_groupchat = _libs['toxav'].toxav_join_av_groupchat
    toxav_join_av_groupchat.argtypes = [POINTER(Tox), c_int32, POINTER(c_uint8), c_uint16, CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int, c_int, POINTER(c_int16), c_uint, c_uint8, c_uint, POINTER(None)), POINTER(None)]
    toxav_join_av_groupchat.restype = c_int

# /usr/local/include/tox/toxav.h: 322
if hasattr(_libs['toxav'], 'toxav_group_send_audio'):
    toxav_group_send_audio = _libs['toxav'].toxav_group_send_audio
    toxav_group_send_audio.argtypes = [POINTER(Tox), c_int, POINTER(c_int16), c_uint, c_uint8, c_uint]
    toxav_group_send_audio.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 42
if hasattr(_libs['toxencryptsave'], 'tox_pass_encryption_extra_length'):
    tox_pass_encryption_extra_length = _libs['toxencryptsave'].tox_pass_encryption_extra_length
    tox_pass_encryption_extra_length.argtypes = []
    tox_pass_encryption_extra_length.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 44
if hasattr(_libs['toxencryptsave'], 'tox_pass_key_length'):
    tox_pass_key_length = _libs['toxencryptsave'].tox_pass_key_length
    tox_pass_key_length.argtypes = []
    tox_pass_key_length.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 46
if hasattr(_libs['toxencryptsave'], 'tox_pass_salt_length'):
    tox_pass_salt_length = _libs['toxencryptsave'].tox_pass_salt_length
    tox_pass_salt_length.argtypes = []
    tox_pass_salt_length.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 49
if hasattr(_libs['toxencryptsave'], 'tox_encrypted_size'):
    tox_encrypted_size = _libs['toxencryptsave'].tox_encrypted_size
    tox_encrypted_size.argtypes = [POINTER(Tox)]
    tox_encrypted_size.restype = c_uint32

# /usr/local/include/tox/toxencryptsave.h: 88
if hasattr(_libs['toxencryptsave'], 'tox_pass_encrypt'):
    tox_pass_encrypt = _libs['toxencryptsave'].tox_pass_encrypt
    tox_pass_encrypt.argtypes = [POINTER(c_uint8), c_uint32, POINTER(c_uint8), c_uint32, POINTER(c_uint8)]
    tox_pass_encrypt.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 99
if hasattr(_libs['toxencryptsave'], 'tox_encrypted_save'):
    tox_encrypted_save = _libs['toxencryptsave'].tox_encrypted_save
    tox_encrypted_save.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8), c_uint32]
    tox_encrypted_save.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 110
if hasattr(_libs['toxencryptsave'], 'tox_pass_decrypt'):
    tox_pass_decrypt = _libs['toxencryptsave'].tox_pass_decrypt
    tox_pass_decrypt.argtypes = [POINTER(c_uint8), c_uint32, POINTER(c_uint8), c_uint32, POINTER(c_uint8)]
    tox_pass_decrypt.restype = c_int

enum_TOX_ERR_ENCRYPTED_NEW = c_int # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_OK = 0 # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_NULL = (TOX_ERR_ENCRYPTED_NEW_OK + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_MALLOC = (TOX_ERR_ENCRYPTED_NEW_NULL + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_PORT_ALLOC = (TOX_ERR_ENCRYPTED_NEW_MALLOC + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_PROXY_BAD_TYPE = (TOX_ERR_ENCRYPTED_NEW_PORT_ALLOC + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_PROXY_BAD_HOST = (TOX_ERR_ENCRYPTED_NEW_PROXY_BAD_TYPE + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_PROXY_BAD_PORT = (TOX_ERR_ENCRYPTED_NEW_PROXY_BAD_HOST + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_PROXY_NOT_FOUND = (TOX_ERR_ENCRYPTED_NEW_PROXY_BAD_PORT + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_LOAD_ENCRYPTED = (TOX_ERR_ENCRYPTED_NEW_PROXY_NOT_FOUND + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_LOAD_BAD_FORMAT = (TOX_ERR_ENCRYPTED_NEW_LOAD_ENCRYPTED + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW_LOAD_DECRYPTION_FAILED = (TOX_ERR_ENCRYPTED_NEW_LOAD_BAD_FORMAT + 1) # /usr/local/include/tox/toxencryptsave.h: 163

TOX_ERR_ENCRYPTED_NEW = enum_TOX_ERR_ENCRYPTED_NEW # /usr/local/include/tox/toxencryptsave.h: 163

# /usr/local/include/tox/toxencryptsave.h: 170
if hasattr(_libs['toxencryptsave'], 'tox_encrypted_new'):
    tox_encrypted_new = _libs['toxencryptsave'].tox_encrypted_new
    tox_encrypted_new.argtypes = [POINTER(struct_Tox_Options), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_ENCRYPTED_NEW)]
    tox_encrypted_new.restype = POINTER(Tox)

# /usr/local/include/tox/toxencryptsave.h: 191
if hasattr(_libs['toxencryptsave'], 'tox_derive_key_from_pass'):
    tox_derive_key_from_pass = _libs['toxencryptsave'].tox_derive_key_from_pass
    tox_derive_key_from_pass.argtypes = [POINTER(c_uint8), c_uint32, POINTER(c_uint8)]
    tox_derive_key_from_pass.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 196
if hasattr(_libs['toxencryptsave'], 'tox_derive_key_with_salt'):
    tox_derive_key_with_salt = _libs['toxencryptsave'].tox_derive_key_with_salt
    tox_derive_key_with_salt.argtypes = [POINTER(c_uint8), c_uint32, POINTER(c_uint8), POINTER(c_uint8)]
    tox_derive_key_with_salt.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 205
if hasattr(_libs['toxencryptsave'], 'tox_get_salt'):
    tox_get_salt = _libs['toxencryptsave'].tox_get_salt
    tox_get_salt.argtypes = [POINTER(c_uint8), POINTER(c_uint8)]
    tox_get_salt.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 218
if hasattr(_libs['toxencryptsave'], 'tox_pass_key_encrypt'):
    tox_pass_key_encrypt = _libs['toxencryptsave'].tox_pass_key_encrypt
    tox_pass_key_encrypt.argtypes = [POINTER(c_uint8), c_uint32, POINTER(c_uint8), POINTER(c_uint8)]
    tox_pass_key_encrypt.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 229
if hasattr(_libs['toxencryptsave'], 'tox_encrypted_key_save'):
    tox_encrypted_key_save = _libs['toxencryptsave'].tox_encrypted_key_save
    tox_encrypted_key_save.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8)]
    tox_encrypted_key_save.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 237
if hasattr(_libs['toxencryptsave'], 'tox_pass_key_decrypt'):
    tox_pass_key_decrypt = _libs['toxencryptsave'].tox_pass_key_decrypt
    tox_pass_key_decrypt.argtypes = [POINTER(c_uint8), c_uint32, POINTER(c_uint8), POINTER(c_uint8)]
    tox_pass_key_decrypt.restype = c_int

# /usr/local/include/tox/toxencryptsave.h: 244
if hasattr(_libs['toxencryptsave'], 'tox_encrypted_key_new'):
    tox_encrypted_key_new = _libs['toxencryptsave'].tox_encrypted_key_new
    tox_encrypted_key_new.argtypes = [POINTER(struct_Tox_Options), POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(TOX_ERR_ENCRYPTED_NEW)]
    tox_encrypted_key_new.restype = POINTER(Tox)

# /usr/local/include/tox/toxencryptsave.h: 253
if hasattr(_libs['toxencryptsave'], 'tox_is_data_encrypted'):
    tox_is_data_encrypted = _libs['toxencryptsave'].tox_is_data_encrypted
    tox_is_data_encrypted.argtypes = [POINTER(c_uint8)]
    tox_is_data_encrypted.restype = c_int

# /usr/local/include/tox/tox.h: 139
TOX_VERSION_MAJOR = 0

# /usr/local/include/tox/tox.h: 145
TOX_VERSION_MINOR = 0

# /usr/local/include/tox/tox.h: 150
TOX_VERSION_PATCH = 0

# /usr/local/include/tox/tox.h: 156
def TOX_VERSION_IS_API_COMPATIBLE(MAJOR, MINOR, PATCH):
    return ((TOX_VERSION_MAJOR == MAJOR) and ((TOX_VERSION_MINOR > MINOR) or ((TOX_VERSION_MINOR == MINOR) and (TOX_VERSION_PATCH >= PATCH))))

# /usr/local/include/tox/tox.h: 197
TOX_VERSION_IS_ABI_COMPATIBLE = (tox_version_is_compatible (TOX_VERSION_MAJOR, TOX_VERSION_MINOR, TOX_VERSION_PATCH))

# /usr/local/include/tox/tox.h: 211
TOX_PUBLIC_KEY_SIZE = 32

# /usr/local/include/tox/tox.h: 216
TOX_SECRET_KEY_SIZE = 32

# /usr/local/include/tox/tox.h: 226
TOX_ADDRESS_SIZE = ((TOX_PUBLIC_KEY_SIZE + sizeof(c_uint32)) + sizeof(c_uint16))

# /usr/local/include/tox/tox.h: 231
TOX_MAX_NAME_LENGTH = 128

# /usr/local/include/tox/tox.h: 236
TOX_MAX_STATUS_MESSAGE_LENGTH = 1007

# /usr/local/include/tox/tox.h: 241
TOX_MAX_FRIEND_REQUEST_LENGTH = 1016

# /usr/local/include/tox/tox.h: 246
TOX_MAX_MESSAGE_LENGTH = 1372

# /usr/local/include/tox/tox.h: 251
TOX_MAX_CUSTOM_PACKET_SIZE = 1373

# /usr/local/include/tox/tox.h: 256
TOX_HASH_LENGTH = 32

# /usr/local/include/tox/tox.h: 261
TOX_FILE_ID_LENGTH = 32

# /usr/local/include/tox/tox.h: 266
TOX_MAX_FILENAME_LENGTH = 255

# /usr/local/include/tox/toxdns.h: 34
TOXDNS_MAX_RECOMMENDED_NAME_LENGTH = 32

# /usr/local/include/tox/toxav.h: 45
RTP_PAYLOAD_SIZE = 65535

Tox = struct_Tox # /usr/local/include/tox/tox.h: 124

Tox_Options = struct_Tox_Options # /usr/local/include/tox/tox.h: 339

_ToxAv = struct__ToxAv # /usr/local/include/tox/toxav.h: 31

_ToxAvCSettings = struct__ToxAvCSettings # /usr/local/include/tox/toxav.h: 132

# No inserted files

