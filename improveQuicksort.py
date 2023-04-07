from statistics import median
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        first = lst[0]
        middle = lst[len(lst)//2]
        last = lst[-1]
        pivot = median([first, middle, last])
        
        left = []
        right = []
        pvt = []
        
        for element in lst:
            if element < pivot:
                left.append(element)
            elif element > pivot:
                right.append(element)
            else:
                pvt.append(element)
        
        return quicksort(left) + pvt + quicksort(right)
    
def main():
    lst = [5,3,6,3,5,3,7,8,5,3,1,5,7,4]
    print(quicksort(lst))
    

main()