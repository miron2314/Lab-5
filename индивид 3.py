r=range(300)
for b in r:
    for k in r:
        for t in r:
            if b+k+t==100 and 20*b+10*k+t==200:
                print (f"{b} бык, {k} коров,{t} телят")
