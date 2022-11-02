a = float(input())
b = float(input())
c = float(input())

d = (b ** 2) - 4 * a * c

if a == 0:
    print("Nilai a tidak boleh sama dengan 0")
elif d < 0:
    print("Tidak memiliki akar real")
else:
    x1 = (-b + d ** (1 / 2)) / (2 * a)
    x2 = (-b - d ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))