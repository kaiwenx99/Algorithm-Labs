class DLLN:
    def __init__(self, contents):
        self.contents = contents
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"DLLN({repr(self.contents)})"

    def insertAfter(self, contents):
        new_node = DLLN(contents)
        new_node.next = self.next
        new_node.prev = self
        if self.next:
            self.next.prev = new_node
        self.next = new_node
        return new_node

    def insertBefore(self, contents):
        new_node = DLLN(contents)
        new_node.next = self
        new_node.prev = self.prev
        if self.prev:
            self.prev.next = new_node
        self.prev = new_node
        return new_node

    def toList(self):
        values = []
        current = self
        while current:
            values.append(current.contents)
            current = current.next
        return values

    def findLast(self):
        current = self
        while current.next:
            current = current.next
        return current

    def findFirst(self):
        current = self
        while current.prev:
            current = current.prev
        return current

    def findAfter(self, needle):
        current = self.next
        while current:
            if current.contents == needle:
                return current
            current = current.next
        raise KeyError(needle)

    def findBefore(self, needle):
        current = self.prev
        while current:
            if current.contents == needle:
                return current
            current = current.prev
        raise KeyError(needle)


def main():
    one = DLLN("one")
    two = one.insertAfter('two')
    print("should be one two:", one.toList())

    five = one.findLast().insertAfter('five')
    print("should be one two five:", one.toList())

    three = two.insertAfter('three')
    print("should be one two three five:", one.toList())

    zero = one.insertBefore('zero')
    print("should be zero one two three five:", one.findFirst().toList())

    four = one.findAfter('five').insertBefore('four')
    print("should be zero one two three four five:", one.findFirst().toList())

    the_two = one.findFirst().findAfter('two')
    print("should successfully find two:", the_two)

    the_two = one.findLast().findBefore('two')
    print("should successfully find two:", the_two)

    print("should fail to find two:")
    try:
        print(two.findBefore('two'), "this should not print")
    except KeyError as ke:
        print("KEY ERROR", ke)


if __name__ == "__main__":
    main()
