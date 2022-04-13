from math import sqrt
#from statistics import mode

training_set = [
    ((-4, -2.1, -1), -1),
    ((-3.6, -1.4, 0.2), 1),
    ((1, -0.2, -0.3), 1),
    ((0.3, -0.5, -0.5), 1),
    ((-2, -3.5, -1), -1),
    ((-4.2, -4, 0.2), 1),
    ((-1.3, -0.1, -3), 1),
    ((-0.7, 0.9, -0.7), 1),
    ((1, 2, 1.4), 1),
    ((2.6, -1.5, 0.2), 1),
    ((2, 4.3, -0.7), -1),
    ((0.6, 0.4, 0.2), -1),
    ((2.9, -1.7, 3.6), -1),
    ((3.6, 0.4, -2.5), -1),
    ((1.2, 4, 1.2), -1),
    ((-1, 0.5, 0.5), -1),
    ((3, 2.7, 2.3), -1),
    ((4, -3, 2.2), -1),
    ((0.1, 0.1, 3.5), -1),
    ((2.8, 1.2, 2.4), -1)
]

test_set = [
    (1, -2, 0),
    (4, -0.5, 2),
    (1, 1.5, -2.5),
    (-2, -1, -2),
    (-4, -1, -1)
]


def manhattan_distance(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i] - y[i])
    return sum


def euclidean_distance(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(len(x)):
        sum += pow(x[i] - y[i], 2)
    sum = sqrt(sum)
    return sum


def get_k_nearest_neighbors(training_set, test, k, distance_func):
    assert callable(distance_func)
    distances = list()
    for data in training_set:
        distance = distance_func(data[0], test)
        distances.append((data, distance))
    distances.sort(key=lambda x: x[1]) # sort by distance
    neighbors = list()
    for i in range(k): # get data of k nearest neighbors
        neighbors.append(distances[i][0])
    return neighbors


def predict_classificataion(training_set, test, k, distance_func):
    assert callable(distance_func)
    neighbors = get_k_nearest_neighbors(training_set, test, k, distance_func)
    classifications = [neighbor[1] for neighbor in neighbors] # list of all classifications
    #prediction = mode(classifications) # get classification most often in k nearest neighbors
    #return prediction
    count_neg = classifications.count(-1)
    count_pos = classifications.count(1)
    assert count_neg + count_pos == k
    if count_pos > count_neg:
        return 1
    if count_pos < count_neg:
        return -1
    if count_pos == count_neg:
        return 0


if __name__ == '__main__':
    print('Classification: k=2 Manhattan Distance')
    for test in test_set:
        prediction = predict_classificataion(
            training_set, test, 2, manhattan_distance)
        print(f'Test {test}: Prediction {prediction}')
    print('\n')
    print('Classification: k=3 Manhattan Distance')
    for test in test_set:
        prediction = predict_classificataion(
            training_set, test, 3, manhattan_distance)
        print(f'Test {test}: Prediction {prediction}')
    print('\n')
    print('Classification: k=2 Euclidean Distance')
    for test in test_set:
        prediction = predict_classificataion(
            training_set, test, 2, euclidean_distance)
        print(f'Test {test}: Prediction {prediction}')
    print('\n')
    print('Classification: k=3 Euclidean Distance')
    for test in test_set:
        prediction = predict_classificataion(
            training_set, test, 3, euclidean_distance)
        print(f'Test {test}: Prediction {prediction}')
