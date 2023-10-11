import math
from collections import defaultdict
x=[]
def main():
    with open('input.txt.txt', 'r') as input_file, open('output5.txt', 'w') as output_file:
        d = defaultdict(lambda: [])
        num_cases = int(input_file.readline().strip())

        for case_number in range(1, num_cases + 1):
            n = int(input_file.readline().strip())

            x = []
            flag = True
            ans = False
            ii = 0

            while True:
                xx = []
                s = 41
                i = 41 - ii
                ii += 1

                if i < 0:
                    break

                nn = n

                while i > 1:
                    if nn % i == 0 and s - i >= 0:
                        while nn % i == 0:
                            xx.append(i)
                            nn = nn // i
                            s -= i

                        if s < 0:
                            break

                        if s == 0 and nn != 1:
                            break

                        if nn == 1:
                            ans = True
                            x.append(xx)
                            l = len(xx)
                            ss = sum(xx)
                            output_file.write(f"Case #{case_number}: {l + 41 - ss} ")
                            for _ in range(41 - ss):
                                output_file.write("1 ")
                            for i in range(l):
                                if i == l - 1:
                                    output_file.write(str(xx[i]) + '\n')
                                else:
                                    output_file.write(str(xx[i]) + ' ')
                            flag = False
                            break
                    i -= 1

                if flag == False:
                    break

            if ans == False:
                output_file.write(f"Case #{case_number}: -1\n")

if __name__ == "__main__":
    main()
