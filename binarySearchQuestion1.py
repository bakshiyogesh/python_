from array import *
def binarySearch():
    sorted_array=array("i",[2,3,5,9,14,16,18])
    target=15
    print(f"soreted_array {sorted_array}")
    target=int(input("Enter a number to search in list"))
    answer_after_search=binarySearchOutput(sorted_array,target)
    print(f"answer_after_search {answer_after_search}")
def binarySearchOutput(sortedArray,target):
    first_element=0
    last_element=len(sortedArray)
    print(last_element,sortedArray)
    print(f"last_element {last_element}")
    print(f"passed array {sortedArray}")
    while(first_element < last_element):
        middle_item=first_element + ((last_element - first_element)//2)
        if target == sortedArray[middle_item]:
            return sortedArray[middle_item]
        elif target< sortedArray[middle_item]:
             last_element=middle_item-1
        elif target > sortedArray[middle_item]:
            first_element=middle_item+1
    
    return -1

binarySearch()         

