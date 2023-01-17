#Task 1
def listed(file):
    arr = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            line = [float(x) for x in line.split(',')]
            arr.append(line)
        return arr


def printed():
    a = listed("Tiny.txt")
    for i in range(len(a)):
        print(f"Miles {a[i][0]},£ {a[i][1]}")


print(listed("Tiny.txt"))
printed()

# Task 2