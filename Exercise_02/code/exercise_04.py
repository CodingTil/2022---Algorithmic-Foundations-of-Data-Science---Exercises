from math import sqrt
from matplotlib import pyplot

X = [
    (-3, 5),
    (-2, 4),
    (-1, 2),
    (-4, 0),
    (1, -2),
    (2, 0),
    (2, 1),
    (3, 5),
]

Z = [X[0], X[1], X[2]] # a+b
#Z = [X[0], X[7], X[3]] # d

def plot(C, Z, k=3):
    colors = ['red', 'green', 'blue']
    for j in range(k):
        x_values = [cj[0] for cj in C[j]]
        y_values = [cj[1] for cj in C[j]]
        pyplot.scatter(x_values, y_values, c=colors[j])
        pyplot.scatter([Z[j][0]], [Z[j][1]], marker='x', c=colors[j])

    # save to file
    pyplot.savefig(f'exercise_04.png')


def equals_list_of_lists(C_1, C_2) -> bool:
    ll_1 = list([set(l_1) for l_1 in C_1])
    ll_2 = list([set(l_2) for l_2 in C_2])
    for l_1 in list(ll_1):
        for l_2 in list(ll_2):
            if l_1 == l_2:
                ll_1.remove(l_1)
                ll_2.remove(l_2)
                break

    return len(ll_1) == 0 and len(ll_2) == 0


def dot_product(a, b) -> float:
    return a[0] * b[0] + a[1] * b[1]


def k_means(X, Z, k=3) -> tuple:
    C = [[] for j in range(k)]
    C_ = list(C) # copy of C_
    first_iteration = True
    while not equals_list_of_lists(C, C_) or first_iteration:
        first_iteration = False
        C = list(C_)
        C_ = [[] for j in range(k)]

        print(f'Clusters: {C} \\\\')
        print(f'Centres: {Z} \\\\\n')

        for x in X:
            distances = list()
            for j in range(k):
                # x_i - z_j
                tmp = (x[0] - Z[j][0], x[1] - Z[j][1])
                distances.append((j, sqrt(dot_product(tmp, tmp))))
            # get min j
            min_distance = float('inf')
            min_j = float('inf')
            for d in distances:
                j = d[0]
                distance = d[1]
                if distance < min_distance:
                    min_distance = distance
                    min_j = j
                elif distance == min_distance and j < min_j:
                    min_j = j
            # add x_i to C_j
            C_ = [C_[j] if j != min_j else C_[j] + [x] for j in range(k)]
        # update z_j
        Z = [(sum([x[0] for x in C_[j]])/len(C_[j]), sum([x[1] for x in C_[j]])/len(C_[j])) if len(C_[j]) != 0 else Z[j] for j in range(k)]
    return (C_, Z)


if __name__ == '__main__':
    (C, Z) = k_means(X, Z, k=3)
    print(f'Final Clusters: {C} \\\\')
    print(f'Final Centers: {Z} \\\\\n')
    plot(C, Z, k=3)
