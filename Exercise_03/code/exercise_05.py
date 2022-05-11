import numpy as np
from copy import deepcopy

def exp3(gamma, rounds, actions, rewards):
    weights = np.ones((len(actions)))
    rounds_arr = [i for i in range(rounds)]
    n = len(actions)
    # for tracking weights and probabilities
    weights_tracking = {}
    probabilities_tracking = {}
    weights_tracking[0] = np.ones(len(actions))
    probabilities_tracking[0] = probability_dist(weights, gamma)
    for round, action in zip(rounds_arr, actions):
        probabilities = probability_dist(weights, gamma)
        probabilities_tracking[round] = probabilities
        reward = rewards[action]
        weights = update_weights(weights, reward, probabilities, action, gamma)
        weights_tracking[round + 1] = deepcopy(weights)

    probabilities_tracking[rounds] = probability_dist(weights, gamma)
    return weights_tracking, probabilities_tracking

def probability_dist(weights, gamma):
    return (1 - gamma) * (weights / np.sum(weights)) + gamma / len(weights)

def update_weights(weights, reward, probabilities, action, gamma):
    n = len(weights)
    # only update chosen action
    weights[action] = weights[action] * np.exp((gamma * reward) / (n * probabilities[action]))
    return weights


action_seq = np.array([ 1, 2, 3 ])
rewards = np.array([ 3, 5, 3 ]) * np.log(2)

weights, probs = exp3(gamma=0.5, rounds=3, actions=action_seq - 1, rewards=rewards)

print(f'Probabilities: \n')
for key, val in probs.items():
    print(f'Round:\t{key + 1}\tProbabilities:\t{val.round(2)}')

print(f'\nWeight vectors: \n')
for key, val in weights.items():
    print(f'Round:\t{key + 1}\tWeights:\t{val.round(2)}')