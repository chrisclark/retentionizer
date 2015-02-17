import pandas as pd
from sbgresults import SbgResults
import bokeh.plotting as bk
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.models.tools import HoverTool
from bokeh.models.glyphs import CircleCross
import numpy as np
from scipy.stats import beta
from collections import OrderedDict


COLORS = ["#7fc97f", "#beaed4", "#fdc086", "#ffff99", "#386cb0", "#f0027f", "#bf5b17"]
LINE_WIDTH = 3


def parse(data_url, periods, discount, value):
    ds = pd.read_csv(data_url)
    ds.reindex(index=ds['t'])
    del ds['t']
    return [SbgResults(c, dict(zip(ds[c].index, ds[c])), periods, discount, value) for c in ds]

def mult100(xs):
    return [100*x for x in xs]

def plot_sbg_results(sbg_results):
    p = bk.figure(title="Actual and Predicted Survival", tools="hover,")
    p.axis[1].axis_label = "%"
    for i, result in enumerate(sbg_results):
        p.line(range(len(result.predicted)), mult100(result.predicted), color=COLORS[i], legend=result.name, line_width = LINE_WIDTH)
        p.scatter(range(len(result.actual)), mult100(result.actual), color=COLORS[i], legend=result.name, marker='o', size=10)
    hover = p.select(dict(type=HoverTool))
    hover.always_active = True
    hover.snap_to_data = True
    hover.tooltips = OrderedDict([
        ("Period", "@x"),
        ("Survive %", "@y"),
    ])
    return components(p, CDN)

def mult100(xs):
    return [100*x for x in xs]

def plot_sbg_retention_distribution(sbg_results):
    p = bk.figure(title="Distribution of Retention Probability", y_range=[0, 6], tools="")
    theta = np.linspace(.001, .999, num=1000)
    for i, result in enumerate(sbg_results):
        pdf = beta.pdf(theta, a = result.alpha, b = result.beta)
        p.line(theta, pdf, color=COLORS[i], legend=result.name, line_width = LINE_WIDTH)
    return components(p, CDN)
