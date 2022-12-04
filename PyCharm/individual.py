x = int(input())
y = int(input())
average = (x + y) / 2
T_diff = average - x
M_diff = average - y
print("average age: ", average)
print("Tanya: {0}\nMitya: {1}\n".format(abs(T_diff), abs(M_diff)))
