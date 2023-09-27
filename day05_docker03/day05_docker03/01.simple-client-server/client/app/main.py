import logging
import os
import random
import time

import requests

SERVER_IP = os.environ.get("SERVER_IP")
if SERVER_IP is None:
    raise ValueError("env: SERVER_IP is not defined")

URL = "http://{server_ip}/?a={a}&b={b}"

log = logging.getLogger("client")
log.setLevel(logging.INFO)

ch = logging.StreamHandler()
log.addHandler(ch)

# fh = logging.FileHandler("/var/log/app/client.txt")
# log.addHandler(fh)


def main() -> None:
    log.warning("=== APPLICATION HAS BEEN STARTED ===")
    while True:
        a = random.randint(0, 99)
        b = random.randint(0, 99)
        server_response = requests.get(URL.format(server_ip=SERVER_IP, a=a, b=b))
        sum_result = server_response.json().get("result")
        if sum_result is None:
            log.error(f"ошибка сложения: {a=}, {b=}")
        else:
            log.info(f"сумма {a:2} и {b:2} равна {sum_result:3}")
        time.sleep(1)


if __name__ == "__main__":
    main()
