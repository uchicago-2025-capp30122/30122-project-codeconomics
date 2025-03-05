import pandas as pd
from lifelines import KaplanMeierFitter
from .merge_data import merge_data_survival
from business.get_data.utils import LICENSE_DESCRIPTION_FOCUS
import plotly.graph_objects as go


def survival_kmf(licenses):
    """
    Make survival analysis
    Input:
        licenses - DataFrame with 'duration', 'closed'

    Output:
         business_kmf.survival graph - KaplanMeierFitter object with fitted data of
         operating duration (days) and  status of the license (closed dummy)
    """

    # Make survival analysis reggresion
    business_kmf = KaplanMeierFitter()
    business_kmf.fit(durations=licenses.duration, event_observed=licenses.closed)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=business_kmf.survival_function_.index,
            y=business_kmf.survival_function_["KM_estimate"],
            mode="lines",
            name="Survival Function",
            line=dict(color="#800000"),
        )
    )

    fig.update_layout(
        title="Kaplan-Meier Survival Curve - all business",
        xaxis_title="Time (years)",
        yaxis_title="Operating Probability",
        margin=dict(l=20, r=20, t=50, b=20),
        height=300,  # Fixed height
        font=dict(family="Arial, sans-serif", size=14),
        template="plotly_white",
    )

    return fig


def survival_kmf_by_quartiles(licenses, variable):
    """
    Generate Kaplan-Meier survival curves split by quartiles of 'variable'.

    Input:
        licenses - DataFrame with 'duration', 'closed', and 'variables'

    Output:
        Plotly figure with survival curves for each quartile group
    """

    # Compute quartiles of 'total_theft'

    licenses["quartile"] = pd.qcut(
        licenses[variable], q=4, labels=["Q1", "Q2", "Q3", "Q4"]
    )

    # Initialize Plotly figure
    fig = go.Figure()

    # Define colors for each quartile
    colors = ["#800000", "#FF5733", "#FFC300", "#28B463"]

    # Fit Kaplan-Meier model for each quartile
    kmf = KaplanMeierFitter()
    for i, quartile in enumerate(licenses["quartile"].unique()):
        subset = licenses[licenses["quartile"] == quartile]
        kmf.fit(
            subset["duration"], event_observed=subset["closed"], label=str(quartile)
        )

        survival_function = kmf.survival_function_.iloc[:, 0]
        # Add survival function to the figure
        fig.add_trace(
            go.Scatter(
                x=survival_function.index,
                y=survival_function.values,
                mode="lines",
                name=f"{variable}: {quartile}",
                line=dict(color=colors[i]),  # Assign color
            )
        )

    # Customize layout
    fig.update_layout(
        title=f"Kaplan-Meier Survival curve by quartiles: {variable}",
        xaxis_title="Time (years)",
        yaxis_title="Operating Probability",
        margin=dict(l=20, r=20, t=50, b=20),
        height=400,
        font=dict(family="Arial, sans-serif", size=14),
        template="plotly_white",
    )

    return fig


# load cleaned data with duration and event dummy
licenses = merge_data_survival()
licenses = licenses[licenses.license_description.isin(LICENSE_DESCRIPTION_FOCUS)]
licenses["duration"] = licenses.duration / 365
licenses = licenses.dropna(subset=["total_crime", "med_income"])

# generate graphs with specific parameters
business_kmf_plot = survival_kmf(licenses)
business_kmf_plot_crime = survival_kmf_by_quartiles(licenses, "total_crime")
business_kmf_plot_income = survival_kmf_by_quartiles(licenses, "med_income")
