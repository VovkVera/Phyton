def get_unique_items(l):
	"""Return unique items from a list"""
	# Only change code below this line
	return list(set(l))
	# Only change code above this line


ok = True
 
def test(x, y, msg):
	if x != y:
		print("Test failed:", msg)
		print("Actual result: ", x)
		print("Expected result: ", y)
		print("")
		global ok
		ok = False
 
test(get_unique_items([]), [], "Empty list")
test(get_unique_items([1, 2, 3]), [1, 2, 3], "All uniques")
test(get_unique_items([1, 1, 2, 2]), [1, 2], "List with duplicates")

if ok:
	print("All tests passed")
