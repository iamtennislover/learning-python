"""
https://www.notion.so/ammul/3-Greedy-Method-39-45-21e266ae274c4aceb7e3b537f23f0cc7#a7c1cea92ea84365b33331e6258d2896
"""

class ItemValue:
  
    """Item Value DataClass - https://www.geeksforgeeks.org/fractional-knapsack-problem/?ref=rp"""
  
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt
  
    def __lt__(self, other):
        return self.cost < other.cost
  
    def __repr__(self):
        return f"ItemValue:i={self.ind}:w={self.wt}:c={self.cost}"
  
# Greedy Approach
  
  
class FractionalKnapSack:
  
    """Time Complexity O(n log n)"""
    @staticmethod
    def getFilledSackWithIndexes(wt, val, capacity):
        """function to get maximum value - https://www.geeksforgeeks.org/fractional-knapsack-problem/?ref=rp"""
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))
  
        # sorting items by value
        iVal.sort(reverse=True)
  
        totalValue = 0
        s = [0]*len(iVal)
        print(f"values: {iVal}")
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
                s[i.ind] = 1
            else:
                fraction = round(capacity / curWt, 2)
                s[i.ind] = fraction
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return s


def myknapsack(pl,wl,mw,af):
	"""
	pl: profits list
	wl: weights list
	mw: max weight (int)
	af: allow fraction (bool)

	returns: list of ints, where int is 1/0 or fraction
	to indicate whether elem/object was added or not in the index of elem

	Logic:
		1. find profit to weight ratio for all objs
		2. sort in reverse order of ratio
		3. use result to store list of elems with their ratio: 1-added, 0-not added
		3. for each obj, until max weight >= weight in result, add obj
	"""
	print(f"given profit,wt,i: {list(zip(pl, wl, range(len(pl))))}\nmax-weight: {mw}")
	n = len(pl)
	assert n == len(wl)
	
	rl = [] # ratio list stores index of object in sorted order, 1st being highest ratio
	for i in range(n):
		r = pl[i]//wl[i] # ratio
		rl.append((r,i))
	# NOTE: This is okay to be used in interview as long as i can implement it using previously discussed sorting algo
	rl = sorted(rl, key=lambda e: e[0], reverse=True)
	
	s = [0]*n # resulting sack list
	print(rl)
	
	currenttotalw = 0
	for r,currenti in rl:
		if currenttotalw + wl[currenti] > mw:
			if af:
				leftoverw = mw - currenttotalw
				currenttotalw += leftoverw
				s[currenti] = round(leftoverw/wl[currenti], 2)
			break

		s[currenti] = 1
		currenttotalw += wl[currenti]
	print(currenttotalw)
	return s


def test_knapsack():
	testcases = (
		# profits, weights, max weight, allow fraction, expected allocation
		([10,5,15,7,6,18,3],
		 [2, 3, 5,7,1, 4,1],
		 15, True,
		 [1, 0.67, 1, 0, 1, 1, 1]),
		([5,20,3],
		 [1, 2, 3],
		 2, True,
		 [0.0,1,0]),
		([5,20,3],
		 [1, 2, 3],
		 2, False,
		 [0,1,0]),
		([2,3,4,10],
		 [1,2,1,2],
		 5, True,
		 [1,0.5,1,1]),
	)
	for pl,wl,mw,af,expected in testcases:
		r = myknapsack(pl,wl,mw,af)
		r2 = FractionalKnapSack.getFilledSackWithIndexes(wl,pl,mw)
		assert (r == expected == r2)


def main():
	test_knapsack()

main()
