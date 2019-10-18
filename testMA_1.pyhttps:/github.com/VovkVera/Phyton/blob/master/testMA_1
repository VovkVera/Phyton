def sum_list_items(l):
	"""Add the items of a list and return the result"""
	sum = 0
	for i in l:
	    sum += i
	return sum
	

ok = True


def test(x, y, msg):
	if x != y:
		print("Test failed:", msg)
		print("Actual result: ", x)
		print("Expected result: ", y)
		print("")
		global ok
		ok = False


test(sum_list_items([]), 0, "Empty list")
test(sum_list_items([1]), 1, "One item")
test(sum_list_items([1, 2, 3, 4]), 10, "Four items")

if ok:
	print("All tests passed")
