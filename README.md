# Steam Popular AppIDs

This repository contains Python code to fetch a list of popular Steam appIDs.

I have a comprehensive list of ~30k appIDs, but my [web app][steam-autocomplete] struggles with it. My objective with
this repository is to shorten the list by filtering out the less popular appIDs.

## Requirements

- Install the latest version of [Python 3.X](https://www.python.org/downloads/).
- Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

To fetch a list of popular Steam appIDs, run:

```bash
python fetch_popular_appids.py
```

## References

- [`steam-store-snapshots`][steam-snapshot]: a comprehensive list of appIDs downloaded in January 2021
- [`gamedatacrunch`][github-gdc]@[PyPI][pypi-gdc]: an API to download data through [GameDataCrunch API][web-gdc]
- [`steam-svelte-autocomplete`][steam-autocomplete]: a single-page app in Svelte to suggest completion of game names

[steam-snapshot]: <https://github.com/woctezuma/steam-store-snapshots>

[github-gdc]: <https://github.com/woctezuma/gamedatacrunch>

[pypi-gdc]: <https://pypi.org/project/gamedatacrunch/>

[web-gdc]: <https://www.gamedatacrunch.com/>

[steam-autocomplete]: <https://github.com/woctezuma/steam-svelte-autocomplete>
