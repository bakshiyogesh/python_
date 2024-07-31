from array import *


def insertion_sort():
    arr=array("i",[5,4,3,1,2])
    for i in range(0,len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j] < arr[j-1]:
                swap(arr,j,j-1)
            else:
                break
    return arr

def swap(array,first_index,second_index):
    # print(f"first index :{first_index} second index:{second_index}")
    temp=array[first_index]
    array[first_index]=array[second_index]
    array[second_index]=temp

answerafter=insertion_sort()
print(f"Answer after sorting {answerafter}")