class FPTree(object):
    def __init__(self, root=None):
        '''
        :param root: `FPTreeNode` instance which is the root element
        '''
        if root is None:
            self.root = FPTreeNode()
        else:
            self.root = root

    def __iter__(self):
        '''
        a breadth first search iterator for the tree
        '''
        to_visit = [self.root]
        for node in to_visit:
            to_visit.extend(node.children.values())
            yield node

    def insert_transaction(self, transaction):
        '''
        :param transaction: It is a list of items to be inserted into
        '''
        current = self.root
        for item in transaction:
            if current.has_child(item):
                current = current.get_child(item)
                current.count += 1
            else:
                new_node = current.add_child(item)
                current = new_node

    def __str__(self):
        str_ = ''
        for node in self:
            str_ = str_ + "\n%s -> %s" % (node.item, node.children.keys())
        return str_


class FPTreeNode(object):
    def __init__(self, item=None):
        self.children = {}
        if item is None:
            self.count = 0
            self.item = '{root}'
            self._root = True
        else:
            self.count = 1
            self.item = item
            self._root = False

    def has_child(self, item):
        '''
        return if the current node has a child with given item
        '''
        return item in self.children

    def get_child(self, item):
        '''
        get the child with the given item, raise a `KeyError` otherwise
        '''
        return self.children[item]

    def add_child(self, item):
        '''
        create a child of the current node with the following item, raises a
        `ValueError` if a child exists with the given item.
        '''
        if item not in self.children:
            child = FPTreeNode(item)
            self.children[item] = child
            return child
        else:
            raise ValueError

    def __str__(self):
        return "(%s: %s)" % self.item, self.count
