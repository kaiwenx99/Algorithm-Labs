class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def isNotEmpty(self):
        return len(self.items) > 0


class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        self.children = []

    def __repr__(self):
        return f"TreeNode('{self.contents}')"

    def addChildren(self, *contents):
        children = [TreeNode(c) for c in contents]
        self.children.extend(children)
        return children

    # **Part 1: DFS using Stack of Pairs**
    def dfs_stack_of_pairs(self):
        ans = []
        stack = Stack()
        stack.push([self, 0])

        while stack.isNotEmpty():
            node, index = stack.pop()
            if index == 0:
                ans.append(node.contents)
            
            if index < len(node.children):
                stack.push([node, index + 1])
                stack.push([node.children[index], 0])
        
        return ans

    # **Part 2: DFS with bad order (Children pushed in order, leading to reversed output)**
    def dfs_todos_badorder(self):
        ans = []
        stack = Stack()
        stack.push(self)

        while stack.isNotEmpty():
            node = stack.pop()
            ans.append(node.contents)
            for child in node.children:
                stack.push(child)  # Push all children (in order), causing a reversed traversal

        return ans

    # **Part 3: DFS with correct order**
    def dfs_todos_goodorder(self):
        ans = []
        stack = Stack()
        stack.push(self)

        while stack.isNotEmpty():
            node = stack.pop()
            ans.append(node.contents)
            for child in reversed(node.children):  # Reverse order to correct traversal
                stack.push(child)

        return ans


# **Tree Construction for Testing**
root1 = TreeNode("Z")
[Q, R, S] = root1.addChildren('Q', 'R', 'S')
[A, B, C] = Q.addChildren('A', 'B', 'C')
[D, E] = R.addChildren('D', 'E')
[F, G, H] = S.addChildren('F', 'G', 'H')
[T, U] = A.addChildren('T', 'U')
[W] = D.addChildren('W')
[X, Y] = G.addChildren('X', 'Y')
[J] = W.addChildren('J')

# **Correct DFS Orders**
correct_dfs = "Z Q A T U B C R D W J E S F G X Y H".split(' ')
weird_correct_dfs = "Z S H G Y X F R E D W J Q C B A U T".split(' ')

# **Test Part 1**
part1_ans = root1.dfs_stack_of_pairs()
print("\nPart 1 goal:   ", correct_dfs)
print("Part 1 actual: ", part1_ans)
print("Part 1 success:", part1_ans == correct_dfs)

# **Test Part 2**
part2_ans = root1.dfs_todos_badorder()
print("\nPart 2 goal:   ", weird_correct_dfs)
print("Part 2 actual: ", part2_ans)
print("Part 2 success:", part2_ans == weird_correct_dfs)

# **Test Part 3**
part3_ans = root1.dfs_todos_goodorder()
print("\nPart 3 goal:   ", correct_dfs)
print("Part 3 actual: ", part3_ans)
print("Part 3 success:", part3_ans == correct_dfs)
