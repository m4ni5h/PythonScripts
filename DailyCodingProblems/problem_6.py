class Node:
    def __init__(self, data):
        self.data = data
        self.both = id(data)

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self, node):
        self.head = node
        self.tail = node
        self.head.both = 0
        self.tail.both = 0

    def add(self, element):
        self.tail.both ^= id(element.data)
        element.both = id(self.tail.data)
        self.tail = element

    def get(self, index):
        prev_node_address = 0
        result_node = self.head
        for i in range(index):
            next_node_address = prev_node_address ^ result_node.both
            prev_node_address = id(result_node.both)
            result_node = dict_map[next_node_address]
        return result_node.data


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

dict_map = dict()
dict_map[id("a")] = a
dict_map[id("b")] = b
dict_map[id("c")] = c
dict_map[id("d")] = d
dict_map[id("e")] = e

link_list = LinkedList(a)
link_list.add(b)
link_list.add(c)
link_list.add(d)
link_list.add(e)

assert link_list.get(0) == "a"
assert link_list.get(1) == "b"
assert link_list.get(2) == "c"
assert link_list.get(3) == "d"
assert link_list.get(4) == "e"