"""test.assert_equals(number([[10,0],[3,5],[5,8]]),5)
test.assert_equals(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
test.assert_equals(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)
"""

def number(bus_stops):
    sleepers = 0
    for i in range(len(bus_stops)):
        sleepers+= bus_stops[i][0]-bus_stops[i][1]
    return sleepers

print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
