import requests

import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
import Token_ya
TOKEN_YA = Token_ya.TOKEN_YA



def create_folder_in_ya(token_ya, path="photos"):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {"path": path}
    headers = {"Authorization": f"OAuth {token_ya}"}
    response = requests.put(url, params=params, headers=headers)
    if response.status_code == 201:
        logging.info("The folder has been created")
    elif response.status_code == 409:
        logging.info("The folder already exists")
    else:
        logging.info("The folder has not been created")
    return response


create_folder_in_ya(TOKEN_YA)