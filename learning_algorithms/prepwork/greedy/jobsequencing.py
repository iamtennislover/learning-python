"""
jobsequencing = js
https://www.notion.so/ammul/3-Greedy-Method-39-45-21e266ae274c4aceb7e3b537f23f0cc7#a7c1cea92ea84365b33331e6258d2896
"""

def myjs(profits,deadlines,maxdeadline):
	"""my job sequencing implementation to find the job sequence with max profit

	Args:
		profits: list of profits
		deadlines: list of deadlines (NOTE: deadlines are 1-indexed, e.g. 1=1pm, 2=2pm, 0=invalid deadline)
		maxdeadline: int

	returns: list of indexes of job sequence in the sequence of jobs

	algo:
		1. store result in a list with indexes (slots).
			we can save some space here by not using 0/1 to avoid filling entire n space
		2. sort jobs in reverse order of profits. We need to remember the job id (lets call it given index)
			we can just use list of tuples (profit, index), but in production, i would use Class to represent a job
		3. because we need to fill high profit jobs with slots first, lets just
			iterate over the above list of sorted job,index and fill the slot
			NOTE: slots don't get filled in-order since based on deadline and profit,
			a job can be placed in later slot.
		4. the condition to check for each job:
			since a job's deadline == slot index,
			if job's deadline slot index isn't taken, fill it, else find later slot index
	
	Time complexity: O(nlogn)
	space complexity: O(n)
	"""
	n = len(profits)
	assert n == len(deadlines) # validate input
	assert 0 not in deadlines # deadlines are only 1-indexed

	# 1st sort profits in reverse order and remember the original index
	index_profits = [(i,p) for i,p in enumerate(profits)]
	sorted_profits = sorted(index_profits, key=lambda e: e[1], reverse=True)
	print("sorted_profits", sorted_profits)

	# make deadline 0-indexed
	deadlines = [d-1 for d in deadlines]	

	# fill with empty slots
	slots = [None]*maxdeadline

	for e in sorted_profits:
		if None not in slots:	# if all slots are filled, skip any lower profit jobs
			break

		currentjobi = e[0]

		# for each current job, try assigning the job to the slot on the same deadline
		# and if slot is taken, go to previous slot
		currentslot = deadlines[currentjobi]	# == deadline of current job
		print(f"currentslot=deadlines[{currentjobi}]={currentslot}")
		while currentslot >= 0: # fill until we reached beginning of slots
			if slots[currentslot] == None:	# if slot is empty, fill it
				print(f"filling slot {currentslot} with job{currentjobi}")
				slots[currentslot] = currentjobi
				break	# stop when slot is filled by job
			else:
				currentslot -= 1	# go to previous slot and check again

	return slots


def test_js():
	testcases = [
		# profits, deadlines, maxdeadline, expected
		([20,15,10,5,1], [2,2,1,3,3], 3, [1,0,3]),
		([35,30,25,20,15,12,5], [3,4,4,2,3,1,2], 4, [3,2,0,1]),
		([100,19,27,25,15],[2,1,2,1,3],3,[2,0,4]) # https://www.geeksforgeeks.org/job-sequencing-problem/
	]
	for profits,deadlines,maxdeadline,expected in testcases:
		jobsequence = myjs(profits,deadlines,maxdeadline)
		# print("result", jobsequence, expected, jobsequence == expected)
		assert jobsequence == expected

def main():
	test_js()

main()
