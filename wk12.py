def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort(seq):
    if len(seq) <= 1:
        return  # already sorted

    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid:]

    # Sort both halves
    mergesort(left)
    mergesort(right)

    # Merge sorted halves and update original list
    merged = merge(left, right)
    for i in range(len(seq)):
        seq[i] = merged[i]
