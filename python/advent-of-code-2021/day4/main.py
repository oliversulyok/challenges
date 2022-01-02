#bingo game
class bingoTable:
    def __init__(self):
        self.table = [5][5]

def open_file(path):
    file = open(path, "r")
    output = []
    for el in file:
        output.append(el)
    return output

def main():
    parsed_input = open_file("input.txt")


if __name__ == "__main__":
    main()