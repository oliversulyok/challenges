def calcMax(list):
    max_id, max_val = 0, 0
    for idx, el in enumerate(list):
        if el > max_val:
            max_val = el
            max_id = idx
    return max_val, max_id

def openFile(path, rw="r"):
    file = open(path, rw).read().splitlines()
    return file

def main():
    file_array = openFile("input.txt")
    elves = []
    semaphore = 1
    for i in file_array:
        if semaphore == 1:
            elves.append(int(i))
            semaphore = 0
        else:
            if i == '':
                semaphore = 1
            else:
                elves[len(elves)-1] += int(i)
    top3 = []
    ctr = 3
    top3_sum = 0
    while ctr != 0:
        max_val, max_id = calcMax(elves)
        print(max_val, max_id)
        elves.pop(max_id)
        top3.append(max_val)
        ctr-=1
    for i in top3:
        top3_sum += i
    print(top3_sum)

if __name__ == "__main__":
    main()

