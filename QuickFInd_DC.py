nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def union(i, j):
    ithvalue = nodes[i]
    jthvalue = nodes[j]
    nodes[j] = ithvalue
    for item in range(0,len(nodes)):
        if nodes[item] == jthvalue:
            nodes[item] = ithvalue


def createpath():
    union(4, 3)
    union(3, 8)
    union(6, 5)
    union(9, 4)
    union(2, 1)
    union(5, 0)
    union(7, 2)
    union(1, 0)


def connected(i, j):
    if nodes[i] == nodes[j]:
        return True
    else:
        return False

createpath()
print(nodes)

print(connected(0, 7))
print(connected(8, 9))
print(connected(0, 9))