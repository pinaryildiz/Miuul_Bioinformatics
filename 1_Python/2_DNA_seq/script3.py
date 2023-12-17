#Verilen dizinin başına ve sonuna uzun "AAAAAAAA" kuyrukları ekle

def kuyruk_ekle(dizi, kuyruk="AAAAAAAA"):
    return kuyruk + dizi + kuyruk

def daha_uzun_kuyruk_ekle(dizi, uzunluk=30):
    return ("A" * uzunluk) + dizi + ("A" * uzunluk)

dna_dizisi = "AGCTATAG"
kuyruklu_dna_dizisi = kuyruk_ekle(dna_dizisi)
daha_uzun_kuyruklu_dna_dizisi = daha_uzun_kuyruk_ekle(dna_dizisi)
