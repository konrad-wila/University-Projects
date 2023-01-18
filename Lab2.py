#Task 1
def listed(file):
    arr = []
    try:
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                line = [float(x) for x in line.split(',')]
                arr.append(line)
            return arr
    except FileNotFoundError:
        print("File not found: %s" % file)


def printed(value):
    try:
        for i in range(len(value)):
            print(f"Miles {value[i][0]},£ {value[i][1]}")
    except Exception as e:
        print("Some error occurred", e)


# Task 2
def selectionSortDistance(values):
    try:
        for i in range(len(values)-1):
            min_pos = i
            for j in range(i+1, len(values)):
                if values[j][0] < values[min_pos][0]:
                    min_pos = j
            values[i], values[min_pos] = values[min_pos], values[i]
        return values
    except Exception as e:
        return f"Something went wrong {e}"
    except len(values) == 0:
        return f"The provided values are empty {values}"
# we can also use sort() function as values.sort(key=lambda x:x[0])


def selectionSortPrice(values):
    try:
        for i in range(len(values)-1):
            min_pos = i
            for j in range(i+1, len(values)):
                if values[j][1] < values[min_pos][1]:
                    min_pos = j
            values[i], values[min_pos] = values[min_pos], values[i]
        return values
    except Exception as e:
        return f"Something went wrong {e}"
    except len(values) == 0:
        return f"The provided values are empty {values}"
# we can also use sort() function as values.sort(key=lambda x:x[1])


if __name__ == "__main__":
    printed(listed("Tiny.txt"))
    print("Sorting according to Distance: ")
    printed(selectionSortDistance(listed("Tiny.txt")))
    print("Sorting according to Price: ")
    printed(selectionSortPrice(listed("Tiny.txt")))
    print(listed("Tiny.txt"))




