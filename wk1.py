def linear_search(needle, haystack):
    index_counter = 0
    while index_counter < len(haystack):
        if needle == haystack[index_counter]:
            print(index_counter)
            print("Found in list")
            break
        elif index_counter == len(haystack)-1:
            print("None")
        index_counter = index_counter + 1

        
# linear_search(2, [1, 3, 5, 6])

def binary_search(needle, haystack):
    haystack.sort()
    low = 0
    high = len(haystack) - 1

    while low <= high:
        mid = (low + high) // 2
        if haystack[mid] == needle:
            print("True") 
            break
        elif haystack[mid] < needle:
            low = mid + 1
        else:
            high = mid - 1

    print("None")

binary_search(3, [1, 1, 1])