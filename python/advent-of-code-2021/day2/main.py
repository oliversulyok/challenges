def go_forward(position, length, aim):
    # print('before', position, aim, length, aim*length)
    position[0] += length
    position[1] += (aim * length)
    # print('after',position, aim, length)
    return position, aim


def go_backward(position, length, aim=0):
    position[0] -= length
    return position


def go_up(position, length, aim):
    # position[1] -= length
    aim -= length
    return position, aim


def go_down(position, length, aim):
    # position[1] += length
    aim += length
    return position, aim


directions = {
    'forward': go_forward,
    'backward': go_backward,
    'up': go_up,
    'down': go_down,
    }


def open_file(path):
    file = open(path, "r")
    output = []
    for el in file:
        output.append(el)
    return output


def iterate(direction, position, aim):
    for el in direction:
        el = el.split()
        position, aim = directions[el[0]](position, int(el[1]), aim)
    print(position)
    return position


def main():
    position = [0, 0]
    aim = 0
    direction = open_file("input.txt")
    position = iterate(direction, position, aim)
    print(position[0] * position[1])


if __name__ == "__main__":
    main()
