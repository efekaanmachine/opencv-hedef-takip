import cv2
import numpy as np
import math

# Fare (hedef) koordinatlarını tutacağımız başlangıç değerleri
hedef_x, hedef_y = 200, 200

# Fare hareket ettiğinde yeni koordinatları alan basit fonksiyon
def fare_hareketi(event, x, y, flags, param):
    global hedef_x, hedef_y
    if event == cv2.EVENT_MOUSEMOVE:
        hedef_x, hedef_y = x, y

# Pencereyi oluştur ve fare hareketlerini dinle
cv2.namedWindow("IHA Hedef Takip Simulasyonu")
cv2.setMouseCallback("IHA Hedef Takip Simulasyonu", fare_hareketi)

while True:
    # 1. 600x800 boyutunda siyah bir kamera ekranı oluştur
    ekran = np.zeros((600, 800, 3), dtype=np.uint8)
    merkez_x, merkez_y = 400, 300 # Ekranın tam ortası

    # 2. Pisagor ile merkez ve hedef arasındaki mesafeyi hesapla
    mesafe = math.hypot(hedef_x - merkez_x, hedef_y - merkez_y)

    # 3. Mesafe 60 pikselden küçükse KİLİTLENDİ (Yeşil), değilse TAKİPTE (Sarı)
    if mesafe < 60:
        renk = (0, 255, 0) # Yeşil
        durum = "DURUM: HEDEF KILITLENDI [LOCKED]"
    else:
        renk = (0, 255, 255) # Sarı
        durum = "DURUM: TAKIP EDILIYOR [TRACKING]"

    # 4. Ekranın ortasına sabit nişangah (Crosshair) çiz
    cv2.line(ekran, (merkez_x - 20, merkez_y), (merkez_x + 20, merkez_y), (255, 255, 255), 1)
    cv2.line(ekran, (merkez_x, merkez_y - 20), (merkez_x, merkez_y + 20), (255, 255, 255), 1)
    cv2.circle(ekran, (merkez_x, merkez_y), 60, (100, 100, 100), 1) # Kilitlenme çemberi

    # 5. Hedefin etrafına kutu çiz ve merkezden hedefe çizgi çek
    cv2.rectangle(ekran, (hedef_x - 25, hedef_y - 25), (hedef_x + 25, hedef_y + 25), renk, 2)
    cv2.line(ekran, (merkez_x, merkez_y), (hedef_x, hedef_y), renk, 2)

    # 6. Sol üste bilgileri yazdır
    cv2.putText(ekran, durum, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, renk, 2)
    cv2.putText(ekran, f"Merkeze Mesafe: {int(mesafe)} px", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    # Ekranı göster ('q' tuşuna basınca çıkar)
    cv2.imshow("IHA Hedef Takip Simulasyonu", ekran)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()