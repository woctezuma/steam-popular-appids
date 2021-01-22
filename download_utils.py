import requests

from disk_utils import get_json_file_name, load_json, save_json


def get_endpoints():
    return ["followers", "peak_ccu", "reviews_total"]


def get_gdc_url(endpoint):
    return f"https://www.gamedatacrunch.com/api/steam/list/all/00/{endpoint}"


def fetch_single_page(endpoint, page_no=1):
    print(f"- page {page_no}")

    params = {"count": 100, "page": page_no}
    response = requests.get(url=get_gdc_url(endpoint), params=params)

    if response.ok:
        data = response.json()
    else:
        print("Status code: {}".format(response.status_code))
        data = {"ranks": []}

    return data


def fetch_from_endpoint(endpoint, num_pages=10, save_to_disk=True):
    fname = get_json_file_name(endpoint, num_pages)

    try:
        ranking = load_json(fname=fname)
    except FileNotFoundError:
        print(f"Fetching {endpoint} for {num_pages} pages")

        ranking = list()

        for i in range(num_pages):
            page_data = fetch_single_page(endpoint, page_no=i + 1)
            ranking += page_data["ranks"]

        if save_to_disk:
            save_json(data=ranking, fname=fname)

    return ranking


def fetch_from_every_endpoint(endpoints=None, num_pages=10):
    if endpoints is None:
        endpoints = get_endpoints()

    rankings = dict()

    for keyword in endpoints:
        rankings[keyword] = fetch_from_endpoint(endpoint=keyword, num_pages=num_pages)

    return rankings
