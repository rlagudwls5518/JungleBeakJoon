#직사각형에서 탈출

x, y, w, h = map(int, input().split())

result = min(x, y, w - x, h - y)
print(result)