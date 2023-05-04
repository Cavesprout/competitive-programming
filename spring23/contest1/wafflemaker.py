rate, duration = input().split()

rate = 180 / int(rate)
duration = int(duration)

endpos = (rate * duration) % 360

if (endpos > 90 and endpos < 270):
    print("down")
else:
    print("up")

print(endpos)