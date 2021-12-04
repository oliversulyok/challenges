def open_file(path):
    file = open(path, "r")
    output = []
    for el in file:
        output.append(el)
    return output


def iterate_over(array):
    result = {}
    for el in array:
        for idx, value in enumerate(el):
            if value in ['1', '0']:
                value = int(value)
                if idx not in result:
                    result[idx] = [value]
                else:
                    result[idx].append(value)
    return result


def calculate_binary_elements(array):
    result = {}
    for k, el in array.items():
        final_value = 0
        for idx, i in enumerate(el):
            final_value += i
        result[k] = [final_value, idx+1]
    return result


def decide_bits(array, common_bit='most'):
    result = 0
    bit = 1 if common_bit == 'most' else 0
    for k, el in array.items():
        result += (bit << k)
        if el[0] <= 500:
            result = result ^ (1 << k)
        print(bin(result))
    return result


def main():
    report = open_file("input.txt")
    binary_notation = iterate_over(report)
    most_common_bits = calculate_binary_elements(binary_notation)
    print(most_common_bits)
    most_bits = decide_bits(most_common_bits, common_bit='most')
    least_bits = decide_bits(most_common_bits, common_bit='least')
    print(most_bits*least_bits)

if __name__ == "__main__":
    main()