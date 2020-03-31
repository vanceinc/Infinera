import os
import json
import logging
import sys


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
ports = 9090

log = log_dir + log_file
logg = logging.basicConfig()

if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)

script_name = "inf_test"

def setup_logger():
    debug_format = '%(asctime)-15s --%(levelname)s-- %(funcName)s(): %(message)s'
    plain_format = '%(message)s'

    display_handler = logging.StreamHandler(stream=sys.stdout)
    log_dir = "log"
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    display_handler.setFormatter(logging.Formatter(fmt=plain_format))
    display_handler.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(os.path.join(log_dir, '{}.log'.format(script_name)))
    logging.basicConfig(handlers=[file_handler, display_handler], level=logging.INFO, format=debug_format)


def main():
    setup_logger()
    l = logging.getLogger(script_name)
    l.info("Starting...")
    print("Starting...")
    io = INFSyncTL1Input(hostname=hostname, port=ports, timeout=5)
    io.setDefaultTimeout(timeout=timeout)
    io.setPrompt(prompt='TL1>>'.encode('utf-8'))
    io.setLogFile(logfile=log)
    io.setLoginCredentials(username=username, password=password)
    io.start()
    print("System banner:")
    print(io.banner)
    print("Logged in. System login messages:")
    print(io.login_messages)
    nodes = io.rtrv_sys()
    print(nodes)

    io.stop()


if __name__ == '__main__':
    main()
