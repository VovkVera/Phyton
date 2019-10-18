def get_3_lagest(l):
	"""Find 3 the largest items from a list"""
	# Only change code below this line
	if len(l)<3: return l
	else:
	    l.sort() #(reverse=True)
	return l[-3:len(l)]
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
 
test(get_3_lagest([]), [], "Empty list")
test(get_3_lagest([1, 2]), [1, 2], "Only 2 items")
test(get_3_lagest([3, 2, 1, 5, -1, 7, 3, 8]), [5, 7, 8], "More than 3 items")

if ok:
	print("All tests passed")
