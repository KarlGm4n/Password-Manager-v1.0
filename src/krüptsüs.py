from cryptography.fernet import Fernet
import base64
key = Fernet.generate_key()
bkey = base64.b64encode(key)
fernet = Fernet(key)

print("Sisesta programmi soovitav parool: ")
krmata = str(input())
krtud = fernet.encrypt(krmata.encode())

f = open("andmed.txt", "w")
f.write(str(bkey)+"\n")
f.write(str(krtud))
f.close()

deckey = base64.b64decode(bkey)

# print(deckey)
# print(key)
# print(bkey)
# print(krmata)
# print(krtud)