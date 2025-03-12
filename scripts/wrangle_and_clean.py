import sys
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from tabulate import tabulate
# DATA_PATH = "../../data/raw/mxmh_survey_results.csv"

def clean_data(path):
    np.random.seed(42)
    data = pd.read_csv(path)
    # Handle NAs
    data = remove_BPM_outliers(data)
    data = fill_BPM_NAs(data)
    data = fill_nulls_unknown(data)
    # Make ordered columns
    data = make_frequency_cols_ordered(data)
    # Derive new columns
    data = make_mental_health_levels(data)
    data = make_data_time(data)
    data = make_time_of_day(data)
    data = create_no_music_hobbies_column(data)
    data = group_ages(data)
    data = make_genre_diversity_score(data)
    #drop permissions
    data = drop_permissions(data)
    return data

def remove_BPM_outliers(data):
    droppedMax = data["BPM"].nlargest(2).index
    droppedMin = data["BPM"].nsmallest(5).index
    droppedOutliers = droppedMax.union(droppedMin)
    data = data.drop(index=droppedOutliers)
    return data

def fill_BPM_NAs(data):
    bpm_values = data["BPM"].dropna()
    bpm_probs = bpm_values.value_counts(normalize=True) 
    music_filled_random_sampling = data.copy()
    music_filled_random_sampling["BPM"] = music_filled_random_sampling["BPM"].apply(
        lambda x: np.random.choice(bpm_probs.index, p=bpm_probs.values) if pd.isna(x) else x
        )
    return music_filled_random_sampling


def fill_nulls_unknown(data):
    data['Age'] = data['Age'].fillna(data['Age'].median())
    data['Primary streaming service'] = data['Primary streaming service'].fillna("Unknown")
    data['While working'] = data['While working'].fillna("Unknown")
    data['Instrumentalist'] = data['Instrumentalist'].fillna("Unknown")
    data['Composer'] = data['Composer'].fillna("Unknown")
    data['Foreign languages'] = data['Foreign languages'].fillna("Unknown")
    data['Music effects'] = data['Music effects'].fillna("No response")
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
    data['Musical_hobbies'] = (
    (data["Composer"] == "No") & (data["Instrumentalist"] == "No")
        ).map({True: "No", False: "Yes"})
    return data

def group_ages(data):
    data["Age_Grouped"] = np.where(data["Age"] > 65, 66, data["Age"])
    return data

def make_genre_diversity_score(data):
    frequency_mapping = {
        "Never": 0,
        "Rarely": 1,
        "Sometimes": 2,
        "Very frequently": 3
    }

    genre_columns = [
        "Frequency [Classical]", "Frequency [Country]", "Frequency [EDM]", "Frequency [Folk]",
        "Frequency [Gospel]", "Frequency [Hip hop]", "Frequency [Jazz]", "Frequency [K pop]",
        "Frequency [Latin]", "Frequency [Lofi]", "Frequency [Metal]", "Frequency [Pop]",
        "Frequency [R&B]", "Frequency [Rap]", "Frequency [Rock]", "Frequency [Video game music]"
    ]

    for col in genre_columns:
        data[col] = data[col].map(frequency_mapping)

    data["Genre Diversity Score"] = (data[genre_columns] > 0).sum(axis=1)
    return data
