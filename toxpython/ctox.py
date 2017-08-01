'''Wrapper for tox.h

Generated with:
/usr/local/bin/ctypesgen.py -ltoxcore /usr/include/tox/tox.h -ltoxdns /usr/include/tox/toxdns.h -ltoxav /usr/include/tox/toxav.h -ltoxencryptsave /usr/include/tox/toxencryptsa ve.h --compile-libdir /usr/lib

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
        return self.load(libname)
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

_libs["toxcore"] = load_library("libtoxcore.so")
_libs["toxdns"] = load_library("libtoxdns.so")
_libs["toxav"] = load_library("libtoxav.so")
_libs["toxencryptsave"] = load_library("libtoxencryptsave.so")

# 4 libraries
# End libraries

# No modules

# /usr/include/tox/tox.h: 146
class struct_Tox(Structure):
    pass

Tox = struct_Tox # /usr/include/tox/tox.h: 146

# /usr/include/tox/tox.h: 168
if hasattr(_libs['toxcore'], 'tox_version_major'):
    tox_version_major = _libs['toxcore'].tox_version_major
    tox_version_major.argtypes = []
    tox_version_major.restype = c_uint32

# /usr/include/tox/tox.h: 177
if hasattr(_libs['toxcore'], 'tox_version_minor'):
    tox_version_minor = _libs['toxcore'].tox_version_minor
    tox_version_minor.argtypes = []
    tox_version_minor.restype = c_uint32

# /usr/include/tox/tox.h: 185
if hasattr(_libs['toxcore'], 'tox_version_patch'):
    tox_version_patch = _libs['toxcore'].tox_version_patch
    tox_version_patch.argtypes = []
    tox_version_patch.restype = c_uint32

# /usr/include/tox/tox.h: 212
if hasattr(_libs['toxcore'], 'tox_version_is_compatible'):
    tox_version_is_compatible = _libs['toxcore'].tox_version_is_compatible
    tox_version_is_compatible.argtypes = [c_uint32, c_uint32, c_uint32]
    tox_version_is_compatible.restype = c_bool

# /usr/include/tox/tox.h: 239
if hasattr(_libs['toxcore'], 'tox_public_key_size'):
    tox_public_key_size = _libs['toxcore'].tox_public_key_size
    tox_public_key_size.argtypes = []
    tox_public_key_size.restype = c_uint32

# /usr/include/tox/tox.h: 246
if hasattr(_libs['toxcore'], 'tox_secret_key_size'):
    tox_secret_key_size = _libs['toxcore'].tox_secret_key_size
    tox_secret_key_size.argtypes = []
    tox_secret_key_size.restype = c_uint32

# /usr/include/tox/tox.h: 253
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_nospam_size'):
        continue
    tox_nospam_size = _lib.tox_nospam_size
    tox_nospam_size.argtypes = []
    tox_nospam_size.restype = c_uint32
    break

# /usr/include/tox/tox.h: 265
if hasattr(_libs['toxcore'], 'tox_address_size'):
    tox_address_size = _libs['toxcore'].tox_address_size
    tox_address_size.argtypes = []
    tox_address_size.restype = c_uint32

# /usr/include/tox/tox.h: 272
if hasattr(_libs['toxcore'], 'tox_max_name_length'):
    tox_max_name_length = _libs['toxcore'].tox_max_name_length
    tox_max_name_length.argtypes = []
    tox_max_name_length.restype = c_uint32

# /usr/include/tox/tox.h: 279
if hasattr(_libs['toxcore'], 'tox_max_status_message_length'):
    tox_max_status_message_length = _libs['toxcore'].tox_max_status_message_length
    tox_max_status_message_length.argtypes = []
    tox_max_status_message_length.restype = c_uint32

# /usr/include/tox/tox.h: 286
if hasattr(_libs['toxcore'], 'tox_max_friend_request_length'):
    tox_max_friend_request_length = _libs['toxcore'].tox_max_friend_request_length
    tox_max_friend_request_length.argtypes = []
    tox_max_friend_request_length.restype = c_uint32

# /usr/include/tox/tox.h: 293
if hasattr(_libs['toxcore'], 'tox_max_message_length'):
    tox_max_message_length = _libs['toxcore'].tox_max_message_length
    tox_max_message_length.argtypes = []
    tox_max_message_length.restype = c_uint32

# /usr/include/tox/tox.h: 300
if hasattr(_libs['toxcore'], 'tox_max_custom_packet_size'):
    tox_max_custom_packet_size = _libs['toxcore'].tox_max_custom_packet_size
    tox_max_custom_packet_size.argtypes = []
    tox_max_custom_packet_size.restype = c_uint32

# /usr/include/tox/tox.h: 307
if hasattr(_libs['toxcore'], 'tox_hash_length'):
    tox_hash_length = _libs['toxcore'].tox_hash_length
    tox_hash_length.argtypes = []
    tox_hash_length.restype = c_uint32

# /usr/include/tox/tox.h: 314
if hasattr(_libs['toxcore'], 'tox_file_id_length'):
    tox_file_id_length = _libs['toxcore'].tox_file_id_length
    tox_file_id_length.argtypes = []
    tox_file_id_length.restype = c_uint32

# /usr/include/tox/tox.h: 321
if hasattr(_libs['toxcore'], 'tox_max_filename_length'):
    tox_max_filename_length = _libs['toxcore'].tox_max_filename_length
    tox_max_filename_length.argtypes = []
    tox_max_filename_length.restype = c_uint32

enum_TOX_USER_STATUS = c_int # /usr/include/tox/tox.h: 354

TOX_USER_STATUS_NONE = 0 # /usr/include/tox/tox.h: 354

TOX_USER_STATUS_AWAY = (TOX_USER_STATUS_NONE + 1) # /usr/include/tox/tox.h: 354

TOX_USER_STATUS_BUSY = (TOX_USER_STATUS_AWAY + 1) # /usr/include/tox/tox.h: 354

TOX_USER_STATUS = enum_TOX_USER_STATUS # /usr/include/tox/tox.h: 354

enum_TOX_MESSAGE_TYPE = c_int # /usr/include/tox/tox.h: 374

TOX_MESSAGE_TYPE_NORMAL = 0 # /usr/include/tox/tox.h: 374

TOX_MESSAGE_TYPE_ACTION = (TOX_MESSAGE_TYPE_NORMAL + 1) # /usr/include/tox/tox.h: 374

TOX_MESSAGE_TYPE = enum_TOX_MESSAGE_TYPE # /usr/include/tox/tox.h: 374

enum_TOX_PROXY_TYPE = c_int # /usr/include/tox/tox.h: 406

TOX_PROXY_TYPE_NONE = 0 # /usr/include/tox/tox.h: 406

TOX_PROXY_TYPE_HTTP = (TOX_PROXY_TYPE_NONE + 1) # /usr/include/tox/tox.h: 406

TOX_PROXY_TYPE_SOCKS5 = (TOX_PROXY_TYPE_HTTP + 1) # /usr/include/tox/tox.h: 406

TOX_PROXY_TYPE = enum_TOX_PROXY_TYPE # /usr/include/tox/tox.h: 406

enum_TOX_SAVEDATA_TYPE = c_int # /usr/include/tox/tox.h: 429

TOX_SAVEDATA_TYPE_NONE = 0 # /usr/include/tox/tox.h: 429

TOX_SAVEDATA_TYPE_TOX_SAVE = (TOX_SAVEDATA_TYPE_NONE + 1) # /usr/include/tox/tox.h: 429

TOX_SAVEDATA_TYPE_SECRET_KEY = (TOX_SAVEDATA_TYPE_TOX_SAVE + 1) # /usr/include/tox/tox.h: 429

TOX_SAVEDATA_TYPE = enum_TOX_SAVEDATA_TYPE # /usr/include/tox/tox.h: 429

enum_TOX_LOG_LEVEL = c_int # /usr/include/tox/tox.h: 462

TOX_LOG_LEVEL_TRACE = 0 # /usr/include/tox/tox.h: 462

TOX_LOG_LEVEL_DEBUG = (TOX_LOG_LEVEL_TRACE + 1) # /usr/include/tox/tox.h: 462

TOX_LOG_LEVEL_INFO = (TOX_LOG_LEVEL_DEBUG + 1) # /usr/include/tox/tox.h: 462

TOX_LOG_LEVEL_WARNING = (TOX_LOG_LEVEL_INFO + 1) # /usr/include/tox/tox.h: 462

TOX_LOG_LEVEL_ERROR = (TOX_LOG_LEVEL_WARNING + 1) # /usr/include/tox/tox.h: 462

TOX_LOG_LEVEL = enum_TOX_LOG_LEVEL # /usr/include/tox/tox.h: 462

tox_log_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), TOX_LOG_LEVEL, String, c_uint32, String, String, POINTER(None)) # /usr/include/tox/tox.h: 482

# /usr/include/tox/tox.h: 499
class struct_Tox_Options(Structure):
    pass

struct_Tox_Options.__slots__ = [
    'ipv6_enabled',
    'udp_enabled',
    'local_discovery_enabled',
    'proxy_type',
    'proxy_host',
    'proxy_port',
    'start_port',
    'end_port',
    'tcp_port',
    'hole_punching_enabled',
    'savedata_type',
    'savedata_data',
    'savedata_length',
    'log_callback',
    'log_user_data',
]
struct_Tox_Options._fields_ = [
    ('ipv6_enabled', c_bool),
    ('udp_enabled', c_bool),
    ('local_discovery_enabled', c_bool),
    ('proxy_type', TOX_PROXY_TYPE),
    ('proxy_host', String),
    ('proxy_port', c_uint16),
    ('start_port', c_uint16),
    ('end_port', c_uint16),
    ('tcp_port', c_uint16),
    ('hole_punching_enabled', c_bool),
    ('savedata_type', TOX_SAVEDATA_TYPE),
    ('savedata_data', POINTER(c_uint8)),
    ('savedata_length', c_size_t),
    ('log_callback', POINTER(tox_log_cb)),
    ('log_user_data', POINTER(None)),
]

# /usr/include/tox/tox.h: 636
if hasattr(_libs['toxcore'], 'tox_options_get_ipv6_enabled'):
    tox_options_get_ipv6_enabled = _libs['toxcore'].tox_options_get_ipv6_enabled
    tox_options_get_ipv6_enabled.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_ipv6_enabled.restype = c_bool

# /usr/include/tox/tox.h: 638
if hasattr(_libs['toxcore'], 'tox_options_set_ipv6_enabled'):
    tox_options_set_ipv6_enabled = _libs['toxcore'].tox_options_set_ipv6_enabled
    tox_options_set_ipv6_enabled.argtypes = [POINTER(struct_Tox_Options), c_bool]
    tox_options_set_ipv6_enabled.restype = None

# /usr/include/tox/tox.h: 640
if hasattr(_libs['toxcore'], 'tox_options_get_udp_enabled'):
    tox_options_get_udp_enabled = _libs['toxcore'].tox_options_get_udp_enabled
    tox_options_get_udp_enabled.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_udp_enabled.restype = c_bool

# /usr/include/tox/tox.h: 642
if hasattr(_libs['toxcore'], 'tox_options_set_udp_enabled'):
    tox_options_set_udp_enabled = _libs['toxcore'].tox_options_set_udp_enabled
    tox_options_set_udp_enabled.argtypes = [POINTER(struct_Tox_Options), c_bool]
    tox_options_set_udp_enabled.restype = None

# /usr/include/tox/tox.h: 644
if hasattr(_libs['toxcore'], 'tox_options_get_local_discovery_enabled'):
    tox_options_get_local_discovery_enabled = _libs['toxcore'].tox_options_get_local_discovery_enabled
    tox_options_get_local_discovery_enabled.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_local_discovery_enabled.restype = c_bool

# /usr/include/tox/tox.h: 646
if hasattr(_libs['toxcore'], 'tox_options_set_local_discovery_enabled'):
    tox_options_set_local_discovery_enabled = _libs['toxcore'].tox_options_set_local_discovery_enabled
    tox_options_set_local_discovery_enabled.argtypes = [POINTER(struct_Tox_Options), c_bool]
    tox_options_set_local_discovery_enabled.restype = None

# /usr/include/tox/tox.h: 648
if hasattr(_libs['toxcore'], 'tox_options_get_proxy_type'):
    tox_options_get_proxy_type = _libs['toxcore'].tox_options_get_proxy_type
    tox_options_get_proxy_type.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_proxy_type.restype = TOX_PROXY_TYPE

# /usr/include/tox/tox.h: 650
if hasattr(_libs['toxcore'], 'tox_options_set_proxy_type'):
    tox_options_set_proxy_type = _libs['toxcore'].tox_options_set_proxy_type
    tox_options_set_proxy_type.argtypes = [POINTER(struct_Tox_Options), TOX_PROXY_TYPE]
    tox_options_set_proxy_type.restype = None

# /usr/include/tox/tox.h: 652
if hasattr(_libs['toxcore'], 'tox_options_get_proxy_host'):
    tox_options_get_proxy_host = _libs['toxcore'].tox_options_get_proxy_host
    tox_options_get_proxy_host.argtypes = [POINTER(struct_Tox_Options)]
    if sizeof(c_int) == sizeof(c_void_p):
        tox_options_get_proxy_host.restype = ReturnString
    else:
        tox_options_get_proxy_host.restype = String
        tox_options_get_proxy_host.errcheck = ReturnString

# /usr/include/tox/tox.h: 654
if hasattr(_libs['toxcore'], 'tox_options_set_proxy_host'):
    tox_options_set_proxy_host = _libs['toxcore'].tox_options_set_proxy_host
    tox_options_set_proxy_host.argtypes = [POINTER(struct_Tox_Options), String]
    tox_options_set_proxy_host.restype = None

# /usr/include/tox/tox.h: 656
if hasattr(_libs['toxcore'], 'tox_options_get_proxy_port'):
    tox_options_get_proxy_port = _libs['toxcore'].tox_options_get_proxy_port
    tox_options_get_proxy_port.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_proxy_port.restype = c_uint16

# /usr/include/tox/tox.h: 658
if hasattr(_libs['toxcore'], 'tox_options_set_proxy_port'):
    tox_options_set_proxy_port = _libs['toxcore'].tox_options_set_proxy_port
    tox_options_set_proxy_port.argtypes = [POINTER(struct_Tox_Options), c_uint16]
    tox_options_set_proxy_port.restype = None

# /usr/include/tox/tox.h: 660
if hasattr(_libs['toxcore'], 'tox_options_get_start_port'):
    tox_options_get_start_port = _libs['toxcore'].tox_options_get_start_port
    tox_options_get_start_port.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_start_port.restype = c_uint16

# /usr/include/tox/tox.h: 662
if hasattr(_libs['toxcore'], 'tox_options_set_start_port'):
    tox_options_set_start_port = _libs['toxcore'].tox_options_set_start_port
    tox_options_set_start_port.argtypes = [POINTER(struct_Tox_Options), c_uint16]
    tox_options_set_start_port.restype = None

# /usr/include/tox/tox.h: 664
if hasattr(_libs['toxcore'], 'tox_options_get_end_port'):
    tox_options_get_end_port = _libs['toxcore'].tox_options_get_end_port
    tox_options_get_end_port.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_end_port.restype = c_uint16

# /usr/include/tox/tox.h: 666
if hasattr(_libs['toxcore'], 'tox_options_set_end_port'):
    tox_options_set_end_port = _libs['toxcore'].tox_options_set_end_port
    tox_options_set_end_port.argtypes = [POINTER(struct_Tox_Options), c_uint16]
    tox_options_set_end_port.restype = None

# /usr/include/tox/tox.h: 668
if hasattr(_libs['toxcore'], 'tox_options_get_tcp_port'):
    tox_options_get_tcp_port = _libs['toxcore'].tox_options_get_tcp_port
    tox_options_get_tcp_port.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_tcp_port.restype = c_uint16

# /usr/include/tox/tox.h: 670
if hasattr(_libs['toxcore'], 'tox_options_set_tcp_port'):
    tox_options_set_tcp_port = _libs['toxcore'].tox_options_set_tcp_port
    tox_options_set_tcp_port.argtypes = [POINTER(struct_Tox_Options), c_uint16]
    tox_options_set_tcp_port.restype = None

# /usr/include/tox/tox.h: 672
if hasattr(_libs['toxcore'], 'tox_options_get_hole_punching_enabled'):
    tox_options_get_hole_punching_enabled = _libs['toxcore'].tox_options_get_hole_punching_enabled
    tox_options_get_hole_punching_enabled.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_hole_punching_enabled.restype = c_bool

# /usr/include/tox/tox.h: 674
if hasattr(_libs['toxcore'], 'tox_options_set_hole_punching_enabled'):
    tox_options_set_hole_punching_enabled = _libs['toxcore'].tox_options_set_hole_punching_enabled
    tox_options_set_hole_punching_enabled.argtypes = [POINTER(struct_Tox_Options), c_bool]
    tox_options_set_hole_punching_enabled.restype = None

# /usr/include/tox/tox.h: 676
if hasattr(_libs['toxcore'], 'tox_options_get_savedata_type'):
    tox_options_get_savedata_type = _libs['toxcore'].tox_options_get_savedata_type
    tox_options_get_savedata_type.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_savedata_type.restype = TOX_SAVEDATA_TYPE

# /usr/include/tox/tox.h: 678
if hasattr(_libs['toxcore'], 'tox_options_set_savedata_type'):
    tox_options_set_savedata_type = _libs['toxcore'].tox_options_set_savedata_type
    tox_options_set_savedata_type.argtypes = [POINTER(struct_Tox_Options), TOX_SAVEDATA_TYPE]
    tox_options_set_savedata_type.restype = None

# /usr/include/tox/tox.h: 680
if hasattr(_libs['toxcore'], 'tox_options_get_savedata_data'):
    tox_options_get_savedata_data = _libs['toxcore'].tox_options_get_savedata_data
    tox_options_get_savedata_data.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_savedata_data.restype = POINTER(c_uint8)

# /usr/include/tox/tox.h: 682
if hasattr(_libs['toxcore'], 'tox_options_set_savedata_data'):
    tox_options_set_savedata_data = _libs['toxcore'].tox_options_set_savedata_data
    tox_options_set_savedata_data.argtypes = [POINTER(struct_Tox_Options), POINTER(c_uint8), c_size_t]
    tox_options_set_savedata_data.restype = None

# /usr/include/tox/tox.h: 684
if hasattr(_libs['toxcore'], 'tox_options_get_savedata_length'):
    tox_options_get_savedata_length = _libs['toxcore'].tox_options_get_savedata_length
    tox_options_get_savedata_length.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_savedata_length.restype = c_size_t

# /usr/include/tox/tox.h: 686
if hasattr(_libs['toxcore'], 'tox_options_set_savedata_length'):
    tox_options_set_savedata_length = _libs['toxcore'].tox_options_set_savedata_length
    tox_options_set_savedata_length.argtypes = [POINTER(struct_Tox_Options), c_size_t]
    tox_options_set_savedata_length.restype = None

# /usr/include/tox/tox.h: 688
if hasattr(_libs['toxcore'], 'tox_options_get_log_callback'):
    tox_options_get_log_callback = _libs['toxcore'].tox_options_get_log_callback
    tox_options_get_log_callback.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_log_callback.restype = POINTER(tox_log_cb)

# /usr/include/tox/tox.h: 690
if hasattr(_libs['toxcore'], 'tox_options_set_log_callback'):
    tox_options_set_log_callback = _libs['toxcore'].tox_options_set_log_callback
    tox_options_set_log_callback.argtypes = [POINTER(struct_Tox_Options), POINTER(tox_log_cb)]
    tox_options_set_log_callback.restype = None

# /usr/include/tox/tox.h: 692
if hasattr(_libs['toxcore'], 'tox_options_get_log_user_data'):
    tox_options_get_log_user_data = _libs['toxcore'].tox_options_get_log_user_data
    tox_options_get_log_user_data.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_get_log_user_data.restype = POINTER(None)

# /usr/include/tox/tox.h: 694
if hasattr(_libs['toxcore'], 'tox_options_set_log_user_data'):
    tox_options_set_log_user_data = _libs['toxcore'].tox_options_set_log_user_data
    tox_options_set_log_user_data.argtypes = [POINTER(struct_Tox_Options), POINTER(None)]
    tox_options_set_log_user_data.restype = None

# /usr/include/tox/tox.h: 707
if hasattr(_libs['toxcore'], 'tox_options_default'):
    tox_options_default = _libs['toxcore'].tox_options_default
    tox_options_default.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_default.restype = None

enum_TOX_ERR_OPTIONS_NEW = c_int # /usr/include/tox/tox.h: 721

TOX_ERR_OPTIONS_NEW_OK = 0 # /usr/include/tox/tox.h: 721

TOX_ERR_OPTIONS_NEW_MALLOC = (TOX_ERR_OPTIONS_NEW_OK + 1) # /usr/include/tox/tox.h: 721

TOX_ERR_OPTIONS_NEW = enum_TOX_ERR_OPTIONS_NEW # /usr/include/tox/tox.h: 721

# /usr/include/tox/tox.h: 734
if hasattr(_libs['toxcore'], 'tox_options_new'):
    tox_options_new = _libs['toxcore'].tox_options_new
    tox_options_new.argtypes = [POINTER(TOX_ERR_OPTIONS_NEW)]
    tox_options_new.restype = POINTER(struct_Tox_Options)

# /usr/include/tox/tox.h: 742
if hasattr(_libs['toxcore'], 'tox_options_free'):
    tox_options_free = _libs['toxcore'].tox_options_free
    tox_options_free.argtypes = [POINTER(struct_Tox_Options)]
    tox_options_free.restype = None

enum_TOX_ERR_NEW = c_int # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_OK = 0 # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_NULL = (TOX_ERR_NEW_OK + 1) # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_MALLOC = (TOX_ERR_NEW_NULL + 1) # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_PORT_ALLOC = (TOX_ERR_NEW_MALLOC + 1) # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_PROXY_BAD_TYPE = (TOX_ERR_NEW_PORT_ALLOC + 1) # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_PROXY_BAD_HOST = (TOX_ERR_NEW_PROXY_BAD_TYPE + 1) # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_PROXY_BAD_PORT = (TOX_ERR_NEW_PROXY_BAD_HOST + 1) # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_PROXY_NOT_FOUND = (TOX_ERR_NEW_PROXY_BAD_PORT + 1) # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_LOAD_ENCRYPTED = (TOX_ERR_NEW_PROXY_NOT_FOUND + 1) # /usr/include/tox/tox.h: 813

TOX_ERR_NEW_LOAD_BAD_FORMAT = (TOX_ERR_NEW_LOAD_ENCRYPTED + 1) # /usr/include/tox/tox.h: 813

TOX_ERR_NEW = enum_TOX_ERR_NEW # /usr/include/tox/tox.h: 813

# /usr/include/tox/tox.h: 832
if hasattr(_libs['toxcore'], 'tox_new'):
    tox_new = _libs['toxcore'].tox_new
    tox_new.argtypes = [POINTER(struct_Tox_Options), POINTER(TOX_ERR_NEW)]
    tox_new.restype = POINTER(Tox)

# /usr/include/tox/tox.h: 841
if hasattr(_libs['toxcore'], 'tox_kill'):
    tox_kill = _libs['toxcore'].tox_kill
    tox_kill.argtypes = [POINTER(Tox)]
    tox_kill.restype = None

# /usr/include/tox/tox.h: 849
if hasattr(_libs['toxcore'], 'tox_get_savedata_size'):
    tox_get_savedata_size = _libs['toxcore'].tox_get_savedata_size
    tox_get_savedata_size.argtypes = [POINTER(Tox)]
    tox_get_savedata_size.restype = c_size_t

# /usr/include/tox/tox.h: 858
if hasattr(_libs['toxcore'], 'tox_get_savedata'):
    tox_get_savedata = _libs['toxcore'].tox_get_savedata
    tox_get_savedata.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_get_savedata.restype = None

enum_TOX_ERR_BOOTSTRAP = c_int # /usr/include/tox/tox.h: 892

TOX_ERR_BOOTSTRAP_OK = 0 # /usr/include/tox/tox.h: 892

TOX_ERR_BOOTSTRAP_NULL = (TOX_ERR_BOOTSTRAP_OK + 1) # /usr/include/tox/tox.h: 892

TOX_ERR_BOOTSTRAP_BAD_HOST = (TOX_ERR_BOOTSTRAP_NULL + 1) # /usr/include/tox/tox.h: 892

TOX_ERR_BOOTSTRAP_BAD_PORT = (TOX_ERR_BOOTSTRAP_BAD_HOST + 1) # /usr/include/tox/tox.h: 892

TOX_ERR_BOOTSTRAP = enum_TOX_ERR_BOOTSTRAP # /usr/include/tox/tox.h: 892

# /usr/include/tox/tox.h: 909
if hasattr(_libs['toxcore'], 'tox_bootstrap'):
    tox_bootstrap = _libs['toxcore'].tox_bootstrap
    tox_bootstrap.argtypes = [POINTER(Tox), String, c_uint16, POINTER(c_uint8), POINTER(TOX_ERR_BOOTSTRAP)]
    tox_bootstrap.restype = c_bool

# /usr/include/tox/tox.h: 924
if hasattr(_libs['toxcore'], 'tox_add_tcp_relay'):
    tox_add_tcp_relay = _libs['toxcore'].tox_add_tcp_relay
    tox_add_tcp_relay.argtypes = [POINTER(Tox), String, c_uint16, POINTER(c_uint8), POINTER(TOX_ERR_BOOTSTRAP)]
    tox_add_tcp_relay.restype = c_bool

enum_TOX_CONNECTION = c_int # /usr/include/tox/tox.h: 953

TOX_CONNECTION_NONE = 0 # /usr/include/tox/tox.h: 953

TOX_CONNECTION_TCP = (TOX_CONNECTION_NONE + 1) # /usr/include/tox/tox.h: 953

TOX_CONNECTION_UDP = (TOX_CONNECTION_TCP + 1) # /usr/include/tox/tox.h: 953

TOX_CONNECTION = enum_TOX_CONNECTION # /usr/include/tox/tox.h: 953

# /usr/include/tox/tox.h: 960
if hasattr(_libs['toxcore'], 'tox_self_get_connection_status'):
    tox_self_get_connection_status = _libs['toxcore'].tox_self_get_connection_status
    tox_self_get_connection_status.argtypes = [POINTER(Tox)]
    tox_self_get_connection_status.restype = TOX_CONNECTION

tox_self_connection_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), TOX_CONNECTION, POINTER(None)) # /usr/include/tox/tox.h: 965

# /usr/include/tox/tox.h: 979
if hasattr(_libs['toxcore'], 'tox_callback_self_connection_status'):
    tox_callback_self_connection_status = _libs['toxcore'].tox_callback_self_connection_status
    tox_callback_self_connection_status.argtypes = [POINTER(Tox), POINTER(tox_self_connection_status_cb)]
    tox_callback_self_connection_status.restype = None

# /usr/include/tox/tox.h: 985
if hasattr(_libs['toxcore'], 'tox_iteration_interval'):
    tox_iteration_interval = _libs['toxcore'].tox_iteration_interval
    tox_iteration_interval.argtypes = [POINTER(Tox)]
    tox_iteration_interval.restype = c_uint32

# /usr/include/tox/tox.h: 991
if hasattr(_libs['toxcore'], 'tox_iterate'):
    tox_iterate = _libs['toxcore'].tox_iterate
    tox_iterate.argtypes = [POINTER(Tox), POINTER(None)]
    tox_iterate.restype = None

# /usr/include/tox/tox.h: 1011
if hasattr(_libs['toxcore'], 'tox_self_get_address'):
    tox_self_get_address = _libs['toxcore'].tox_self_get_address
    tox_self_get_address.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_address.restype = None

# /usr/include/tox/tox.h: 1020
if hasattr(_libs['toxcore'], 'tox_self_set_nospam'):
    tox_self_set_nospam = _libs['toxcore'].tox_self_set_nospam
    tox_self_set_nospam.argtypes = [POINTER(Tox), c_uint32]
    tox_self_set_nospam.restype = None

# /usr/include/tox/tox.h: 1026
if hasattr(_libs['toxcore'], 'tox_self_get_nospam'):
    tox_self_get_nospam = _libs['toxcore'].tox_self_get_nospam
    tox_self_get_nospam.argtypes = [POINTER(Tox)]
    tox_self_get_nospam.restype = c_uint32

# /usr/include/tox/tox.h: 1034
if hasattr(_libs['toxcore'], 'tox_self_get_public_key'):
    tox_self_get_public_key = _libs['toxcore'].tox_self_get_public_key
    tox_self_get_public_key.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_public_key.restype = None

# /usr/include/tox/tox.h: 1042
if hasattr(_libs['toxcore'], 'tox_self_get_secret_key'):
    tox_self_get_secret_key = _libs['toxcore'].tox_self_get_secret_key
    tox_self_get_secret_key.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_secret_key.restype = None

enum_TOX_ERR_SET_INFO = c_int # /usr/include/tox/tox.h: 1074

TOX_ERR_SET_INFO_OK = 0 # /usr/include/tox/tox.h: 1074

TOX_ERR_SET_INFO_NULL = (TOX_ERR_SET_INFO_OK + 1) # /usr/include/tox/tox.h: 1074

TOX_ERR_SET_INFO_TOO_LONG = (TOX_ERR_SET_INFO_NULL + 1) # /usr/include/tox/tox.h: 1074

TOX_ERR_SET_INFO = enum_TOX_ERR_SET_INFO # /usr/include/tox/tox.h: 1074

# /usr/include/tox/tox.h: 1088
if hasattr(_libs['toxcore'], 'tox_self_set_name'):
    tox_self_set_name = _libs['toxcore'].tox_self_set_name
    tox_self_set_name.argtypes = [POINTER(Tox), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_SET_INFO)]
    tox_self_set_name.restype = c_bool

# /usr/include/tox/tox.h: 1098
if hasattr(_libs['toxcore'], 'tox_self_get_name_size'):
    tox_self_get_name_size = _libs['toxcore'].tox_self_get_name_size
    tox_self_get_name_size.argtypes = [POINTER(Tox)]
    tox_self_get_name_size.restype = c_size_t

# /usr/include/tox/tox.h: 1112
if hasattr(_libs['toxcore'], 'tox_self_get_name'):
    tox_self_get_name = _libs['toxcore'].tox_self_get_name
    tox_self_get_name.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_name.restype = None

# /usr/include/tox/tox.h: 1121
if hasattr(_libs['toxcore'], 'tox_self_set_status_message'):
    tox_self_set_status_message = _libs['toxcore'].tox_self_set_status_message
    tox_self_set_status_message.argtypes = [POINTER(Tox), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_SET_INFO)]
    tox_self_set_status_message.restype = c_bool

# /usr/include/tox/tox.h: 1131
if hasattr(_libs['toxcore'], 'tox_self_get_status_message_size'):
    tox_self_get_status_message_size = _libs['toxcore'].tox_self_get_status_message_size
    tox_self_get_status_message_size.argtypes = [POINTER(Tox)]
    tox_self_get_status_message_size.restype = c_size_t

# /usr/include/tox/tox.h: 1145
if hasattr(_libs['toxcore'], 'tox_self_get_status_message'):
    tox_self_get_status_message = _libs['toxcore'].tox_self_get_status_message
    tox_self_get_status_message.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_status_message.restype = None

# /usr/include/tox/tox.h: 1152
if hasattr(_libs['toxcore'], 'tox_self_set_status'):
    tox_self_set_status = _libs['toxcore'].tox_self_set_status
    tox_self_set_status.argtypes = [POINTER(Tox), TOX_USER_STATUS]
    tox_self_set_status.restype = None

# /usr/include/tox/tox.h: 1157
if hasattr(_libs['toxcore'], 'tox_self_get_status'):
    tox_self_get_status = _libs['toxcore'].tox_self_get_status
    tox_self_get_status.argtypes = [POINTER(Tox)]
    tox_self_get_status.restype = TOX_USER_STATUS

enum_TOX_ERR_FRIEND_ADD = c_int # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD_OK = 0 # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD_NULL = (TOX_ERR_FRIEND_ADD_OK + 1) # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD_TOO_LONG = (TOX_ERR_FRIEND_ADD_NULL + 1) # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD_NO_MESSAGE = (TOX_ERR_FRIEND_ADD_TOO_LONG + 1) # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD_OWN_KEY = (TOX_ERR_FRIEND_ADD_NO_MESSAGE + 1) # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD_ALREADY_SENT = (TOX_ERR_FRIEND_ADD_OWN_KEY + 1) # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD_BAD_CHECKSUM = (TOX_ERR_FRIEND_ADD_ALREADY_SENT + 1) # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD_SET_NEW_NOSPAM = (TOX_ERR_FRIEND_ADD_BAD_CHECKSUM + 1) # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD_MALLOC = (TOX_ERR_FRIEND_ADD_SET_NEW_NOSPAM + 1) # /usr/include/tox/tox.h: 1218

TOX_ERR_FRIEND_ADD = enum_TOX_ERR_FRIEND_ADD # /usr/include/tox/tox.h: 1218

# /usr/include/tox/tox.h: 1244
if hasattr(_libs['toxcore'], 'tox_friend_add'):
    tox_friend_add = _libs['toxcore'].tox_friend_add
    tox_friend_add.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_ADD)]
    tox_friend_add.restype = c_uint32

# /usr/include/tox/tox.h: 1265
if hasattr(_libs['toxcore'], 'tox_friend_add_norequest'):
    tox_friend_add_norequest = _libs['toxcore'].tox_friend_add_norequest
    tox_friend_add_norequest.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_ADD)]
    tox_friend_add_norequest.restype = c_uint32

enum_TOX_ERR_FRIEND_DELETE = c_int # /usr/include/tox/tox.h: 1279

TOX_ERR_FRIEND_DELETE_OK = 0 # /usr/include/tox/tox.h: 1279

TOX_ERR_FRIEND_DELETE_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_DELETE_OK + 1) # /usr/include/tox/tox.h: 1279

TOX_ERR_FRIEND_DELETE = enum_TOX_ERR_FRIEND_DELETE # /usr/include/tox/tox.h: 1279

# /usr/include/tox/tox.h: 1293
if hasattr(_libs['toxcore'], 'tox_friend_delete'):
    tox_friend_delete = _libs['toxcore'].tox_friend_delete
    tox_friend_delete.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_DELETE)]
    tox_friend_delete.restype = c_bool

enum_TOX_ERR_FRIEND_BY_PUBLIC_KEY = c_int # /usr/include/tox/tox.h: 1321

TOX_ERR_FRIEND_BY_PUBLIC_KEY_OK = 0 # /usr/include/tox/tox.h: 1321

TOX_ERR_FRIEND_BY_PUBLIC_KEY_NULL = (TOX_ERR_FRIEND_BY_PUBLIC_KEY_OK + 1) # /usr/include/tox/tox.h: 1321

TOX_ERR_FRIEND_BY_PUBLIC_KEY_NOT_FOUND = (TOX_ERR_FRIEND_BY_PUBLIC_KEY_NULL + 1) # /usr/include/tox/tox.h: 1321

TOX_ERR_FRIEND_BY_PUBLIC_KEY = enum_TOX_ERR_FRIEND_BY_PUBLIC_KEY # /usr/include/tox/tox.h: 1321

# /usr/include/tox/tox.h: 1330
if hasattr(_libs['toxcore'], 'tox_friend_by_public_key'):
    tox_friend_by_public_key = _libs['toxcore'].tox_friend_by_public_key
    tox_friend_by_public_key.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_BY_PUBLIC_KEY)]
    tox_friend_by_public_key.restype = c_uint32

# /usr/include/tox/tox.h: 1336
if hasattr(_libs['toxcore'], 'tox_friend_exists'):
    tox_friend_exists = _libs['toxcore'].tox_friend_exists
    tox_friend_exists.argtypes = [POINTER(Tox), c_uint32]
    tox_friend_exists.restype = c_bool

# /usr/include/tox/tox.h: 1344
if hasattr(_libs['toxcore'], 'tox_self_get_friend_list_size'):
    tox_self_get_friend_list_size = _libs['toxcore'].tox_self_get_friend_list_size
    tox_self_get_friend_list_size.argtypes = [POINTER(Tox)]
    tox_self_get_friend_list_size.restype = c_size_t

# /usr/include/tox/tox.h: 1354
if hasattr(_libs['toxcore'], 'tox_self_get_friend_list'):
    tox_self_get_friend_list = _libs['toxcore'].tox_self_get_friend_list
    tox_self_get_friend_list.argtypes = [POINTER(Tox), POINTER(c_uint32)]
    tox_self_get_friend_list.restype = None

enum_TOX_ERR_FRIEND_GET_PUBLIC_KEY = c_int # /usr/include/tox/tox.h: 1368

TOX_ERR_FRIEND_GET_PUBLIC_KEY_OK = 0 # /usr/include/tox/tox.h: 1368

TOX_ERR_FRIEND_GET_PUBLIC_KEY_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_GET_PUBLIC_KEY_OK + 1) # /usr/include/tox/tox.h: 1368

TOX_ERR_FRIEND_GET_PUBLIC_KEY = enum_TOX_ERR_FRIEND_GET_PUBLIC_KEY # /usr/include/tox/tox.h: 1368

# /usr/include/tox/tox.h: 1380
if hasattr(_libs['toxcore'], 'tox_friend_get_public_key'):
    tox_friend_get_public_key = _libs['toxcore'].tox_friend_get_public_key
    tox_friend_get_public_key.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_GET_PUBLIC_KEY)]
    tox_friend_get_public_key.restype = c_bool

enum_TOX_ERR_FRIEND_GET_LAST_ONLINE = c_int # /usr/include/tox/tox.h: 1395

TOX_ERR_FRIEND_GET_LAST_ONLINE_OK = 0 # /usr/include/tox/tox.h: 1395

TOX_ERR_FRIEND_GET_LAST_ONLINE_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_GET_LAST_ONLINE_OK + 1) # /usr/include/tox/tox.h: 1395

TOX_ERR_FRIEND_GET_LAST_ONLINE = enum_TOX_ERR_FRIEND_GET_LAST_ONLINE # /usr/include/tox/tox.h: 1395

# /usr/include/tox/tox.h: 1404
if hasattr(_libs['toxcore'], 'tox_friend_get_last_online'):
    tox_friend_get_last_online = _libs['toxcore'].tox_friend_get_last_online
    tox_friend_get_last_online.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_GET_LAST_ONLINE)]
    tox_friend_get_last_online.restype = c_uint64

enum_TOX_ERR_FRIEND_QUERY = c_int # /usr/include/tox/tox.h: 1437

TOX_ERR_FRIEND_QUERY_OK = 0 # /usr/include/tox/tox.h: 1437

TOX_ERR_FRIEND_QUERY_NULL = (TOX_ERR_FRIEND_QUERY_OK + 1) # /usr/include/tox/tox.h: 1437

TOX_ERR_FRIEND_QUERY_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_QUERY_NULL + 1) # /usr/include/tox/tox.h: 1437

TOX_ERR_FRIEND_QUERY = enum_TOX_ERR_FRIEND_QUERY # /usr/include/tox/tox.h: 1437

# /usr/include/tox/tox.h: 1447
if hasattr(_libs['toxcore'], 'tox_friend_get_name_size'):
    tox_friend_get_name_size = _libs['toxcore'].tox_friend_get_name_size
    tox_friend_get_name_size.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_name_size.restype = c_size_t

# /usr/include/tox/tox.h: 1463
if hasattr(_libs['toxcore'], 'tox_friend_get_name'):
    tox_friend_get_name = _libs['toxcore'].tox_friend_get_name
    tox_friend_get_name.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_name.restype = c_bool

tox_friend_name_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 1472

# /usr/include/tox/tox.h: 1480
if hasattr(_libs['toxcore'], 'tox_callback_friend_name'):
    tox_callback_friend_name = _libs['toxcore'].tox_callback_friend_name
    tox_callback_friend_name.argtypes = [POINTER(Tox), POINTER(tox_friend_name_cb)]
    tox_callback_friend_name.restype = None

# /usr/include/tox/tox.h: 1486
if hasattr(_libs['toxcore'], 'tox_friend_get_status_message_size'):
    tox_friend_get_status_message_size = _libs['toxcore'].tox_friend_get_status_message_size
    tox_friend_get_status_message_size.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_status_message_size.restype = c_size_t

# /usr/include/tox/tox.h: 1500
if hasattr(_libs['toxcore'], 'tox_friend_get_status_message'):
    tox_friend_get_status_message = _libs['toxcore'].tox_friend_get_status_message
    tox_friend_get_status_message.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_status_message.restype = c_bool

tox_friend_status_message_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 1511

# /usr/include/tox/tox.h: 1520
if hasattr(_libs['toxcore'], 'tox_callback_friend_status_message'):
    tox_callback_friend_status_message = _libs['toxcore'].tox_callback_friend_status_message
    tox_callback_friend_status_message.argtypes = [POINTER(Tox), POINTER(tox_friend_status_message_cb)]
    tox_callback_friend_status_message.restype = None

# /usr/include/tox/tox.h: 1529
if hasattr(_libs['toxcore'], 'tox_friend_get_status'):
    tox_friend_get_status = _libs['toxcore'].tox_friend_get_status
    tox_friend_get_status.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_status.restype = TOX_USER_STATUS

tox_friend_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_USER_STATUS, POINTER(None)) # /usr/include/tox/tox.h: 1536

# /usr/include/tox/tox.h: 1544
if hasattr(_libs['toxcore'], 'tox_callback_friend_status'):
    tox_callback_friend_status = _libs['toxcore'].tox_callback_friend_status
    tox_callback_friend_status.argtypes = [POINTER(Tox), POINTER(tox_friend_status_cb)]
    tox_callback_friend_status.restype = None

# /usr/include/tox/tox.h: 1558
if hasattr(_libs['toxcore'], 'tox_friend_get_connection_status'):
    tox_friend_get_connection_status = _libs['toxcore'].tox_friend_get_connection_status
    tox_friend_get_connection_status.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_connection_status.restype = TOX_CONNECTION

tox_friend_connection_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_CONNECTION, POINTER(None)) # /usr/include/tox/tox.h: 1566

# /usr/include/tox/tox.h: 1579
if hasattr(_libs['toxcore'], 'tox_callback_friend_connection_status'):
    tox_callback_friend_connection_status = _libs['toxcore'].tox_callback_friend_connection_status
    tox_callback_friend_connection_status.argtypes = [POINTER(Tox), POINTER(tox_friend_connection_status_cb)]
    tox_callback_friend_connection_status.restype = None

# /usr/include/tox/tox.h: 1590
if hasattr(_libs['toxcore'], 'tox_friend_get_typing'):
    tox_friend_get_typing = _libs['toxcore'].tox_friend_get_typing
    tox_friend_get_typing.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_FRIEND_QUERY)]
    tox_friend_get_typing.restype = c_bool

tox_friend_typing_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_bool, POINTER(None)) # /usr/include/tox/tox.h: 1598

# /usr/include/tox/tox.h: 1606
if hasattr(_libs['toxcore'], 'tox_callback_friend_typing'):
    tox_callback_friend_typing = _libs['toxcore'].tox_callback_friend_typing
    tox_callback_friend_typing.argtypes = [POINTER(Tox), POINTER(tox_friend_typing_cb)]
    tox_callback_friend_typing.restype = None

enum_TOX_ERR_SET_TYPING = c_int # /usr/include/tox/tox.h: 1629

TOX_ERR_SET_TYPING_OK = 0 # /usr/include/tox/tox.h: 1629

TOX_ERR_SET_TYPING_FRIEND_NOT_FOUND = (TOX_ERR_SET_TYPING_OK + 1) # /usr/include/tox/tox.h: 1629

TOX_ERR_SET_TYPING = enum_TOX_ERR_SET_TYPING # /usr/include/tox/tox.h: 1629

# /usr/include/tox/tox.h: 1642
if hasattr(_libs['toxcore'], 'tox_self_set_typing'):
    tox_self_set_typing = _libs['toxcore'].tox_self_set_typing
    tox_self_set_typing.argtypes = [POINTER(Tox), c_uint32, c_bool, POINTER(TOX_ERR_SET_TYPING)]
    tox_self_set_typing.restype = c_bool

enum_TOX_ERR_FRIEND_SEND_MESSAGE = c_int # /usr/include/tox/tox.h: 1681

TOX_ERR_FRIEND_SEND_MESSAGE_OK = 0 # /usr/include/tox/tox.h: 1681

TOX_ERR_FRIEND_SEND_MESSAGE_NULL = (TOX_ERR_FRIEND_SEND_MESSAGE_OK + 1) # /usr/include/tox/tox.h: 1681

TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_SEND_MESSAGE_NULL + 1) # /usr/include/tox/tox.h: 1681

TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_CONNECTED = (TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_FOUND + 1) # /usr/include/tox/tox.h: 1681

TOX_ERR_FRIEND_SEND_MESSAGE_SENDQ = (TOX_ERR_FRIEND_SEND_MESSAGE_FRIEND_NOT_CONNECTED + 1) # /usr/include/tox/tox.h: 1681

TOX_ERR_FRIEND_SEND_MESSAGE_TOO_LONG = (TOX_ERR_FRIEND_SEND_MESSAGE_SENDQ + 1) # /usr/include/tox/tox.h: 1681

TOX_ERR_FRIEND_SEND_MESSAGE_EMPTY = (TOX_ERR_FRIEND_SEND_MESSAGE_TOO_LONG + 1) # /usr/include/tox/tox.h: 1681

TOX_ERR_FRIEND_SEND_MESSAGE = enum_TOX_ERR_FRIEND_SEND_MESSAGE # /usr/include/tox/tox.h: 1681

# /usr/include/tox/tox.h: 1707
if hasattr(_libs['toxcore'], 'tox_friend_send_message'):
    tox_friend_send_message = _libs['toxcore'].tox_friend_send_message
    tox_friend_send_message.argtypes = [POINTER(Tox), c_uint32, TOX_MESSAGE_TYPE, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_SEND_MESSAGE)]
    tox_friend_send_message.restype = c_uint32

tox_friend_read_receipt_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, POINTER(None)) # /usr/include/tox/tox.h: 1715

# /usr/include/tox/tox.h: 1724
if hasattr(_libs['toxcore'], 'tox_callback_friend_read_receipt'):
    tox_callback_friend_read_receipt = _libs['toxcore'].tox_callback_friend_read_receipt
    tox_callback_friend_read_receipt.argtypes = [POINTER(Tox), POINTER(tox_friend_read_receipt_cb)]
    tox_callback_friend_read_receipt.restype = None

tox_friend_request_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 1740

# /usr/include/tox/tox.h: 1749
if hasattr(_libs['toxcore'], 'tox_callback_friend_request'):
    tox_callback_friend_request = _libs['toxcore'].tox_callback_friend_request
    tox_callback_friend_request.argtypes = [POINTER(Tox), POINTER(tox_friend_request_cb)]
    tox_callback_friend_request.restype = None

tox_friend_message_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_MESSAGE_TYPE, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 1756

# /usr/include/tox/tox.h: 1765
if hasattr(_libs['toxcore'], 'tox_callback_friend_message'):
    tox_callback_friend_message = _libs['toxcore'].tox_callback_friend_message
    tox_callback_friend_message.argtypes = [POINTER(Tox), POINTER(tox_friend_message_cb)]
    tox_callback_friend_message.restype = None

# /usr/include/tox/tox.h: 1795
if hasattr(_libs['toxcore'], 'tox_hash'):
    tox_hash = _libs['toxcore'].tox_hash
    tox_hash.argtypes = [POINTER(c_uint8), POINTER(c_uint8), c_size_t]
    tox_hash.restype = c_bool

enum_TOX_FILE_KIND = c_int # /usr/include/tox/tox.h: 1797

TOX_FILE_KIND_DATA = 0 # /usr/include/tox/tox.h: 1797

TOX_FILE_KIND_AVATAR = (TOX_FILE_KIND_DATA + 1) # /usr/include/tox/tox.h: 1797

enum_TOX_FILE_CONTROL = c_int # /usr/include/tox/tox.h: 1852

TOX_FILE_CONTROL_RESUME = 0 # /usr/include/tox/tox.h: 1852

TOX_FILE_CONTROL_PAUSE = (TOX_FILE_CONTROL_RESUME + 1) # /usr/include/tox/tox.h: 1852

TOX_FILE_CONTROL_CANCEL = (TOX_FILE_CONTROL_PAUSE + 1) # /usr/include/tox/tox.h: 1852

TOX_FILE_CONTROL = enum_TOX_FILE_CONTROL # /usr/include/tox/tox.h: 1852

enum_TOX_ERR_FILE_CONTROL = c_int # /usr/include/tox/tox.h: 1898

TOX_ERR_FILE_CONTROL_OK = 0 # /usr/include/tox/tox.h: 1898

TOX_ERR_FILE_CONTROL_FRIEND_NOT_FOUND = (TOX_ERR_FILE_CONTROL_OK + 1) # /usr/include/tox/tox.h: 1898

TOX_ERR_FILE_CONTROL_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_CONTROL_FRIEND_NOT_FOUND + 1) # /usr/include/tox/tox.h: 1898

TOX_ERR_FILE_CONTROL_NOT_FOUND = (TOX_ERR_FILE_CONTROL_FRIEND_NOT_CONNECTED + 1) # /usr/include/tox/tox.h: 1898

TOX_ERR_FILE_CONTROL_NOT_PAUSED = (TOX_ERR_FILE_CONTROL_NOT_FOUND + 1) # /usr/include/tox/tox.h: 1898

TOX_ERR_FILE_CONTROL_DENIED = (TOX_ERR_FILE_CONTROL_NOT_PAUSED + 1) # /usr/include/tox/tox.h: 1898

TOX_ERR_FILE_CONTROL_ALREADY_PAUSED = (TOX_ERR_FILE_CONTROL_DENIED + 1) # /usr/include/tox/tox.h: 1898

TOX_ERR_FILE_CONTROL_SENDQ = (TOX_ERR_FILE_CONTROL_ALREADY_PAUSED + 1) # /usr/include/tox/tox.h: 1898

TOX_ERR_FILE_CONTROL = enum_TOX_ERR_FILE_CONTROL # /usr/include/tox/tox.h: 1898

# /usr/include/tox/tox.h: 1911
if hasattr(_libs['toxcore'], 'tox_file_control'):
    tox_file_control = _libs['toxcore'].tox_file_control
    tox_file_control.argtypes = [POINTER(Tox), c_uint32, c_uint32, TOX_FILE_CONTROL, POINTER(TOX_ERR_FILE_CONTROL)]
    tox_file_control.restype = c_bool

tox_file_recv_control_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, TOX_FILE_CONTROL, POINTER(None)) # /usr/include/tox/tox.h: 1923

# /usr/include/tox/tox.h: 1933
if hasattr(_libs['toxcore'], 'tox_callback_file_recv_control'):
    tox_callback_file_recv_control = _libs['toxcore'].tox_callback_file_recv_control
    tox_callback_file_recv_control.argtypes = [POINTER(Tox), POINTER(tox_file_recv_control_cb)]
    tox_callback_file_recv_control.restype = None

enum_TOX_ERR_FILE_SEEK = c_int # /usr/include/tox/tox.h: 1972

TOX_ERR_FILE_SEEK_OK = 0 # /usr/include/tox/tox.h: 1972

TOX_ERR_FILE_SEEK_FRIEND_NOT_FOUND = (TOX_ERR_FILE_SEEK_OK + 1) # /usr/include/tox/tox.h: 1972

TOX_ERR_FILE_SEEK_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_SEEK_FRIEND_NOT_FOUND + 1) # /usr/include/tox/tox.h: 1972

TOX_ERR_FILE_SEEK_NOT_FOUND = (TOX_ERR_FILE_SEEK_FRIEND_NOT_CONNECTED + 1) # /usr/include/tox/tox.h: 1972

TOX_ERR_FILE_SEEK_DENIED = (TOX_ERR_FILE_SEEK_NOT_FOUND + 1) # /usr/include/tox/tox.h: 1972

TOX_ERR_FILE_SEEK_INVALID_POSITION = (TOX_ERR_FILE_SEEK_DENIED + 1) # /usr/include/tox/tox.h: 1972

TOX_ERR_FILE_SEEK_SENDQ = (TOX_ERR_FILE_SEEK_INVALID_POSITION + 1) # /usr/include/tox/tox.h: 1972

TOX_ERR_FILE_SEEK = enum_TOX_ERR_FILE_SEEK # /usr/include/tox/tox.h: 1972

# /usr/include/tox/tox.h: 1986
if hasattr(_libs['toxcore'], 'tox_file_seek'):
    tox_file_seek = _libs['toxcore'].tox_file_seek
    tox_file_seek.argtypes = [POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(TOX_ERR_FILE_SEEK)]
    tox_file_seek.restype = c_bool

enum_TOX_ERR_FILE_GET = c_int # /usr/include/tox/tox.h: 2010

TOX_ERR_FILE_GET_OK = 0 # /usr/include/tox/tox.h: 2010

TOX_ERR_FILE_GET_NULL = (TOX_ERR_FILE_GET_OK + 1) # /usr/include/tox/tox.h: 2010

TOX_ERR_FILE_GET_FRIEND_NOT_FOUND = (TOX_ERR_FILE_GET_NULL + 1) # /usr/include/tox/tox.h: 2010

TOX_ERR_FILE_GET_NOT_FOUND = (TOX_ERR_FILE_GET_FRIEND_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2010

TOX_ERR_FILE_GET = enum_TOX_ERR_FILE_GET # /usr/include/tox/tox.h: 2010

# /usr/include/tox/tox.h: 2024
if hasattr(_libs['toxcore'], 'tox_file_get_file_id'):
    tox_file_get_file_id = _libs['toxcore'].tox_file_get_file_id
    tox_file_get_file_id.argtypes = [POINTER(Tox), c_uint32, c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_FILE_GET)]
    tox_file_get_file_id.restype = c_bool

enum_TOX_ERR_FILE_SEND = c_int # /usr/include/tox/tox.h: 2069

TOX_ERR_FILE_SEND_OK = 0 # /usr/include/tox/tox.h: 2069

TOX_ERR_FILE_SEND_NULL = (TOX_ERR_FILE_SEND_OK + 1) # /usr/include/tox/tox.h: 2069

TOX_ERR_FILE_SEND_FRIEND_NOT_FOUND = (TOX_ERR_FILE_SEND_NULL + 1) # /usr/include/tox/tox.h: 2069

TOX_ERR_FILE_SEND_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_SEND_FRIEND_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2069

TOX_ERR_FILE_SEND_NAME_TOO_LONG = (TOX_ERR_FILE_SEND_FRIEND_NOT_CONNECTED + 1) # /usr/include/tox/tox.h: 2069

TOX_ERR_FILE_SEND_TOO_MANY = (TOX_ERR_FILE_SEND_NAME_TOO_LONG + 1) # /usr/include/tox/tox.h: 2069

TOX_ERR_FILE_SEND = enum_TOX_ERR_FILE_SEND # /usr/include/tox/tox.h: 2069

# /usr/include/tox/tox.h: 2131
if hasattr(_libs['toxcore'], 'tox_file_send'):
    tox_file_send = _libs['toxcore'].tox_file_send
    tox_file_send.argtypes = [POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FILE_SEND)]
    tox_file_send.restype = c_uint32

enum_TOX_ERR_FILE_SEND_CHUNK = c_int # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK_OK = 0 # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK_NULL = (TOX_ERR_FILE_SEND_CHUNK_OK + 1) # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_FOUND = (TOX_ERR_FILE_SEND_CHUNK_NULL + 1) # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_CONNECTED = (TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK_NOT_FOUND = (TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_CONNECTED + 1) # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK_NOT_TRANSFERRING = (TOX_ERR_FILE_SEND_CHUNK_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK_INVALID_LENGTH = (TOX_ERR_FILE_SEND_CHUNK_NOT_TRANSFERRING + 1) # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK_SENDQ = (TOX_ERR_FILE_SEND_CHUNK_INVALID_LENGTH + 1) # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK_WRONG_POSITION = (TOX_ERR_FILE_SEND_CHUNK_SENDQ + 1) # /usr/include/tox/tox.h: 2184

TOX_ERR_FILE_SEND_CHUNK = enum_TOX_ERR_FILE_SEND_CHUNK # /usr/include/tox/tox.h: 2184

# /usr/include/tox/tox.h: 2203
if hasattr(_libs['toxcore'], 'tox_file_send_chunk'):
    tox_file_send_chunk = _libs['toxcore'].tox_file_send_chunk
    tox_file_send_chunk.argtypes = [POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FILE_SEND_CHUNK)]
    tox_file_send_chunk.restype = c_bool

tox_file_chunk_request_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, c_uint64, c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 2228

# /usr/include/tox/tox.h: 2237
if hasattr(_libs['toxcore'], 'tox_callback_file_chunk_request'):
    tox_callback_file_chunk_request = _libs['toxcore'].tox_callback_file_chunk_request
    tox_callback_file_chunk_request.argtypes = [POINTER(Tox), POINTER(tox_file_chunk_request_cb)]
    tox_callback_file_chunk_request.restype = None

tox_file_recv_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, c_uint32, c_uint64, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 2266

# /usr/include/tox/tox.h: 2275
if hasattr(_libs['toxcore'], 'tox_callback_file_recv'):
    tox_callback_file_recv = _libs['toxcore'].tox_callback_file_recv
    tox_callback_file_recv.argtypes = [POINTER(Tox), POINTER(tox_file_recv_cb)]
    tox_callback_file_recv.restype = None

tox_file_recv_chunk_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, c_uint64, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 2293

# /usr/include/tox/tox.h: 2303
if hasattr(_libs['toxcore'], 'tox_callback_file_recv_chunk'):
    tox_callback_file_recv_chunk = _libs['toxcore'].tox_callback_file_recv_chunk
    tox_callback_file_recv_chunk.argtypes = [POINTER(Tox), POINTER(tox_file_recv_chunk_cb)]
    tox_callback_file_recv_chunk.restype = None

enum_TOX_CONFERENCE_TYPE = c_int # /usr/include/tox/tox.h: 2329

TOX_CONFERENCE_TYPE_TEXT = 0 # /usr/include/tox/tox.h: 2329

TOX_CONFERENCE_TYPE_AV = (TOX_CONFERENCE_TYPE_TEXT + 1) # /usr/include/tox/tox.h: 2329

TOX_CONFERENCE_TYPE = enum_TOX_CONFERENCE_TYPE # /usr/include/tox/tox.h: 2329

tox_conference_invite_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, TOX_CONFERENCE_TYPE, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 2342

# /usr/include/tox/tox.h: 2351
if hasattr(_libs['toxcore'], 'tox_callback_conference_invite'):
    tox_callback_conference_invite = _libs['toxcore'].tox_callback_conference_invite
    tox_callback_conference_invite.argtypes = [POINTER(Tox), POINTER(tox_conference_invite_cb)]
    tox_callback_conference_invite.restype = None

tox_conference_message_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, TOX_MESSAGE_TYPE, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 2360

# /usr/include/tox/tox.h: 2369
if hasattr(_libs['toxcore'], 'tox_callback_conference_message'):
    tox_callback_conference_message = _libs['toxcore'].tox_callback_conference_message
    tox_callback_conference_message.argtypes = [POINTER(Tox), POINTER(tox_conference_message_cb)]
    tox_callback_conference_message.restype = None

tox_conference_title_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 2377

# /usr/include/tox/tox.h: 2388
if hasattr(_libs['toxcore'], 'tox_callback_conference_title'):
    tox_callback_conference_title = _libs['toxcore'].tox_callback_conference_title
    tox_callback_conference_title.argtypes = [POINTER(Tox), POINTER(tox_conference_title_cb)]
    tox_callback_conference_title.restype = None

enum_TOX_CONFERENCE_STATE_CHANGE = c_int # /usr/include/tox/tox.h: 2410

TOX_CONFERENCE_STATE_CHANGE_PEER_JOIN = 0 # /usr/include/tox/tox.h: 2410

TOX_CONFERENCE_STATE_CHANGE_PEER_EXIT = (TOX_CONFERENCE_STATE_CHANGE_PEER_JOIN + 1) # /usr/include/tox/tox.h: 2410

TOX_CONFERENCE_STATE_CHANGE_PEER_NAME_CHANGE = (TOX_CONFERENCE_STATE_CHANGE_PEER_EXIT + 1) # /usr/include/tox/tox.h: 2410

TOX_CONFERENCE_STATE_CHANGE = enum_TOX_CONFERENCE_STATE_CHANGE # /usr/include/tox/tox.h: 2410

tox_conference_namelist_change_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, c_uint32, TOX_CONFERENCE_STATE_CHANGE, POINTER(None)) # /usr/include/tox/tox.h: 2418

# /usr/include/tox/tox.h: 2427
if hasattr(_libs['toxcore'], 'tox_callback_conference_namelist_change'):
    tox_callback_conference_namelist_change = _libs['toxcore'].tox_callback_conference_namelist_change
    tox_callback_conference_namelist_change.argtypes = [POINTER(Tox), POINTER(tox_conference_namelist_change_cb)]
    tox_callback_conference_namelist_change.restype = None

enum_TOX_ERR_CONFERENCE_NEW = c_int # /usr/include/tox/tox.h: 2441

TOX_ERR_CONFERENCE_NEW_OK = 0 # /usr/include/tox/tox.h: 2441

TOX_ERR_CONFERENCE_NEW_INIT = (TOX_ERR_CONFERENCE_NEW_OK + 1) # /usr/include/tox/tox.h: 2441

TOX_ERR_CONFERENCE_NEW = enum_TOX_ERR_CONFERENCE_NEW # /usr/include/tox/tox.h: 2441

# /usr/include/tox/tox.h: 2451
if hasattr(_libs['toxcore'], 'tox_conference_new'):
    tox_conference_new = _libs['toxcore'].tox_conference_new
    tox_conference_new.argtypes = [POINTER(Tox), POINTER(TOX_ERR_CONFERENCE_NEW)]
    tox_conference_new.restype = c_uint32

enum_TOX_ERR_CONFERENCE_DELETE = c_int # /usr/include/tox/tox.h: 2465

TOX_ERR_CONFERENCE_DELETE_OK = 0 # /usr/include/tox/tox.h: 2465

TOX_ERR_CONFERENCE_DELETE_CONFERENCE_NOT_FOUND = (TOX_ERR_CONFERENCE_DELETE_OK + 1) # /usr/include/tox/tox.h: 2465

TOX_ERR_CONFERENCE_DELETE = enum_TOX_ERR_CONFERENCE_DELETE # /usr/include/tox/tox.h: 2465

# /usr/include/tox/tox.h: 2475
if hasattr(_libs['toxcore'], 'tox_conference_delete'):
    tox_conference_delete = _libs['toxcore'].tox_conference_delete
    tox_conference_delete.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_CONFERENCE_DELETE)]
    tox_conference_delete.restype = c_bool

enum_TOX_ERR_CONFERENCE_PEER_QUERY = c_int # /usr/include/tox/tox.h: 2502

TOX_ERR_CONFERENCE_PEER_QUERY_OK = 0 # /usr/include/tox/tox.h: 2502

TOX_ERR_CONFERENCE_PEER_QUERY_CONFERENCE_NOT_FOUND = (TOX_ERR_CONFERENCE_PEER_QUERY_OK + 1) # /usr/include/tox/tox.h: 2502

TOX_ERR_CONFERENCE_PEER_QUERY_PEER_NOT_FOUND = (TOX_ERR_CONFERENCE_PEER_QUERY_CONFERENCE_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2502

TOX_ERR_CONFERENCE_PEER_QUERY_NO_CONNECTION = (TOX_ERR_CONFERENCE_PEER_QUERY_PEER_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2502

TOX_ERR_CONFERENCE_PEER_QUERY = enum_TOX_ERR_CONFERENCE_PEER_QUERY # /usr/include/tox/tox.h: 2502

# /usr/include/tox/tox.h: 2508
if hasattr(_libs['toxcore'], 'tox_conference_peer_count'):
    tox_conference_peer_count = _libs['toxcore'].tox_conference_peer_count
    tox_conference_peer_count.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_CONFERENCE_PEER_QUERY)]
    tox_conference_peer_count.restype = c_uint32

# /usr/include/tox/tox.h: 2513
if hasattr(_libs['toxcore'], 'tox_conference_peer_get_name_size'):
    tox_conference_peer_get_name_size = _libs['toxcore'].tox_conference_peer_get_name_size
    tox_conference_peer_get_name_size.argtypes = [POINTER(Tox), c_uint32, c_uint32, POINTER(TOX_ERR_CONFERENCE_PEER_QUERY)]
    tox_conference_peer_get_name_size.restype = c_size_t

# /usr/include/tox/tox.h: 2522
if hasattr(_libs['toxcore'], 'tox_conference_peer_get_name'):
    tox_conference_peer_get_name = _libs['toxcore'].tox_conference_peer_get_name
    tox_conference_peer_get_name.argtypes = [POINTER(Tox), c_uint32, c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_CONFERENCE_PEER_QUERY)]
    tox_conference_peer_get_name.restype = c_bool

# /usr/include/tox/tox.h: 2531
if hasattr(_libs['toxcore'], 'tox_conference_peer_get_public_key'):
    tox_conference_peer_get_public_key = _libs['toxcore'].tox_conference_peer_get_public_key
    tox_conference_peer_get_public_key.argtypes = [POINTER(Tox), c_uint32, c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_CONFERENCE_PEER_QUERY)]
    tox_conference_peer_get_public_key.restype = c_bool

# /usr/include/tox/tox.h: 2537
if hasattr(_libs['toxcore'], 'tox_conference_peer_number_is_ours'):
    tox_conference_peer_number_is_ours = _libs['toxcore'].tox_conference_peer_number_is_ours
    tox_conference_peer_number_is_ours.argtypes = [POINTER(Tox), c_uint32, c_uint32, POINTER(TOX_ERR_CONFERENCE_PEER_QUERY)]
    tox_conference_peer_number_is_ours.restype = c_bool

enum_TOX_ERR_CONFERENCE_INVITE = c_int # /usr/include/tox/tox.h: 2557

TOX_ERR_CONFERENCE_INVITE_OK = 0 # /usr/include/tox/tox.h: 2557

TOX_ERR_CONFERENCE_INVITE_CONFERENCE_NOT_FOUND = (TOX_ERR_CONFERENCE_INVITE_OK + 1) # /usr/include/tox/tox.h: 2557

TOX_ERR_CONFERENCE_INVITE_FAIL_SEND = (TOX_ERR_CONFERENCE_INVITE_CONFERENCE_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2557

TOX_ERR_CONFERENCE_INVITE = enum_TOX_ERR_CONFERENCE_INVITE # /usr/include/tox/tox.h: 2557

# /usr/include/tox/tox.h: 2568
if hasattr(_libs['toxcore'], 'tox_conference_invite'):
    tox_conference_invite = _libs['toxcore'].tox_conference_invite
    tox_conference_invite.argtypes = [POINTER(Tox), c_uint32, c_uint32, POINTER(TOX_ERR_CONFERENCE_INVITE)]
    tox_conference_invite.restype = c_bool

enum_TOX_ERR_CONFERENCE_JOIN = c_int # /usr/include/tox/tox.h: 2608

TOX_ERR_CONFERENCE_JOIN_OK = 0 # /usr/include/tox/tox.h: 2608

TOX_ERR_CONFERENCE_JOIN_INVALID_LENGTH = (TOX_ERR_CONFERENCE_JOIN_OK + 1) # /usr/include/tox/tox.h: 2608

TOX_ERR_CONFERENCE_JOIN_WRONG_TYPE = (TOX_ERR_CONFERENCE_JOIN_INVALID_LENGTH + 1) # /usr/include/tox/tox.h: 2608

TOX_ERR_CONFERENCE_JOIN_FRIEND_NOT_FOUND = (TOX_ERR_CONFERENCE_JOIN_WRONG_TYPE + 1) # /usr/include/tox/tox.h: 2608

TOX_ERR_CONFERENCE_JOIN_DUPLICATE = (TOX_ERR_CONFERENCE_JOIN_FRIEND_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2608

TOX_ERR_CONFERENCE_JOIN_INIT_FAIL = (TOX_ERR_CONFERENCE_JOIN_DUPLICATE + 1) # /usr/include/tox/tox.h: 2608

TOX_ERR_CONFERENCE_JOIN_FAIL_SEND = (TOX_ERR_CONFERENCE_JOIN_INIT_FAIL + 1) # /usr/include/tox/tox.h: 2608

TOX_ERR_CONFERENCE_JOIN = enum_TOX_ERR_CONFERENCE_JOIN # /usr/include/tox/tox.h: 2608

# /usr/include/tox/tox.h: 2620
if hasattr(_libs['toxcore'], 'tox_conference_join'):
    tox_conference_join = _libs['toxcore'].tox_conference_join
    tox_conference_join.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_CONFERENCE_JOIN)]
    tox_conference_join.restype = c_uint32

enum_TOX_ERR_CONFERENCE_SEND_MESSAGE = c_int # /usr/include/tox/tox.h: 2650

TOX_ERR_CONFERENCE_SEND_MESSAGE_OK = 0 # /usr/include/tox/tox.h: 2650

TOX_ERR_CONFERENCE_SEND_MESSAGE_CONFERENCE_NOT_FOUND = (TOX_ERR_CONFERENCE_SEND_MESSAGE_OK + 1) # /usr/include/tox/tox.h: 2650

TOX_ERR_CONFERENCE_SEND_MESSAGE_TOO_LONG = (TOX_ERR_CONFERENCE_SEND_MESSAGE_CONFERENCE_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2650

TOX_ERR_CONFERENCE_SEND_MESSAGE_NO_CONNECTION = (TOX_ERR_CONFERENCE_SEND_MESSAGE_TOO_LONG + 1) # /usr/include/tox/tox.h: 2650

TOX_ERR_CONFERENCE_SEND_MESSAGE_FAIL_SEND = (TOX_ERR_CONFERENCE_SEND_MESSAGE_NO_CONNECTION + 1) # /usr/include/tox/tox.h: 2650

TOX_ERR_CONFERENCE_SEND_MESSAGE = enum_TOX_ERR_CONFERENCE_SEND_MESSAGE # /usr/include/tox/tox.h: 2650

# /usr/include/tox/tox.h: 2671
if hasattr(_libs['toxcore'], 'tox_conference_send_message'):
    tox_conference_send_message = _libs['toxcore'].tox_conference_send_message
    tox_conference_send_message.argtypes = [POINTER(Tox), c_uint32, TOX_MESSAGE_TYPE, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_CONFERENCE_SEND_MESSAGE)]
    tox_conference_send_message.restype = c_bool

enum_TOX_ERR_CONFERENCE_TITLE = c_int # /usr/include/tox/tox.h: 2696

TOX_ERR_CONFERENCE_TITLE_OK = 0 # /usr/include/tox/tox.h: 2696

TOX_ERR_CONFERENCE_TITLE_CONFERENCE_NOT_FOUND = (TOX_ERR_CONFERENCE_TITLE_OK + 1) # /usr/include/tox/tox.h: 2696

TOX_ERR_CONFERENCE_TITLE_INVALID_LENGTH = (TOX_ERR_CONFERENCE_TITLE_CONFERENCE_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2696

TOX_ERR_CONFERENCE_TITLE_FAIL_SEND = (TOX_ERR_CONFERENCE_TITLE_INVALID_LENGTH + 1) # /usr/include/tox/tox.h: 2696

TOX_ERR_CONFERENCE_TITLE = enum_TOX_ERR_CONFERENCE_TITLE # /usr/include/tox/tox.h: 2696

# /usr/include/tox/tox.h: 2705
if hasattr(_libs['toxcore'], 'tox_conference_get_title_size'):
    tox_conference_get_title_size = _libs['toxcore'].tox_conference_get_title_size
    tox_conference_get_title_size.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_CONFERENCE_TITLE)]
    tox_conference_get_title_size.restype = c_size_t

# /usr/include/tox/tox.h: 2720
if hasattr(_libs['toxcore'], 'tox_conference_get_title'):
    tox_conference_get_title = _libs['toxcore'].tox_conference_get_title
    tox_conference_get_title.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), POINTER(TOX_ERR_CONFERENCE_TITLE)]
    tox_conference_get_title.restype = c_bool

# /usr/include/tox/tox.h: 2730
if hasattr(_libs['toxcore'], 'tox_conference_set_title'):
    tox_conference_set_title = _libs['toxcore'].tox_conference_set_title
    tox_conference_set_title.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_CONFERENCE_TITLE)]
    tox_conference_set_title.restype = c_bool

# /usr/include/tox/tox.h: 2737
if hasattr(_libs['toxcore'], 'tox_conference_get_chatlist_size'):
    tox_conference_get_chatlist_size = _libs['toxcore'].tox_conference_get_chatlist_size
    tox_conference_get_chatlist_size.argtypes = [POINTER(Tox)]
    tox_conference_get_chatlist_size.restype = c_size_t

# /usr/include/tox/tox.h: 2743
if hasattr(_libs['toxcore'], 'tox_conference_get_chatlist'):
    tox_conference_get_chatlist = _libs['toxcore'].tox_conference_get_chatlist
    tox_conference_get_chatlist.argtypes = [POINTER(Tox), POINTER(c_uint32)]
    tox_conference_get_chatlist.restype = None

enum_TOX_ERR_CONFERENCE_GET_TYPE = c_int # /usr/include/tox/tox.h: 2761

TOX_ERR_CONFERENCE_GET_TYPE_OK = 0 # /usr/include/tox/tox.h: 2761

TOX_ERR_CONFERENCE_GET_TYPE_CONFERENCE_NOT_FOUND = (TOX_ERR_CONFERENCE_GET_TYPE_OK + 1) # /usr/include/tox/tox.h: 2761

TOX_ERR_CONFERENCE_GET_TYPE = enum_TOX_ERR_CONFERENCE_GET_TYPE # /usr/include/tox/tox.h: 2761

# /usr/include/tox/tox.h: 2764
if hasattr(_libs['toxcore'], 'tox_conference_get_type'):
    tox_conference_get_type = _libs['toxcore'].tox_conference_get_type
    tox_conference_get_type.argtypes = [POINTER(Tox), c_uint32, POINTER(TOX_ERR_CONFERENCE_GET_TYPE)]
    tox_conference_get_type.restype = TOX_CONFERENCE_TYPE

enum_TOX_ERR_FRIEND_CUSTOM_PACKET = c_int # /usr/include/tox/tox.h: 2819

TOX_ERR_FRIEND_CUSTOM_PACKET_OK = 0 # /usr/include/tox/tox.h: 2819

TOX_ERR_FRIEND_CUSTOM_PACKET_NULL = (TOX_ERR_FRIEND_CUSTOM_PACKET_OK + 1) # /usr/include/tox/tox.h: 2819

TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_FOUND = (TOX_ERR_FRIEND_CUSTOM_PACKET_NULL + 1) # /usr/include/tox/tox.h: 2819

TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_CONNECTED = (TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_FOUND + 1) # /usr/include/tox/tox.h: 2819

TOX_ERR_FRIEND_CUSTOM_PACKET_INVALID = (TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_CONNECTED + 1) # /usr/include/tox/tox.h: 2819

TOX_ERR_FRIEND_CUSTOM_PACKET_EMPTY = (TOX_ERR_FRIEND_CUSTOM_PACKET_INVALID + 1) # /usr/include/tox/tox.h: 2819

TOX_ERR_FRIEND_CUSTOM_PACKET_TOO_LONG = (TOX_ERR_FRIEND_CUSTOM_PACKET_EMPTY + 1) # /usr/include/tox/tox.h: 2819

TOX_ERR_FRIEND_CUSTOM_PACKET_SENDQ = (TOX_ERR_FRIEND_CUSTOM_PACKET_TOO_LONG + 1) # /usr/include/tox/tox.h: 2819

TOX_ERR_FRIEND_CUSTOM_PACKET = enum_TOX_ERR_FRIEND_CUSTOM_PACKET # /usr/include/tox/tox.h: 2819

# /usr/include/tox/tox.h: 2842
if hasattr(_libs['toxcore'], 'tox_friend_send_lossy_packet'):
    tox_friend_send_lossy_packet = _libs['toxcore'].tox_friend_send_lossy_packet
    tox_friend_send_lossy_packet.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_CUSTOM_PACKET)]
    tox_friend_send_lossy_packet.restype = c_bool

# /usr/include/tox/tox.h: 2861
if hasattr(_libs['toxcore'], 'tox_friend_send_lossless_packet'):
    tox_friend_send_lossless_packet = _libs['toxcore'].tox_friend_send_lossless_packet
    tox_friend_send_lossless_packet.argtypes = [POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(TOX_ERR_FRIEND_CUSTOM_PACKET)]
    tox_friend_send_lossless_packet.restype = c_bool

tox_friend_lossy_packet_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 2869

# /usr/include/tox/tox.h: 2877
if hasattr(_libs['toxcore'], 'tox_callback_friend_lossy_packet'):
    tox_callback_friend_lossy_packet = _libs['toxcore'].tox_callback_friend_lossy_packet
    tox_callback_friend_lossy_packet.argtypes = [POINTER(Tox), POINTER(tox_friend_lossy_packet_cb)]
    tox_callback_friend_lossy_packet.restype = None

tox_friend_lossless_packet_cb = CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_uint32, POINTER(c_uint8), c_size_t, POINTER(None)) # /usr/include/tox/tox.h: 2884

# /usr/include/tox/tox.h: 2892
if hasattr(_libs['toxcore'], 'tox_callback_friend_lossless_packet'):
    tox_callback_friend_lossless_packet = _libs['toxcore'].tox_callback_friend_lossless_packet
    tox_callback_friend_lossless_packet.argtypes = [POINTER(Tox), POINTER(tox_friend_lossless_packet_cb)]
    tox_callback_friend_lossless_packet.restype = None

# /usr/include/tox/tox.h: 2915
if hasattr(_libs['toxcore'], 'tox_self_get_dht_id'):
    tox_self_get_dht_id = _libs['toxcore'].tox_self_get_dht_id
    tox_self_get_dht_id.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_self_get_dht_id.restype = None

enum_TOX_ERR_GET_PORT = c_int # /usr/include/tox/tox.h: 2929

TOX_ERR_GET_PORT_OK = 0 # /usr/include/tox/tox.h: 2929

TOX_ERR_GET_PORT_NOT_BOUND = (TOX_ERR_GET_PORT_OK + 1) # /usr/include/tox/tox.h: 2929

TOX_ERR_GET_PORT = enum_TOX_ERR_GET_PORT # /usr/include/tox/tox.h: 2929

# /usr/include/tox/tox.h: 2935
if hasattr(_libs['toxcore'], 'tox_self_get_udp_port'):
    tox_self_get_udp_port = _libs['toxcore'].tox_self_get_udp_port
    tox_self_get_udp_port.argtypes = [POINTER(Tox), POINTER(TOX_ERR_GET_PORT)]
    tox_self_get_udp_port.restype = c_uint16

# /usr/include/tox/tox.h: 2941
if hasattr(_libs['toxcore'], 'tox_self_get_tcp_port'):
    tox_self_get_tcp_port = _libs['toxcore'].tox_self_get_tcp_port
    tox_self_get_tcp_port.argtypes = [POINTER(Tox), POINTER(TOX_ERR_GET_PORT)]
    tox_self_get_tcp_port.restype = c_uint16

# /usr/include/tox/toxdns.h: 56
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_dns3_new'):
        continue
    tox_dns3_new = _lib.tox_dns3_new
    tox_dns3_new.argtypes = [POINTER(c_uint8)]
    tox_dns3_new.restype = POINTER(None)
    break

# /usr/include/tox/toxdns.h: 60
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_dns3_kill'):
        continue
    tox_dns3_kill = _lib.tox_dns3_kill
    tox_dns3_kill.argtypes = [POINTER(None)]
    tox_dns3_kill.restype = None
    break

# /usr/include/tox/toxdns.h: 74
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_generate_dns3_string'):
        continue
    tox_generate_dns3_string = _lib.tox_generate_dns3_string
    tox_generate_dns3_string.argtypes = [POINTER(None), POINTER(c_uint8), c_uint16, POINTER(c_uint32), POINTER(c_uint8), c_uint8]
    tox_generate_dns3_string.restype = c_int
    break

# /usr/include/tox/toxdns.h: 89
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_decrypt_dns3_TXT'):
        continue
    tox_decrypt_dns3_TXT = _lib.tox_decrypt_dns3_TXT
    tox_decrypt_dns3_TXT.argtypes = [POINTER(None), POINTER(c_uint8), POINTER(c_uint8), c_uint32, c_uint32]
    tox_decrypt_dns3_TXT.restype = c_int
    break

# /usr/include/tox/toxav.h: 88
class struct_ToxAV(Structure):
    pass

ToxAV = struct_ToxAV # /usr/include/tox/toxav.h: 88

enum_TOXAV_ERR_NEW = c_int # /usr/include/tox/toxav.h: 123

TOXAV_ERR_NEW_OK = 0 # /usr/include/tox/toxav.h: 123

TOXAV_ERR_NEW_NULL = (TOXAV_ERR_NEW_OK + 1) # /usr/include/tox/toxav.h: 123

TOXAV_ERR_NEW_MALLOC = (TOXAV_ERR_NEW_NULL + 1) # /usr/include/tox/toxav.h: 123

TOXAV_ERR_NEW_MULTIPLE = (TOXAV_ERR_NEW_MALLOC + 1) # /usr/include/tox/toxav.h: 123

TOXAV_ERR_NEW = enum_TOXAV_ERR_NEW # /usr/include/tox/toxav.h: 123

# /usr/include/tox/toxav.h: 129
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_new'):
        continue
    toxav_new = _lib.toxav_new
    toxav_new.argtypes = [POINTER(Tox), POINTER(TOXAV_ERR_NEW)]
    toxav_new.restype = POINTER(ToxAV)
    break

# /usr/include/tox/toxav.h: 138
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_kill'):
        continue
    toxav_kill = _lib.toxav_kill
    toxav_kill.argtypes = [POINTER(ToxAV)]
    toxav_kill.restype = None
    break

# /usr/include/tox/toxav.h: 143
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_get_tox'):
        continue
    toxav_get_tox = _lib.toxav_get_tox
    toxav_get_tox.argtypes = [POINTER(ToxAV)]
    toxav_get_tox.restype = POINTER(Tox)
    break

# /usr/include/tox/toxav.h: 158
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_iteration_interval'):
        continue
    toxav_iteration_interval = _lib.toxav_iteration_interval
    toxav_iteration_interval.argtypes = [POINTER(ToxAV)]
    toxav_iteration_interval.restype = c_uint32
    break

# /usr/include/tox/toxav.h: 165
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_iterate'):
        continue
    toxav_iterate = _lib.toxav_iterate
    toxav_iterate.argtypes = [POINTER(ToxAV)]
    toxav_iterate.restype = None
    break

enum_TOXAV_ERR_CALL = c_int # /usr/include/tox/toxav.h: 215

TOXAV_ERR_CALL_OK = 0 # /usr/include/tox/toxav.h: 215

TOXAV_ERR_CALL_MALLOC = (TOXAV_ERR_CALL_OK + 1) # /usr/include/tox/toxav.h: 215

TOXAV_ERR_CALL_SYNC = (TOXAV_ERR_CALL_MALLOC + 1) # /usr/include/tox/toxav.h: 215

TOXAV_ERR_CALL_FRIEND_NOT_FOUND = (TOXAV_ERR_CALL_SYNC + 1) # /usr/include/tox/toxav.h: 215

TOXAV_ERR_CALL_FRIEND_NOT_CONNECTED = (TOXAV_ERR_CALL_FRIEND_NOT_FOUND + 1) # /usr/include/tox/toxav.h: 215

TOXAV_ERR_CALL_FRIEND_ALREADY_IN_CALL = (TOXAV_ERR_CALL_FRIEND_NOT_CONNECTED + 1) # /usr/include/tox/toxav.h: 215

TOXAV_ERR_CALL_INVALID_BIT_RATE = (TOXAV_ERR_CALL_FRIEND_ALREADY_IN_CALL + 1) # /usr/include/tox/toxav.h: 215

TOXAV_ERR_CALL = enum_TOXAV_ERR_CALL # /usr/include/tox/toxav.h: 215

# /usr/include/tox/toxav.h: 232
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_call'):
        continue
    toxav_call = _lib.toxav_call
    toxav_call.argtypes = [POINTER(ToxAV), c_uint32, c_uint32, c_uint32, POINTER(TOXAV_ERR_CALL)]
    toxav_call.restype = c_bool
    break

toxav_call_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, c_bool, c_bool, POINTER(None)) # /usr/include/tox/toxav.h: 242

# /usr/include/tox/toxav.h: 249
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_callback_call'):
        continue
    toxav_callback_call = _lib.toxav_callback_call
    toxav_callback_call.argtypes = [POINTER(ToxAV), POINTER(toxav_call_cb), POINTER(None)]
    toxav_callback_call.restype = None
    break

enum_TOXAV_ERR_ANSWER = c_int # /usr/include/tox/toxav.h: 286

TOXAV_ERR_ANSWER_OK = 0 # /usr/include/tox/toxav.h: 286

TOXAV_ERR_ANSWER_SYNC = (TOXAV_ERR_ANSWER_OK + 1) # /usr/include/tox/toxav.h: 286

TOXAV_ERR_ANSWER_CODEC_INITIALIZATION = (TOXAV_ERR_ANSWER_SYNC + 1) # /usr/include/tox/toxav.h: 286

TOXAV_ERR_ANSWER_FRIEND_NOT_FOUND = (TOXAV_ERR_ANSWER_CODEC_INITIALIZATION + 1) # /usr/include/tox/toxav.h: 286

TOXAV_ERR_ANSWER_FRIEND_NOT_CALLING = (TOXAV_ERR_ANSWER_FRIEND_NOT_FOUND + 1) # /usr/include/tox/toxav.h: 286

TOXAV_ERR_ANSWER_INVALID_BIT_RATE = (TOXAV_ERR_ANSWER_FRIEND_NOT_CALLING + 1) # /usr/include/tox/toxav.h: 286

TOXAV_ERR_ANSWER = enum_TOXAV_ERR_ANSWER # /usr/include/tox/toxav.h: 286

# /usr/include/tox/toxav.h: 302
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_answer'):
        continue
    toxav_answer = _lib.toxav_answer
    toxav_answer.argtypes = [POINTER(ToxAV), c_uint32, c_uint32, c_uint32, POINTER(TOXAV_ERR_ANSWER)]
    toxav_answer.restype = c_bool
    break

enum_TOXAV_FRIEND_CALL_STATE = c_int # /usr/include/tox/toxav.h: 314

TOXAV_FRIEND_CALL_STATE_NONE = 0 # /usr/include/tox/toxav.h: 314

TOXAV_FRIEND_CALL_STATE_ERROR = 1 # /usr/include/tox/toxav.h: 314

TOXAV_FRIEND_CALL_STATE_FINISHED = 2 # /usr/include/tox/toxav.h: 314

TOXAV_FRIEND_CALL_STATE_SENDING_A = 4 # /usr/include/tox/toxav.h: 314

TOXAV_FRIEND_CALL_STATE_SENDING_V = 8 # /usr/include/tox/toxav.h: 314

TOXAV_FRIEND_CALL_STATE_ACCEPTING_A = 16 # /usr/include/tox/toxav.h: 314

TOXAV_FRIEND_CALL_STATE_ACCEPTING_V = 32 # /usr/include/tox/toxav.h: 314

toxav_call_state_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, c_uint32, POINTER(None)) # /usr/include/tox/toxav.h: 368

# /usr/include/tox/toxav.h: 375
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_callback_call_state'):
        continue
    toxav_callback_call_state = _lib.toxav_callback_call_state
    toxav_callback_call_state.argtypes = [POINTER(ToxAV), POINTER(toxav_call_state_cb), POINTER(None)]
    toxav_callback_call_state.restype = None
    break

enum_TOXAV_CALL_CONTROL = c_int # /usr/include/tox/toxav.h: 429

TOXAV_CALL_CONTROL_RESUME = 0 # /usr/include/tox/toxav.h: 429

TOXAV_CALL_CONTROL_PAUSE = (TOXAV_CALL_CONTROL_RESUME + 1) # /usr/include/tox/toxav.h: 429

TOXAV_CALL_CONTROL_CANCEL = (TOXAV_CALL_CONTROL_PAUSE + 1) # /usr/include/tox/toxav.h: 429

TOXAV_CALL_CONTROL_MUTE_AUDIO = (TOXAV_CALL_CONTROL_CANCEL + 1) # /usr/include/tox/toxav.h: 429

TOXAV_CALL_CONTROL_UNMUTE_AUDIO = (TOXAV_CALL_CONTROL_MUTE_AUDIO + 1) # /usr/include/tox/toxav.h: 429

TOXAV_CALL_CONTROL_HIDE_VIDEO = (TOXAV_CALL_CONTROL_UNMUTE_AUDIO + 1) # /usr/include/tox/toxav.h: 429

TOXAV_CALL_CONTROL_SHOW_VIDEO = (TOXAV_CALL_CONTROL_HIDE_VIDEO + 1) # /usr/include/tox/toxav.h: 429

TOXAV_CALL_CONTROL = enum_TOXAV_CALL_CONTROL # /usr/include/tox/toxav.h: 429

enum_TOXAV_ERR_CALL_CONTROL = c_int # /usr/include/tox/toxav.h: 461

TOXAV_ERR_CALL_CONTROL_OK = 0 # /usr/include/tox/toxav.h: 461

TOXAV_ERR_CALL_CONTROL_SYNC = (TOXAV_ERR_CALL_CONTROL_OK + 1) # /usr/include/tox/toxav.h: 461

TOXAV_ERR_CALL_CONTROL_FRIEND_NOT_FOUND = (TOXAV_ERR_CALL_CONTROL_SYNC + 1) # /usr/include/tox/toxav.h: 461

TOXAV_ERR_CALL_CONTROL_FRIEND_NOT_IN_CALL = (TOXAV_ERR_CALL_CONTROL_FRIEND_NOT_FOUND + 1) # /usr/include/tox/toxav.h: 461

TOXAV_ERR_CALL_CONTROL_INVALID_TRANSITION = (TOXAV_ERR_CALL_CONTROL_FRIEND_NOT_IN_CALL + 1) # /usr/include/tox/toxav.h: 461

TOXAV_ERR_CALL_CONTROL = enum_TOXAV_ERR_CALL_CONTROL # /usr/include/tox/toxav.h: 461

# /usr/include/tox/toxav.h: 473
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_call_control'):
        continue
    toxav_call_control = _lib.toxav_call_control
    toxav_call_control.argtypes = [POINTER(ToxAV), c_uint32, TOXAV_CALL_CONTROL, POINTER(TOXAV_ERR_CALL_CONTROL)]
    toxav_call_control.restype = c_bool
    break

enum_TOXAV_ERR_BIT_RATE_SET = c_int # /usr/include/tox/toxav.h: 516

TOXAV_ERR_BIT_RATE_SET_OK = 0 # /usr/include/tox/toxav.h: 516

TOXAV_ERR_BIT_RATE_SET_SYNC = (TOXAV_ERR_BIT_RATE_SET_OK + 1) # /usr/include/tox/toxav.h: 516

TOXAV_ERR_BIT_RATE_SET_INVALID_AUDIO_BIT_RATE = (TOXAV_ERR_BIT_RATE_SET_SYNC + 1) # /usr/include/tox/toxav.h: 516

TOXAV_ERR_BIT_RATE_SET_INVALID_VIDEO_BIT_RATE = (TOXAV_ERR_BIT_RATE_SET_INVALID_AUDIO_BIT_RATE + 1) # /usr/include/tox/toxav.h: 516

TOXAV_ERR_BIT_RATE_SET_FRIEND_NOT_FOUND = (TOXAV_ERR_BIT_RATE_SET_INVALID_VIDEO_BIT_RATE + 1) # /usr/include/tox/toxav.h: 516

TOXAV_ERR_BIT_RATE_SET_FRIEND_NOT_IN_CALL = (TOXAV_ERR_BIT_RATE_SET_FRIEND_NOT_FOUND + 1) # /usr/include/tox/toxav.h: 516

TOXAV_ERR_BIT_RATE_SET = enum_TOXAV_ERR_BIT_RATE_SET # /usr/include/tox/toxav.h: 516

# /usr/include/tox/toxav.h: 530
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_bit_rate_set'):
        continue
    toxav_bit_rate_set = _lib.toxav_bit_rate_set
    toxav_bit_rate_set.argtypes = [POINTER(ToxAV), c_uint32, c_int32, c_int32, POINTER(TOXAV_ERR_BIT_RATE_SET)]
    toxav_bit_rate_set.restype = c_bool
    break

toxav_bit_rate_status_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, c_uint32, c_uint32, POINTER(None)) # /usr/include/tox/toxav.h: 543

# /usr/include/tox/toxav.h: 551
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_callback_bit_rate_status'):
        continue
    toxav_callback_bit_rate_status = _lib.toxav_callback_bit_rate_status
    toxav_callback_bit_rate_status.argtypes = [POINTER(ToxAV), POINTER(toxav_bit_rate_status_cb), POINTER(None)]
    toxav_callback_bit_rate_status.restype = None
    break

enum_TOXAV_ERR_SEND_FRAME = c_int # /usr/include/tox/toxav.h: 607

TOXAV_ERR_SEND_FRAME_OK = 0 # /usr/include/tox/toxav.h: 607

TOXAV_ERR_SEND_FRAME_NULL = (TOXAV_ERR_SEND_FRAME_OK + 1) # /usr/include/tox/toxav.h: 607

TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND = (TOXAV_ERR_SEND_FRAME_NULL + 1) # /usr/include/tox/toxav.h: 607

TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL = (TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND + 1) # /usr/include/tox/toxav.h: 607

TOXAV_ERR_SEND_FRAME_SYNC = (TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL + 1) # /usr/include/tox/toxav.h: 607

TOXAV_ERR_SEND_FRAME_INVALID = (TOXAV_ERR_SEND_FRAME_SYNC + 1) # /usr/include/tox/toxav.h: 607

TOXAV_ERR_SEND_FRAME_PAYLOAD_TYPE_DISABLED = (TOXAV_ERR_SEND_FRAME_INVALID + 1) # /usr/include/tox/toxav.h: 607

TOXAV_ERR_SEND_FRAME_RTP_FAILED = (TOXAV_ERR_SEND_FRAME_PAYLOAD_TYPE_DISABLED + 1) # /usr/include/tox/toxav.h: 607

TOXAV_ERR_SEND_FRAME = enum_TOXAV_ERR_SEND_FRAME # /usr/include/tox/toxav.h: 607

# /usr/include/tox/toxav.h: 630
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_audio_send_frame'):
        continue
    toxav_audio_send_frame = _lib.toxav_audio_send_frame
    toxav_audio_send_frame.argtypes = [POINTER(ToxAV), c_uint32, POINTER(c_int16), c_size_t, c_uint8, c_uint32, POINTER(TOXAV_ERR_SEND_FRAME)]
    toxav_audio_send_frame.restype = c_bool
    break

# /usr/include/tox/toxav.h: 648
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_video_send_frame'):
        continue
    toxav_video_send_frame = _lib.toxav_video_send_frame
    toxav_video_send_frame.argtypes = [POINTER(ToxAV), c_uint32, c_uint16, c_uint16, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(TOXAV_ERR_SEND_FRAME)]
    toxav_video_send_frame.restype = c_bool
    break

toxav_audio_receive_frame_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, POINTER(c_int16), c_size_t, c_uint8, c_uint32, POINTER(None)) # /usr/include/tox/toxav.h: 672

# /usr/include/tox/toxav.h: 680
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_callback_audio_receive_frame'):
        continue
    toxav_callback_audio_receive_frame = _lib.toxav_callback_audio_receive_frame
    toxav_callback_audio_receive_frame.argtypes = [POINTER(ToxAV), POINTER(toxav_audio_receive_frame_cb), POINTER(None)]
    toxav_callback_audio_receive_frame.restype = None
    break

toxav_video_receive_frame_cb = CFUNCTYPE(UNCHECKED(None), POINTER(ToxAV), c_uint32, c_uint16, c_uint16, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), c_int32, c_int32, c_int32, POINTER(None)) # /usr/include/tox/toxav.h: 704

# /usr/include/tox/toxav.h: 713
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_callback_video_receive_frame'):
        continue
    toxav_callback_video_receive_frame = _lib.toxav_callback_video_receive_frame
    toxav_callback_video_receive_frame.argtypes = [POINTER(ToxAV), POINTER(toxav_video_receive_frame_cb), POINTER(None)]
    toxav_callback_video_receive_frame.restype = None
    break

# /usr/include/tox/toxav.h: 728
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_add_av_groupchat'):
        continue
    toxav_add_av_groupchat = _lib.toxav_add_av_groupchat
    toxav_add_av_groupchat.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, c_int, POINTER(c_int16), c_uint, c_uint8, c_uint, POINTER(None)), POINTER(None)]
    toxav_add_av_groupchat.restype = c_int
    break

# /usr/include/tox/toxav.h: 741
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_join_av_groupchat'):
        continue
    toxav_join_av_groupchat = _lib.toxav_join_av_groupchat
    toxav_join_av_groupchat.argtypes = [POINTER(Tox), c_int32, POINTER(c_uint8), c_uint16, CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, c_int, POINTER(c_int16), c_uint, c_uint8, c_uint, POINTER(None)), POINTER(None)]
    toxav_join_av_groupchat.restype = c_int
    break

# /usr/include/tox/toxav.h: 757
for _lib in _libs.values():
    if not hasattr(_lib, 'toxav_group_send_audio'):
        continue
    toxav_group_send_audio = _lib.toxav_group_send_audio
    toxav_group_send_audio.argtypes = [POINTER(Tox), c_int, POINTER(c_int16), c_uint, c_uint8, c_uint]
    toxav_group_send_audio.restype = c_int
    break

# /usr/include/tox/tox.h: 166
TOX_VERSION_MAJOR = 0

# /usr/include/tox/tox.h: 175
TOX_VERSION_MINOR = 1

# /usr/include/tox/tox.h: 183
TOX_VERSION_PATCH = 9

# /usr/include/tox/tox.h: 193
def TOX_VERSION_IS_API_COMPATIBLE(MAJOR, MINOR, PATCH):
    return ((((TOX_VERSION_MAJOR > 0) and (TOX_VERSION_MAJOR == MAJOR)) and ((TOX_VERSION_MINOR > MINOR) or ((TOX_VERSION_MINOR == MINOR) and (TOX_VERSION_PATCH >= PATCH)))) or (((TOX_VERSION_MAJOR == 0) and (MAJOR == 0)) and ((((TOX_VERSION_MINOR > 0) and (TOX_VERSION_MINOR == MINOR)) and (TOX_VERSION_PATCH >= PATCH)) or (((TOX_VERSION_MINOR == 0) and (MINOR == 0)) and (TOX_VERSION_PATCH == PATCH)))))

# /usr/include/tox/tox.h: 218
TOX_VERSION_IS_ABI_COMPATIBLE = (tox_version_is_compatible (TOX_VERSION_MAJOR, TOX_VERSION_MINOR, TOX_VERSION_PATCH))

# /usr/include/tox/tox.h: 237
TOX_PUBLIC_KEY_SIZE = 32

# /usr/include/tox/tox.h: 244
TOX_SECRET_KEY_SIZE = 32

# /usr/include/tox/tox.h: 251
TOX_NOSPAM_SIZE = sizeof(c_uint32)

# /usr/include/tox/tox.h: 263
TOX_ADDRESS_SIZE = ((TOX_PUBLIC_KEY_SIZE + TOX_NOSPAM_SIZE) + sizeof(c_uint16))

# /usr/include/tox/tox.h: 270
TOX_MAX_NAME_LENGTH = 128

# /usr/include/tox/tox.h: 277
TOX_MAX_STATUS_MESSAGE_LENGTH = 1007

# /usr/include/tox/tox.h: 284
TOX_MAX_FRIEND_REQUEST_LENGTH = 1016

# /usr/include/tox/tox.h: 291
TOX_MAX_MESSAGE_LENGTH = 1372

# /usr/include/tox/tox.h: 298
TOX_MAX_CUSTOM_PACKET_SIZE = 1373

# /usr/include/tox/tox.h: 305
TOX_HASH_LENGTH = 32

# /usr/include/tox/tox.h: 312
TOX_FILE_ID_LENGTH = 32

# /usr/include/tox/tox.h: 319
TOX_MAX_FILENAME_LENGTH = 255

# /usr/include/tox/toxdns.h: 34
TOXDNS_MAX_RECOMMENDED_NAME_LENGTH = 32

Tox = struct_Tox # /usr/include/tox/tox.h: 146

Tox_Options = struct_Tox_Options # /usr/include/tox/tox.h: 499

ToxAV = struct_ToxAV # /usr/include/tox/toxav.h: 88

# No inserted files

