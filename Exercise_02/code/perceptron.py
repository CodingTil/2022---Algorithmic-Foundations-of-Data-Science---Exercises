from matplotlib import pyplot

S = [
    ((2, 1), -1),
    ((-1, 3), 1),
    ((-3, 1), 1),
    ((-2, -1), 1),
    ((-1, -5), -1),
    ((2, -3), -1),
]


def plot(S, w):
    # scatter points
    x_values = [s[0][0] for s in S]
    y_values = [s[0][1] for s in S]
    colors = ['green' if s[1] == 1 else 'red' for s in S]

    pyplot.scatter(x_values, y_values, c=colors)

    # plot linear seperator
    x_min = min(x_values)
    x_max = max(x_values)
    y_min = min(y_values)
    y_max = max(y_values)

    ortho_w = (-w[1], w[0])

    p_1 = (x_min, ortho_w[1] * (x_min / ortho_w[0]))
    p_2 = (x_max, ortho_w[1] * (x_max / ortho_w[0]))
    p_3 = (ortho_w[0] * (y_min / ortho_w[1]), y_min)
    p_4 = (ortho_w[0] * (y_max / ortho_w[1]), y_max)

    p_x_values = (p_1[0], p_2[0], p_3[0], p_4[0])
    p_y_values = (p_1[1], p_2[1], p_3[1], p_4[1])

    pyplot.plot(p_x_values, p_y_values)

    # save to file
    pyplot.savefig('perceptron.png')


def sgn(value) -> int:
    if value > 0:
        return 1
    elif value == 0:
        return 0
    else:
        return -1


def dot_product(a, b) -> int:
    return a[0] * b[0] + a[1] * b[1]


def check_consistency(S, w) -> bool:
    for s in S:
        if sgn(dot_product(s[0], w)) != s[1]:
            return False
    return True


def perceptron(S) -> tuple:
    w = (0, 0)
    while not check_consistency(S, w):
        for s in S:
            if sgn(dot_product(s[0], w)) != s[1]:
                w_old = w
                # w <- w + yx
                w_x = w[0] + s[1] * s[0][0]
                w_y = w[1] + s[1] * s[0][1]
                w = (w_x, w_y)
                # printing formatted for latex. Just copy and paste
                print(f'Updating vector $w={w_old}$ using $(x,y)={s}$ \\\\')
                print(
                    f'$w={w} \\rightarrow w={w_old} + y={s[1]} * x={s[0]}$ \\\\ \n\\bigskip \n')
    return w


if __name__ == '__main__':
    w = perceptron(S)
    plot(S, w)
