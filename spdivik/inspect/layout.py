from enum import Enum, unique

import dash_core_components as dcc
import dash_html_components as html

from spdivik.summary import depth
from spdivik.inspect.app import divik_result
from spdivik.inspect.figure import clusters_figure


def _as_id(name: str) -> str:
    return name.lower().replace('_', '-')


_FIELDS = ['TITLE', 'CLUSTERS', 'LEVEL']


# noinspection PyArgumentList
Fields = unique(Enum(
    'Fields', [(name, _as_id(name)) for name in _FIELDS], type=str))


def make_layout():
    result_depth = depth(divik_result())
    return html.Div([
        html.H1(id=Fields.TITLE, children='Visualization'),
        dcc.Graph(id=Fields.CLUSTERS,
                  figure=clusters_figure(1, 'Clusters')),
        dcc.Slider(id=Fields.LEVEL,
                   value=1,
                   min=1,
                   max=result_depth,
                   step=1,
                   marks={i: i for i in range(result_depth + 1)})
    ])
