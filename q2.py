"""Write a function called all_false_in_dict_key_val(mydict)
that returns True if all keys and values of items is falsy, else return False

e.g. 
>>> all_false_in_dict_key_val({0:False, False:None, None:None})
True

>>> all_true_in_dict({1:"xx", "2": "ff", 3:0})
False

"""
def all_false_in_dict_key_val(mydict):
  for x, y in mydict.items():
      c = x or y
      print(x, y, c)
      if c: #if any key or value is truthy then return false 
        return False
      
  return True

dict_4 = {False: 1, False: 0, None: 0}
return_dict_4 = all_false_in_dict_key_val(dict_4)
print ("This returnsxxx:", return_dict_4)