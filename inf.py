# coding=utf-8
from __future__ import unicode_literals
import sys
import json
import logging
import re
import os
import sys

from protocols.tl1 import *
from protocols.base import *
from protocols.exceptions import *


class INFTL1LanguageInput(TL1LanguageInput):

    """
    start is re-implemented here, because of vendor-specific behavior
    """
    def start(self):
        """Make sure the actual I/O for the file or device is ready. logs in, authorize.
        You shouldn't call it more than once"""
        logger = logging.getLogger("protocols")
        logger.debug("Fetching information from %s using %s" % (self.getTarget(), type(self).__name__))
        if not self.autocallbacks:
            self.autocallbacks = {}

        # "hack" the driver terminator. it gets hung up on expecting a CRLF at the end of the input stream right
        # after connect, which infinera doesn't provide. he'll be back
        old_arnold = self.terminator
        self.terminator = b">>"

        self.connect()

        # flush out the banner that gets sent on connect.
        self.banner = self.flush_buffer()

        # he's back
        self.terminator = old_arnold

        self.login()
        self.authorize()

        # do the same for the login messages
        self.login_messages = self.flush_buffer()


    def flush_buffer(self, flush_timeout=1):
        logger = logging.getLogger("protocols")
        old_level = logger.getEffectiveLevel()
        #mute the logger; this call will probably have adverse consequences in a multithreading space
        logger.setLevel(logging.CRITICAL + 10)
        output = ""
        while True:
            try:
                output += self.readmessage(flush_timeout)
            except TimeOut:
                break

        #unmute the logger
        logger.setLevel(old_level)
        return output

    def rtrv_alm_all(self, tid='', timeout=90, debug_run=False):
        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_ALM", encoding="utf-8") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
            response = response.split('\n')
        else:
            response = self.command('rtrv-alm-all:{}::;'.format(tid, timeout=timeout))
            l.debug("Sending command %s to device" % response)

        node_dict = dict()

        for lines in response:
            if debug_run:
                result = lines.rstrip(',')
                result = result.split(':')
                l.debug("Debug results: %s" % result)
                node_dict[result[0]] = {result[1]: {y.split('=')[0]: y.split('=')[1] for y in result[2].split(',')}}
            else:
                result = lines.rstrip(',')
                result = result.split(':')
                l.debug("Split results: %s" % result)
                node_dict[result[0]] = {result[1]: {y.split('=')[0]: y.split('=')[1] for y in result[2].split(',')}}

        return node_dict



    def rtrv_sys(self, tid='', timeout=90, debug_run=False):
        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_SYS", encoding="utf-8") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
            response = response.split('\n')
        else:
            response = self.command('rtrv-sys:{}::;'.format(tid, timeout=timeout))
            l.debug("Sending command %s to device" % response)

        node_dict = dict()

        for lines in response:
            if debug_run:
                result = lines.rstrip(',')
                result = result.split(':')
                l.debug("Debug results: %s" % result)
                node_dict[result[0]] = {result[1]: {y.split('=')[0]: y.split('=')[1] for y in result[2].split(',')}}
            else:
                result = lines.rstrip(',')
                result = result.split(':')
                l.debug("Split results: %s" % result)
                node_dict[result[0]] = {result[1]: {y.split('=')[0]: y.split('=')[1] for y in result[2].split(',')}}

        return node_dict


class INFSyncTL1Input(TL1IOInput, INFTL1LanguageInput, BaseSyncInput):
    pass


class INFASyncTL1Input(TL1IOInput, INFTL1LanguageInput, BaseAsyncInput):
    pass


def test_setup():
    pass


def main():
    test_setup()


if __name__ == '__main__':
    main()
