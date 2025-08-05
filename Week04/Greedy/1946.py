import sys
T = int(sys.stdin.readline())

case = []

for _ in range(T):
    N = int(sys.stdin.readline())
    applicants = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        applicants.append((a, b))
    case.append(applicants)






