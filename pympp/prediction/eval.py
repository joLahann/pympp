# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/05_prediction.eval.ipynb.

# %% auto 0
__all__ = ['ds_folder', 'ds_names', 'logs', 'ppms']

# %% ../../nbs/05_prediction.eval.ipynb 4
from ..process import *
from .predict import *
from .models import *
from .mppn import *


# %% ../../nbs/05_prediction.eval.ipynb 8
ds_folder = "../data/logs/csv/mppn_ds/"
ds_names=[
    "Helpdesk",
    "Mobis",
    "BPIC_12",
    "BPIC_12_A",
    "BPIC_12_O",
    "BPIC_12_Wcomplete",
    "BPIC_13_CP",
    "BPIC_17_OFFER",
    "BPIC_20_RFP"

]
logs = [f"{ds_folder}{ds_name}.csv" for ds_name in ds_names]
ppms=[
    PPM_Evermann,
    PPM_Tax_Spezialized,
    PPM_Tax_Shared,
    PPM_Tax_Mixed,
    PPM_Camargo_Spezialized,
    PPM_Camargo_concat,
    PPM_Camargo_fullconcat,
    PPM_MiDA,
    PPM_MPPN
]

# %% ../../nbs/05_prediction.eval.ipynb 11
from tqdm import tqdm as tqdm_console
import fire
from fastai.basics import *
