import os
import json

from inf import INFSyncTL1Input

config = 'config.json'

with open(config) as config_file:
    cf = json.load(config_file)

log_level = cf['LOG_LEVEL']
log_dir = cf['LOG_DIR']
log_file = cf['LOG_FILE']
timeout = cf['TIMEOUT']
username = cf['USER']
password = cf['PASS']
hostname = "10.10.96.44"

log = log_dir + log_file

if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)


io = INFSyncTL1Input(hostname=hostname)
io.setDefaultTimeout(timeout=timeout)
io.setLogFile(logfile=log)
io.setLoginCredentials(username=username, password=password)


def main():
    io.start()

    nodes = io.rtrv_sys()

    # for value in nodes.values():
    #     for tids in value.keys():
    #        tid = tids
    #      print("TID: ", tid)

    for key in nodes.keys():
        node_num = key + "-ALL"
        shelf = io.rtrv_shelf(shelfaid=node_num)
        print('Shelf: ', shelf)

        for keys in shelf.keys():
            shelf_num = keys + "-ALL"
            eqpt = io.rtrv_eqpt(eqptaid=shelf_num)
            print("Equipment: ", eqpt)
            xdsl_stuff = io.rtrv_xdsl(xdslaid="{}".format(shelf_num))
            print("xDSL: ", xdsl_stuff)
            adsl_stuff = io.rtrv_adsl(adslaid="{}".format(shelf_num))
            print("ADSL: ", adsl_stuff)

    # for key in nodes.keys():
    #     node_num = key + "-ALL"
    #     shelf = io.rtrv_shelf(shelfaid=node_num)
    #     for keys in shelf.keys():
    #         shelf_num = keys + "-ALL"
    #         vir_bridge = io.rtrv_vb(vbaid="{}".format(shelf_num))
    #         for vKey in vir_bridge.keys():
    #             node_vb = vKey + "-all"
    #             vlan = io.rtrv_vlan(vlanaid="{}".format(node_vb))
    #             print(vlan)
    io.stop()


if __name__ == '__main__':
    main()
