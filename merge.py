print('Merge Sort!')

def merge_sort(array):
 
 if(len(array) < 2):
 	return array

 center = int(len(array)/2)

 left = array[:center]
 
 return left	


print(merge_sort([1, 2, 3, 4]))

print(merge_sort([1, 2, 3, 4, 5]))

print(merge_sort([1, 2]))

print(merge_sort([1]))
