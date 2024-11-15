import hashlib

metin = input("Bir metin giriniz: ")
metin = bytes(metin, "UTF8")

hashNesnesi = hashlib.sha1(metin)
hashDegeri = hashNesnesi.hexdigest()

print(hashDegeri)