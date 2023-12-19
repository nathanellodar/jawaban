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
        print('Data berhasil ditambahkan!')
    def urutUsia(self):
        self.inorder(self._root)
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left())
            print(node.operator()['nama'], '-',node.operator()['usia'], 'tahun',end = ' ')
            print()
            self.inorder(node.right())

tree = BinaryTree()
while True:
    print('Pilih Menu:')
    print('1. Tambah Penduduk.')
    print('2. Tampilkan Urut Nama.')
    print('3. Tampilkan Urut Usia.')
    print('4. Exit.')
    pilihan_menu = input('Pilihan Anda: ')
    if pilihan_menu == '1':
        nama = input('Masukkan Nama: ')
        usia = int(input('Masukan Usia: '))
        data = {'nama' : nama, 'usia': usia}
        tree.add(data)
    elif pilihan_menu == '3':
        tree.urutUsia()
    else:
        break
