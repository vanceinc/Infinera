import logging
import re
import socket

__module_name__ = "c7"

from protocols.tl1 import *

debug_run = False


class c7_tl1(ip=None, user=None, password=None):
    def __init__(self, ip="", port=23, user="", password=""):
        c7_tl1.__init__(self, port=port, password=password)
        self.ip = ip
        self.user = user
        self.password = password
        self.is_logged_in = False
        self.equip_dict = dict()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        l = logging.getLogger(__module_name__)
        if type:
            l.exception("Exception occurred in exit method for c7tl1 class.")
        self.stop()
        return True

    def start(self):
        l = logging.getLogger(__module_name__)
        self.setup_connection()
        # l.debug("Connection info. TL1 obj: %s, Status: %s", self.tl1,)
        if self.connected:
            if self.protocol.upper() == "TELNET":
                response = self.login()
                if "DENY" in response and "Already Logged In" not in response:
                    l.debug("Login Failed!")
                    self.is_logged_in = False
                else:
                    l.debug("Login Successful!")
                    self.is_logged_in = True
            elif self.protocol.upper() == "SSH":
                l.debug("SSH protocol doesn't need login.")
                self.is_logged_in = True

    def stop(self):
        if self.connected:
            if 'COMPLD' in self.logout():
                self.is_logged_in = False
            self.close()

    def setup_connection(self):
        l = logging.getLogger(__module_name__)

        # Do an address lookup to verify hostname/IP is valid, if not this will raise gaierror and addr_info
        # will not be set.
        addr_info = socket.getaddrinfo(self.ip, 0, 0, 0, 0)

        # print("Huh, that actually worked!")
        l.info("Establishing connection to C7 network %s" % self.ip)
        self.connect()
        l.debug("Connection established via port %s.", self.port)
        if self.connected:
            l.info("Connection established!")

    def inhibit_all_messages(self):
        self.sendSock("INH-MSG-ALL;")
        response = self.readTL1response()  # flush it again from INH-MSG-ALL response
        response = re.sub(r'^\r$', '', response)
        return response

    def allow_all_messages(self):
        self.sendSock("ALW-MSG-ALL;")
        response = self.readTL1response()  # flush it again from INH-MSG-ALL response
        response = re.sub(r'^\r$', '', response)
        return response

    def retrieve_equipment(self, aid):
        l = logging.getLogger(__module_name__)

        if debug_run:
            with open("PLVWMNXPH01_EQPT.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)

        else:
            command = "RTRV-EQPT::{0};".format(aid)
            l.debug("Sending command %s to device" % command)
            self.sendSock(command)
            response = self.readTL1response()
            response = re.sub(r'^\r$', '', response)
            l.debug("TL1 Response: %s" % response)

        eqpt_dict = dict()
        if debug_run:
            lines = response.split("\n")
        else:
            lines = response.split("\r\n")
        for line in lines:

            if re.match(r'^\s+"N\d+-\d+-(CS[AB]|MS|FT|\d+):.*$', line):
                # l.debug("Before RegEx: %s", line)
                line = re.sub(r'(^\s+|\s+$)', '', line)
                line = re.sub(r'["\\;]', '', line)

                # l.debug("After RegEx: %s", line)
                pairs = line.split(':')

                eqpt_aid = pairs[0]
                eqpt_types = pairs[1].split(',')
                key_value_pairs = pairs[2].split(',')
                if len(key_value_pairs[-1]) == 0:
                    key_value_pairs = key_value_pairs[:-1]
                eqpt_dict[eqpt_aid] = {"types": eqpt_types, "params": dict(kv.split('=') for kv in key_value_pairs)}
                # output_lines.append(line)

        self.equip_dict = eqpt_dict
        return eqpt_dict

    def retrieve_vbports(self, vb_aid):
        vlans = []
        l = logging.getLogger(__module_name__)

        if debug_run:
            with open("PLVWMNXPH01_VBPORT.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)

        else:

            command = "RTRV-VBPORT::{0};".format(vb_aid)
            l.debug("Sending command %s to device" % command)
            self.sendSock(command)
            response = self.readTL1response()
            response = re.sub(r'^\r$', '', response)
            l.debug("TL1 Response: %s" % response)

        vbport_dict = {}
        if debug_run:
            lines = response.split("\n")
        else:
            lines = response.split("\r\n")
        for line in lines:

            if re.match(r'^\s+"N\d+-\d+-VB\d+-\d+::.*$', line):
                # l.debug("Before RegEx: %s", line)
                line = re.sub(r'(^\s+|\s+$)', '', line)
                line = re.sub(r'["\\;]', '', line)
                # l.debug("After RegEx: %s", line)
                pairs = line.split('::')

                vbport = pairs[0]
                key_value_pairs = pairs[1].split(',')
                if len(key_value_pairs[-1]) == 0:
                    key_value_pairs = key_value_pairs[:-1]
                vbport_dict[vbport] = dict(kv.split('=') for kv in key_value_pairs)
                # output_lines.append(line)

        return vbport_dict

    def retrieve_vlan_vbports(self, vb_aid):
        vlans = []
        l = logging.getLogger(__module_name__)

        command = "RTRV-VLAN-VBPORT::{0};".format(vb_aid)
        l.debug("Sending command %s to device" % command)
        self.sendSock(command)
        response = self.readTL1response()
        response = re.sub(r'^\r$', '', response)
        l.debug("TL1 Response: %s" % response)

        vlan_vbport_dict = {}
        if debug_run:
            lines = response.split("\n")
        else:
            lines = response.split("\r\n")
        for line in lines:
            if re.match(r'^\s+"N\d+-\d+-VB\d+-\d+::.*$', line):
                # l.debug("Before RegEx: %s", line)
                line = re.sub(r'(^\s+|\s+$)', '', line)
                line = re.sub(r'["\\;]', '', line)
                # l.debug("After RegEx: %s", line)
                pairs = line.split('::')

                vbport = pairs[0]
                key_value_pairs = pairs[1].split(',')
                if len(key_value_pairs[-1]) == 0:
                    key_value_pairs = key_value_pairs[:-1]
                vlan_vbport_dict[vbport] = dict(kv.split('=') for kv in key_value_pairs)
                # output_lines.append(line)

        return vlan_vbport_dict

    def retrieve_vlans(self, vb_aid):
        vlans = []
        l = logging.getLogger(__module_name__)

        command = "RTRV-VLAN::{0};".format(vb_aid)
        l.debug("Sending command %s to device" % command)
        self.sendSock(command)
        response = self.readTL1response()
        response = re.sub(r'^\r$', '', response)
        l.debug("TL1 Response: %s" % response)

        vlan_dict = {}
        lines = response.split("\r\n")
        for line in lines:

            if re.match(r'^\s+"N\d+-\d+-VB\d+-VLAN\d+::.*$', line):
                # l.debug("Before RegEx: %s", line)
                line = re.sub(r'(^\s+|\s+$)', '', line)
                line = re.sub(r'["\\;]', '', line)
                # l.debug("After RegEx: %s", line)
                pairs = line.split('::')

                vbport = pairs[0]
                key_value_pairs = pairs[1].split(',')
                if len(key_value_pairs[-1]) == 0:
                    key_value_pairs = key_value_pairs[:-1]
                vlan_dict[vbport] = dict(kv.split('=') for kv in key_value_pairs)
                # output_lines.append(line)

        return vlan_dict

    def retrieve_cvidreg(self, vbport_aid):
        vlans = []
        l = logging.getLogger(__module_name__)

        command = "RTRV-CVIDREG::{0};".format(vbport_aid)
        l.debug("Sending command %s to device" % command)
        self.sendSock(command)
        response = self.readTL1response()
        response = re.sub(r'^\r$', '', response)
        l.debug("TL1 Response: %s" % response)

        cvidreg_dict = {}

        lines = response.split("\r\n")
        for line in lines:

            if re.match(r'^\s+"N\d+-\d+-VB\d+-\d+-.*::.*$', line):
                # l.debug("Before RegEx: %s", line)
                line = re.sub(r'(^\s+|\s+$)', '', line)
                line = re.sub(r'["\\;]', '', line)
                # l.debug("After RegEx: %s", line)
                pairs = line.split('::')

                vbport = pairs[0]
                key_value_pairs = pairs[1].split(',')
                if len(key_value_pairs[-1]) == 0:
                    key_value_pairs = key_value_pairs[:-1]
                cvidreg_dict[vbport] = dict(kv.split('=') for kv in key_value_pairs)
                # output_lines.append(line)

        return cvidreg_dict

    def retrieve_crs_vc(self, aid, scope="NTWK"):
        vlans = []
        l = logging.getLogger(__module_name__)

        if debug_run:
            with open("PLVWMNXPH01_CRS_VC.txt") as input_file:
                response = input_file.read()
                l.debug("TL1 Response(cached): %s" % response)
        else:
            command = "RTRV-CRS-VC::{0}::::SCOPE={1};".format(aid, scope)
            l.debug("Sending command %s to device" % command)
            self.sendSock(command)
            response = self.readTL1response()
            response = re.sub(r'^\r$', '', response)
            l.debug("TL1 Response: %s" % response)

        crs_vc_dict = {}
        if debug_run:
            lines = response.split("\n")
        else:
            lines = response.split("\r\n")
        for line in lines:

            if re.match(r'.*(1WAY|2WAY).*', line):
                # l.debug("Before RegEx: %s", line)
                line = re.sub(r'(^\s+|\s+$)', '', line)
                line = re.sub(r'["\\;]', '', line)

                # l.debug("After RegEx: %s", line)
                pairs = line.split(':')

                endpoint_pair = pairs[0].split(',')

                crs_type = pairs[1]
                key_value_pairs = pairs[2].split(',')
                if len(key_value_pairs[-1]) == 0:
                    key_value_pairs = key_value_pairs[:-1]
                crs_vc_dict[endpoint_pair[0]] = {"endpoint_aid": endpoint_pair[1], "crs_type": crs_type,
                                                 "crs_options": dict(kv.split('=') for kv in key_value_pairs)}
                crs_vc_dict[endpoint_pair[1]] = {"endpoint_aid": endpoint_pair[0], "crs_type": crs_type,
                                                 "crs_options": dict(kv.split('=') for kv in key_value_pairs)}
                # output_lines.append(line)

        return crs_vc_dict

    def retrieve_port(self, type, aid):
        vlans = []
        l = logging.getLogger(__module_name__)
        command = "RTRV-{0}::{1};".format(type, aid)
        l.debug("Sending command %s to device" % command)
        self.sendSock(command)
        response = self.readTL1response()
        if command not in response:
            response = self.readTL1response()
        response = re.sub(r'^\r$', '', response)
        l.debug("TL1 Response: %s" % response)
        output_lines = []
        port_dict = {}
        if debug_run:
            lines = response.split("\n")
        else:
            lines = response.split("\r\n")
        for line in lines:

            if aid in line and command not in line:
                # l.debug("Before RegEx: %s", line)
                line = re.sub(r'(^\s+|\s+$)', '', line)
                line = re.sub(r'["\\;]', '', line)

                line = re.sub(r',$', '', line)
                # l.debug("After RegEx: %s", line)
                pairs = line.split(':')

                key_value_pairs = pairs[2].split(',')
                if len(key_value_pairs[-1]) == 0:
                    key_value_pairs = key_value_pairs[:-1]
                svc = pairs[3].split(',')
                port_dict[pairs[0]] = {'params': dict(kv.split('=') for kv in key_value_pairs), "state": svc}
                # output_lines.append(line)

        return port_dict

    def retrieve_vlan_ifs(self, vb, downlink_aid):

        vlan_ifs = []
        l = logging.getLogger(__module_name__)
        command = "RTRV-VLAN-IF::{0}::::BRIDGE={1};".format(downlink_aid, vb)
        l.debug("Sending command %s to device" % command)
        self.sendSock(command)
        response = self.readTL1response()
        response = re.sub(r'^\r$', '', response)
        l.debug("TL1 Response: %s" % response)

        lines = response.split("\r\n")
        vlan_ifs = []
        for line in lines:

            if re.match(r'^.*::VLAN=\d+.*$', line):
                line = re.sub(r'(^\s+|\s+$)', '', line)
                line = re.sub(r'["\\;]', '', line)
                pairs = line.split('::')
                pairs = pairs[1].split(',')
