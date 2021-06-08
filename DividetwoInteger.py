dividend = 1
divisor = 1
count = 0
sign = 0
if dividend < 0 or divisor < 0:
    sign = -1
else:
    sign = 1
newdivident = abs(dividend)
newdivisor = abs(divisor)
while newdivident >= newdivisor:
   newdivident = newdivident - newdivisor
   count +=1
print(count * sign)