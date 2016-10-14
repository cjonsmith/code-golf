"""Takes two words sperated by a comma and space. 

If the words are anagrams of each other, print True. 54 bytes.

Idea to save functions to variable from: 
http://codegolf.stackexchange.com/a/1314/60037 
Saved 1 byte
"""
x=input().split(', ');S=sorted;print(S(x[0])==S(x[1]))
