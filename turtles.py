# Prints alternating facing turtles based on input. Bottom turtle always faces right. 176 bytes.
x=int(input())
for i in range(x):f=x-i;s=' ';u='_';print(s*f+u*((i+1)*2)+'\n'+s*(f-1)+'/,'+u*(i*2)+',\\o')if f%2==1 else print(s*f+u*((i+1)*2)+'\n'+s*(f-2)+'o/,'+u*(i*2)+',\\')