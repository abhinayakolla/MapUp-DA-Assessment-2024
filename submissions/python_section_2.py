Question 9: Distance Matrix Calculation::

import pandas as pd
import numpy as np
def calculate_distance_matrix(df):
    ids = df['id'].unique()
    distance_matrix = pd.DataFrame(np.zeros((len(ids), len(ids))), index=ids, columns=ids)
    for index, row in df.iterrows():
        id_start, id_end, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.loc[id_start, id_end] = distance
        distance_matrix.loc[id_end, id_start] = distance  # Ensure symmetry
    for k in ids:
        for i in ids:
            for j in ids:
                if distance_matrix.loc[i, j] == 0 and i != j:
                    distance_matrix.loc[i, j] = min(
                        distance_matrix.loc[i, k] + distance_matrix.loc[k, j],
                        distance_matrix.loc[i, j] or np.inf
                    )
    return distance_matrix

Question 10: Unroll Distance Matrix::

def unroll_distance_matrix(distance_matrix):
    unrolled_data = []
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:
                distance = distance_matrix.loc[id_start, id_end]
                unrolled_data.append([id_start, id_end, distance])
    unrolled_df = pd.DataFrame(unrolled_data, columns=['id_start', 'id_end', 'distance'])
    return unrolled_df


Question 11: Finding IDs within Percentage Threshold::

def unroll_distance_matrix(distance_matrix):
    unrolled_data = []
    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:
                distance = distance_matrix.loc[id_start, id_end]
                unrolled_data.append([id_start, id_end, distance])
    unrolled_df = pd.DataFrame(unrolled_data, columns=['id_start', 'id_end', 'distance'])
    return unrolled_df


Question 12: Calculate Toll Rate::

def calculate_toll_rate(df):
    df['moto'] = df['distance'] * 0.8
    df['car'] = df['distance'] * 1.2
    df['rv'] = df['distance'] * 1.5
    df['bus'] = df['distance'] * 2.2
    df['truck'] = df['distance'] * 3.6
    return df


Question 13: Calculate Time-Based Toll Rates::

import datetime

def calculate_time_based_toll_rates(df):
    df['start_day'] = 'Monday'  
    df['end_day'] = 'Sunday'    
    df['start_time'] = datetime.time(0, 0) 
    df['end_time'] = datetime.time(23, 59)  
    
    for i, row in df.iterrows():
        day = row['start_day']
        start_time = row['start_time']
        
        if day in ['Saturday', 'Sunday']:
            discount_factor = 0.7
        elif datetime.time(0, 0) <= start_time <= datetime.time(10, 0):
            discount_factor = 0.8
        elif datetime.time(10, 0) <= start_time <= datetime.time(18, 0):
            discount_factor = 1.2
        else:
            discount_factor = 0.8

        df.at[i, 'moto'] *= discount_factor
        df.at[i, 'car'] *= discount_factor
        df.at[i, 'rv'] *= discount_factor
        df.at[i, 'bus'] *= discount_factor
        df.at[i, 'truck'] *= discount_factor
    return df
