from copy import deepcopy

def find_missing(input):
    length = len(input)
    if length <= 0:
        return -1

    myInput = deepcopy(input)
    myInput.sort()
    i = 0
    while i < length-1:
        curr = myInput[i]
        next = myInput[i+1]
        if next != curr+1:
            return curr+1
        i = i+1

    # all there
    return -1


def main():
    input = [3,7,1,2,8,4,5]
    missing = find_missing(input)
    print("input array: " + str(input))
    print('missing number: %d' % missing)


if __name__ == "__main__":
    main()

