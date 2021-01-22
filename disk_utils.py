import json

import numpy as np


def get_data_folder_name():
    return "data/"


def get_json_file_name(endpoint, num_pages):
    return get_data_folder_name() + f"{endpoint}_{num_pages}.json"


def load_json(fname):
    with open(fname, "r", encoding="utf8") as f:
        data = json.load(f)

    return data


def save_json(data, fname):
    with open(fname, "w", encoding="utf8") as f:
        json.dump(data, f)

    return


def save_npy(data, fname):
    # NB: data type is uint32 (max value ~ 4 billion), which is far greater than max appID (~ 2 million)

    np.save(
        fname,
        np.asarray(data, dtype=np.uint32),
        allow_pickle=False,
        fix_imports=False,
    )

    return


def save_app_ids(app_ids, fname_root="app_ids"):
    save_json(data=app_ids, fname=get_data_folder_name() + f"{fname_root}.json")
    save_npy(data=app_ids, fname=get_data_folder_name() + f"{fname_root}.npy")

    return
