def is_palindrome(s):
	"""A string is said to be palindrome if reverse of the string is same as string. 
	Return True if s is palindrome
	"""
	# Only change code below this line
	return all(s[i] == s[~i] for i in range(len(s))) 
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
 
test(is_palindrome(""), True, "Empty string")
test(is_palindrome("abc"), False, "Is not palindrome")
test(is_palindrome("abba"), True, "Is palindrome")

if ok:
	print("All tests passed")
