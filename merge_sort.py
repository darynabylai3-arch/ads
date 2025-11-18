def merge_sort(arr):
    if len(arr)>1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0 

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i+=1
                k+=1
            else: 
                arr[k] = right[j]
                j+=1
                k+=1

        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j<len(right):
            arr[k] = right[j]   
            j+=1
            k+=1

    
arr1 = [ 1, 43,4 ,2,422 ,52,5,2,42,32,2]
merge_sort(arr1)
print(arr1)