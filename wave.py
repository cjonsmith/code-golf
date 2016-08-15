# Given a string with 0 or more spaces terminated by a period, print an
# additional space at the beginning.  Or, if the string is a repitition of
# slashes, print the next one in the pattern. 83 characters.
i=input()
if '.' in i:print(' '+i)
else:print(i+'\\')if i[-1]=='/'else print(i+'/')