from lifelines import KaplanMeierFitter
from matplotlib import pyplot
from business.analyze import merge_data


def survival_kmf():
    """
    Make survival analysis regression and return coefficients 
    and regg output
    """
    # load cleaned data with duration and event dummy
    licenses = merge_data()

    # Make survival analysis reggresion
    kmf = KaplanMeierFitter(durations=licenses.duration, 
                            event_observed=licenses.closed)
    
    # Return KaplanMeierFitter object
    return kmf


    
