import pandas as pd

labels_dict = {'very low':0, 'low':1, 'med':2, 'high':3, 'very high':4}

mean_labels = []
median_labels = []

csv_input = pd.read_csv("discretized_dataset.csv")

for i in range(0,len(csv_input)):
    mean_cat = csv_input['mean_groups'][i]
    median_cat = csv_input['median_groups'][i]
    mean_labels.append(labels_dict[mean_cat])
    median_labels.append(labels_dict[median_cat])
    
csv_input['LABELLED_MEAN'] = mean_labels
csv_input['LABELLED_MEDIAN'] = median_labels
    
csv_input = csv_input.drop('mean_groups', axis = 'columns')
csv_input = csv_input.drop('median_groups', axis = 'columns')

csv_input.to_csv('labelled_dataset.csv', index=False)