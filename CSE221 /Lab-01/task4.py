
inp = open("input4.txt",'r')
out = open("output4.txt" , "w")
f = inp.readlines()

coins, target = map(int, f[0].split())
line = f[1].split(" ")

coin_list = []
for count in line:
    coin_list.append(int(count))

coin_array = [0] + [float("inf")] * target

def Allocating_Coins(check, coin):
    for count in range(coin, len(check)):
        check[count] = min(check[count], check[count - coin] + 1)
    return check

for coin in coin_list:
    coin_array = Allocating_Coins(coin_array, coin)

def Minimum_Coins(a):
    if a[-1] == float("inf"):
        return -1
    else:
        return a[-1]

out.writelines(f"{Minimum_Coins(coin_array)}")

inp.close()
out.close()