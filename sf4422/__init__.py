#! /usr/bin/python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Author:   Fabien Marteau <fabien.marteau@armadeus.com>
# Created:  03/01/2022
#-----------------------------------------------------------------------------
#  Copyright (2022)  Armadeus Systems
#-----------------------------------------------------------------------------
""" __init__
"""

import serial
from typing import List

class Sefram4422Error(Exception):
    pass

class Sefram4422(object):
    baudrate = 19200
    timeout = 1
    ser = None
    identity = {"constructor":"Sefram",
                "model": "4422",
                "version": "V0.11"}

    def __init__(self, devname):
        self._devname = devname
        self._connect_RS232()

    def __del__(self):
        if self.ser is not None:
            self.ser.close()

    def _connect_RS232(self):
        self.ser = serial.Serial(self._devname,
                                self.baudrate,
                                timeout=self.timeout)
        idlist = self.identify()
        if self.identity["constructor"] != idlist[0]:
            raise Sefram4422Error(f"Wrong constructor ({idlist[0]}),"
                                f"should be {self.identity['constructor']}")
        if self.identity["model"] != idlist[1]:
            raise Sefram4422Error(f"Wrong product ({idlist[1]}),"
                                  f"should be {self.identity['model']}")

    def identify(self) -> List[str]:
        self.ser.write(b"*IDN?\n")
        retval = self.ser.readline()
        return retval.decode('utf-8').strip().split(",")

    def get_freq(self):
        self.ser.write("*FREQ?\n".encode("utf-8"))
        retval = float(self.ser.readline().decode("utf-8").strip())
        return retval
