from analysis import stat_analysis 
from hume_pipeline import call_hume
from weights import weights_anal

def complete_analysis(filename):
    # call_hume()
    stat_analysis(filename)
    weights_anal()