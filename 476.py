a, b = map(int, input().split())

matrix = [[i * j for j in range(b)] for i in range(a)]

print(matrix)

