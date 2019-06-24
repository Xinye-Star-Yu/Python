def max_list_iter(int_list):  # must use iteration not recursion
	max = 0
	if int_list is None:
		raise ValueError
	if len(int_list) == 0:
		return None
	for integer in int_list:
		if integer > max:
			max = integer
	return max
			
def reverse_rec(int_list):   # must use recursion
	
	if int_list is None:
		raise ValueError
	if len(int_list) == 0:
		return []

	return int_list[-1:] + reverse_rec(int_list[:-1])
	
def bin_search(target, low, high, int_list):  # must use recursion
# searches for target in int_list[low..high] and returns index if found
# If target is not found returns None. If list is None, raises ValueError 
	if int_list is None:
		raise ValueError
	
	if low > high:
		return None
	
	middle = (high + low) // 2
	if target == int_list[middle]:
		return middle
	if target < int_list[middle]:
		return bin_search(target, low, middle - 1, int_list)
	return bin_search(target, middle + 1, high, int_list)
	
