import random 
import time
print("sayi tahmin oyununa hoşgeldiniz1-100 arasında bir sayı tahmin edin")
sayi = random.randint(1,100)
tahmin_hakki = 5
while True:
    tahmin = int(input("Tahmininiz:"))
    if tahmin == sayi:
        print("Sayi sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! dogru.bildiniz")
        break
    elif tahmin>sayi:
        print("sayi sorugulaniyor")
        time.sleep(1)
        tahmin_hakki-=1
        print("daha küçük bir sayı giriniz")
        print(f"alan tahmin hakkı:{tahmin_hakki}")
    else:
        print("sayi sorgulaniyor...")
        time.sleep(1)
        tahmin_hakki = tahmin_hakki +1
        print("daha büyük bir sayı giriniz")
        print(f"kalan tahmin hakkı {tahmin_hakki}")
    if tahmin_hakki==0:
        print("tahmin hakkınız bitmiştir")
        print(f"Bilgisayarın tahmini:{sayi}")
        break
            