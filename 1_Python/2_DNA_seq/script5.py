#verilen diziyi 3'er 3'er gruplayan program yazınız.
#örnek: AGCTATAGT
#       AGC TAT AGT

#fonksiyon tanımlama
def grupla(dizi):
    gruplar = []
    for i in range(0,len(dizi),3):
        gruplar.append(dizi[i:i+3])
    return gruplar

#ana program
dna_dizisi = "AGCTATAGT"
gruplar = grupla(dna_dizisi)

# Baska nasil yapabiliriz?
# Mesela list comprehension ile nasil yazilabilir?
# range fonksiyonunun 3. parametresi nedir?
# append fonksiyonu nedir?
# dizi[i:i+3] ifadesi ne yapar?




