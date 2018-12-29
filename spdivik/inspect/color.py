import colorsys
import itertools
from fractions import Fraction

from functional import as_arguments_of, for_each, pipe
import numpy as np


def _get_fractions():
    """
    [Fraction(0, 1), Fraction(1, 2), Fraction(1, 4), Fraction(3, 4), Fraction(1, 8), Fraction(3, 8), Fraction(5, 8), Fraction(7, 8), Fraction(1, 16), Fraction(3, 16), ...]
    [0.0, 0.5, 0.25, 0.75, 0.125, 0.375, 0.625, 0.875, 0.0625, 0.1875, ...]
    """
    yield 0
    for k in itertools.count():
        i = 2 ** k
        for j in range(1, i, 2):
            yield Fraction(j, i)


_DEFAULT_SATURATIONS = [Fraction(6, 10)]
_DEFAULT_VALUES = [Fraction(8, 10), Fraction(5, 10)]


def _generate_hsv_neighbourhood(h):
    for s in _DEFAULT_SATURATIONS:
        for v in _DEFAULT_VALUES:
            yield (h, s, v)


flatten = itertools.chain.from_iterable


def as_colormap_color(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    r, g, b = int(255 * r), int(255 * g), int(255 * b)
    return 'rgb({0},{1},{2})'.format(r, g, b)


colormap = pipe(
    _get_fractions,
    for_each(_generate_hsv_neighbourhood),
    flatten,
    for_each(as_arguments_of(as_colormap_color))
)


def make_colormap(values):
    return [
        [value / values.max(), color]
        for value, color
        in zip(np.unique(values), colormap())
    ]
