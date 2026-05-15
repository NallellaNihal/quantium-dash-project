import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_header_is_present():
    layout_children = app.layout.children[0].children
    header = layout_children[0]

    assert header.children == "Soul Foods Pink Morsel Sales Visualiser"


def test_visualisation_is_present():
    layout_children = app.layout.children[0].children
    graph = layout_children[3]

    assert graph.id == "sales-line-chart"


def test_region_picker_is_present():
    layout_children = app.layout.children[0].children
    region_picker_container = layout_children[2]
    radio_items = region_picker_container.children[1]

    assert radio_items.id == "region-filter"
