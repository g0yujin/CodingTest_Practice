dial = {3: "ABC", 4: "DEF", 5: "GHI", 6: "JKL", 7: "MNO", 8: "PQRS",
        9: "TUV", 10:"WXYZ"}

word = input()
time = 0

for i in word:
    for key, value in dial.items():
        if i in value:
            time += key
print (time)