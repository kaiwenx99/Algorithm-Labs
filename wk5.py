class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        self.parent = None
        self.children = []
      
    def __repr__(self):
        return f"TreeNode(contents={repr(self.contents)}, parent-contents={repr(self.parent.contents if self.parent else 'NOPARENT')}, num-children={len(self.children)})"

    def appendChild(self, contents):
        node = TreeNode(contents)
        node.parent = self
        self.children.append(node)
        return node

    def prependChild(self, contents):
        node = TreeNode(contents)
        node.parent = self
        self.children.insert(0, node)
        return node

    def findRoot(self):
        node = self
        while node.parent:
            node = node.parent
        return node

    def findLeftmostLeaf(self):
        node = self
        while node.children:
            node = node.children[0]
        return node

    def findRightmostLeaf(self):
        node = self
        while node.children:
            node = node.children[-1]
        return node

def case1():
    root = TreeNode("A")
    root.appendChild("B")
    root.appendChild("C")
    root.appendChild("D")

    print("\ncase1")
    print("I hope the root has 3 children")
    print(root)
    print("I hope the leftmost leaf is B, and B's parent is A")
    print(root.findLeftmostLeaf())
    print("I hope the rightmost leaf is D, and D's parent is A")
    print(root.findRightmostLeaf())

def case2():
    root = TreeNode("A")
    root.prependChild("C")
    root.appendChild("D")
    root.prependChild("B")

    print("\ncase2")
    print("I hope the root has 3 children")
    print(root)
    print("I hope the leftmost leaf is B, and B's parent is A")
    print(root.findLeftmostLeaf())
    print("I hope the rightmost leaf is D, and D's parent is A")
    print(root.findRightmostLeaf())

def case3():
    root = TreeNode("A")
    c = root.appendChild("C")
    d = root.appendChild("D")
    b = root.prependChild("B")
    g = d.prependChild("G")
    f = d.prependChild("F")
    e = b.appendChild("E")

    print("\ncase3")
    for node in [root, b, c, d, e, f, g]:
        r = node.findRoot()
        print("node:", node, "   found root:   ", r, "   is correct tho? ", r == root)

    print("findLeftmostLeaf of root, should be E:", root.findLeftmostLeaf())
    print("findLeftmostLeaf of D, should be F:", d.findLeftmostLeaf())
    print("findRightmostLeaf of D, should be G:", d.findRightmostLeaf())

def main(args):
    case1()
    case2()
    case3()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
