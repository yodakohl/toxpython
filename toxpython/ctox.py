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

# /usr/local/include/tox/tox.h: 130
class struct_Tox(Structure):
    pass

Tox = struct_Tox # /usr/local/include/tox/tox.h: 130

# /usr/local/include/tox/tox.h: 183
if hasattr(_libs['toxcore'], 'tox_version_major'):
    tox_version_major = _libs['toxcore'].tox_version_major
    tox_version_major.argtypes = []
    tox_version_major.restype = c_uint32

# /usr/local/include/tox/tox.h: 188
if hasattr(_libs['toxcore'], 'tox_version_minor'):
    tox_version_minor = _libs['toxcore'].tox_version_minor
    tox_version_minor.argtypes = []
    tox_version_minor.restype = c_uint32

# /usr/local/include/tox/tox.h: 193
if hasattr(_libs['toxcore'], 'tox_version_patch'):
    tox_version_patch = _libs['toxcore'].tox_version_patch
    tox_version_patch.argtypes = []
    tox_version_patch.restype = c_uint32

# /usr/local/include/tox/tox.h: 199
if hasattr(_libs['toxcore'], 'tox_version_is_compatible'):
    tox_version_is_compatible = _libs['toxcore'].tox_version_is_compatible
    tox_version_is_compatible.argtypes = [c_uint32, c_uint32, c_uint32]
    tox_version_is_compatible.restype = c_bool

enum_TOX_USER_STATUS = c_int # /usr/local/include/tox/tox.h: 308

TOX_USER_STATUS_NONE = 0 # /usr/local/include/tox/tox.h: 308

TOX_USER_STATUS_AWAY = (TOX_USER_STATUS_NONE + 1) # /usr/local/include/tox/tox.h: 308

TOX_USER_STATUS_BUSY = (TOX_USER_STATUS_AWAY + 1) # /usr/local/include/tox/tox.h: 308

TOX_USER_STATUS = enum_TOX_USER_STATUS # /usr/local/include/tox/tox.h: 308

enum_TOX_MESSAGE_TYPE = c_int # /usr/local/include/tox/tox.h: 328

TOX_MESSAGE_TYPE_NORMAL = 0 # /usr/local/include/tox/tox.h: 328

TOX_MESSAGE_TYPE_ACTION = (TOX_MESSAGE_TYPE_NORMAL + 1) # /usr/local/include/tox/tox.h: 328

TOX_MESSAGE_TYPE = enum_TOX_MESSAGE_TYPE # /usr/local/include/tox/tox.h: 328

enum_TOX_PROXY_TYPE = c_int # /usr/local/include/tox/tox.h: 360

TOX_PROXY_TYPE_NONE = 0 # /usr/local/include/tox/tox.h: 360

TOX_PROXY_TYPE_HTTP = (TOX_PROXY_TYPE_NONE + 1) # /usr/local/include/tox/tox.h: 360

TOX_PROXY_TYPE_SOCKS5 = (TOX_PROXY_TYPE_HTTP + 1) # /usr/local/include/tox/tox.h: 360

TOX_PROXY_TYPE = enum_TOX_PROXY_TYPE # /usr/local/include/tox/tox.h: 360

enum_TOX_SAVEDATA_TYPE = c_int # /usr/local/include/tox/tox.h: 383

TOX_SAVEDATA_TYPE_NONE = 0 # /usr/local/include/tox/tox.h: 383

TOX_SAVEDATA_TYPE_TOX_SAVE = (TOX_SAVEDATA_TYPE_NONE + 1) # /usr/local/include/tox/tox.h: 383

TOX_SAVEDATA_TYPE_SECRET_KEY = (TOX_SAVEDATA_TYPE_TOX_SAVE + 1) # /usr/local/include/tox/tox.h: 383

TOX_SAVEDATA_TYPE = enum_TOX_SAVEDATA_TYPE # /usr/local/include/tox/tox.h: 383

# /usr/local/include/tox/tox.h: 391
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
    'tcp_port',
    'savedata_type',
    'savedata_data',
    'savedata_length',
]
struct_Tox_Options._fields_ = [
    ('ipv6_enabled', c_bool),
    ('udp_enabled', c_bool),
    ('proxy_type', TOX_PROXY_TYPE),
    ('proxy_host', String),
    ('proxy_port', c_uint16),
    ('start_port', c_uint16),
    ('end_port', c_uint16),
    ('tcp_port', c_uint16),
    ('savedata_type', TOX_SAVEDATA_TYPE),
    ('savedata_data', POINTER(c_uint8)),
    ('savedata_length', c_size_t),
]

# /usr/local/include/tox/tox.h: 507
if hasattr(_libs['toxcore'], 'tox_options_default'):
    tox_options_default = _libs['toxcore'].tox_options_default
    tox_options_default.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_default.restype = None

enum_TOX_ERR_OPTIONS_NEW = c_int # /usr/local/include/tox/tox.h: 521

TOX_ERR_OPTIONS_NEW_OK = 0 # /usr/local/include/tox/tox.h: 521

TOX_ERR_OPTIONS_NEW_MALLOC = (TOX_ERR_OPTIONS_NEW_OK + 1) # /usr/local/include/tox/tox.h: 521

TOX_ERR_OPTIONS_NEW = enum_TOX_ERR_OPTIONS_NEW # /usr/local/include/tox/tox.h: 521

# /usr/local/include/tox/tox.h: 534
if hasattr(_libs['toxcore'], 'tox_options_new'):
    tox_options_new = _libs['toxcore'].tox_options_new
    tox_options_new.argtypes = [POINTER(TOX_ERR_OPTIONS_NEW)]
    tox_options_new.restype = POINTER(struct_Tox_Options)

# /usr/local/include/tox/tox.h: 542
if hasattr(_libs['toxcore'], 'tox_options_free'):
    tox_options_free = _libs['toxcore'].tox_options_free
    tox_options_free.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_free.restype = None

enum_TOX_ERR_NEW = c_int # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_OK = 0 # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_NULL = (TOX_ERR_NEW_OK + 1) # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_MALLOC = (TOX_ERR_NEW_NULL + 1) # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_PORT_ALLOC = (TOX_ERR_NEW_MALLOC + 1) # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_PROXY_BAD_TYPE = (TOX_ERR_NEW_PORT_ALLOC + 1) # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_PROXY_BAD_HOST = (TOX_ERR_NEW_PROXY_BAD_TYPE + 1) # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_PROXY_BAD_PORT = (TOX_ERR_NEW_PROXY_BAD_HOST + 1) # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_PROXY_NOT_FOUND = (TOX_ERR_NEW_PROXY_BAD_PORT + 1) # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_LOAD_ENCRYPTED = (TOX_ERR_NEW_PROXY_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW_LOAD_BAD_FORMAT = (TOX_ERR_NEW_LOAD_ENCRYPTED + 1) # /usr/local/include/tox/tox.h: 613

TOX_ERR_NEW = enum_TOX_ERR_NEW # /usr/local/include/tox/tox.h: 613

# /usr/local/include/tox/tox.h: 632
if hasattr(_libs['toxcore'], 'tox_new'):
    tox_new = _libs['toxcore'].tox_new
    tox_new.argtypes = [POINTER(struct_Tox_Options), POINTER(TOX_ERR_NEW)]
    tox_new.restype = POINTER(Tox)

# /usr/local/include/tox/tox.h: 641
if hasattr(_libs['toxcore'], 'tox_kill'):
    tox_kill = _libs['toxcore'].tox_kill
    tox_kill.argtypes = [POINTER(Tox)]
    tox_kill.restype = None

# /usr/local/include/tox/tox.h: 649
if hasattr(_libs['toxcore'], 'tox_get_savedata_size'):
    tox_get_savedata_size = _libs['toxcore'].tox_get_savedata_size
    tox_get_savedata_size.argtypes = [POINTER(Tox)]
    tox_get_savedata_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 658
if hasattr(_libs['toxcore'], 'tox_get_savedata'):
    tox_get_savedata = _libs['toxcore'].tox_get_savedata
    tox_get_savedata.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_get_savedata.restype = None

enum_TOX_ERR_BOOTSTRAP = c_int # /usr/local/include/tox/tox.h: 692

TOX_ERR_BOOTSTRAP_OK = 0 # /usr/local/include/tox/tox.h: 692

TOX_ERR_BOOTSTRAP_NULL = (TOX_ERR_BOOTSTRAP_OK + 1) # /usr/local/include/tox/tox.h: 692

TOX_ERR_BOOTSTRAP_BAD_HOST = (TOX_ERR_BOOTSTRAP_NULL + 1) # /usr/local/include/tox/tox.h: 692

TOX_ERR_BOOTSTRAP_BAD_PORT = (TOX_ERR_BOOTSTRAP_BAD_HOST + 1) # /usr/local/include/tox/tox.h: 692

TOX_ERR_BOOTSTRAP = enum_TOX_ERR_BOOTSTRAP # /usr/local/include/tox/tox.h: 692

# /usr/local/include/tox/tox.h: 709
if hasattr(_libs['toxcore'], 'tox_bootstrap'):
    tox_bootstrap = _libs['toxcore'].tox_bootstrap
    tox_bootstrap.argtypes = [POINTER(Tox), String, c_uint16, POINTER(c_uint8), POINTER(TOX_ERR_BOOTSTRAP)]
    tox_bootstrap.restype = c_bool

# /usr/local/include/tox/tox.h: 724
if hasattr(_libs['toxcore'], 'tox_add_tcp_relay'):
    tox_add_tcp_relay = _libs['toxcore'].tox_add_tcp_relay
    tox_add_tcp_relay.argtypes = [POINTER(Tox), String, c_uint16, POINTER(c_uint8), POINTER(TOX_ERR_BOOTSTRAP)]
    tox_add_tcp_relay.restype = c_bool

enum_TOX_CONNECTION = c_int # /usr/local/include/tox/tox.h: 753

TOX_CONNECTION_NONE = 0 # /usr/local/include/tox/tox.h: 753

TOX_CONNECTION_TCP = (TOX_CONNECTION_NONE + 1) # /usr/local/include/tox/tox.h: 753

TOX_CONNECTION_UDP = (TOX_CONNECTION_TCP + 1) # /usr/local/include/tox/tox.h: 753

TOX_CONNECTION = enum_TOX_CONNECTION # /usr/local/include/tox/tox.h: 753

# /usr/local/include/tox/tox.h: 760
if hasattr(_libs['toxcore'], 'tox_self_get_connection_status'):
    tox_self_get_connection_status = _libs['toxcore'].tox_self_get_connection_status
    tox_self_get_connection_status.argtypes = [POINTER(Tox)]
    tox_self_get_connection_status.restype = TOX_CONNECTION

tox_self_connection_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), TOX_CONNECTION, POINTER(None)) # /usr/local/include/tox/tox.h: 765

# /usr/local/include/tox/tox.h: 779
if hasattr(_libs['toxcore'], 'tox_callback_self_connection_status'):
    tox_callback_self_connection_status = _libs['toxcore'].tox_callback_self_connection_status
    tox_callback_self_connection_status.argtypes = [POINTER(Tox), POINTER(tox_self_connection_status_cb), POINTER(None)]
    tox_callback_self_connection_status.restype = None

# /usr/local/include/tox/tox.h: 785
if hasattr(_libs['toxcore'], 'tox_iteration_interval'):
    tox_iteration_interval = _libs['toxcore'].tox_iteration_interval
    tox_iteration_interval.argtypes = [POINTER(Tox)]
    tox_iteration_interval.restype = c_uint32

# /usr/local/include/tox/tox.h: 791
if hasattr(_libs['toxcore'], 'tox_iterate'):
    tox_iterate = _libs['toxcore'].tox_iterate
    tox_iterate.argtypes = [POINTER(Tox)]
    tox_iterate.restype = None

# /usr/local/include/tox/tox.h: 811
if hasattr(_libs['toxcore'], 'tox_self_get_address'):
    tox_self_get_address = _libs['toxcore'].tox_self_get_address
    tox_self_get_address.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_address.restype = None

# /usr/local/include/tox/tox.h: 818
if hasattr(_libs['toxcore'], 'tox_self_set_nospam'):
    tox_self_set_nospam = _libs['toxcore'].tox_self_set_nospam
    tox_self_set_nospam.argtypes = [POINTER(Tox), c_uint32]
    tox_self_set_nospam.restype = None

# /usr/local/include/tox/tox.h: 823
if hasattr(_libs['toxcore'], 'tox_self_get_nospam'):
    tox_self_get_nospam = _libs['toxcore'].tox_self_get_nospam
    tox_self_get_nospam.argtypes = [POINTER(Tox)]
    tox_self_get_nospam.restype = c_uint32

# /usr/local/include/tox/tox.h: 831
if hasattr(_libs['toxcore'], 'tox_self_get_public_key'):
    tox_self_get_public_key = _libs['toxcore'].tox_self_get_public_key
    tox_self_get_public_key.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_public_key.restype = None

# /usr/local/include/tox/tox.h: 839
if hasattr(_libs['toxcore'], 'tox_self_get_secret_key'):
    tox_self_get_secret_key = _libs['toxcore'].tox_self_get_secret_key
    tox_self_get_secret_key.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_secret_key.restype = None

enum_TOX_ERR_SET_INFO = c_int # /usr/local/include/tox/tox.h: 871

TOX_ERR_SET_INFO_OK = 0 # /usr/local/include/tox/tox.h: 871

TOX_ERR_SET_INFO_NULL = (TOX_ERR_SET_INFO_OK + 1) # /usr/local/include/tox/tox.h: 871

TOX_ERR_SET_INFO_TOO_LONG = (TOX_ERR_SET_INFO_NULL + 1) # /usr/local/include/tox/tox.h: 871

TOX_ERR_SET_INFO = enum_TOX_ERR_SET_INFO # /usr/local/include/tox/tox.h: 871

# /usr/local/include/tox/tox.h: 885
if hasattr(_libs['toxcore'], 'tox_self_set_name'):
    tox_self_set_name = _libs['toxcore'].tox_self_set_name
    tox_self_set_name.argtypes = [POINTER(Tox), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_SET_INFO)]
    tox_self_set_name.restype = c_bool

# /usr/local/include/tox/tox.h: 895
if hasattr(_libs['toxcore'], 'tox_self_get_name_size'):
    tox_self_get_name_size = _libs['toxcore'].tox_self_get_name_size
    tox_self_get_name_size.argtypes = [POINTER(Tox)]
    tox_self_get_name_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 909
if hasattr(_libs['toxcore'], 'tox_self_get_name'):
    tox_self_get_name = _libs['toxcore'].tox_self_get_name
    tox_self_get_name.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_name.restype = None

# /usr/local/include/tox/tox.h: 918
if hasattr(_libs['toxcore'], 'tox_self_set_status_message'):
    tox_self_set_status_message = _libs['toxcore'].tox_self_set_status_message
    tox_self_set_status_message.argtypes = [POINTER(Tox), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_SET_INFO)]
    tox_self_set_status_message.restype = c_bool

# /usr/local/include/tox/tox.h: 928
if hasattr(_libs['toxcore'], 'tox_self_get_status_message_size'):
    tox_self_get_status_message_size = _libs['toxcore'].tox_self_get_status_message_size
    tox_self_get_status_message_size.argtypes = [POINTER(Tox)]
    tox_self_get_status_message_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 942
if hasattr(_libs['toxcore'], 'tox_self_get_status_message'):
    tox_self_get_status_message = _libs['toxcore'].tox_self_get_status_message
    tox_self_get_status_message.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_status_message.restype = None

# /usr/local/include/tox/tox.h: 949
if hasattr(_libs['toxcore'], 'tox_self_set_status'):
    tox_self_set_status = _libs['toxcore'].tox_self_set_status
    tox_self_set_status.argtypes = [POINTER(Tox), TOX_USER_STATUS]
    tox_self_set_status.restype = None

# /usr/local/include/tox/tox.h: 954
if hasattr(_libs['toxcore'], 'tox_self_get_status'):
    tox_self_get_status = _libs['toxcore'].tox_self_get_status
    tox_self_get_status.argtypes = [POINTER(Tox)]
    tox_self_get_status.restype = TOX_USER_STATUS

enum_TOX_ERR_FRIEND_ADD = c_int # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD_OK = 0 # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD_NULL = (TOX_ERR_FRIEND_ADD_OK + 1) # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD_TOO_LONG = (TOX_ERR_FRIEND_ADD_NULL + 1) # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD_NO_MESSAGE = (TOX_ERR_FRIEND_ADD_TOO_LONG + 1) # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD_OWN_KEY = (TOX_ERR_FRIEND_ADD_NO_MESSAGE + 1) # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD_ALREADY_SENT = (TOX_ERR_FRIEND_ADD_OWN_KEY + 1) # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD_BAD_CHECKSUM = (TOX_ERR_FRIEND_ADD_ALREADY_SENT + 1) # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD_SET_NEW_NOSPAM = (TOX_ERR_FRIEND_ADD_BAD_CHECKSUM + 1) # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD_MALLOC = (TOX_ERR_FRIEND_ADD_SET_NEW_NOSPAM + 1) # /usr/local/include/tox/tox.h: 1015

TOX_ERR_FRIEND_ADD = enum_TOX_ERR_FRIEND_ADD # /usr/local/include/tox/tox.h: 1015

# /usr/local/include/tox/tox.h: 1041
if hasattr(_libs['toxcore'], 'tox_friend_add'):
    tox_friend_add = _libs['toxcore'].tox_friend_add
    tox_friend_add.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_ADD)]
    tox_friend_add.restype = c_uint32

# /usr/local/include/tox/tox.h: 1062
if hasattr(_libs['toxcore'], 'tox_friend_add_norequest'):
    tox_friend_add_norequest = _libs['toxcore'].tox_friend_add_norequest
    tox_friend_add_norequest.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_ADD)]
    tox_friend_add_norequest.restype = c_uint32

enum_TOX_ERR_FRIEND_DELETE = c_int # /usr/local/include/tox/tox.h: 1076

TOX_ERR_FRIEND_DELETE_OK = 0 # /usr/local/include/tox/tox.h: 1076

TOX_ERR_FRIEND_DELETE_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_DELETE_OK + 1) # /usr/local/include/tox/tox.h: 1076

TOX_ERR_FRIEND_DELETE = enum_TOX_ERR_FRIEND_DELETE # /usr/local/include/tox/tox.h: 1076

# /usr/local/include/tox/tox.h: 1090
if hasattr(_libs['toxcore'], 'tox_friend_delete'):
    tox_friend_delete = _libs['toxcore'].tox_friend_delete
    tox_friend_delete.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_DELETE)]
    tox_friend_delete.restype = c_bool

enum_TOX_ERR_FRIEND_BY_PUBLIC_KEY = c_int # /usr/local/include/tox/tox.h: 1118

TOX_ERR_FRIEND_BY_PUBLIC_KEY_OK = 0 # /usr/local/include/tox/tox.h: 1118

TOX_ERR_FRIEND_BY_PUBLIC_KEY_NULL = (TOX_ERR_FRIEND_BY_PUBLIC_KEY_OK + 1) # /usr/local/include/tox/tox.h: 1118

TOX_ERR_FRIEND_BY_PUBLIC_KEY_NOT_FOUND = (TOX_ERR_FRIEND_BY_PUBLIC_KEY_NULL + 1) # /usr/local/include/tox/tox.h: 1118

TOX_ERR_FRIEND_BY_PUBLIC_KEY = enum_TOX_ERR_FRIEND_BY_PUBLIC_KEY # /usr/local/include/tox/tox.h: 1118

# /usr/local/include/tox/tox.h: 1127
if hasattr(_libs['toxcore'], 'tox_friend_by_public_key'):
    tox_friend_by_public_key = _libs['toxcore'].tox_friend_by_public_key
    tox_friend_by_public_key.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_BY_PUBLIC_KEY)]
    tox_friend_by_public_key.restype = c_uint32

# /usr/local/include/tox/tox.h: 1133
if hasattr(_libs['toxcore'], 'tox_friend_exists'):
    tox_friend_exists = _libs['toxcore'].tox_friend_exists
    tox_friend_exists.argtypes = [POINTER(Tox), c_uint32]
    tox_friend_exists.restype = c_bool

# /usr/local/include/tox/tox.h: 1141
if hasattr(_libs['toxcore'], 'tox_self_get_friend_list_size'):
    tox_self_get_friend_list_size = _libs['toxcore'].tox_self_get_friend_list_size
    tox_self_get_friend_list_size.argtypes = [POINTER(Tox)]
    tox_self_get_friend_list_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 1151
if hasattr(_libs['toxcore'], 'tox_self_get_friend_list'):
    tox_self_get_friend_list = _libs['toxcore'].tox_self_get_friend_list
    tox_self_get_friend_list.argtypes = [POINTER(Tox), POINTER(c_uint32)]
    tox_self_get_friend_list.restype = None

enum_TOX_ERR_FRIEND_GET_PUBLIC_KEY = c_int # /usr/local/include/tox/tox.h: 1165

TOX_ERR_FRIEND_GET_PUBLIC_KEY_OK = 0 # /usr/local/include/tox/tox.h: 1165

TOX_ERR_FRIEND_GET_PUBLIC_KEY_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_GET_PUBLIC_KEY_OK + 1) # /usr/local/include/tox/tox.h: 1165

TOX_ERR_FRIEND_GET_PUBLIC_KEY = enum_TOX_ERR_FRIEND_GET_PUBLIC_KEY # /usr/local/include/tox/tox.h: 1165

# /usr/local/include/tox/tox.h: 1177
if hasattr(_libs['toxcore'], 'tox_friend_get_public_key'):
    tox_friend_get_public_key = _libs['toxcore'].tox_friend_get_public_key
    tox_friend_get_public_key.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_GET_PUBLIC_KEY)]
    tox_friend_get_public_key.restype = c_bool

enum_TOX_ERR_FRIEND_GET_LAST_ONLINE = c_int # /usr/local/include/tox/tox.h: 1192

TOX_ERR_FRIEND_GET_LAST_ONLINE_OK = 0 # /usr/local/include/tox/tox.h: 1192

TOX_ERR_FRIEND_GET_LAST_ONLINE_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_GET_LAST_ONLINE_OK + 1) # /usr/local/include/tox/tox.h: 1192

TOX_ERR_FRIEND_GET_LAST_ONLINE = enum_TOX_ERR_FRIEND_GET_LAST_ONLINE # /usr/local/include/tox/tox.h: 1192

# /usr/local/include/tox/tox.h: 1201
if hasattr(_libs['toxcore'], 'tox_friend_get_last_online'):
    tox_friend_get_last_online = _libs['toxcore'].tox_friend_get_last_online
    tox_friend_get_last_online.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_GET_LAST_ONLINE)]
    tox_friend_get_last_online.restype = c_uint64

enum_TOX_ERR_FRIEND_QUERY = c_int # /usr/local/include/tox/tox.h: 1234

TOX_ERR_FRIEND_QUERY_OK = 0 # /usr/local/include/tox/tox.h: 1234

TOX_ERR_FRIEND_QUERY_NULL = (TOX_ERR_FRIEND_QUERY_OK + 1) # /usr/local/include/tox/tox.h: 1234

TOX_ERR_FRIEND_QUERY_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_QUERY_NULL + 1) # /usr/local/include/tox/tox.h: 1234

TOX_ERR_FRIEND_QUERY = enum_TOX_ERR_FRIEND_QUERY # /usr/local/include/tox/tox.h: 1234

# /usr/local/include/tox/tox.h: 1244
if hasattr(_libs['toxcore'], 'tox_friend_get_name_size'):
    tox_friend_get_name_size = _libs['toxcore'].tox_friend_get_name_size
    tox_friend_get_name_size.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_name_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 1260
if hasattr(_libs['toxcore'], 'tox_friend_get_name'):
    tox_friend_get_name = _libs['toxcore'].tox_friend_get_name
    tox_friend_get_name.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_name.restype = c_bool

tox_friend_name_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1269

# /usr/local/include/tox/tox.h: 1277
if hasattr(_libs['toxcore'], 'tox_callback_friend_name'):
    tox_callback_friend_name = _libs['toxcore'].tox_callback_friend_name
    tox_callback_friend_name.argtypes = [POINTER(Tox), POINTER(tox_friend_name_cb), POINTER(None)]
    tox_callback_friend_name.restype = None

# /usr/local/include/tox/tox.h: 1283
if hasattr(_libs['toxcore'], 'tox_friend_get_status_message_size'):
    tox_friend_get_status_message_size = _libs['toxcore'].tox_friend_get_status_message_size
    tox_friend_get_status_message_size.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_status_message_size.restype = c_size_t

# /usr/local/include/tox/tox.h: 1297
if hasattr(_libs['toxcore'], 'tox_friend_get_status_message'):
    tox_friend_get_status_message = _libs['toxcore'].tox_friend_get_status_message
    tox_friend_get_status_message.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_status_message.restype = c_bool

tox_friend_status_message_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1308

# /usr/local/include/tox/tox.h: 1317
if hasattr(_libs['toxcore'], 'tox_callback_friend_status_message'):
    tox_callback_friend_status_message = _libs['toxcore'].tox_callback_friend_status_message
    tox_callback_friend_status_message.argtypes = [POINTER(Tox), POINTER(tox_friend_status_message_cb), POINTER(None)]
    tox_callback_friend_status_message.restype = None

# /usr/local/include/tox/tox.h: 1326
if hasattr(_libs['toxcore'], 'tox_friend_get_status'):
    tox_friend_get_status = _libs['toxcore'].tox_friend_get_status
    tox_friend_get_status.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_status.restype = TOX_USER_STATUS

tox_friend_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_USER_STATUS, POINTER(None)) # /usr/local/include/tox/tox.h: 1333

# /usr/local/include/tox/tox.h: 1341
if hasattr(_libs['toxcore'], 'tox_callback_friend_status'):
    tox_callback_friend_status = _libs['toxcore'].tox_callback_friend_status
    tox_callback_friend_status.argtypes = [POINTER(Tox), POINTER(tox_friend_status_cb), POINTER(None)]
    tox_callback_friend_status.restype = None

# /usr/local/include/tox/tox.h: 1355
if hasattr(_libs['toxcore'], 'tox_friend_get_connection_status'):
    tox_friend_get_connection_status = _libs['toxcore'].tox_friend_get_connection_status
    tox_friend_get_connection_status.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_connection_status.restype = TOX_CONNECTION

tox_friend_connection_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_CONNECTION, POINTER(None)) # /usr/local/include/tox/tox.h: 1363

# /usr/local/include/tox/tox.h: 1376
if hasattr(_libs['toxcore'], 'tox_callback_friend_connection_status'):
    tox_callback_friend_connection_status = _libs['toxcore'].tox_callback_friend_connection_status
    tox_callback_friend_connection_status.argtypes = [POINTER(Tox), POINTER(tox_friend_connection_status_cb), POINTER(None)]
    tox_callback_friend_connection_status.restype = None

# /usr/local/include/tox/tox.h: 1387
if hasattr(_libs['toxcore'], 'tox_friend_get_typing'):
    tox_friend_get_typing = _libs['toxcore'].tox_friend_get_typing
    tox_friend_get_typing.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_typing.restype = c_bool

tox_friend_typing_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_bool, POINTER(None)) # /usr/local/include/tox/tox.h: 1395

# /usr/local/include/tox/tox.h: 1403
if hasattr(_libs['toxcore'], 'tox_callback_friend_typing'):
    tox_callback_friend_typing = _libs['toxcore'].tox_callback_friend_typing
    tox_callback_friend_typing.argtypes = [POINTER(Tox), POINTER(tox_friend_typing_cb), POINTER(None)]
    tox_callback_friend_typing.restype = None

enum_TOX_ERR_SET_TYPING = c_int # /usr/local/include/tox/tox.h: 1426

TOX_ERR_SET_TYPING_OK = 0 # /usr/local/include/tox/tox.h: 1426

TOX_ERR_SET_TYPING_FRIEND_NOT_FOUND = (TOX_ERR_SET_TYPING_OK + 1) # /usr/local/include/tox/tox.h: 1426

TOX_ERR_SET_TYPING = enum_TOX_ERR_SET_TYPING # /usr/local/include/tox/tox.h: 1426

# /usr/local/include/tox/tox.h: 1439
if hasattr(_libs['toxcore'], 'tox_self_set_typing'):
    tox_self_set_typing = _libs['toxcore'].tox_self_set_typing
    tox_self_set_typing.argtypes = [POINTER(Tox), c_uint32, c_bool, POINTER(TOX_ERR_SET_TYPING)]
    tox_self_set_typing.restype = c_bool

enum_TOX_ERR_FRIEND_SEND_MESSAGE = c_int # /usr/local/include/tox/tox.h: 1478

TOX_ERR_FRIEND_SEND_MESSAGE_OK = 0 # /usr/local/include/tox/tox.h: 1478

TOX_ERR_FRIEND_SEND_MESSAGE_NULL = (TOX_ERR_FRIEND_SEND_MESSAGE_OK + 1) # /usr/local/include/tox/tox.h: 1478

TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_SEND_MESSAGE_NULL + 1) # /usr/local/include/tox/tox.h: 1478

TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_CONNECTED = (TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1478

TOX_ERR_FRIEND_SEND_MESSAGE_SENDQ = (TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1478

TOX_ERR_FRIEND_SEND_MESSAGE_TOO_LONG = (TOX_ERR_FRIEND_SEND_MESSAGE_SENDQ + 1) # /usr/local/include/tox/tox.h: 1478

TOX_ERR_FRIEND_SEND_MESSAGE_EMPTY = (TOX_ERR_FRIEND_SEND_MESSAGE_TOO_LONG + 1) # /usr/local/include/tox/tox.h: 1478

TOX_ERR_FRIEND_SEND_MESSAGE = enum_TOX_ERR_FRIEND_SEND_MESSAGE # /usr/local/include/tox/tox.h: 1478

# /usr/local/include/tox/tox.h: 1504
if hasattr(_libs['toxcore'], 'tox_friend_send_message'):
    tox_friend_send_message = _libs['toxcore'].tox_friend_send_message
    tox_friend_send_message.argtypes = [POINTER(Tox), c_uint32, TOX_MESSAGE_TYPE, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_SEND_MESSAGE)]
    tox_friend_send_message.restype = c_uint32

tox_friend_read_receipt_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, POINTER(None)) # /usr/local/include/tox/tox.h: 1512

# /usr/local/include/tox/tox.h: 1521
if hasattr(_libs['toxcore'], 'tox_callback_friend_read_receipt'):
    tox_callback_friend_read_receipt = _libs['toxcore'].tox_callback_friend_read_receipt
    tox_callback_friend_read_receipt.argtypes = [POINTER(Tox), POINTER(tox_friend_read_receipt_cb), POINTER(None)]
    tox_callback_friend_read_receipt.restype = None

tox_friend_request_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1542

# /usr/local/include/tox/tox.h: 1551
if hasattr(_libs['toxcore'], 'tox_callback_friend_request'):
    tox_callback_friend_request = _libs['toxcore'].tox_callback_friend_request
    tox_callback_friend_request.argtypes = [POINTER(Tox), POINTER(tox_friend_request_cb), POINTER(None)]
    tox_callback_friend_request.restype = None

tox_friend_message_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_MESSAGE_TYPE, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 1561

# /usr/local/include/tox/tox.h: 1570
if hasattr(_libs['toxcore'], 'tox_callback_friend_message'):
    tox_callback_friend_message = _libs['toxcore'].tox_callback_friend_message
    tox_callback_friend_message.argtypes = [POINTER(Tox), POINTER(tox_friend_message_cb), POINTER(None)]
    tox_callback_friend_message.restype = None

# /usr/local/include/tox/tox.h: 1600
if hasattr(_libs['toxcore'], 'tox_hash'):
    tox_hash = _libs['toxcore'].tox_hash
    tox_hash.argtypes = [POINTER(c_uint8), POINTER(c_uint8), c_size_t]
    tox_hash.restype = c_bool

enum_TOX_FILE_KIND = c_int # /usr/local/include/tox/tox.h: 1602

TOX_FILE_KIND_DATA = 0 # /usr/local/include/tox/tox.h: 1602

TOX_FILE_KIND_AVATAR = (TOX_FILE_KIND_DATA + 1) # /usr/local/include/tox/tox.h: 1602

enum_TOX_FILE_CONTROL = c_int # /usr/local/include/tox/tox.h: 1657

TOX_FILE_CONTROL_RESUME = 0 # /usr/local/include/tox/tox.h: 1657

TOX_FILE_CONTROL_PAUSE = (TOX_FILE_CONTROL_RESUME + 1) # /usr/local/include/tox/tox.h: 1657

TOX_FILE_CONTROL_CANCEL = (TOX_FILE_CONTROL_PAUSE + 1) # /usr/local/include/tox/tox.h: 1657

TOX_FILE_CONTROL = enum_TOX_FILE_CONTROL # /usr/local/include/tox/tox.h: 1657

enum_TOX_ERR_FILE_CONTROL = c_int # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_CONTROL_OK = 0 # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_CONTROL_FRIEND_NOT_FOUND = (TOX_ERR_FILE_CONTROL_OK + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_CONTROL_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_CONTROL_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_CONTROL_NOT_FOUND = (TOX_ERR_FILE_CONTROL_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_CONTROL_NOT_PAUSED = (TOX_ERR_FILE_CONTROL_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_CONTROL_DENIED = (TOX_ERR_FILE_CONTROL_NOT_PAUSED + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_CONTROL_ALREADY_PAUSED = (TOX_ERR_FILE_CONTROL_DENIED + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_CONTROL_SENDQ = (TOX_ERR_FILE_CONTROL_ALREADY_PAUSED + 1) # /usr/local/include/tox/tox.h: 1703

TOX_ERR_FILE_CONTROL = enum_TOX_ERR_FILE_CONTROL # /usr/local/include/tox/tox.h: 1703

# /usr/local/include/tox/tox.h: 1716
if hasattr(_libs['toxcore'], 'tox_file_control'):
    tox_file_control = _libs['toxcore'].tox_file_control
    tox_file_control.argtypes = [POINTER(Tox), c_uint32, c_uint32, TOX_FILE_CONTROL, POINTER(TOX_ERR_FILE_CONTROL)]
    tox_file_control.restype = c_bool

tox_file_recv_control_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, TOX_FILE_CONTROL, POINTER(None)) # /usr/local/include/tox/tox.h: 1728

# /usr/local/include/tox/tox.h: 1738
if hasattr(_libs['toxcore'], 'tox_callback_file_recv_control'):
    tox_callback_file_recv_control = _libs['toxcore'].tox_callback_file_recv_control
    tox_callback_file_recv_control.argtypes = [POINTER(Tox), POINTER(tox_file_recv_control_cb), POINTER(None)]
    tox_callback_file_recv_control.restype = None

enum_TOX_ERR_FILE_SEEK = c_int # /usr/local/include/tox/tox.h: 1777

TOX_ERR_FILE_SEEK_OK = 0 # /usr/local/include/tox/tox.h: 1777

TOX_ERR_FILE_SEEK_FRIEND_NOT_FOUND = (TOX_ERR_FILE_SEEK_OK + 1) # /usr/local/include/tox/tox.h: 1777

TOX_ERR_FILE_SEEK_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_SEEK_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1777

TOX_ERR_FILE_SEEK_NOT_FOUND = (TOX_ERR_FILE_SEEK_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1777

TOX_ERR_FILE_SEEK_DENIED = (TOX_ERR_FILE_SEEK_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1777

TOX_ERR_FILE_SEEK_INVALID_POSITION = (TOX_ERR_FILE_SEEK_DENIED + 1) # /usr/local/include/tox/tox.h: 1777

TOX_ERR_FILE_SEEK_SENDQ = (TOX_ERR_FILE_SEEK_INVALID_POSITION + 1) # /usr/local/include/tox/tox.h: 1777

TOX_ERR_FILE_SEEK = enum_TOX_ERR_FILE_SEEK # /usr/local/include/tox/tox.h: 1777

# /usr/local/include/tox/tox.h: 1791
if hasattr(_libs['toxcore'], 'tox_file_seek'):
    tox_file_seek = _libs['toxcore'].tox_file_seek
    tox_file_seek.argtypes = [POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(TOX_ERR_FILE_SEEK)]
    tox_file_seek.restype = c_bool

enum_TOX_ERR_FILE_GET = c_int # /usr/local/include/tox/tox.h: 1815

TOX_ERR_FILE_GET_OK = 0 # /usr/local/include/tox/tox.h: 1815

TOX_ERR_FILE_GET_NULL = (TOX_ERR_FILE_GET_OK + 1) # /usr/local/include/tox/tox.h: 1815

TOX_ERR_FILE_GET_FRIEND_NOT_FOUND = (TOX_ERR_FILE_GET_NULL + 1) # /usr/local/include/tox/tox.h: 1815

TOX_ERR_FILE_GET_NOT_FOUND = (TOX_ERR_FILE_GET_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1815

TOX_ERR_FILE_GET = enum_TOX_ERR_FILE_GET # /usr/local/include/tox/tox.h: 1815

# /usr/local/include/tox/tox.h: 1829
if hasattr(_libs['toxcore'], 'tox_file_get_file_id'):
    tox_file_get_file_id = _libs['toxcore'].tox_file_get_file_id
    tox_file_get_file_id.argtypes = [POINTER(Tox), c_uint32, c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FILE_GET)]
    tox_file_get_file_id.restype = c_bool

enum_TOX_ERR_FILE_SEND = c_int # /usr/local/include/tox/tox.h: 1874

TOX_ERR_FILE_SEND_OK = 0 # /usr/local/include/tox/tox.h: 1874

TOX_ERR_FILE_SEND_NULL = (TOX_ERR_FILE_SEND_OK + 1) # /usr/local/include/tox/tox.h: 1874

TOX_ERR_FILE_SEND_FRIEND_NOT_FOUND = (TOX_ERR_FILE_SEND_NULL + 1) # /usr/local/include/tox/tox.h: 1874

TOX_ERR_FILE_SEND_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_SEND_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1874

TOX_ERR_FILE_SEND_NAME_TOO_LONG = (TOX_ERR_FILE_SEND_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1874

TOX_ERR_FILE_SEND_TOO_MANY = (TOX_ERR_FILE_SEND_NAME_TOO_LONG + 1) # /usr/local/include/tox/tox.h: 1874

TOX_ERR_FILE_SEND = enum_TOX_ERR_FILE_SEND # /usr/local/include/tox/tox.h: 1874

# /usr/local/include/tox/tox.h: 1936
if hasattr(_libs['toxcore'], 'tox_file_send'):
    tox_file_send = _libs['toxcore'].tox_file_send
    tox_file_send.argtypes = [POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FILE_SEND)]
    tox_file_send.restype = c_uint32

enum_TOX_ERR_FILE_SEND_CHUNK = c_int # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK_OK = 0 # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK_NULL = (TOX_ERR_FILE_SEND_CHUNK_OK + 1) # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_FOUND = (TOX_ERR_FILE_SEND_CHUNK_NULL + 1) # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK_NOT_FOUND = (TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK_NOT_TRANSFERRING = (TOX_ERR_FILE_SEND_CHUNK_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK_INVALID_LENGTH = (TOX_ERR_FILE_SEND_CHUNK_NOT_TRANSFERRING + 1) # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK_SENDQ = (TOX_ERR_FILE_SEND_CHUNK_INVALID_LENGTH + 1) # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK_WRONG_POSITION = (TOX_ERR_FILE_SEND_CHUNK_SENDQ + 1) # /usr/local/include/tox/tox.h: 1989

TOX_ERR_FILE_SEND_CHUNK = enum_TOX_ERR_FILE_SEND_CHUNK # /usr/local/include/tox/tox.h: 1989

# /usr/local/include/tox/tox.h: 2008
if hasattr(_libs['toxcore'], 'tox_file_send_chunk'):
    tox_file_send_chunk = _libs['toxcore'].tox_file_send_chunk
    tox_file_send_chunk.argtypes = [POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FILE_SEND_CHUNK)]
    tox_file_send_chunk.restype = c_bool

tox_file_chunk_request_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, c_uint64, c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 2033

# /usr/local/include/tox/tox.h: 2042
if hasattr(_libs['toxcore'], 'tox_callback_file_chunk_request'):
    tox_callback_file_chunk_request = _libs['toxcore'].tox_callback_file_chunk_request
    tox_callback_file_chunk_request.argtypes = [POINTER(Tox), POINTER(tox_file_chunk_request_cb), POINTER(None)]
    tox_callback_file_chunk_request.restype = None

tox_file_recv_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, c_uint32, c_uint64, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 2071

# /usr/local/include/tox/tox.h: 2080
if hasattr(_libs['toxcore'], 'tox_callback_file_recv'):
    tox_callback_file_recv = _libs['toxcore'].tox_callback_file_recv
    tox_callback_file_recv.argtypes = [POINTER(Tox), POINTER(tox_file_recv_cb), POINTER(None)]
    tox_callback_file_recv.restype = None

tox_file_recv_chunk_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 2098

# /usr/local/include/tox/tox.h: 2108
if hasattr(_libs['toxcore'], 'tox_callback_file_recv_chunk'):
    tox_callback_file_recv_chunk = _libs['toxcore'].tox_callback_file_recv_chunk
    tox_callback_file_recv_chunk.argtypes = [POINTER(Tox), POINTER(tox_file_recv_chunk_cb), POINTER(None)]
    tox_callback_file_recv_chunk.restype = None

enum_TOX_ERR_FRIEND_CUSTOM_PACKET = c_int # /usr/local/include/tox/tox.h: 2180

TOX_ERR_FRIEND_CUSTOM_PACKET_OK = 0 # /usr/local/include/tox/tox.h: 2180

TOX_ERR_FRIEND_CUSTOM_PACKET_NULL = (TOX_ERR_FRIEND_CUSTOM_PACKET_OK + 1) # /usr/local/include/tox/tox.h: 2180

TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_CUSTOM_PACKET_NULL + 1) # /usr/local/include/tox/tox.h: 2180

TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_CONNECTED = (TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/tox.h: 2180

TOX_ERR_FRIEND_CUSTOM_PACKET_INVALID = (TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/tox.h: 2180

TOX_ERR_FRIEND_CUSTOM_PACKET_EMPTY = (TOX_ERR_FRIEND_CUSTOM_PACKET_INVALID + 1) # /usr/local/include/tox/tox.h: 2180

TOX_ERR_FRIEND_CUSTOM_PACKET_TOO_LONG = (TOX_ERR_FRIEND_CUSTOM_PACKET_EMPTY + 1) # /usr/local/include/tox/tox.h: 2180

TOX_ERR_FRIEND_CUSTOM_PACKET_SENDQ = (TOX_ERR_FRIEND_CUSTOM_PACKET_TOO_LONG + 1) # /usr/local/include/tox/tox.h: 2180

TOX_ERR_FRIEND_CUSTOM_PACKET = enum_TOX_ERR_FRIEND_CUSTOM_PACKET # /usr/local/include/tox/tox.h: 2180

# /usr/local/include/tox/tox.h: 2203
if hasattr(_libs['toxcore'], 'tox_friend_send_lossy_packet'):
    tox_friend_send_lossy_packet = _libs['toxcore'].tox_friend_send_lossy_packet
    tox_friend_send_lossy_packet.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_CUSTOM_PACKET)]
    tox_friend_send_lossy_packet.restype = c_bool

# /usr/local/include/tox/tox.h: 2222
if hasattr(_libs['toxcore'], 'tox_friend_send_lossless_packet'):
    tox_friend_send_lossless_packet = _libs['toxcore'].tox_friend_send_lossless_packet
    tox_friend_send_lossless_packet.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_CUSTOM_PACKET)]
    tox_friend_send_lossless_packet.restype = c_bool

tox_friend_lossy_packet_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 2230

# /usr/local/include/tox/tox.h: 2238
if hasattr(_libs['toxcore'], 'tox_callback_friend_lossy_packet'):
    tox_callback_friend_lossy_packet = _libs['toxcore'].tox_callback_friend_lossy_packet
    tox_callback_friend_lossy_packet.argtypes = [POINTER(Tox), POINTER(tox_friend_lossy_packet_cb), POINTER(None)]
    tox_callback_friend_lossy_packet.restype = None

tox_friend_lossless_packet_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/local/include/tox/tox.h: 2245

# /usr/local/include/tox/tox.h: 2253
if hasattr(_libs['toxcore'], 'tox_callback_friend_lossless_packet'):
    tox_callback_friend_lossless_packet = _libs['toxcore'].tox_callback_friend_lossless_packet
    tox_callback_friend_lossless_packet.argtypes = [POINTER(Tox), POINTER(tox_friend_lossless_packet_cb), POINTER(None)]
    tox_callback_friend_lossless_packet.restype = None

# /usr/local/include/tox/tox.h: 2276
if hasattr(_libs['toxcore'], 'tox_self_get_dht_id'):
    tox_self_get_dht_id = _libs['toxcore'].tox_self_get_dht_id
    tox_self_get_dht_id.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_dht_id.restype = None

enum_TOX_ERR_GET_PORT = c_int # /usr/local/include/tox/tox.h: 2290

TOX_ERR_GET_PORT_OK = 0 # /usr/local/include/tox/tox.h: 2290

TOX_ERR_GET_PORT_NOT_BOUND = (TOX_ERR_GET_PORT_OK + 1) # /usr/local/include/tox/tox.h: 2290

TOX_ERR_GET_PORT = enum_TOX_ERR_GET_PORT # /usr/local/include/tox/tox.h: 2290

# /usr/local/include/tox/tox.h: 2296
if hasattr(_libs['toxcore'], 'tox_self_get_udp_port'):
    tox_self_get_udp_port = _libs['toxcore'].tox_self_get_udp_port
    tox_self_get_udp_port.argtypes = [POINTER(Tox), POINTER(TOX_ERR_GET_PORT)]
    tox_self_get_udp_port.restype = c_uint16

# /usr/local/include/tox/tox.h: 2302
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

# /usr/local/include/tox/toxav.h: 90
class struct_ToxAV(Structure):
    pass

ToxAV = struct_ToxAV # /usr/local/include/tox/toxav.h: 90

# /usr/local/include/tox/toxav.h: 147
if hasattr(_libs['toxav'], 'toxav_version_major'):
    toxav_version_major = _libs['toxav'].toxav_version_major
    toxav_version_major.argtypes = []
    toxav_version_major.restype = c_uint32

# /usr/local/include/tox/toxav.h: 152
if hasattr(_libs['toxav'], 'toxav_version_minor'):
    toxav_version_minor = _libs['toxav'].toxav_version_minor
    toxav_version_minor.argtypes = []
    toxav_version_minor.restype = c_uint32

# /usr/local/include/tox/toxav.h: 157
if hasattr(_libs['toxav'], 'toxav_version_patch'):
    toxav_version_patch = _libs['toxav'].toxav_version_patch
    toxav_version_patch.argtypes = []
    toxav_version_patch.restype = c_uint32

# /usr/local/include/tox/toxav.h: 163
if hasattr(_libs['toxav'], 'toxav_version_is_compatible'):
    toxav_version_is_compatible = _libs['toxav'].toxav_version_is_compatible
    toxav_version_is_compatible.argtypes = [c_uint32, c_uint32, c_uint32]
    toxav_version_is_compatible.restype = c_bool

enum_TOXAV_ERR_NEW = c_int # /usr/local/include/tox/toxav.h: 189

TOXAV_ERR_NEW_OK = 0 # /usr/local/include/tox/toxav.h: 189

TOXAV_ERR_NEW_NULL = (TOXAV_ERR_NEW_OK + 1) # /usr/local/include/tox/toxav.h: 189

TOXAV_ERR_NEW_MALLOC = (TOXAV_ERR_NEW_NULL + 1) # /usr/local/include/tox/toxav.h: 189

TOXAV_ERR_NEW_MULTIPLE = (TOXAV_ERR_NEW_MALLOC + 1) # /usr/local/include/tox/toxav.h: 189

TOXAV_ERR_NEW = enum_TOXAV_ERR_NEW # /usr/local/include/tox/toxav.h: 189

# /usr/local/include/tox/toxav.h: 194
if hasattr(_libs['toxav'], 'toxav_new'):
    toxav_new = _libs['toxav'].toxav_new
    toxav_new.argtypes = [POINTER(Tox), POINTER(TOXAV_ERR_NEW)]
    toxav_new.restype = POINTER(ToxAV)

# /usr/local/include/tox/toxav.h: 203
if hasattr(_libs['toxav'], 'toxav_kill'):
    toxav_kill = _libs['toxav'].toxav_kill
    toxav_kill.argtypes = [POINTER(ToxAV)]
    toxav_kill.restype = None

# /usr/local/include/tox/toxav.h: 208
if hasattr(_libs['toxav'], 'toxav_get_tox'):
    toxav_get_tox = _libs['toxav'].toxav_get_tox
    toxav_get_tox.argtypes = [POINTER(ToxAV)]
    toxav_get_tox.restype = POINTER(Tox)

# /usr/local/include/tox/toxav.h: 220
if hasattr(_libs['toxav'], 'toxav_iteration_interval'):
    toxav_iteration_interval = _libs['toxav'].toxav_iteration_interval
    toxav_iteration_interval.argtypes = [POINTER(ToxAV)]
    toxav_iteration_interval.restype = c_uint32

# /usr/local/include/tox/toxav.h: 227
if hasattr(_libs['toxav'], 'toxav_iterate'):
    toxav_iterate = _libs['toxav'].toxav_iterate
    toxav_iterate.argtypes = [POINTER(ToxAV)]
    toxav_iterate.restype = None

enum_TOXAV_ERR_CALL = c_int # /usr/local/include/tox/toxav.h: 266

TOXAV_ERR_CALL_OK = 0 # /usr/local/include/tox/toxav.h: 266

TOXAV_ERR_CALL_MALLOC = (TOXAV_ERR_CALL_OK + 1) # /usr/local/include/tox/toxav.h: 266

TOXAV_ERR_CALL_SYNC = (TOXAV_ERR_CALL_MALLOC + 1) # /usr/local/include/tox/toxav.h: 266

TOXAV_ERR_CALL_FRIEND_NOT_FOUND = (TOXAV_ERR_CALL_SYNC + 1) # /usr/local/include/tox/toxav.h: 266

TOXAV_ERR_CALL_FRIEND_NOT_CONNECTED = (TOXAV_ERR_CALL_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/toxav.h: 266

TOXAV_ERR_CALL_FRIEND_ALREADY_IN_CALL = (TOXAV_ERR_CALL_FRIEND_NOT_CONNECTED + 1) # /usr/local/include/tox/toxav.h: 266

TOXAV_ERR_CALL_INVALID_BIT_RATE = (TOXAV_ERR_CALL_FRIEND_ALREADY_IN_CALL + 1) # /usr/local/include/tox/toxav.h: 266

TOXAV_ERR_CALL = enum_TOXAV_ERR_CALL # /usr/local/include/tox/toxav.h: 266

# /usr/local/include/tox/toxav.h: 282
if hasattr(_libs['toxav'], 'toxav_call'):
    toxav_call = _libs['toxav'].toxav_call
    toxav_call.argtypes = [POINTER(ToxAV), c_uint32, c_uint32, c_uint32, POINTER(TOXAV_ERR_CALL)]
    toxav_call.restype = c_bool

toxav_call_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, c_bool, c_bool, POINTER(None)) # /usr/local/include/tox/toxav.h: 292

# /usr/local/include/tox/toxav.h: 299
if hasattr(_libs['toxav'], 'toxav_callback_call'):
    toxav_callback_call = _libs['toxav'].toxav_callback_call
    toxav_callback_call.argtypes = [POINTER(ToxAV), POINTER(toxav_call_cb), POINTER(None)]
    toxav_callback_call.restype = None

enum_TOXAV_ERR_ANSWER = c_int # /usr/local/include/tox/toxav.h: 329

TOXAV_ERR_ANSWER_OK = 0 # /usr/local/include/tox/toxav.h: 329

TOXAV_ERR_ANSWER_SYNC = (TOXAV_ERR_ANSWER_OK + 1) # /usr/local/include/tox/toxav.h: 329

TOXAV_ERR_ANSWER_CODEC_INITIALIZATION = (TOXAV_ERR_ANSWER_SYNC + 1) # /usr/local/include/tox/toxav.h: 329

TOXAV_ERR_ANSWER_FRIEND_NOT_FOUND = (TOXAV_ERR_ANSWER_CODEC_INITIALIZATION + 1) # /usr/local/include/tox/toxav.h: 329

TOXAV_ERR_ANSWER_FRIEND_NOT_CALLING = (TOXAV_ERR_ANSWER_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/toxav.h: 329

TOXAV_ERR_ANSWER_INVALID_BIT_RATE = (TOXAV_ERR_ANSWER_FRIEND_NOT_CALLING + 1) # /usr/local/include/tox/toxav.h: 329

TOXAV_ERR_ANSWER = enum_TOXAV_ERR_ANSWER # /usr/local/include/tox/toxav.h: 329

# /usr/local/include/tox/toxav.h: 344
if hasattr(_libs['toxav'], 'toxav_answer'):
    toxav_answer = _libs['toxav'].toxav_answer
    toxav_answer.argtypes = [POINTER(ToxAV), c_uint32, c_uint32, c_uint32, POINTER(TOXAV_ERR_ANSWER)]
    toxav_answer.restype = c_bool

enum_TOXAV_FRIEND_CALL_STATE = c_int # /usr/local/include/tox/toxav.h: 353

TOXAV_FRIEND_CALL_STATE_ERROR = 1 # /usr/local/include/tox/toxav.h: 353

TOXAV_FRIEND_CALL_STATE_FINISHED = 2 # /usr/local/include/tox/toxav.h: 353

TOXAV_FRIEND_CALL_STATE_SENDING_A = 4 # /usr/local/include/tox/toxav.h: 353

TOXAV_FRIEND_CALL_STATE_SENDING_V = 8 # /usr/local/include/tox/toxav.h: 353

TOXAV_FRIEND_CALL_STATE_ACCEPTING_A = 16 # /usr/local/include/tox/toxav.h: 353

TOXAV_FRIEND_CALL_STATE_ACCEPTING_V = 32 # /usr/local/include/tox/toxav.h: 353

toxav_call_state_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, c_uint32, POINTER(None)) # /usr/local/include/tox/toxav.h: 394

# /usr/local/include/tox/toxav.h: 400
if hasattr(_libs['toxav'], 'toxav_callback_call_state'):
    toxav_callback_call_state = _libs['toxav'].toxav_callback_call_state
    toxav_callback_call_state.argtypes = [POINTER(ToxAV), POINTER(toxav_call_state_cb), POINTER(None)]
    toxav_callback_call_state.restype = None

enum_TOXAV_CALL_CONTROL = c_int # /usr/local/include/tox/toxav.h: 442

TOXAV_CALL_CONTROL_RESUME = 0 # /usr/local/include/tox/toxav.h: 442

TOXAV_CALL_CONTROL_PAUSE = (TOXAV_CALL_CONTROL_RESUME + 1) # /usr/local/include/tox/toxav.h: 442

TOXAV_CALL_CONTROL_CANCEL = (TOXAV_CALL_CONTROL_PAUSE + 1) # /usr/local/include/tox/toxav.h: 442

TOXAV_CALL_CONTROL_MUTE_AUDIO = (TOXAV_CALL_CONTROL_CANCEL + 1) # /usr/local/include/tox/toxav.h: 442

TOXAV_CALL_CONTROL_UNMUTE_AUDIO = (TOXAV_CALL_CONTROL_MUTE_AUDIO + 1) # /usr/local/include/tox/toxav.h: 442

TOXAV_CALL_CONTROL_HIDE_VIDEO = (TOXAV_CALL_CONTROL_UNMUTE_AUDIO + 1) # /usr/local/include/tox/toxav.h: 442

TOXAV_CALL_CONTROL_SHOW_VIDEO = (TOXAV_CALL_CONTROL_HIDE_VIDEO + 1) # /usr/local/include/tox/toxav.h: 442

TOXAV_CALL_CONTROL = enum_TOXAV_CALL_CONTROL # /usr/local/include/tox/toxav.h: 442

enum_TOXAV_ERR_CALL_CONTROL = c_int # /usr/local/include/tox/toxav.h: 467

TOXAV_ERR_CALL_CONTROL_OK = 0 # /usr/local/include/tox/toxav.h: 467

TOXAV_ERR_CALL_CONTROL_SYNC = (TOXAV_ERR_CALL_CONTROL_OK + 1) # /usr/local/include/tox/toxav.h: 467

TOXAV_ERR_CALL_CONTROL_FRIEND_NOT_FOUND = (TOXAV_ERR_CALL_CONTROL_SYNC + 1) # /usr/local/include/tox/toxav.h: 467

TOXAV_ERR_CALL_CONTROL_FRIEND_NOT_IN_CALL = (TOXAV_ERR_CALL_CONTROL_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/toxav.h: 467

TOXAV_ERR_CALL_CONTROL_INVALID_TRANSITION = (TOXAV_ERR_CALL_CONTROL_FRIEND_NOT_IN_CALL + 1) # /usr/local/include/tox/toxav.h: 467

TOXAV_ERR_CALL_CONTROL = enum_TOXAV_ERR_CALL_CONTROL # /usr/local/include/tox/toxav.h: 467

# /usr/local/include/tox/toxav.h: 478
if hasattr(_libs['toxav'], 'toxav_call_control'):
    toxav_call_control = _libs['toxav'].toxav_call_control
    toxav_call_control.argtypes = [POINTER(ToxAV), c_uint32, TOXAV_CALL_CONTROL, POINTER(TOXAV_ERR_CALL_CONTROL)]
    toxav_call_control.restype = c_bool

enum_TOXAV_ERR_BIT_RATE_SET = c_int # /usr/local/include/tox/toxav.h: 512

TOXAV_ERR_BIT_RATE_SET_OK = 0 # /usr/local/include/tox/toxav.h: 512

TOXAV_ERR_BIT_RATE_SET_SYNC = (TOXAV_ERR_BIT_RATE_SET_OK + 1) # /usr/local/include/tox/toxav.h: 512

TOXAV_ERR_BIT_RATE_SET_INVALID_AUDIO_BIT_RATE = (TOXAV_ERR_BIT_RATE_SET_SYNC + 1) # /usr/local/include/tox/toxav.h: 512

TOXAV_ERR_BIT_RATE_SET_INVALID_VIDEO_BIT_RATE = (TOXAV_ERR_BIT_RATE_SET_INVALID_AUDIO_BIT_RATE + 1) # /usr/local/include/tox/toxav.h: 512

TOXAV_ERR_BIT_RATE_SET_FRIEND_NOT_FOUND = (TOXAV_ERR_BIT_RATE_SET_INVALID_VIDEO_BIT_RATE + 1) # /usr/local/include/tox/toxav.h: 512

TOXAV_ERR_BIT_RATE_SET_FRIEND_NOT_IN_CALL = (TOXAV_ERR_BIT_RATE_SET_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/toxav.h: 512

TOXAV_ERR_BIT_RATE_SET = enum_TOXAV_ERR_BIT_RATE_SET # /usr/local/include/tox/toxav.h: 512

# /usr/local/include/tox/toxav.h: 525
if hasattr(_libs['toxav'], 'toxav_bit_rate_set'):
    toxav_bit_rate_set = _libs['toxav'].toxav_bit_rate_set
    toxav_bit_rate_set.argtypes = [POINTER(ToxAV), c_uint32, c_int32, c_int32, POINTER(TOXAV_ERR_BIT_RATE_SET)]
    toxav_bit_rate_set.restype = c_bool

toxav_bit_rate_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, c_uint32, c_uint32, POINTER(None)) # /usr/local/include/tox/toxav.h: 538

# /usr/local/include/tox/toxav.h: 545
if hasattr(_libs['toxav'], 'toxav_callback_bit_rate_status'):
    toxav_callback_bit_rate_status = _libs['toxav'].toxav_callback_bit_rate_status
    toxav_callback_bit_rate_status.argtypes = [POINTER(ToxAV), POINTER(toxav_bit_rate_status_cb), POINTER(None)]
    toxav_callback_bit_rate_status.restype = None

enum_TOXAV_ERR_SEND_FRAME = c_int # /usr/local/include/tox/toxav.h: 589

TOXAV_ERR_SEND_FRAME_OK = 0 # /usr/local/include/tox/toxav.h: 589

TOXAV_ERR_SEND_FRAME_NULL = (TOXAV_ERR_SEND_FRAME_OK + 1) # /usr/local/include/tox/toxav.h: 589

TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND = (TOXAV_ERR_SEND_FRAME_NULL + 1) # /usr/local/include/tox/toxav.h: 589

TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL = (TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND + 1) # /usr/local/include/tox/toxav.h: 589

TOXAV_ERR_SEND_FRAME_SYNC = (TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL + 1) # /usr/local/include/tox/toxav.h: 589

TOXAV_ERR_SEND_FRAME_INVALID = (TOXAV_ERR_SEND_FRAME_SYNC + 1) # /usr/local/include/tox/toxav.h: 589

TOXAV_ERR_SEND_FRAME_PAYLOAD_TYPE_DISABLED = (TOXAV_ERR_SEND_FRAME_INVALID + 1) # /usr/local/include/tox/toxav.h: 589

TOXAV_ERR_SEND_FRAME_RTP_FAILED = (TOXAV_ERR_SEND_FRAME_PAYLOAD_TYPE_DISABLED + 1) # /usr/local/include/tox/toxav.h: 589

TOXAV_ERR_SEND_FRAME = enum_TOXAV_ERR_SEND_FRAME # /usr/local/include/tox/toxav.h: 589

# /usr/local/include/tox/toxav.h: 611
if hasattr(_libs['toxav'], 'toxav_audio_send_frame'):
    toxav_audio_send_frame = _libs['toxav'].toxav_audio_send_frame
    toxav_audio_send_frame.argtypes = [POINTER(ToxAV), c_uint32, POINTER(c_int16), c_size_t, c_uint8, c_uint32, POINTER(TOXAV_ERR_SEND_FRAME)]
    toxav_audio_send_frame.restype = c_bool

# /usr/local/include/tox/toxav.h: 630
if hasattr(_libs['toxav'], 'toxav_video_send_frame'):
    toxav_video_send_frame = _libs['toxav'].toxav_video_send_frame
    toxav_video_send_frame.argtypes = [POINTER(ToxAV), c_uint32, c_uint16, c_uint16, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(TOXAV_ERR_SEND_FRAME)]
    toxav_video_send_frame.restype = c_bool

toxav_audio_receive_frame_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, POINTER(c_int16), c_size_t, c_uint8, c_uint32, POINTER(None)) # /usr/local/include/tox/toxav.h: 652

# /usr/local/include/tox/toxav.h: 660
if hasattr(_libs['toxav'], 'toxav_callback_audio_receive_frame'):
    toxav_callback_audio_receive_frame = _libs['toxav'].toxav_callback_audio_receive_frame
    toxav_callback_audio_receive_frame.argtypes = [POINTER(ToxAV), POINTER(toxav_audio_receive_frame_cb), POINTER(None)]
    toxav_callback_audio_receive_frame.restype = None

toxav_video_receive_frame_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, c_uint16, c_uint16, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), c_int32, c_int32, c_int32, POINTER(None)) # /usr/local/include/tox/toxav.h: 683

# /usr/local/include/tox/toxav.h: 691
if hasattr(_libs['toxav'], 'toxav_callback_video_receive_frame'):
    toxav_callback_video_receive_frame = _libs['toxav'].toxav_callback_video_receive_frame
    toxav_callback_video_receive_frame.argtypes = [POINTER(ToxAV), POINTER(toxav_video_receive_frame_cb), POINTER(None)]
    toxav_callback_video_receive_frame.restype = None

# /usr/local/include/tox/toxav.h: 706
if hasattr(_libs['toxav'], 'toxav_add_av_groupchat'):
    toxav_add_av_groupchat = _libs['toxav'].toxav_add_av_groupchat
    toxav_add_av_groupchat.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, c_int, POINTER(c_int16), c_uint, c_uint8, c_uint, POINTER(None)), POINTER(None)]
    toxav_add_av_groupchat.restype = c_int

# /usr/local/include/tox/toxav.h: 719
if hasattr(_libs['toxav'], 'toxav_join_av_groupchat'):
    toxav_join_av_groupchat = _libs['toxav'].toxav_join_av_groupchat
    toxav_join_av_groupchat.argtypes = [POINTER(Tox), c_int32, POINTER(c_uint8), c_uint16, CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, c_int, POINTER(c_int16), c_uint, c_uint8, c_uint, POINTER(None)), POINTER(None)]
    toxav_join_av_groupchat.restype = c_int

# /usr/local/include/tox/toxav.h: 735
if hasattr(_libs['toxav'], 'toxav_group_send_audio'):
    toxav_group_send_audio = _libs['toxav'].toxav_group_send_audio
    toxav_group_send_audio.argtypes = [POINTER(Tox), c_int, POINTER(c_int16), c_uint, c_uint8, c_uint]
    toxav_group_send_audio.restype = c_int

enum_TOX_ERR_KEY_DERIVATION = c_int # /usr/local/include/tox/toxencryptsave.h: 84

TOX_ERR_KEY_DERIVATION_OK = 0 # /usr/local/include/tox/toxencryptsave.h: 84

TOX_ERR_KEY_DERIVATION_NULL = (TOX_ERR_KEY_DERIVATION_OK + 1) # /usr/local/include/tox/toxencryptsave.h: 84

TOX_ERR_KEY_DERIVATION_FAILED = (TOX_ERR_KEY_DERIVATION_NULL + 1) # /usr/local/include/tox/toxencryptsave.h: 84

TOX_ERR_KEY_DERIVATION = enum_TOX_ERR_KEY_DERIVATION # /usr/local/include/tox/toxencryptsave.h: 84

enum_TOX_ERR_ENCRYPTION = c_int # /usr/local/include/tox/toxencryptsave.h: 102

TOX_ERR_ENCRYPTION_OK = 0 # /usr/local/include/tox/toxencryptsave.h: 102

TOX_ERR_ENCRYPTION_NULL = (TOX_ERR_ENCRYPTION_OK + 1) # /usr/local/include/tox/toxencryptsave.h: 102

TOX_ERR_ENCRYPTION_KEY_DERIVATION_FAILED = (TOX_ERR_ENCRYPTION_NULL + 1) # /usr/local/include/tox/toxencryptsave.h: 102

TOX_ERR_ENCRYPTION_FAILED = (TOX_ERR_ENCRYPTION_KEY_DERIVATION_FAILED + 1) # /usr/local/include/tox/toxencryptsave.h: 102

TOX_ERR_ENCRYPTION = enum_TOX_ERR_ENCRYPTION # /usr/local/include/tox/toxencryptsave.h: 102

enum_TOX_ERR_DECRYPTION = c_int # /usr/local/include/tox/toxencryptsave.h: 130

TOX_ERR_DECRYPTION_OK = 0 # /usr/local/include/tox/toxencryptsave.h: 130

TOX_ERR_DECRYPTION_NULL = (TOX_ERR_DECRYPTION_OK + 1) # /usr/local/include/tox/toxencryptsave.h: 130

TOX_ERR_DECRYPTION_INVALID_LENGTH = (TOX_ERR_DECRYPTION_NULL + 1) # /usr/local/include/tox/toxencryptsave.h: 130

TOX_ERR_DECRYPTION_BAD_FORMAT = (TOX_ERR_DECRYPTION_INVALID_LENGTH + 1) # /usr/local/include/tox/toxencryptsave.h: 130

TOX_ERR_DECRYPTION_KEY_DERIVATION_FAILED = (TOX_ERR_DECRYPTION_BAD_FORMAT + 1) # /usr/local/include/tox/toxencryptsave.h: 130

TOX_ERR_DECRYPTION_FAILED = (TOX_ERR_DECRYPTION_KEY_DERIVATION_FAILED + 1) # /usr/local/include/tox/toxencryptsave.h: 130

TOX_ERR_DECRYPTION = enum_TOX_ERR_DECRYPTION # /usr/local/include/tox/toxencryptsave.h: 130

# /usr/local/include/tox/toxencryptsave.h: 146
if hasattr(_libs['toxencryptsave'], 'tox_pass_encrypt'):
    tox_pass_encrypt = _libs['toxencryptsave'].tox_pass_encrypt
    tox_pass_encrypt.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(TOX_ERR_ENCRYPTION)]
    tox_pass_encrypt.restype = c_bool

# /usr/local/include/tox/toxencryptsave.h: 158
if hasattr(_libs['toxencryptsave'], 'tox_pass_decrypt'):
    tox_pass_decrypt = _libs['toxencryptsave'].tox_pass_decrypt
    tox_pass_decrypt.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(TOX_ERR_DECRYPTION)]
    tox_pass_decrypt.restype = c_bool

# /usr/local/include/tox/toxencryptsave.h: 173
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'salt',
    'key',
]
struct_anon_3._fields_ = [
    ('salt', c_uint8 * 32),
    ('key', c_uint8 * 32),
]

TOX_PASS_KEY = struct_anon_3 # /usr/local/include/tox/toxencryptsave.h: 173

# /usr/local/include/tox/toxencryptsave.h: 186
if hasattr(_libs['toxencryptsave'], 'tox_derive_key_from_pass'):
    tox_derive_key_from_pass = _libs['toxencryptsave'].tox_derive_key_from_pass
    tox_derive_key_from_pass.argtypes = [POINTER(c_uint8), c_size_t, POINTER(TOX_PASS_KEY), POINTER(TOX_ERR_KEY_DERIVATION)]
    tox_derive_key_from_pass.restype = c_bool

# /usr/local/include/tox/toxencryptsave.h: 192
if hasattr(_libs['toxencryptsave'], 'tox_derive_key_with_salt'):
    tox_derive_key_with_salt = _libs['toxencryptsave'].tox_derive_key_with_salt
    tox_derive_key_with_salt.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(TOX_PASS_KEY), POINTER(TOX_ERR_KEY_DERIVATION)]
    tox_derive_key_with_salt.restype = c_bool

# /usr/local/include/tox/toxencryptsave.h: 203
if hasattr(_libs['toxencryptsave'], 'tox_get_salt'):
    tox_get_salt = _libs['toxencryptsave'].tox_get_salt
    tox_get_salt.argtypes = [POINTER(c_uint8), POINTER(c_uint8)]
    tox_get_salt.restype = c_bool

# /usr/local/include/tox/toxencryptsave.h: 215
if hasattr(_libs['toxencryptsave'], 'tox_pass_key_encrypt'):
    tox_pass_key_encrypt = _libs['toxencryptsave'].tox_pass_key_encrypt
    tox_pass_key_encrypt.argtypes = [POINTER(c_uint8), c_size_t, POINTER(TOX_PASS_KEY), POINTER(c_uint8), POINTER(TOX_ERR_ENCRYPTION)]
    tox_pass_key_encrypt.restype = c_bool

# /usr/local/include/tox/toxencryptsave.h: 225
if hasattr(_libs['toxencryptsave'], 'tox_pass_key_decrypt'):
    tox_pass_key_decrypt = _libs['toxencryptsave'].tox_pass_key_decrypt
    tox_pass_key_decrypt.argtypes = [POINTER(c_uint8), c_size_t, POINTER(TOX_PASS_KEY), POINTER(c_uint8), POINTER(TOX_ERR_DECRYPTION)]
    tox_pass_key_decrypt.restype = c_bool

# /usr/local/include/tox/toxencryptsave.h: 230
if hasattr(_libs['toxencryptsave'], 'tox_is_data_encrypted'):
    tox_is_data_encrypted = _libs['toxencryptsave'].tox_is_data_encrypted
    tox_is_data_encrypted.argtypes = [POINTER(c_uint8)]
    tox_is_data_encrypted.restype = c_bool

# /usr/local/include/tox/tox.h: 146
TOX_VERSION_MAJOR = 0

# /usr/local/include/tox/tox.h: 153
TOX_VERSION_MINOR = 0

# /usr/local/include/tox/tox.h: 159
TOX_VERSION_PATCH = 0

# /usr/local/include/tox/tox.h: 165
def TOX_VERSION_IS_API_COMPATIBLE(MAJOR, MINOR, PATCH):
    return ((TOX_VERSION_MAJOR == MAJOR) and ((TOX_VERSION_MINOR > MINOR) or ((TOX_VERSION_MINOR == MINOR) and (TOX_VERSION_PATCH >= PATCH))))

# /usr/local/include/tox/tox.h: 205
TOX_VERSION_IS_ABI_COMPATIBLE = (tox_version_is_compatible (TOX_VERSION_MAJOR, TOX_VERSION_MINOR, TOX_VERSION_PATCH))

# /usr/local/include/tox/tox.h: 220
TOX_PUBLIC_KEY_SIZE = 32

# /usr/local/include/tox/tox.h: 225
TOX_SECRET_KEY_SIZE = 32

# /usr/local/include/tox/tox.h: 235
TOX_ADDRESS_SIZE = ((TOX_PUBLIC_KEY_SIZE + sizeof(c_uint32)) + sizeof(c_uint16))

# /usr/local/include/tox/tox.h: 240
TOX_MAX_NAME_LENGTH = 128

# /usr/local/include/tox/tox.h: 245
TOX_MAX_STATUS_MESSAGE_LENGTH = 1007

# /usr/local/include/tox/tox.h: 250
TOX_MAX_FRIEND_REQUEST_LENGTH = 1016

# /usr/local/include/tox/tox.h: 255
TOX_MAX_MESSAGE_LENGTH = 1372

# /usr/local/include/tox/tox.h: 260
TOX_MAX_CUSTOM_PACKET_SIZE = 1373

# /usr/local/include/tox/tox.h: 265
TOX_HASH_LENGTH = 32

# /usr/local/include/tox/tox.h: 270
TOX_FILE_ID_LENGTH = 32

# /usr/local/include/tox/tox.h: 275
TOX_MAX_FILENAME_LENGTH = 255

# /usr/local/include/tox/toxdns.h: 34
TOXDNS_MAX_RECOMMENDED_NAME_LENGTH = 32

# /usr/local/include/tox/toxav.h: 103
TOXAV_VERSION_MAJOR = 0

# /usr/local/include/tox/toxav.h: 110
TOXAV_VERSION_MINOR = 0

# /usr/local/include/tox/toxav.h: 116
TOXAV_VERSION_PATCH = 0

# /usr/local/include/tox/toxav.h: 122
def TOXAV_VERSION_IS_API_COMPATIBLE(MAJOR, MINOR, PATCH):
    return ((TOXAV_VERSION_MAJOR == MAJOR) and ((TOXAV_VERSION_MINOR > MINOR) or ((TOXAV_VERSION_MINOR == MINOR) and (TOXAV_VERSION_PATCH >= PATCH))))

# /usr/local/include/tox/toxav.h: 139
TOXAV_VERSION_IS_ABI_COMPATIBLE = (toxav_version_is_compatible (TOXAV_VERSION_MAJOR, TOXAV_VERSION_MINOR, TOXAV_VERSION_PATCH))

# /usr/local/include/tox/toxencryptsave.h: 41
TOX_PASS_SALT_LENGTH = 32

# /usr/local/include/tox/toxencryptsave.h: 42
TOX_PASS_KEY_LENGTH = 32

# /usr/local/include/tox/toxencryptsave.h: 43
TOX_PASS_ENCRYPTION_EXTRA_LENGTH = 80

Tox = struct_Tox # /usr/local/include/tox/tox.h: 130

Tox_Options = struct_Tox_Options # /usr/local/include/tox/tox.h: 391

ToxAV = struct_ToxAV # /usr/local/include/tox/toxav.h: 90

# No inserted files

