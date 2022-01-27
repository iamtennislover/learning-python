# Q6. is_palendrome. 2 pts.

# Implement the following function according to specification.

"""Returns True if the text is a palendrome, which is to say it
    reads the same backwards and forwards. Spaces and lettercase are ignored.

    Assumes no punctation in text.

    Examples:
    >>> is_palendrome('madam')
    True
    >>> is_palendrome('Nurses run')
    True
    >>> is_palendrome('xyz')
    False
    """
def lower(s):
  lowers = s.lower()
  return lowers

def reverse(s): 
  return s[::-1] 
  
def is_palendrome(s): 
    # Calling reverse function 
    rev = reverse(s)
    lows = lower(s)
    lowr = lower(rev)
  
    s1 = lows.replace(" ", "")
    r1 = lowr.replace(" ", "")
    # Checking if both string are equal or not
    print("s is: ", s) 
    print("rev is: ", rev) 
    print("lows is: ", lows) 
    print("lowr is: ", lowr) 
    print("s1 is: ", s1)
    print("r1 is: ", r1) 
    if (s1 == r1): 
        return True

    return False

#word = 'madam'
#check = is_palendrome(word)
#print ("This is a palindrome", check)


word = 'Nurses run'
check = is_palendrome(word)
print ("This is a palindrome", check)
  