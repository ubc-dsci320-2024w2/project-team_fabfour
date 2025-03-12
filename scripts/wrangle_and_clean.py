import sys
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from tabulate import tabulate
# DATA_PATH = "../../data/raw/mxmh_survey_results.csv"

def clean_data(path):
    data = pd.read_csv(path)
    data = make_frequency_cols_ordered(data)
    data = make_mental_health_levels(data)
    data = make_data_time(data)
    data = make_time_of_day(data)
    data = drop_permissions(data)
    data = create_no_music_hobbies_column(data)
    data = group_ages(data)
    return data


def make_frequency_cols_ordered(data):
    order = ["Never", "Rarely", "Sometimes", "Very frequently"]
    for col in data.columns:
        if "Frequency" in col:
            data[col] = pd.Categorical(data[col], categories=order, ordered=True)
    return data

def make_mental_health_levels(data):
    data['Anxiety_Level'] = pd.cut(
        data['Anxiety'], 
        bins=[0, 3, 6, 10], 
        labels=['Low', 'Medium', 'High'],
        include_lowest=True)

    data['Depression_Level'] = pd.cut(
        data['Depression'], 
        bins=[0, 3, 6, 10],  
        labels=['Low', 'Medium', 'High'],
        include_lowest=True)

    data['Insomnia_Level'] = pd.cut(
        data['Insomnia'], 
        bins=[0, 3, 6, 10],  
        labels=['Low', 'Medium', 'High'],
        include_lowest=True)

    data['OCD_Level'] = pd.cut(
        data['OCD'], 
        bins=[0, 3, 6, 10],  
        labels=['Low', 'Medium', 'High'],
        include_lowest=True)
    return data

def make_data_time(data):
    data["Timestamp"] = pd.to_datetime(data["Timestamp"])
    data["Date"] = pd.to_datetime(data["Timestamp"].dt.date)
    data["Time"] = data["Timestamp"].dt.strftime("%H:%M:%S")
    return data;

def make_time_of_day(data):
    time_order = ["Morning", "Afternoon", "Evening", "Night"]
    data["Time of Day"] = data["Timestamp"].apply(categorize_time_of_day)
    data["Time of Day"] = pd.Categorical(
        data["Time of Day"], 
        categories=time_order, 
        ordered=True)
    return data

def categorize_time_of_day(timestamp):
    hour = timestamp.hour
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    elif 18 <= hour < 24:
        return "Evening"
    else:
        return "Night"

def drop_permissions(data):
    data = data.drop(columns=["Permissions"])
    return data

def create_no_music_hobbies_column(data):
    data['No_musical_hobbies'] = (
    (data["Composer"] == "No") & (data["Instrumentalist"] == "No")
        ).map({True: "Yes", False: "No"})
    return data

def group_ages(data):
    data["Age_Grouped"] = np.where(data["Age"] > 65, 66, data["Age"])
