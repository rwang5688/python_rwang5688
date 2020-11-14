def find_sum_of_two(A, val):
    length = len(A)
    if length < 2:
        return False

    i = 0
    while i < length:
        curr = A[i]
        diff = val - curr
        if diff in A:
            diff_index = A.index(diff)
            if diff_index != i:
                return True
        i = i + 1

    # no sum of two exists
    return False


def main():
    A = [5,7,1,2,8,4,3]
    val = 10
    exists = find_sum_of_two(A, val)
    print("For A=" + str(A) + ", val=" + str(val))
    print("sum of two exists: " + str(exists))

    A = [5,7,1,2,8,4,3]
    val = 19
    exists = find_sum_of_two(A, val)
    print("For A=" + str(A) + ", val=" + str(val))
    print("sum of two exists: " + str(exists))

    A = [5,7,1,2,8,4,3]
    val = 2
    exists = find_sum_of_two(A, val)
    print("For A=" + str(A) + ", val=" + str(val))
    print("sum of two exists: " + str(exists))


if __name__ == "__main__":
    main()

