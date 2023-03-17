def kelime_say(metin):
    kucuk_metin = metin.lower()
    kelime_listesi = metin.split()
    kelime_sayilari = {}
    
    for kelime in kelime_listesi:
        if kelime in kelime_sayilari:
            kelime_sayilari[kelime] += 1
        else:
            kelime_sayilari[kelime]= 1
        
    return kelime_sayilari    
    
metin = input("Bir metin giriniz: ")
sonuc = kelime_say(metin)

print(sonuc)