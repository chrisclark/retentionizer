import pandas as pd
from sbgresults import SbgResults
import bokeh.plotting as bk
from bokeh.resources import CDN
from bokeh.embed import components

COLORS = ["#7fc97f", "#beaed4", "#fdc086", "#ffff99", "#386cb0", "#f0027f", "#bf5b17"]


def parse(data_url):
    ds = pd.read_csv(data_url)
    ds.reindex(index=ds['t'])
    del ds['t']
    return [SbgResults(c, dict(zip(ds[c].index, ds[c]))) for c in ds]


def plot_sbg_results(sbg_results):
    p = bk.figure(title="Actual and Predicted Survival")
    for i, result in enumerate(sbg_results):
        p.line(range(len(result.predicted)), result.predicted, color=COLORS[i], legend=result.name)
        p.scatter(range(len(result.actual)), result.actual, color=COLORS[i], legend=result.name)
    return components(p, CDN)