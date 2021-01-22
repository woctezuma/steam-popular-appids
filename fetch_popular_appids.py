from disk_utils import save_app_ids
from download_utils import get_endpoints, fetch_from_every_endpoint
from fetch_snapshot_appids import load_snapshot_app_ids


def aggregate_top_app_ids(endpoints, rankings, num_apps=3000, save_to_disk=False):
    app_ids = set()
    for keyword in endpoints:
        top_ranking = rankings[keyword][:num_apps]

        for app in top_ranking:
            id = int(app["steam_appid"])
            app_ids.add(id)

        print("[{}] #apps = {}".format(keyword, len(app_ids)))

    print("Total = {}".format(len(app_ids)))

    app_ids = list(sorted(app_ids))

    if save_to_disk:
        save_app_ids(app_ids)

    return app_ids


def load_aggregated_app_ids():
    endpoints = get_endpoints()
    rankings = fetch_from_every_endpoint(endpoints=endpoints, num_pages=50)
    popular_app_ids = aggregate_top_app_ids(
        endpoints=endpoints,
        rankings=rankings,
        num_apps=3000,
        save_to_disk=False,
    )

    return popular_app_ids


def main():
    popular_app_ids = load_aggregated_app_ids()

    all_known_app_ids = load_snapshot_app_ids()
    intersected_app_ids = set(all_known_app_ids).intersection(popular_app_ids)

    print("After intersection: {} apps".format(len(intersected_app_ids)))

    save_app_ids(list(intersected_app_ids), "intersected_app_ids")

    return


if __name__ == "__main__":
    main()
