import argparse
import logging
import argparse
import datetime
import time
from pathlib import Path
from bluetooth.ble import DiscoveryService

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="BLE scanner")
    p.add_argument(
        "timeout",
        help="number of seconds to scan for BLE devices",
        nargs="?",
        type=int,
        default=5,
    )
   
    #Added in the Argument for the folder to put the data into
    p.add_argument(
        "logpath",
        help="Directory to write the Bluetooth Detected Output to",
        default = "."
    )
    P = p.parse_args()

    #Added in the code for the Time/Date for the file name
    FMT = "%Y-%m-%dT%H_%M_%S"
    now = datetime.datetime.now().strftime(FMT)

    timeout = P.timeout

    print(f"Scanning BLE devices for {timeout} seconds")

    svc = DiscoveryService()
    ble_devs = svc.discover(timeout)

    #Once done scanning, get ready to parse the results into a txt file
    logpath = Path(P.logpath).expanduser()
    logpath.mkdir(parents=True, exist_ok=True)
    logfile = logpath / ("ble_" + now + ".txt")
    print("Logging data to", logfile)
  
    for u, n in ble_devs.items():
        now = datetime.datetime.now().strftime(FMT)
        print(u, n)

        if not u:
            logging.error(f"no data recorded {now}")
            time.sleep(1)
            continue

        file = open(logfile, 'a')
        # we add a line ending so the data isn't all on one line for all times
        file.write(u)
        file.write(" ")
        file.write(n)
        file.write('\n')
    file.close()
