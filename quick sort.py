from random import randrange

def quick_sort(array):

    def partition(array, start, finish):
        pivot = array[start]

        less = [element for element in array[start+1:finish+1] if element < pivot]
        greaterequal = [element for element in array[start+1 :finish+1] if element >= pivot]
        new_array = less +  [pivot] + greaterequal

        for i in range(start+1, finish +1):
            array[i] = new_array.pop(0)

        return start + len(less)

    def quick_sort_rec(array, start, finish):
        if start < finish:
            pos = partition(array, start, finish)
            quick_sort_rec(array, start, pos-1)
            quick_sort_rec(array,pos+1,finish)

    quick_sort_rec(array, 0, len(array)-1)

ar = [randrange(100) for i in range(20)]
print(ar)
quick_sort(ar)
print(ar)
