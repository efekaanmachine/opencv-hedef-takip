# 🎯 OpenCV İHA Hedef Takip ve Kilitleme Simülasyonu

Görüntü işleme (OpenCV) temellerini ve otonom sistemlerdeki hedef merkezleme mantığını pratik etmek amacıyla geliştirilmiş gerçek zamanlı bir hedef takip (HUD) simülasyonu.

## 🚀 Özellikler
* **Gerçek Zamanlı Mesafe Hesabı:** Ekran merkezi (Crosshair) ile hareketli hedef arasındaki Öklid/Pisagor mesafesini anlık olarak piksel bazında hesaplar.
* **Dinamik Durum Değişimi:** Hedef belirlenen menzil çemberine (60 px) girdiğinde sistem otomatik olarak `TRACKING` (Sarı) durumundan `LOCKED` (Yeşil) durumuna geçer.
* **Sıfır Donanım İhtiyacı:** Kamera veya harici video gerektirmeden fare (mouse) koordinatları üzerinden simüle edilir.

## 💻 Kurulum ve Çalıştırma

Gerekli kütüphaneleri yükleyin:
```bash
pip install opencv-python numpy
