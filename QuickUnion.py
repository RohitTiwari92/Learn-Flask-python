nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def root(i):
    print("in root OL : " + str(i) + "," + str(nodes[i]))
    while i != nodes[i]:
        i=nodes[i]
        print("in root in Loop : "+ str( i )+ "," + str(nodes[i]) )
    return i

def union(p,q):
    print("u req pq : "+ str(p) +" , " + str(q))
    i=root(p)
    j=root(q)
    print("u req ij: " + str(i) + " , " + str(j))
    nodes[i]=j
    print(nodes)

def connected(i,j):
    return root(i)==root(j)

def createpath():
    union(4, 3)
    union(3, 8)
    union(6, 5)
    union(9, 4)
    union(2, 1)
    union(5, 0)
    union(7, 2)
    union(1, 0)


createpath()
print(nodes)

print(connected(0, 7))
print(connected(8, 9))
print(connected(0, 9))