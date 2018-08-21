print('Merge Sort!')

def merge_sort(array):
 
 if(len(array) < 2):
 	return array

 center = round(len(array)/2, 0) 
 
 return center	


print(merge_sort([1, 2, 3, 4]))

print(merge_sort([1, 2, 3, 4, 5]))

print(merge_sort([1, 2]))

print(merge_sort([1]))
