def bubble_sort(items):
    '''
    Return array of items, sorted in ascending order
    the function bubbles up large items accordingly from largest to least largest
    arg:
    items (list) :
        list of items to be sorted in ascending order
    Return :
        gives a list of sorted items
    Example:
        >>> bubble_sort(['E','D','S','A'])
            ['A','D','E','S']
        >>> bubble_sort([3,7,2,3,1])
            [1,2,3,3,7]
    '''
    check = 0
    for i in range(len(items) -1 ) :
        if items[i+1] < items[i]:
            items[i],items[i+1] = items[i+1],items[i]
        else :
            check += 1
    if check != len(items) - 1:
        bubble_sort(items)
    return items

def merge_sort(items):
    '''
    Return array of items, sorted in ascending order
    the function split the items into single element then sort then by merging from the first element
    arg:
    items (list) :
        list of items to be sorted in ascending order
    Return :
        gives a list of sorted items
    Example:
        >>> merge_sort(['E','D','S','A'])
            ['A','D','E','S']
        >>> merge_sort([3,7,2,3,1])
            [1,2,3,3,7]
    '''
    if len(items) == 1:
        return items

    mid = len(items)//2
    item1 = merge_sort(items[:mid])
    item2 = merge_sort(items[mid:])
    return merge(item1,item2)
def merge(list1, list2):
    sorted_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            sorted_list.append(list1[0])
            list1.pop(0)
        else:
            sorted_list.append(list2[0])
            list2.pop(0)

    if len(list1) == 0:
        sorted_list = sorted_list + list2
    if len(list2) == 0:
        sorted_list = sorted_list + list1
    return sorted_list

def quick_sort(items):
    '''
    Return array of items, sorted in ascending order
    picks the last element as pivot
    arg:
    items (list) :
        list of items to be sorted in ascending order
    Return :
        gives a list of sorted items
    Example:
        >>> quick_sort(['E','D','S','A'])
            ['A','D','E','S']
        >>> quick_sort([3,7,2,3,1])
            [1,2,3,3,7]
    '''
    size = len(items)
    if size <= 1:
        return items

    pivot = items[-1]
    low = []
    high = []
    dup = []
    for i in items:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        elif i == pivot:
            dup.append(i)

    low = quick_sort(low)
    high = quick_sort(high)

    return low + dup + high
