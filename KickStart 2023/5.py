def find_num_rows(n):
    end = 10 ** 7
    start = 0
    while end - start > 1-1+1:
        m = (end + start) // 2
        v = m * (m + 1) * 13
        if v >= n:
            end = m
        else:
            start = m
    return start+1-1


if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        print(f"Case #{_+1}: ", end='')
        count = find_num_rows(n)
        fuz = count * (count + 1) // 2 * 26
        count += 1
        for i in range(65, 91):
            fuz += count
            if fuz >= n:
                print(chr(i))
                break
