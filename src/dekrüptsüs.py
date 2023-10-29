from cryptography.fernet import Fernet
import base64

f = open("andmed.txt", "r")
bkey = str(f.readline())
bkey = bkey.strip()
bkey = bkey[2:-1]
# print("bkey: " + bkey)
krtud = f.readline()
krtud = krtud.strip()
krtud = krtud[2:-1]
# print("krtud: " + krtud)
f.close()

key = base64.b64decode(bkey)
fernet = Fernet(key)
krmata = fernet.decrypt(krtud.encode()).decode()

# print(bkey)
# print(key)
# print(krmata)
# print(krtud)

print("Sisesta parool: ")
par = str(input())
if krmata==par:
    print("Õige parool!")
else:
    print("Vale parool!")

# import base64
# string = 'data to be encoded'
# data = base64.b64encode(string.encode())
# print(data)