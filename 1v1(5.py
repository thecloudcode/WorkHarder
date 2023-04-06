# # cook your dish here
T = int(input())
for i in range(T):
    Pa, Pb, Qa, Qb = map(int,input().split())
    if Pa<Qa and Pb<Qb:
        print("P")
    elif Pa>Qa and Pb>Qb:
        print("Q")
    else:
        print("TIE")
# cook your dish here
# T = int(input())
# for i in range(T):
#     Pa, Qa, Pb, Qb = map(int,input().split())
#     Pm = max(Pa, Pb)
#     Qm = max(Qa, Qb)
#     if Pm>Qm:
#         print("Q")
#     elif Pm == Qm:
#         print("TIE")
#     else:
#         print("P")