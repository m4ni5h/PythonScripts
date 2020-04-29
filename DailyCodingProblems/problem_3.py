import json


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def serialise(root):
    if not root:
        return None

    serial_tree_map = dict()
    serial_left = serialise(root.left)
    serial_right = serialise(root.right)

    serial_tree_map['data'] = root.data
    if serial_left:
        serial_tree_map['left'] = serial_left
    if serial_right:
        serial_tree_map['right'] = serial_right

    return json.dumps(serial_tree_map)


def deserialise(serialized_object):
    serial_tree_map = json.loads(serialized_object)
    node = Node(serial_tree_map['data'])
    if 'left' in serial_tree_map:
        node.left = deserialise(serial_tree_map['left'])
    if 'right' in serial_tree_map:
        node.right = deserialise(serial_tree_map['right'])
    return node

# a
# left(b left (d) right(e))
# right (c left (f) right(g))
node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
node_g = Node('g')
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

a = serialise(node_a)
print(a)

d_a = deserialise(a)
assert str(d_a) == "a"
