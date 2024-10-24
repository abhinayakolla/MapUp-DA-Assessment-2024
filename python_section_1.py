PYTHON SECTION-1::

1) REVERSE A LIST BY N ELEMENTS::

def reverse_list_by_n(lst, n):
    result = []
    for i in range(0, len(lst), n):
        group = lst[i:i+n] 
        if len(group) < n:
            result.extend(reversed(group))
        else:
            result.extend(reversed(group))
    return result
print(reverse_list_by_n([1, 2, 3, 4, 5, 6, 7, 8], 3))  
print(reverse_list_by_n([1, 2, 3, 4, 5], 2))           
print(reverse_list_by_n([10, 20, 30, 40, 50, 60, 70], 4)) 

2) LIST& DICTIONARIES::

def group_strings_by_length(strings):
    length_dict = {}
    for string in strings:
        length = len(string)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(string)
    return dict(sorted(length_dict.items()))
print(group_strings_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))

3) FLATTEN A NESTED DICTIONARY::

def flatten_dictionary(nested_dict):
    def flatten(current_dict, parent_key='', sep='.'):
        items = {}
        for k, v in current_dict.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten(v, new_key, sep=sep))
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    items.update(flatten({f"[{i}]": item}, new_key, sep=sep))
            else:
                items[new_key] = v
        return items
    return flatten(nested_dict)
input_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}
print(flatten_dictionary(input_dict))

4) GENERATE UNIQUE PERMUTATIONS::

from itertools import permutations
def unique_permutations(lst):
    return list(map(list, set(permutations(lst))))
print(unique_permutations([1, 1, 2]))


5) FIND ALL DATES IN A TEXT::

import re
def find_all_dates(text):
    date_patterns = [
        r'\b\d{2}-\d{2}-\d{4}\b',  
        r'\b\d{2}/\d{2}/\d{4}\b',  
        r'\b\d{4}\.\d{2}\.\d{2}\b'  
    ]
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))
    return dates
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
print(find_all_dates(text))



6)  DECODE POLYLINE , COVERT TO DATAFRAME:: 

import pandas as pd
import polyline
import numpy as np
def decode_polyline_to_df(polyline_str):
    coordinates = polyline.decode(polyline_str)
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])
    df['distance'] = 0.0
    for i in range(1, len(df)):
        lat1, lon1 = df.loc[i-1, 'latitude'], df.loc[i-1, 'longitude']
        lat2, lon2 = df.loc[i, 'latitude'], df.loc[i, 'longitude']
        lat1, lon1, lat2, lon2 = map(lambda x: x * (np.pi / 180), [lat1, lon1, lat2, lon2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (np.sin(dlat / 2)**2 +
             np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2)
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        distance = 6371 * c  # Radius of Earth in kilometers
        df.loc[i, 'distance'] = distance 

    return df
polyline_str = 'u{~nF~zqQfAv@f@Jg@Nm@L{D?b@Jg@f@g@l@g@r@c@l@e@jA'  # Valid polyline string
print(decode_polyline_to_df(polyline_str))


7)  MATRIX ROTATION AND TRANSFORMATION::D
    
    def rotate_and_transform_matrix(matrix):
    n = len(matrix)
    rotated_matrix = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
    transformed_matrix = [[0]*n for _ in range(n)]  
    for i in range(n):
        for j in range(n):
            row_sum = sum(rotated_matrix[i])
            col_sum = sum(rotated_matrix[k][j] for k in range(n))
            transformed_matrix[i][j] = row_sum + col_sum - rotated_matrix[i][j]
    return transformed_matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_and_transform_matrix(matrix))


8)  TIME CHECK::

import pandas as pd
def check_time_completeness(df):
    print("Column names:", df.columns)
    df.columns = df.columns.str.strip()
    expected_columns = ['startDay', 'startTime', 'endDay', 'endTime']
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing columns: {missing_columns}")
        return None  # Exit if required columns are missing
    df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])    
    def check_group(group):
        start_times = group['start'].dt.time
        end_times = group['end'].dt.time
        return (start_times.min() <= pd.to_datetime('00:00:00').time() and 
                end_times.max() >= pd.to_datetime('23:59:59').time())
    result = df.groupby(['id', 'id_2']).apply(check_group)  
    return result
df = pd.read_csv(r"C:\Users\honey chowdary\OneDrive\Desktop\dataset-2.csv")
print(check_time_completeness(df))





