steps=8
path= "UDDDUDUU"
numValley =0
level=0
for step in path:
    if step=='U': 
        level+=1

    else:
        if level==0:
            numValley+=1
        level-=1

print(numValley)

    

