p,q,s = input().split()

high = max(int(p),int(q))
low = min(int(p),int(q))
s = int(s)


highBlinks = set()
lowBlinks = set()

syncBlink = False

blinkTime = high
count = 1
while (blinkTime <= s):
    highBlinks.add(blinkTime)
    count += 1
    blinkTime = high * count
    
    

blinkTime = low
count = 1
while (blinkTime <= s):
    if blinkTime in highBlinks:
        # print("found match at", blinkTime)
        syncBlink = True
        break
    count += 1
    blinkTime = low * count
    

if syncBlink:
    print("yes")
else:
    print("no")