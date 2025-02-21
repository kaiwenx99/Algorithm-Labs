from pt1 import LLN

def reverse(lln):
    prev = None
    current = lln
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # New head of the reversed list


def main():
    first = LLN("one")
    second = first.insertAfter("two")
    third = first.findLast().insertAfter("three")
    fourth = first.findLast().insertAfter("four")

    print("before we reverse the list, starting at first:", first.toList())
    newBegin = reverse(first)
    print("now that we have reversed, the list from first is very short:", first.toList())
    print("but the list from the new beginning is longer:", newBegin.toList())
    print("and since newBegin is fourth, here it is again:", fourth.toList())


if __name__ == "__main__":
    main()
