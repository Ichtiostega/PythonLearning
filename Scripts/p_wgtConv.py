import myHeaders
myHeaders.printp("Weight Converter")

inWeight = input("Input your weight ")

wValue = int(inWeight.partition(" ")[0])
wType = inWeight.partition(" ")[2]

if wType.find("lbs") != -1:
    print(f"{wValue * 0.45} kg")
elif wType.find("kg") != -1:
    print(f"{wValue / 0.45} lbs")
else:
    print("No such thing")