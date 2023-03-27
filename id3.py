import pandas as pd
import numpy as np
import math

# Load dataset
data = pd.read_csv('weather.csv')

# Define function to calculate entropy
def calculate_entropy(df):
    # Get target variable values
    values = df['play'].unique()
    
    # Calculate entropy
    entropy = 0
    for value in values:
        probability = len(df[df['play'] == value]) / len(df)
        entropy += -probability * math.log2(probability)
    
    return entropy

# Define function to calculate information gain
def calculate_information_gain(df, attribute):
    # Calculate overall entropy
    entropy = calculate_entropy(df)
    
    # Calculate entropy for each value of the attribute
    values = df[attribute].unique()
    attribute_entropy = 0
    for value in values:
        subset = df[df[attribute] == value]
        subset_entropy = calculate_entropy(subset)
        attribute_entropy += len(subset) / len(df) * subset_entropy
    
    # Calculate information gain
    information_gain = entropy - attribute_entropy
    
    return information_gain

# Define ID3 algorithm
def id3(df, attributes, target_attribute):
    # Create root node
    root = {}
    
    # If all examples are positive, return a leaf node with label = "play"
    if len(df[df['play'] == 'yes']) == len(df):
        root['label'] = 'yes'
        return root
    
    # If all examples are negative, return a leaf node with label = "not play"
    elif len(df[df['play'] == 'no']) == len(df):
        root['label'] = 'no'
        return root
    
    # If there are no more attributes to split on, return a leaf node with the majority label
    elif len(attributes) == 0:
        root['label'] = df['play'].value_counts().idxmax()
        return root
    
    # Otherwise, find the attribute with the highest information gain
    else:
        information_gains = []
        for attribute in attributes:
            information_gain = calculate_information_gain(df, attribute)
            information_gains.append(information_gain)
        best_attribute_index = np.argmax(information_gains)
        best_attribute = attributes[best_attribute_index]
        
        # Create a new node with the best attribute
        root['attribute'] = best_attribute
        root['children'] = []
        
        # Recursively split on the best attribute
        values = df[best_attribute].unique()
        for value in values:
            subset = df[df[best_attribute] == value]
            if len(subset) == 0:
                child = {'label': df['play'].value_counts().idxmax()}
            else:
                new_attributes = [x for x in attributes if x != best_attribute]
                child = id3(subset, new_attributes, target_attribute)
            root['children'].append((value, child))
    
    return root

# Run ID3 algorithm on 'weather.csv' dataset
attributes = ['outlook', 'temperature', 'humidity', 'windy']
target_attribute = 'play'
tree = id3(data, attributes, target_attribute)
print(tree)


# tree = {'attribute': 'outlook',
#         'children': [('sunny',
#                       {'attribute': 'humidity',
#                        'children': [('high',
#                                      {'label': 'no'}),
#                                     ('normal',
#                                      {'label': 'yes'})]}),
#                      ('overcast',
#                       {'label': 'yes'}),
#                      ('rainy',
#                       {'attribute': 'windy',
#                        'children': [(False,
#                                      {'label': 'yes'}),
#                                     (True,
#                                      {'label': 'no'})]})]}