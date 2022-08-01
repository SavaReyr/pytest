import json

import requests
token = "AQAAAAAxOJC1AAhGoIsx-htFT0uqlsUk4u6Tz4c"
apiurl = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': 'OAuth ' + token}


def create_folder(folder_name):
    params = {'path': folder_name}
    result = requests.put(apiurl, headers=headers, params=params)
    return result.status_code


if __name__ == '__main__':
    print(create_folder("dswcs"))