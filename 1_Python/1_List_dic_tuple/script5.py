# Önceki scriptlerdeki fonksiyonları buraya çağırıyoruz
from script1 import liste_yapma
from script2 import sozluk_yapma
from script3 import nukleotid_sayimi
from script4 import pozisyon_belirleme


# Ana işlem
def ana_islem(dizi):
    nukleotidler = nukleotid_sayimi(dizi)
    liste = liste_yapma(dizi)
    sozluk = sozluk_yapma(dizi)
    pozisyon = pozisyon_belirleme(dizi)

    return nukleotidler, liste, sozluk, pozisyon

# DNA dizisi
dna_dizisi = "AGCTATAG"

# Fonksiyonu çağırıyoruz
nukleotidler, liste, sozluk, pozisyon = ana_islem(dna_dizisi)


