# this file is part of toxicpie - a ctypes python wrapper for Project Tox
# Copyright (C) 2014  tox.im project
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import binascii
import threading
from ctypes import create_string_buffer, c_char,c_uint8, addressof


class ToxError(Exception):
    def __init__(self, message, err=None):
        self.err = err
        Exception.__init__(self, message)


class ScopedRLock(object):
    def __init__(self):
        self._lockable = threading.RLock()

    def __enter__(self):
        self._lockable.acquire()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lockable.release()


def buffer_to_hex(buffer, size=None):
    if size is not None:
        buffer = ptr_to_buffer(buffer, size)
    else:
        buffer = buffer.raw
    return binascii.hexlify(buffer).decode('ascii').upper()


def hex_to_buffer(string):
    binary = binascii.unhexlify(string)
    return create_string_buffer(binary, len(binary))


def ptr_to_string(p, length):
    #return ptr_to_buffer(p, length).decode('utf-8')
    return ptr_to_buffer(p, length)


def ptr_to_buffer(p, length):
    return (c_char * length).from_address(addressof(p.contents)).raw





def ptr_to_uint8(p,length):
	return (c_uint8 * length).from_address(addressof(p)).raw






