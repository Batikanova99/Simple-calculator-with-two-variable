def topla(a,b):
	sonuc = a + b
	return sonuc

def cikar(a,b):
	sonuc = a - b
	return sonuc

def bol(a,b):
	sonuc = a / b
	return sonuc

def carp(a,b):
	sonuc = a * b
	return sonuc

def main(a,b):
	
	islem = input("Topla, Çıkar, Böl, Çarp:")

	if islem == "topla":
		sonuc = topla(a,b)
		print(sonuc)


	elif islem == "cikar":
		sonuc = cikar(a,b)
		print(sonuc)

	elif islem == "bol":
		sonuc = bol(a,b)
		print(sonuc)

	elif islem == "carp":
		sonuc = carp(a,b)
		print(sonuc)

	return sonuc
	
while True:
	a = float(input("1.sayiyi giriniz:"))
	b = float(input("2.sayiyi giriniz:"))
	sonuc = main(a,b)
	