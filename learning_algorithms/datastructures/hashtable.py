from typing import List


def simple_hash_table():
	def _get_hash(k):
		return abs(hash(k)) % n

	n = 5
	hashtable = [None]*n
	k = "john"; v = "red"
	# hash val is i
	i = _get_hash(k)
	hashtable[i] = v
	print(hashtable)
	k = "will"; v = "yellow"
	i = _get_hash(k)
	hashtable[i] = v
	print(hashtable)


class Entry:
	def __init__(self, k, v):
		self.k = k
		self.v = v
		self.hash = hash(k)

	def equals(self, o):
		# compare hash first, if hash is different, the key must be different
		if self.o.hash != self.hash:
			return False
		# compare key only, since key is unique
		return self.k == o.key
	
	def __repr__(self):
		return f"Entry:{self.k}=>{self.v}"


class HashTableSeparatedChaining:
	def __init__(self, n):
		self.n = n
		# hashtable containing list of linkedlists (list)
		self._table: List[List[Entry]] = [None]*n
	
	def _normalize_index(self, key_hash):
		# convert hash value into index using modulo
		return abs(key_hash)%self.n
	
	def contains_key(self, k):
		i = self._normalize_index(hash(k))
		return self._bucket_seek_entry(i, k) != None

	def _bucket_seek_entry(self, i, k) -> Entry:
		if k == None: return None
		bucket = self._table[i]	# linked list
		if bucket == None: return None
		# find entry in linked list
		for e in bucket:
			if e.k == k: return e

	def put(self, k, v):
		if k == None: raise Exception("None key not allowed")
		# create new entry
		e = Entry(k, v)
		i = self._normalize_index(e.hash)
		bucket = self._table[i]

		# if no existing linkedlist already, create one
		if bucket == None:
			self._table[i] = bucket = []
		
		# find existing entry
		existing_entry = self._bucket_seek_entry(i, k)
		if existing_entry == None:
			# if no entry, add
			bucket.append(e)
			return None	# no previous entry
		else:
			# modify existing entry
			old = existing_entry.v
			existing_entry.v = e.v
			return old	# return old entry val

	def get(self, k):
		i = self._normalize_index(hash(k))
		return self._bucket_seek_entry(i, k).v



def main():
	# simple_hash_table()
	# for i in range(5):
	# 	print(hash("john"), hash("will"))


	h = HashTableSeparatedChaining(5)
	h.put("a", "b")
	h.put("b", "c")
	h.put("a", "c")
	assert h.contains_key("a")
	assert h.get("a") == "c"
	print(h._table)

main()