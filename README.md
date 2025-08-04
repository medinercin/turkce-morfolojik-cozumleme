# Türkçe Morfolojik Çözümleme

Bu proje, Türkçe kelimelerin morfolojik analizini gerçekleştiren Flask tabanlı bir web uygulamasıdır. Kelimeleri kök ve eklerine ayırarak kullanıcıya dilsel olarak detaylı bir analiz sunar. Sistem, hem kök türünü (isim, fiil, sıfat vb.) belirlemekte hem de ekleri anlamlarına göre sınıflandırmaktadır.

## Özellikler

- Gelişmiş tokenizasyon: Kelimeleri ve noktalama işaretlerini ayrı ayrı işler.
- Morfolojik çözümleme: Kelimeleri kök ve eklerine ayırarak yapılarını analiz eder.
- Türkçe ek tanıma: Yaygın çekim ve yapım eklerini tanır ve anlamlarını gösterir.
- Kök türü belirleme: Kökün isim mi, fiil mi yoksa sıfat mı olduğunu analiz eder.
- Anlamlı ek filtreleme: Yalnızca dilbilgisel açıdan anlamlı ekler kullanıcıya sunulur.
- Noktalama işareti tanıma: Noktalama işaretlerini ayırt ederek dil çözümlemesinden ayrı tutar.
- Flask arayüzü: Web tabanlı, kullanıcı dostu bir etkileşim sağlar.

## Kurulum

1. Repository’yi klonlayın:

```bash
git clone https://github.com/medinercin/turkce-morfolojik-cozumleme.git
cd turkce-morfolojik-cozumleme
```

2. Sanal ortam oluşturun ve etkinleştirin:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# veya
source venv/bin/activate  # Linux/Mac
```

3. Gereken Python kütüphanelerini yükleyin:

```bash
pip install flask
```

4. Uygulamayı başlatın:

```bash
python app.py
```

## Katkıda Bulunulan Proje

Bu projede Türkçe morfolojik analiz için aşağıdaki açık kaynaklı projeden faydalanılmıştır:

- [starlangsoftware/TurkishMorphologicalAnalysis-Cy](https://github.com/starlangsoftware/TurkishMorphologicalAnalysis-Cy)  
  Java tabanlı Türkçe biçimbilim çözümleyicisi, bu projeye Python arayüzü üzerinden entegre edilmiştir.




