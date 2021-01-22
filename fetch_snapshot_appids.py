import requests

from disk_utils import load_json, get_snapshot_fname, save_json


def get_snapshot_url():
    fname = get_snapshot_fname()
    return f"https://raw.githubusercontent.com/woctezuma/steam-store-snapshots/main/{fname}"


def download_snapshot():
    print('Downloading')
    response = requests.get(url=get_snapshot_url())

    if response.ok:
        data = response.json()
        save_json(data, get_snapshot_fname())
    else:
        print("Status code: {}".format(response.status_code))
        data = {"response": {"apps": []}}

    return data


def load_snapshot():
    try:
        data = load_json(get_snapshot_fname())
    except FileNotFoundError:
        data = download_snapshot()
    return data


def load_snapshot_app_ids():
    data = load_snapshot()
    all_known_app_ids = [int(app["appid"]) for app in data["response"]["apps"]]

    return all_known_app_ids


if __name__ == "__main__":
    all_known_app_ids = load_snapshot_app_ids()
    print(len(all_known_app_ids))
