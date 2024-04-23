from Node import Node
a = Node(0)
b = Node(10)
a.setLink(b)
d = Node(12)

c = a.listPart(a, d)
print(c[0])