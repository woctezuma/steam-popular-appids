from disk_utils import save_app_ids
from download_utils import get_endpoints, fetch_from_every_endpoint


def aggregate_top_app_ids(endpoints, rankings, num_apps=3000):
    app_ids = set()
    for keyword in endpoints:
        top_ranking = rankings[keyword][:num_apps]

        for app in top_ranking:
            id = int(app["steam_appid"])
            app_ids.add(id)

        print("[{}] #apps = {}".format(keyword, len(app_ids)))

    print("Total = {}".format(len(app_ids)))

    app_ids = list(sorted(app_ids))

    return app_ids


def main():
    endpoints = get_endpoints()
    rankings = fetch_from_every_endpoint(endpoints=endpoints)
    app_ids = aggregate_top_app_ids(endpoints=endpoints, rankings=rankings)
    save_app_ids(app_ids)

    return


if __name__ == "__main__":
    main()
