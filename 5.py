arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Node:
    def _init_(self, data, izq, der):
        self.data = data
        self.izq = izq
        self.der = der

def printAll(node):
    if node is not None:
        print(node.data)
        printAll(node.izq)
        printAll(node.der)

nodeList = []
for i in range(len(arr)):
    node = Node(arr[i], None, None)
    nodeList.append(node)

if len(nodeList) > 0:
    for i in range(int(len(arr)/2)-1):
        if nodeList[2*i + 1].izq is None:
            nodeList[i].izq = nodeList[2*i+1]
        if nodeList[2*i + 2].der is None:
            nodeList[i].der = nodeList[2*i +2]
    lastIdx = int(len(arr)/2) - 1
    nodeList[lastIdx].izq = nodeList[lastIdx * 2 +1]
    if len(arr) % 2 == 1:
        nodeList[lastIdx].der = nodeList[lastIdx * 2 + 2]

if _name_ == '_main_':
    if nodeList is not None:
        printAll(nodeList[0])