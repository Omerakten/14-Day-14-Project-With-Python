#KÜTÜPHANE PROJESİ
#İŞLEMLER
#SİSTEME GİRİŞ İÇİN KULLANICI ADI ŞİFRESİ OLACAKTIR
#SİSTEME GİRİŞ YAPILIRKEN 3 DEFA HATALI GİRİŞ OLURSA SİSTEM KAPANACAK
#GİRİŞ YAPILDIKTAN SONRA AŞAĞIDAKİ MENÜ ÇIKACAK
#1- KİTAP EKLE  // İD KİTAP_AD YAZAR_AD
#2- KİTAP SİL   // VERİLEN ID İLE SİLME İŞLEMİ YAPILACAK
#3- ÜYE EKLE  // İD İSİM SOYİSİM YAŞ YAŞADIĞI YER
#4- ÜYE SİL   // VERİLEN ID İLE SİLME İŞLEMİ YAPILACAK


#5- ÖDÜNÇ VER   //İD İLE KULLANICI SEÇİLECEKTİR > VERİLEN KİTABIN ID'Sİ SEÇİLECEK
#               //KULLANICI BİLGİLERİ VE VERİLEN KİTAP ÖDÜNÇ VERİLEN KİTAPLARIN
#               //OLDUĞU TXT DOSYASINA KAYDEDİLECEKTİR.
#               //ÖDÜNC VERİLEN KİTAP KİTAPLAR LİSTESİNDEN SİLİNECEKTİR
#6- TESLİM AL   //KULLANICI İD'Sİ VERİLECEK > ÖDÜNC ALINANLAR LİSTESİNDEN SİLİNECEK
#               //KİTAP İD Sİ İLE KİTAPLAR LİSTESİNE EKLENECEK


#7- TÜM KİTAPLARI GÖSTER // TÜM KİTAPLARIN OLDUĞU LİSTE YAZDIRILACAKTIR
#8- ÜYE LİSTESİ          // TÜM ÜYELER LİSTESİ YAZDIRILACAKTIR
#9- SİSTEMDEN ÇIKIŞ YAP
#VERİLER TXT DOSYASINDA TUTULACAK.
#TÜM İŞLEMLER TXT DOSYASI ÜZERİNE İŞLENECEKTİR.

## TOPLAMDA KAÇ KİTAP OLDUĞUNU SAYI HALİNDE VERSİN

#kitap üye eklenince kayıt olduğu tarihi de eklesin

## VERİLEN KİTAPLAR LİSTESİ
## TESLİM ALINANLAR LİSTESİ


import random
randGen = random.SystemRandom()
secV =randGen.randint(11111111,99999999)
print(secV)
#rastglele sayı üretme kodu