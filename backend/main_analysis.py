from analysis import stat_analysis 
from hume_pipeline import call_hume
from weights import weights_anal

def complete_analysis(filename, spokeFirst, onLeft):
    # call_hume()

    # face_0 is always left, spk_0 is always first
    stat_analysis(filename, spokeFirst, onLeft)
    weights_anal(filename, spokeFirst, onLeft)