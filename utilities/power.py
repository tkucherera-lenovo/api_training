import csv
import os 

file = os.path.abspath('/opt/api_training/utilities/cluster_power.csv')

#file = '/opt/api_training/utilities/cluster_power.csv'


def get_node_total_power(node):
    time = ""
    with open(file, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            if node == row[1]:
                return (row[0], row[-1])


