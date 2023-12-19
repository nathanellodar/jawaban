class Node:
    def __init__(self, data, parent):
        self._data = data
        self._parent = parent
        self._left = None
        self._right = None

    def insert(self, data):
        if data['usia'] < self.operator()['usia']:
            if self.left() is None:
                self._left = Node(data, self)
            else:
                self.left().insert(data)
        elif data['usia'] > self.operator()['usia']:
            if self.right() is None:
                self._right = Node(data, self)
            else:
                self.right().insert(data)
        else:
            return False 
        return True 

    def operator(self):
        return self._data

    def left(self):
        return self._left

    def right(self):
        return self._right


class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0
    def add(self, data):
        if self._root is None:
            self._root = Node(data, None)
            self._size += 1
        else:
            if self._root.insert(data):
                self._size += 1
    def nodes(self):
        self.inorder(self._root)
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left())
            print(node.operator(), end = ' ')
            print()
            self.inorder(node.right())

# class Penduduk:
#     def __init__(self):
#         self._nama = None
#         self._usia = None
#     def setNamaUsia(self, nama, usia):
#         self._nama = nama
#         self._usia = usia

data1 = {'nama' : 'Thane', 'usia' : 12}
data2 = {'nama' : 'Ani', 'usia' : 40}
data3 = {'nama' : 'Vina', 'usia' : 30}

tree = BinaryTree()
tree.add(data1)
tree.add(data2)
tree.add(data3)
data = tree
print()
print(type(data))
