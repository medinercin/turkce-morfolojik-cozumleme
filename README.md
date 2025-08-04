# Türkçe Morfolojik Çözümleme

Bu proje, Türkçe kelimelerin morfolojik analizini yapan Flask tabanlı bir web uygulamasıdır. Kelimeleri köklerine ve eklerine ayırarak detaylı bir analiz sunar.

## Özellikler

- **Gelişmiş Tokenizasyon**: Kelimeleri ve noktalama işaretlerini ayrı ayrı işler
- **Morfolojik Ayrıştırma**: Kelimeleri kök ve eklerine ayırır
- **Türkçe Ek Tanıma**: Yaygın Türkçe ekleri tanır ve anlamlarını gösterir
- **İnteraktif Arayüz**: Butonlar ve tooltip'ler ile kullanıcı dostu arayüz
- **Kök Türü Belirleme**: İsim, fiil, sıfat köklerini otomatik belirler

## Kurulum

1. Repository'yi klonlayın:
```bash
git clone https://github.com/medinercin/turkce-morfolojik-cozumleme.git
cd turkce-morfolojik-cozumleme
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# veya
source venv/bin/activate  # Linux/Mac
```

3. Gerekli paketleri yükleyin:
```bash
pip install flask
```

4. Uygulamayı çalıştırın:
```bash
python app.py
```







