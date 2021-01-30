from kedro.pipeline import node, Pipeline
from spaceflights.pipelines.print_catalog.nodes import fetch_catalog, print_catalog_path


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=fetch_catalog,
                inputs=None,
                outputs="catalog_dict",
                name="fetch_catalog",
            ),
            node(
                func=print_catalog_path,
                inputs="catalog_dict",
                outputs=None,
                name="print_catalog_path",
            ),
        ]
    )
