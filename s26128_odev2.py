print("sifrenizi giriniz")
sifre= input()
kucukHarfListe=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
buyukHarfListe=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ozelKarakterlerListe=["(",")","*","+",",","-","."] 
sayiListesi=["0","1","2","3","4","5","6","7","8","9"]
izinliKarakterler=[]
izinliKarakterler.extend(kucukHarfListe)
izinliKarakterler.extend(buyukHarfListe)
izinliKarakterler.extend(ozelKarakterlerListe)
izinliKarakterler.extend(sayiListesi)
a=True
b=True
kucukHarfSayisi=0
buyukHarfSayisi=0
sayiSayisi=0
ozelKarakterSayisi=0
if len(sifre)<4:
    print("Geçersiz Şifre")
    print("Şifre çok kısa")
    a=False
elif len(sifre)>8:
    print("Geçersiz Şifre")
    print("Şifre en fazla 8 karakter olabilir")
    a=False

elif not any(x in kucukHarfListe for x in sifre):
    print("Geçersiz Şifre")
    print("Şifre en az bir küçük harf içermeli")
    a=False

elif not any(x in buyukHarfListe for x in sifre):
    print("Geçersiz Şifre")
    print("Şifre en az bir büyük harf içermeli") 
    a=False

elif not any(x.isdigit() for x in sifre):
    print("Geçersiz Şifre")
    print("Şifre en az bir rakam içermeli")
    a=False
    
elif not any(x in ozelKarakterlerListe for x in sifre):
    print("Geçersiz Şifre")
    print("Şifre izin verilen özel karakterlerden en az birini içermeli")
    a=False


elif b==True:
    for harf in sifre:
        if not(harf in izinliKarakterler):
            print("Geçersiz Şifre")
            print("Şifre yalnızca sayı, harf ve izin verilen özel karakterlerden oluşmalı")
            a=False

for i in kucukHarfListe:
    for j in sifre:
        if i==j:
            kucukHarfSayisi+=1
   
for i in buyukHarfListe:
    for j in sifre:
        if i==j:
            buyukHarfSayisi+=1

for i in sayiListesi:
    for j in sifre:
        if i==j:
            sayiSayisi+=1

for i in ozelKarakterlerListe:
    for j in sifre:
        if i==j:
            ozelKarakterSayisi+=1
            
if a==True:
    print("Geçerli Şifre")
    G = 3*(kucukHarfSayisi+1)*5*(buyukHarfSayisi+1)*2*(sayiSayisi+1)*4*(ozelKarakterSayisi+1)-120
    if G<2000:
        print("Çok Zayıf Şifre")
    elif G>=2000 and G<4000:
        print("Zayıf Şifre")
    elif G>=4000 and G<6000:
        print("Ortalama Şifre")
    elif G>=6000 and G<9000:
        print("Güçlü Şifre")
    elif G >=9000:
        print("Çok Güçlü Şifre")
            



    
    