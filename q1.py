
# Learning truthy/falsy
"""
In python if MYVARIABLE is a truthy variable, then 
that if statement is True and hence that if block runs.

e.g. 
if MYVARIABLE:
  print("MYVARIABLE is TRUTHY")
else:
  print("MYVARIABLE is NOT TRUTHY")

MYVARIABLE is considered truthy if the variable's content is not any of the following:
- 0
- None
- False
- []
- {}
- ()

"""

"""Write a function called all_true_in_dict_val(mydict)
that returns True if all values of items is truthy, else return False

e.g. 
>>> all_true_in_dict_val({1:"xx", "2": "ff"})
True

>>> all_true_in_dict_val({1:"xx", "2": "ff", 3:0})
False

"""
def all_true_in_dict_val(mydict):
  values = mydict.values() # [0]
  for i in values:  # i = 0 first time
    if not i:
      return False

  return True

dict_2 = {1:"xx", 2: None}
return_this_dict_2 = all_true_in_dict_val(dict_2)
print ("This is the return of the dict",return_this_dict_2 )

#dict_3= {1:"xx", 2: 0}
dict_3= {2: 3, 4:5, 66:{}}
return_this_dict_3 = all_true_in_dict_val(dict_3)
print ("This is the return of the dict",return_this_dict_3)




