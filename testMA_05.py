def count_words(text):
	"""Find quantities of each unique word in a text.
	Return list of tuples (word, count) sorted by counts"""
	# Only change code below this line
	list_tuples = []
	words = text.split()
	unique_words = set(words)
	print(words)
	for uw in unique_words:
	    quantities_uw = 0
	    for w in words:
	        if w == uw:
	            quantities_uw +=1
	    #list_tuples+= [(uw, quantities_uw)]
	    list_tuples.append((uw, quantities_uw))
	return sorted(list_tuples, key = lambda x: -x[1]) #, reverse = True)
	#return list_tuples.sort(key = lambda x: x[1])
	# .sort(key = 1) 
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
 
test(count_words(""), [], "Empty string")
test(count_words("a b c"), [('a', 1), ('b', 1), ('c', 1)], "Same frequencies")
test(count_words("a b a"), [('a', 2), ('b', 1)], "Different frequencies")
test(count_words("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum."""), 
[('in', 3), ('dolor', 2), ('ut', 2), ('dolore', 2), ('Lorem', 1), ('ipsum', 1),
('sit', 1), ('amet,', 1), ('consectetur', 1), ('adipiscing', 1), ('elit,', 1),
('sed', 1), ('do', 1), ('eiusmod', 1), ('tempor', 1), ('incididunt', 1), 
('labore', 1), ('et', 1), ('magna', 1), ('aliqua.', 1), ('Ut', 1), ('enim', 1),
('ad', 1), ('minim', 1), ('veniam,', 1), ('quis', 1), ('nostrud', 1), 
('exercitation', 1), ('ullamco', 1), ('laboris', 1), ('nisi', 1), 
('aliquip', 1), ('ex', 1), ('ea', 1), ('commodo', 1), ('consequat.', 1), 
('Duis', 1), ('aute', 1), ('irure', 1), ('reprehenderit', 1), ('voluptate', 1),
('velit', 1), ('esse', 1), ('cillum', 1), ('eu', 1), ('fugiat', 1), 
('nulla', 1), ('pariatur.', 1), ('Excepteur', 1), ('sint', 1), ('occaecat', 1), 
('cupidatat', 1), ('non', 1), ('proident,', 1), ('sunt', 1), ('culpa', 1),
('qui', 1), ('officia', 1), ('deserunt', 1), ('mollit', 1), ('anim', 1), 
('id', 1), ('est', 1), ('laborum.', 1)]
, "Real text")

if ok:
	print("All tests passed")
