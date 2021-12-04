from time import perf_counter


def open_file(path):
    file = open(path, "r")
    output = []
    for el in file:
        output.append(el)
    return output


def make_decision(array):
    final_list = []
    for idx, el in enumerate(array):
        el = int(el)
        if idx > 0:
            tmp = el - final_list[idx - 1][0]
            if tmp < 0:
                final_list.append((el, 'decreased'))
            else:
                final_list.append((el, 'increased'))
        else:
            final_list.append((el, 'N/A'))
    return final_list


def count(array, what='increased'):
    counted_elements = 0
    for el in array:
        if el[1] == what:
            counted_elements += 1
    return counted_elements


def set_flags(array, start_chr=97, size=3):
    i = iter(array)
    win = []
    for e in range(0, size):
        win.append(next(i) + (chr(start_chr),))
    yield win
    for e in i:
        win = win[1:] + [e + (chr(start_chr),)]
        yield win


def main():
    t1_start = perf_counter()
    file_array = open_file("input.txt")
    final_list = make_decision(file_array)
    count_elements = count(final_list)
    flagging = set_flags(final_list)

    for i in flagging:
        print(i)

    print(count_elements)

    t1_stop = perf_counter()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the whole program in seconds:",
          t1_stop - t1_start)
    # for (i=0; i<f.length; i++) {
    #
    #     }


if __name__ == "__main__":
    main()
