class StackUsingList():
    def __init__(self):
        self._list = []
        self._iter_index = -1

    def size(self):
        return len(self._list)

    def is_empty(self):
        return self.size() == 0

    def push(self, elem):
        self._list.append(elem)

    def pop(self):
        if self.is_empty(): raise IndexError()
        return self._list.pop()

    def peek(self):
        if self.is_empty(): raise IndexError()
        return self._list[self.size() - 1]

    def __repr__(self):
        return f"StackUsingList: {str(self._list)}"

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty() or self._iter_index == 0:
            raise StopIteration()
        if self._iter_index == -1:
            self._iter_index = self.size()
        x = self._list[self._iter_index - 1]
        self._iter_index -= 1
        return x


def brackets_problem_using_stack(s: str):
    """
	https://www.youtube.com/watch?v=L3ud3rXpIxA&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=8

	Logic:
	1. for each char found, get reversed char (e.g. [ -> ])
	2. if char is left bracket push char to stack
	3. if stack is empty while iterating on string, its invalid since first characeters found where right bracket
	4. if next char is right bracket, pop last char (i.e. left bracket) from stack.
			if popped last char (i.e. left bracket) is not equal to reverse of next char (i.e. right bracket), consider invalid

	Cases:
	[{}]][
	[]{}
	[[]][]
	[{[]}]
	[[]]{}({})
	"""
    l_to_r_bracket_map = {"[": "]", "{": "}", "(": ")"}
    r_to_l_bracket_map = {v: k for k, v in l_to_r_bracket_map.items()}
    stack = []
    s = list(s)
    statement = ""
    for c in s:
        # print('stack is', stack)
        rc = l_to_r_bracket_map.get(c) or r_to_l_bracket_map.get(c)
        if c in l_to_r_bracket_map:  # is left bracket
            stack = [c] + stack  # push into stack
        elif len(stack) == 0:
            # if stack is empty, it means first entry was right bracket which is invalid
            statement = "INVALID since right bracket found 1st"
            break
        else:
            # pop the last entry which should be a left bracket (from previous iteration)
            # and it should match reverse of right bracket (from current iteration)
            # to be valid, else return False
            if stack.pop(0) != rc:
                statement = "INVALID since left-right mismatch found"
                break

        if len(stack) == 0:
            statement = "VALID"
        else:
            statement = "INVALID" if not statement else statement

    print("stack", stack, statement)


def brackets_problem_failed_attempt():
    """solved by `brackets_problem_using_stack()`
	https://www.youtube.com/watch?v=L3ud3rXpIxA&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=8

	Logic:
	1. string must have even chars
	2. compare even char adjacent pairs - i.e. 1,2; 3,4; etc.
	3. compare 1st-last pairs - i.e. 1,6; 2,5; etc.
	[1,2,3,4,5,6]
	"""
    s = list("[[]]{}({})")  # this fails
    # s = list("[]{}")
    # s = list("[{()}]")
    # s = list("[{((}]")
    n = len(s)
    p1 = ["(", "[", "{"]
    p2 = [')', ']', '}']
    np = len(p1)
    assert n % 2 == 0, "string must be of even length"
    print("n", n)
    matched = [None] * n
    for i in range(n):
        # print(i, n-i-1)
        # if i % 2 == 0:
        # 	print(i, i+1)
        for j in range(np):
            if i % 2 == 0 and s[i] == p1[j] and s[i + 1] == p2[j]:
                matched[i] = s[i]
                matched[i + 1] = s[i + 1]
            elif s[i] == p1[j] and s[n - i - 1] == p2[j]:
                matched[i] = s[i]
                matched[n - i - 1] = s[n - i - 1]

    print(matched == s)


def main():
    # brackets_problem_failed_attempt()
    l = """[{}]][
	[]{}
	[[]][]
	[{[]}]
	[[]]{}({})"""
    # for s in l.splitlines():
    # 	brackets_problem_using_stack(s.strip())
    # brackets_problem_using_stack()
    s = StackUsingList()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.pop()
    print(s)
    assert s.peek() == 30
    for i in s:
        print(i)


main()
