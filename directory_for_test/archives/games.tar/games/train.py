# for i in range(16):

#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)
#     width = 5


print("-"*15)

for num in range(0,1000,5):
    print(f"{chr(num)} - {chr(num+1)} - {chr(num+2)} - {chr(num+3)} - {chr(num+4)} - {chr(num+5)}")
    print(num)
    

