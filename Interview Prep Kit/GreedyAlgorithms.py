def min_max(l, k):
    """Given a list of integers, l, and a single integer k, find a list of length k from elements of l such
    that its unfairness is minimized. Call that array sub_l. Unfairness of an array is calculated as
    max(sub_l)-min(sub_l)"""
    l.sort()
    unfairness = -1
    for i in range(0, len(l)-k+1):
        sub_list_unfairness = l[i+k-1] - l[i]
        if sub_list_unfairness < unfairness or unfairness < 0:
            unfairness = sub_list_unfairness

    return unfairness


def get_minimum_cost(k, c):
    c.sort()
    minimum_cost = 0
    multiply_factor = 1
    while c:
        minimum_cost += multiply_factor * sum(c[-k:])
        c = c[:-k]
        multiply_factor += 1

    return minimum_cost


assert(get_minimum_cost(3, [1, 3, 5, 7, 9]) == 29)


def minimum_absolute_difference(arr):
    min_difference = abs(arr[0] - arr[1])
    for i in range(2, len(arr)):
        for j in range(0, i):
            if abs(arr[i] - arr[j]) < min_difference:
                min_difference = abs(arr[i] - arr[j])
    return min_difference


print(minimum_absolute_difference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))


def minimum_absolute_difference_using_sort(arr):
    arr.sort()
    min_difference = abs(arr[0] - arr[1])
    for i in range(2, len(arr)):
        if abs(arr[i-1] - arr[i]) < min_difference:
            min_difference = abs(arr[i-1] - arr[i])
    return min_difference


print(minimum_absolute_difference_using_sort([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
