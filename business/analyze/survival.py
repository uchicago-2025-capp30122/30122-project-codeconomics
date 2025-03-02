from lifelines import KaplanMeierFitter
from matplotlib import pyplot
from business.analyze import merge_data_survival
from business.get_data import LICENSE_DESCRIPTION_FOCUS

def survival_kmf():
    """
    Make survival analysis
    Input:
        None - Uses function merge_data_survival to get data with 
        duration and event
    
    Output:
         business_kmf - KaplanMeierFitter object with fitted data of 
         operating duration (days) and  status of the license (closed dummy)
    """
    # load cleaned data with duration and event dummy
    licenses = merge_data_survival()
    #filtered_licenses = licenses[licenses.license_description.isin(LICENSE_DESCRIPTION_FOCUS)]
    #filtered_licenses.closed.sum()


    # Make survival analysis reggresion
    business_kmf = KaplanMeierFitter()
    business_kmf.fit(durations=licenses.duration,
                      event_observed=licenses.closed)
    
    # Return KaplanMeierFitter object
    #print("Surv function:\n", business_kmf.survival_function_)
    #print("Median operating time:\n", business_kmf.median_survival_time_)
    
    return business_kmf





    
