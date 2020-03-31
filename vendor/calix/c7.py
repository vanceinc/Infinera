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


class C7TL1LanguageInput(TL1LanguageInput):

    def rtrv_sys(self, tid='', timeout=10):
        results = self.command("rtrv-sys:{}::;".format(tid), timeout=timeout)
        sys_info = {}
        """
                {
                  "VPPOOL": "4000\\u0026\\u00264090",
                  "ADMIN": "N23-1",
                  "RSVDVLANSTART": "1002",
                  "VCPOOL": "4094",
                  "TDMBWC": "N",
                  "VIDPROV": "AVT",
                  "PROVLOCK": "N",
                  "DEFONTPROF": "NONE"
                }
        """
        for line in results:
            trim = line.strip('::')
            parts = trim.split(",")
            for lines in parts:
                k, v = lines.split("=")
                sys_info[k] = v
        return sys_info

    def rtrv_node(self, tid='', nodeaid='ALL', timeout=90, debug_run=False):
        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_NODE", encoding="utf-8") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
            response = response.split('\n')
        else:
            response = self.command('rtrv-node:{}:{}:;'.format(tid, nodeaid, timeout=timeout))
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

    def rtrv_shelf(self, tid='', shelfaid='ALL', timeout=90):

        results = self.command('rtrv-shelf:{}:{}:;'.format(tid, shelfaid), timeout=timeout)
        result_dict = dict()
        for lines in results:
            result = lines.rstrip(',')
            result = result.split(':')
            result_dict[result[0]] = {result[1]: {y.split('=')[0]: y.split('=')[1] for y in result[2].split(',')}}

        return result_dict

    def rtrv_eqpt(self, tid='', eqptaid='ALL', eqtyp='', timeout=90, debug_run=False):
        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_EQPT.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
                for row in response:
                    lines = row.split("\r\n")
                    l.debug("Test data After RegEx: %s", lines)
        else:
            response = self.command('rtrv-eqpt:{}:{}:{};'.format(tid, eqptaid, eqtyp), timeout=timeout)
            l.debug("Sending command %s to device" % response)

            equip_dict = dict()
            for row in response:
                lines = row.split("\r\n")
                for line in lines:
                    if re.match(r'^\s*N\d+-\d+-(CS[AB]|MS|FT|\d+):.*?', line):
                        l.debug("Before RegEx: %s", line)
                        line = re.sub(r'(^\s+|\s+$)', '', line)
                        line = re.sub(r'["\\;]', '', line)

                        pairs = line.split(':')
                        eqpt_aid = pairs[0]
                        eqpt_types = {"PROVTYPE": pairs[1].split(',')[0], "EQUIPTYPE": pairs[1].split(',')[1]}

                        key_value_pairs = pairs[2].split(',')
                        if len(key_value_pairs[-1]) == 0:
                            key_value_pairs = key_value_pairs[:-1]  # remove empty "pair"
                        service_state = {"PST": pairs[3].split(',')[0], "SST": pairs[3].split(',')[1]}
                        params = dict(kv.split('=') for kv in key_value_pairs)
                        equip_dict[eqpt_aid] = {**eqpt_types, **params, **service_state}

            equip_dict = equip_dict
            return equip_dict

    def rtrv_xdsl(self, tid='', xdslaid='ALL', details='N', timeout=90, debug_run=False):

        ## RTRV-XDSL:[TID]:<XdslAid>:[CTAG]:::[DETAILS=<DETAILS>];

        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_XDSL.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
                for row in response:
                    lines = row.split("\r\n")
                    l.debug("Test data After RegEx: %s", lines)
        else:
            response = self.command('rtrv-xdsl:{}:{}::::details={};'.format(tid, xdslaid, details), timeout=timeout)
            l.debug('Sending command %s to device' % response)

            xdsl_dict = dict()
            for row in response:
                lines = row.split("\r\n")
                for line in lines:
                    if re.match(r'\s*N\d+-\d+-\d*-\d*:.*?', line):
                        print(line)

                        line = re.sub(r'(^\s+|\s+$)', '', line)
                        line = re.sub(r'["\\;]', '', line)

                        l.debug("After RegEx: %s", line)
                        groups = line.split(':')
                        print(groups)
                        xdsl_aid = groups[0]
                        xdls_types = {"SRVTYPE": groups[1]}

                        key_value_pairs = groups[2].split(',')
                        if len(key_value_pairs[-1]) == 0:
                            key_value_pairs = key_value_pairs[:-1]  # remove empty "pair"
                        temp_ser_state = groups[3].split(',')
                        if len(temp_ser_state) == 1:
                            service_state = {"PST": temp_ser_state[0]}
                        elif len(temp_ser_state) == 2:
                            service_state = {"PST": temp_ser_state[0], "SST": temp_ser_state[1]}
                        else:
                            l.warning("Service state on xDSL port has more than 2 fields after comma split.")
                            service_state = {"PST": temp_ser_state[0], "SST": temp_ser_state[1]}
                        params = dict(kv.split('=') for kv in key_value_pairs)
                        xdsl_dict[xdsl_aid] = {**xdls_types, **params, **service_state}

            xdsl_dict = xdsl_dict
            return xdsl_dict

    def rtrv_adsl(self, tid='', adslaid='', timeout=90, debug_run=False):

        ## RTRV-ADSL:[TID]:< AdslAid >:[CTAG];

        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_ADSL.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
                for row in response:
                    lines = row.split("\r\n")
                    l.debug("Test data After RegEx: %s", lines)
        else:
            response = self.command('rtrv-adsl:{}:{}:;'.format(tid, adslaid), timeout=timeout)
            l.debug('Sending command %s to device' % response)

            adsl_dict = dict()
            for row in response:
                lines = row.split("\r\n")
                for line in lines:
                    if re.match(r'\s*N\d+-\d+-\d*-\d*:.*?', line):
                        print(line)

                        line = re.sub(r'(^\s+|\s+$)', '', line)
                        line = re.sub(r'["\\;]', '', line)

                        l.debug("After RegEx: %s", line)
                        groups = line.split(':')
                        print(groups)
                        adsl_aid = groups[0]

                        adls_types = {"PROVTYPE": groups[1].split(',')[0], "CHNL0": groups[1].split(',')[1],
                                      "CHNL1": groups[2].split(',')[2]}

                        key_value_pairs = groups[2].split(',')
                        if len(key_value_pairs[-1]) == 0:
                            key_value_pairs = key_value_pairs[:-1]  # remove empty "pair"
                        temp_ser_state = groups[3].split(',')
                        if len(temp_ser_state) == 1:
                            service_state = {"PST": temp_ser_state[0]}
                        elif len(temp_ser_state) == 2:
                            service_state = {"PST": temp_ser_state[0], "SST": temp_ser_state[1]}
                        else:
                            l.warning("Service state on ADSL port has more than 2 fields after comma split.")
                            service_state = {"PST": temp_ser_state[0], "SST": temp_ser_state[1]}
                        params = dict(kv.split('=') for kv in key_value_pairs)
                        adsl_dict[adsl_aid] = {**adls_types, **params, **service_state}

            adsl_dict = adsl_dict
            return adsl_dict

    def rtrv_vb(self, tid='', vbaid='n1-1-all', option82='', l2rlymode='', timeout=10, debug_run=False):

        # RTRV-VB:[TID]:<VbAid>:[CTAG]:::[[OPTION82=<OPTION82>,][L2RLYMODE=<L2RLYMODE>]];
        # "N1-1-VB1::BW=0,AGETMR=300,PPPOAIWF=Y,DESC=\"\":IS-NR,"
        # "N1-1-VB2::BW=0,AGETMR=300,PPPOAIWF=Y,DESC=\"\":IS-NR"

        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_VB.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
                for row in response:
                    lines = row.split("\r\n")
                    l.debug("Test data After RegEx: %s", lines)
        else:
            response = self.command(
                'rtrv-vb:{}:{}::::OPTION82={},L2RLYMODE={};'.format(tid, vbaid, option82, l2rlymode),
                timeout=timeout)
            l.debug('Sending command %s to device' % response)

            vb_dict = {}
            for row in response:
                lines = row.split("\r\n")
                for line in lines:
                    if re.match(r'^\s*N\d+-\d+-VB\d+::.*$', line):

                        l.debug("Before RegEx: %s", line)
                        line = re.sub(r'(^\s+|\s+$)', '', line)

                        line = re.sub(r'[\"\\;]', '', line)

                        l.debug("After RegEx: %s", line)
                        pairs = line.split('::')

                        vbport = pairs[0]
                        key_value_pairs = pairs[1].split(',')
                        if len(key_value_pairs[-1]) == 0:
                            key_value_pairs = key_value_pairs[:-1]
                        vb_dict[vbport] = dict(kv.split('=') for kv in key_value_pairs)
                    # output_lines.append(line)
            return vb_dict

    def rtrv_vbport(self, tid='', vbportaid='n1-1-vb2-all', timeout=10, debug_run=False):

        # RTRV-VBPORT:[TID]:<VbPortAid>:[CTAG]:::[[OPTION82=<OPTION82>,][L2RLYMODE=<L2RLYMODE>]];

        # N1-1-VB1-19-1::ENCAP=ETHERNETV2,DOS =N,STP=OFF,DIRN=BOTH,STPCOST=4,STPPRIO=128,STAGTYPE=CTAG_8100,
        # PORTTYPE=TRUNK, N1-1-VB2-1::ENCAP=ETHERNETV2,DOS=Y,STP =OFF,DIRN=DOWN,STPCOST =100,STPPRIO=128,
        # STAGTYPE=CTAG_8100,PORTTYPE=EDGE,PINNED=N,

        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_VBPORT.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
                for row in response:
                    lines = row.split("\r\n")
                    l.debug("Test data After RegEx: %s", lines)
        else:
            response = self.command('rtrv-vbport:{}:{}:;'.format(tid, vbportaid),
                                    timeout=timeout)

            l.debug('Sending command %s to device' % response)

            vbp_dict = {}
            for row in response:
                lines = row.split("\r\n")
                for line in lines:
                    if re.match(r'^\s*N\d+-\d+-VB\d+-\d+(-\d+|)::.*$', line):
                        l.debug("Before RegEx: %s", line)

                        line = re.sub(r'(^\s+|\s+$)', '', line)
                        l.debug("After RegEx: %s", line)

                        pairs = line.split('::')

                        vbport = pairs[0]
                        key_value_pairs = pairs[1].split(',')
                        if len(key_value_pairs[-1]) == 0:
                            key_value_pairs = key_value_pairs[:-1]
                        vbp_dict[vbport] = dict(kv.split('=') for kv in key_value_pairs)
                    # output_lines.append(line)
            return vbp_dict

    def rtrv_vlan(self, tid='', vlanaid='n1-1-all', option82='', l2rlymode='', timeout=10, debug_run=False):

        # RTRV-VLAN:[TID]:<VlanAid>:[CTAG]:::[[OPTION82=<OPTION82>,][L2RLYMODE=<L2RLYMODE>]];
        # RTRV-VLAN::N3-2-VB2-VLAN4:543:::OPTION82=NONE,L2RLYMODE=NONE;

        #VLAN112::APPMODE=VLANPERSERVICE,OPTION82=NONE,L2RLYMODE=NONE,NUMPRIO=1,IGMPMODE=NONE,STBRLYARP=N,DHCPLOCK=N,MFF
        #= N,RMTIDOPT=STND,DESC =\"Adtran Management\"

        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_XDSL.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
                for row in response:
                    lines = row.split("\r\n")
                    l.debug("Test data After RegEx: %s", lines)
        else:
            response = self.command(
                'rtrv-vlan:{}:{}::::OPTION82={},L2RLYMODE={};'.format(tid, vlanaid, option82, l2rlymode),
                timeout=timeout)
            l.debug('Sending command %s to device' % response)

            vlan_dict = {}
            for row in response:
                lines = row.split("\r\n")
                for line in lines:
                    if re.match(r'^\s*N\d+-\d+-VB\d+-VLAN\d+::.*$', line):

                        l.debug("Before RegEx: %s", line)
                        line = re.sub(r'(^\s+|\s+$)', '', line)

                        line = re.sub(r'[\"\\;]', '', line)

                        l.debug("After RegEx: %s", line)
                        pairs = line.split('::')

                        vlan = pairs[0]
                        key_value_pairs = pairs[1].split(',')
                        if len(key_value_pairs[-1]) == 0:
                            key_value_pairs = key_value_pairs[:-1]
                        vlan_dict[vlan] = dict(kv.split('=') for kv in key_value_pairs)
                    # output_lines.append(line)
            return vlan_dict

    def rtrv_vlan_port(self, tid='', vlanportaid='n1-1-all', timeout=10, debug_run=False):

        # RTRV-VLAN-PORT:[TID]:<VLanPortAid>:[CTAG];

        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_XDSL.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
                for row in response:
                    lines = row.split("\r\n")
                    l.debug("Test data After RegEx: %s", lines)
        else:
            response = self.command('rtrv-vlan-port:{}:{}:;'.format(tid, vlanportaid),
                                    timeout=timeout)
            l.debug('Sending command %s to device' % response)

            vlan_dict = {}
            for row in response:
                lines = row.split("\r\n")
                for line in lines:
                    if re.match(r'^\s*N\d+-\d+-VB\d+-VLAN\d+::.*$', line):

                        l.debug("Before RegEx: %s", line)
                        line = re.sub(r'(^\s+|\s+$)', '', line)

                        line = re.sub(r'[\"\\;]', '', line)

                        l.debug("After RegEx: %s", line)
                        pairs = line.split('::')

                        vlan = pairs[0]
                        key_value_pairs = pairs[1].split(',')
                        if len(key_value_pairs[-1]) == 0:
                            key_value_pairs = key_value_pairs[:-1]
                        vlan_dict[vlan] = dict(kv.split('=') for kv in key_value_pairs)
                    # output_lines.append(line)
            return vlan_dict

    def rtrv_vlan_vbport(self, tid='', vbportaid='n1-1-vb2-all', vlan='n1-1-vb2-vlan622', opt82act='', timeout=10,
                         debug_run=False):
        # RTRV-VLAN-VBPORT:[TID]:<VbPortAid>:[CTAG]:::[[VLAN=<VLAN>,][OPT82ACT=<OPT82ACT>]];

        l = logging.getLogger()

        if debug_run:
            with open("tests/raw/RTRV_VLAN_VB_PORTL.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
                for row in response:
                    lines = row.split("\r\n")
                    l.debug("Test data After RegEx: %s", lines)
        else:
            response = self.command(
                'rtrv-vlan-vbport:{}:{}::::vlan={},opt82act={};'.format(tid, vbportaid, vlan, opt82act),
                timeout=timeout)
            l.debug('Sending command %s to device' % response)

            vbpvlan_dict = {}
            for row in response:
                lines = row.split("\r\n")
                for line in lines:
                    if re.match(r'^\s*N\d+-\d+-VB\d+-\d+(-\d+|)::.*$', line):

                        l.debug("Before RegEx: %s", line)
                        line = re.sub(r'(^\s+|\s+$)', '', line)

                        l.debug("After RegEx: %s", line)
                        pairs = line.split('::')

                        vbvlan = pairs[0]
                        key_value_pairs = pairs[1].split(',')
                        if len(key_value_pairs[-1]) == 0:
                            key_value_pairs = key_value_pairs[:-1]
                        vbpvlan_dict[vbvlan] = dict(kv.split('=') for kv in key_value_pairs)
                    # output_lines.append(line)
            return vbpvlan_dict


class C7SyncTL1Input(TL1IOInput, C7TL1LanguageInput, BaseSyncInput):
    pass


class C7ASyncTL1Input(TL1IOInput, C7TL1LanguageInput, BaseAsyncInput):
    pass


def test_setup():
    pass


def main():
    test_setup()


if __name__ == '__main__':
    main()
