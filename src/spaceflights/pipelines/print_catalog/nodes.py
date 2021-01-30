from kedro.config import ConfigLoader
from typing import Dict

conf_paths = ["conf/base", "conf/local"]
conf_loader = ConfigLoader(conf_paths)

conf_catalog = conf_loader.get("catalog*", "catalog*/**")


def fetch_catalog() -> Dict[str, Dict]:
    """Fetch the catalog dict

    Returns:
        Dict[str, Dict]: catalog dict
    """
    return conf_catalog


def print_catalog_path(conf_catalog: Dict[str, Dict]):
    """Print the catalog entries' path

    Args:
        conf_catalog (Dict[str, Dict]): catalog dict
    """
    print("Catalog entry path:")
    for dataset in conf_catalog.keys():
        print(f'{dataset} -- {conf_catalog[dataset]["filepath"]}')
