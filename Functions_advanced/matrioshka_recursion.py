smallest = 5


def find_hidden_matrioshkas(biggest, counting=0):
    if biggest > smallest:
        counting += 1
        return find_hidden_matrioshkas(biggest - 2, counting)
    return counting


print(find_hidden_matrioshkas(10))