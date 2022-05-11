import numpy as np

q_1 = 3 * np.log(2)
q_2 = 5 * np.log(2)
q_3 = 3 * np.log(2)

Q = np.array([q_1, q_2, q_3])


def exp3(gamma=0.5, t=3, n=3) -> str:
    log = ''

    # rows = action, columns = s
    w = np.matrix([np.ones(t+1) for i in range(n)])

    for s in range(t):
        log += f'Iteration s={s+1} of {t}: \n\n'
        log += f'Weights:\n'
        for a in range(n):
            log += f'\tw_{a+1}^{s+1} = {round(w[a,s], 2)}\n'

        log += f'\nProbabilities:\n'
        # calculate probabilities
        P = np.zeros(n)
        for a in range(n):
            P[a] = (1 - gamma) * (w[a, s])/(np.sum(w[:, s])) + (gamma / n)
            log += f'\tp_{a+1}^{s+1} = {round(P[a], 2)}\n'

        # select action
        action_s = s

        # get reward for action_s
        q = Q[action_s]

        # update weights
        for a in range(n):
            if a == action_s:
                w[a, s+1] = w[a, s] * np.exp((gamma * q) / (n * P[a]))
            else:
                w[a, s+1] = w[a, s]

        log += '\n'

    log += f'\nFinal Weights:\n'
    for a in range(n):
        log += f'\tw_{a+1}^{t+1} = {round(w[a,t], 2)}\n'

    return log


if __name__ == '__main__':
    log = exp3()

    logfile = open('exercise_05_output.txt', 'w')
    logfile.write(log)
    logfile.close()
