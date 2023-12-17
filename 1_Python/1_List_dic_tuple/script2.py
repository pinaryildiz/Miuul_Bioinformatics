def sozluk_yapma(dizi):
    sozluk = {}
    for nukleotid in set(dizi):
        sozluk[nukleotid] = dizi.count(nukleotid)
    return sozluk

