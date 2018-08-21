print('Merge Sort!')

def merge_sort(array):
	if(len(array) < 2):
		return array

	center = int(len(array)/2)
	
	left = array[:center]

	right = array[center:]
 
	return merge( merge_sort(left), merge_sort(right))




def merge(left_array, right_array):
	result, left_indx, right_indx = [], 0, 0

	while(left_indx < len(left_array) && right_indx < len(right_array)):

		if(left_array[left_indx] < right_array[right_indx]):

			result.append(left_array[left_indx])

			left_indx += 1
		else:
			result.append(right_array[right_indx])

			right += 1	






print(merge_sort([1, 2, 3, 4]))

print(merge_sort([1, 2, 3, 4, 5]))

print(merge_sort([1, 2]))

print(merge_sort([1]))
