# Given a string a number, repeat the string `number` amount of times. If the first
# and last characters of the string are the same character, do not repeat the
# characters. 44 bytes.
lambda x,y:x*y if x[0]!=x[-1] else x+x[1:]*y
