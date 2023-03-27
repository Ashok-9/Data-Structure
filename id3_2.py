import pandas as pd
import math
import numpy as np

# Step 1: Load the dataset
df = pd.read_csv('weather.csv')

# Step 2: Split the data into training and testing sets
train = df.sample(frac=0.7, random_state=1)
test = df.drop(train.index)

# Step 3: Define a function to calculate entropy
def entropy(data):
    target_col = data.keys()[-1]
    entropy = 0
    values = data[target_col].unique()
    for value in values:
        fraction = data[target_col].value_counts()[value]/len(data[target_col])
        entropy += -fraction*math.log2(fraction)
    return entropy

# Step 4: Define a function to calculate information gain
def information_gain(data, feature):
    target_col = data.keys()[-1]
    total_entropy = entropy(data)
    values = data[feature].unique()
    weighted_entropy = 0
    for value in values:
        subset = data[data[feature] == value]
        subset_entropy = entropy(subset)
        weighted_entropy += (len(subset)/len(data))*subset_entropy
    information_gain = total_entropy - weighted_entropy
    return information_gain

# Step 5: Define a function to recursively build the decision tree
def id3(data, original_data, features, target_attribute_name="play"):
    
    # base cases
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    elif len(data) == 0:
        return np.unique(original_data[target_attribute_name]).value_counts().index[0]
    elif len(features) == 0:
        return target_value
    
    # recursion
    else:
        target_value = np.unique(data[target_attribute_name]).value_counts().index[0]
        item_values = [information_gain(data, feature) for feature in features] # info gain for each feature
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        tree = {best_feature:{}}
        features = [i for i in features if i != best_feature]
        for value in np.unique(data[best_feature]):
            value = value
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = id3(sub_data, original_data, features, target_attribute_name)
            tree[best_feature][value] = subtree
        return(tree)

# Step 6: Build the decision tree using the ID3 algorithm
features = ['outlook', 'temperature', 'humidity', 'windy']
tree = id3(train, train, features)


