inp = open("input3.txt" ,'r')
out = open("output3.txt", "w")
f = inp.readlines()

steps = int(f[0])
store = [None]*(steps+2)
store[0] = 0
store[1] = 1

for count in range(len(store)):
    if count <= ((len(store))-3):
        store[count+2] = store[count] + store[count+1]
    else:
        break
# print(store)
out.writelines(f"{store[-1]}")

inp.close()
out.close()