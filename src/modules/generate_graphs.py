import streamlit as st
from pandas import DataFrame


def plot_call_distribution(data: DataFrame) -> None:
    """
    Plot the distribution of answered and missed calls.

    Args:
        data (DataFrame): The dataset to plot the distribution from.
    """
    labels = ["Answered Calls", "Missed Calls"]
    values = [
        data["Answered Calls"].sum(),
        data["Incoming Calls"].sum() - data["Answered Calls"].sum(),
    ]

    distribution_data = DataFrame({"labels": labels, "values": values})

    st.bar_chart(distribution_data.set_index("labels"))


def plot_call_ratio(data: DataFrame) -> None:
    """
    Plot the ratio of answered and missed calls.

    Args:
        data (DataFrame): The dataset to plot the ratio from.
    """
    labels = ["Answered Calls", "Missed Calls"]
    sizes = [
        data["Answered Calls"].sum(),
        data["Incoming Calls"].sum() - data["Answered Calls"].sum(),
    ]

    ratio_data = DataFrame({"labels": labels, "sizes": sizes})

    st.bar_chart(ratio_data.set_index("labels"))
