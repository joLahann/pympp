# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_logs.ipynb.

# %% auto 0
__all__ = ['convert_to_df']

# %% ../nbs/00_logs.ipynb 4
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.conversion.log import converter as log_converter
import gzip
import json

# %% ../nbs/00_logs.ipynb 5
def convert_to_df(path):
    log = xes_importer.apply(bpi_2012)
    df = log_converter.apply(log, variant=log_converter.Variants.TO_DATA_FRAME)
    return df