h = int(input())
m = int(input())
s = int(input())
if (h >= 12):
    h -= 12
angle = (h * 30 + m / 2 + s / 120)
print(angle)
