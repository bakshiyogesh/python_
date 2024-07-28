from array import *
def orderAgnosticBinarySearch():
    sorted_array=array("i",[25,22,21,19,18,16,14])
    target=16
    start=0
    end=len(sorted_array)-1
    is_ascending=sorted_array[start] < sorted_array[end]
    print(f"sorted_array {sorted_array}")
    while(start <= end):
        # print('inside the while loop')
        middle_item=start + ((end - start)//2)
        #print(f"middle_item {middle_item}")
        if target == sorted_array[middle_item]:
            print('yes')
            return middle_item
        if is_ascending:
            if target< sorted_array[middle_item]:
             start=middle_item-1
            elif target > sorted_array[middle_item]:
                end=middle_item+1
        else:
            print('inside else part')
            if target< sorted_array[middle_item]:
             start=middle_item+1
            elif target > sorted_array[middle_item]:
                end=middle_item-1
    return -1

answer=orderAgnosticBinarySearch()
print(f"answer returned {answer}")