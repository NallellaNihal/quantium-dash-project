import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_app_title():
    assert app.title is not None


def test_layout_exists():
    assert app.layout is not None


def test_header_present():
    layout_children = app.layout.children[0].children

    header = layout_children[0]

    assert "Soul Foods" in header.children


def test_graph_exists():
    layout_children = app.layout.children[0].children

    graph = layout_children[3]

    assert graph.id == "sales-line-chart"
