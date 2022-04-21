# Roll::    21CS60A01
# Name: AGNIK SAHA
# Assignment number: 2

import numpy as np

import csv
with open('project2.csv', 'r') as read_obj: 
    csv_reader = csv.reader(read_obj) 
    training_data  = list(csv_reader)

def y_values(rows):
    ys = []  
    for row in rows:
        label = row[-1]
        ys.append(label)
    return ys

ys = y_values(training_data)
label = ys[1:]

def train_data(rows):
    training_data = []
    for row in rows:
        info = row[:-1]
        training_data.append(info)
    return training_data

xs = train_data(training_data)
xs = xs[1:]

dataset = []
for row in xs:
    row = [float(i) for i in row]
    dataset.append(row)


def distance(instance1, instance2):
    instance1, instance2 = np.array(instance1), np.array(instance2)
    return np.sqrt(sum((instance1 - instance2)**2))


def get_neighbors(training_set, test_instance, k):
    distances = [(i, distance(test_instance, instance)) for i, instance in enumerate(training_set)]
    distances.sort(key=lambda x: x[1])
    return [i[0] for i in distances[:k]]

def make_prediction(neighbor_index, label):
    label = np.array(label)
    neighbor_label = label[neighbor_index]
    prediction = {}
    for x in neighbor_label:
        if x in prediction:
            prediction[x] += 1
        else:
            prediction[x] = 1
    total = sum(prediction.values())
    probability_prediction = {k: v/total for k, v in prediction.items()}
    return probability_prediction

def knn_classifier(training_set, label, test_set, k):
    result = []
    for instance in test_set:
        neighbor_index = get_neighbors(training_set, instance, k)
        prediction = make_prediction(neighbor_index, label)
        result.append(max(prediction, key=prediction.get))
    return np.array(result)

with open('project2_test.csv', 'r') as read_obj: 
    csv_reader = csv.reader(read_obj) 
    test_data  = list(csv_reader)

test_data = test_data[1:]

test = []
for row in test_data:
    row = [float(i) for i in row]
    test.append(row)

outputs = []

k = int(input("Enter the value of k: "))
for i in range(0,len(test)):
    outputs.append(knn_classifier(dataset, label, [test[i]], k))

f = open("21CS60A01_p2.out", "w")
for val in outputs:
    f.write(val[0]+ " ")

f.close()