import sys
import os
sys.path.append('TurkishMorphologicalAnalysis')

from TurkishMorphologicalAnalysis.MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

# Türkçe morfolojik analizörü oluştur
morph = FsmMorphologicalAnalyzer()

# Test kelimeleri
test_words = [
    "olan",      # ol-an (sıfat-fiil)
    "çıktısı",   # çıktı-sı (tamlanan eki)
    "raporlar",  # rapor-lar (çoğul)
    "kesinlikle", # kesin-lik-le (isimden isim yapma + isimden isim yapma)
    "ile",       # ile (bağlaç)
    "düzgün",    # düz-gün (isimden isim yapma)
    "doygun",    # doy-gun (fiilden isim yapma)
    "yazılacak", # yaz-ıl-acak (edilgenlik + sıfat-fiil)
    "olacak",    # ol-acak (sıfat-fiil)
    "ve",        # ve (bağlaç)
    "çizilecektir", # çiz-il-ecek-tir (edilgenlik + gelecek zaman + yüklem)
    "edilmeyecektir" # et-il-me-yecek-tir (edilgenlik + olumsuzluk + gelecek zaman + yüklem)
]

print("Türkçe Morfolojik Analiz Testleri")
print("=" * 50)

for word in test_words:
    print(f"\nKelime: {word}")
    try:
        result = morph.morphologicalAnalysis(word)
        if result and result.size() > 0:
            for i in range(result.size()):
                parse = result.getFsmParse(i)
                print(f"  Analiz {i+1}: {parse}")
        else:
            print("  Analiz bulunamadı.")
    except Exception as e:
        print(f"  Hata: {e}")
