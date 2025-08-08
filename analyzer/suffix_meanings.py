def get_suffix_meaning(suffix):
    meanings = {
        # Temel türler
        "NOUN": "İsim", 
        "VERB": "Fiil", 
        "ADJ": "Sıfat",
        
        # Kişi ekleri
        "A1SG": "1. Tekil Kişi", 
        "A2SG": "2. Tekil Kişi", 
        "A3SG": "3. Tekil Kişi",
        "A1PL": "1. Çoğul Kişi", 
        "A2PL": "2. Çoğul Kişi", 
        "A3PL": "3. Çoğul Kişi",
        
        # İyelik ekleri
        "P1SG": "1. Tekil Sahip", 
        "P2SG": "2. Tekil Sahip", 
        "P3SG": "3. Tekil Sahip",
        "PNON": "Sahipsiz",
        
        # Durum ekleri
        "NOM": "Yalın", 
        "ACC": "Belirtme", 
        "DAT": "Yönelme", 
        "LOC": "Bulunma", 
        "ABL": "Ayrılma",
        "INS": "Araç Durumu", 
        "GEN": "İyelik",
        
        # Zaman ekleri
        "PAST": "Geçmiş Zaman", 
        "FUT": "Gelecek Zaman", 
        "PRES": "Geniş Zaman", 
        "PROG1": "Şimdiki Zaman",
        
        # Olumluluk/Olumsuzluk
        "NEG": "Olumsuz", 
        "POS": "Olumlu", 
        "OPT": "Dilek", 
        "COND": "Koşul", 
        "IMP": "Emir",
        
        # Çatı ekleri
        "CAUS": "Ettirgen", 
        "PASS": "Edilgen", 
        "REFL": "Dönüşlü", 
        "RECP": "İşteş",
        
        # Fiilimsi ekleri
        "INF": "Mastar", 
        "PART": "Sıfat-Fiil", 
        "GER": "İsim-Fiil",
        
        # Diğer ekler
        "QUES": "Soru", 
        "DET": "Belirteç", 
        "PROP": "Özel İsim",
        
        # Yaygın suffix kodları
        "A1SG": "1. Tekil Kişi",
        "A2SG": "2. Tekil Kişi", 
        "A3SG": "3. Tekil Kişi",
        "A1PL": "1. Çoğul Kişi",
        "A2PL": "2. Çoğul Kişi",
        "A3PL": "3. Çoğul Kişi",
        "P1SG": "1. Tekil Sahip",
        "P2SG": "2. Tekil Sahip",
        "P3SG": "3. Tekil Sahip",
        "PNON": "Sahipsiz",
        "NOM": "Yalın",
        "ACC": "Belirtme",
        "DAT": "Yönelme",
        "LOC": "Bulunma",
        "ABL": "Ayrılma",
        "INS": "Araç Durumu",
        "GEN": "İyelik",
        "PAST": "Geçmiş Zaman",
        "FUT": "Gelecek Zaman",
        "PRES": "Geniş Zaman",
        "PROG1": "Şimdiki Zaman",
        "NEG": "Olumsuz",
        "POS": "Olumlu",
        "OPT": "Dilek",
        "COND": "Koşul",
        "IMP": "Emir",
        "CAUS": "Ettirgen",
        "PASS": "Edilgen",
        "REFL": "Dönüşlü",
        "RECP": "İşteş",
        "INF": "Mastar",
        "PART": "Sıfat-Fiil",
        "GER": "İsim-Fiil",
        "QUES": "Soru",
        "DET": "Belirteç",
        "PROP": "Özel İsim"
    }
    return meanings.get(suffix, suffix)

def get_suffix_display_info(suffix):
    """
    Suffix için görüntüleme bilgilerini döndürür.
    Returns: (display_text, tooltip_text)
    """
    # Tamlanan eki özel kontrolü
    if suffix in ['sı', 'si', 'su', 'sü']:
        return f"-{suffix} : tamlanan", "Tamlanan Eki"
    
    # Tek anlamlı ekler
    single_meanings = {
        # Geçmiş zaman ekleri
        "ti": "Geçmiş Zaman",
        "tı": "Geçmiş Zaman", 
        "tu": "Geçmiş Zaman",
        "tü": "Geçmiş Zaman",
        "di": "Geçmiş Zaman",
        "dı": "Geçmiş Zaman", 
        "du": "Geçmiş Zaman",
        "dü": "Geçmiş Zaman",
        
        # Kişi ekleri (tek harfli)
        "m": "1. Tekil Kişi",
        "n": "2. Tekil Kişi", 
        "k": "1. Çoğul Kişi",
        "z": "1. Çoğul Kişi",
        "r": "3. Çoğul Kişi",
        
        # Gelecek zaman ekleri
        "cek": "Gelecek Zaman",
        "cak": "Gelecek Zaman",
        
        # Şimdiki zaman ekleri
        "iyor": "Şimdiki Zaman",
        "ıyor": "Şimdiki Zaman",
        "uyor": "Şimdiki Zaman", 
        "üyor": "Şimdiki Zaman",
        
        # Geçmiş zaman ekleri (miş'li)
        "miş": "Geçmiş Zaman",
        "mış": "Geçmiş Zaman",
        "muş": "Geçmiş Zaman",
        "müş": "Geçmiş Zaman",
        
        # Yeterlilik kipi ekleri
        "meli": "Yeterlilik Kipi",
        "malı": "Yeterlilik Kipi",
        
        # Şart kipi ekleri
        "sa": "Şart Kipi",
        "se": "Şart Kipi",
        
        # İstek kipi ekleri
        "sin": "İstek Kipi",
        "sın": "İstek Kipi",
        "sun": "İstek Kipi",
        "sün": "İstek Kipi",
        
        # İyelik ekleri
        "im": "1. Tekil Sahip",
        "ım": "1. Tekil Sahip",
        "um": "1. Tekil Sahip",
        "üm": "1. Tekil Sahip",
        "in": "2. Tekil Sahip",
        "ın": "2. Tekil Sahip",
        "un": "2. Tekil Sahip",
        "ün": "2. Tekil Sahip",
        
        # Çoğul ekleri
        "ler": "Çoğul Eki",
        "lar": "Çoğul Eki",
        
        # Mastar ekleri
        "mak": "Mastar",
        "mek": "Mastar",
        
        # İsim-fiil ekleri
        "me": "İsim-Fiil Eki",
        "ma": "İsim-Fiil Eki",
        
        # Sıfat-fiil ekleri
        "en": "Sıfat-Fiil Eki",
        "an": "Sıfat-Fiil Eki",
        
        # Zarf-fiil ekleri
        "ip": "Zarf-Fiil Eki",
        "ıp": "Zarf-Fiil Eki",
        "up": "Zarf-Fiil Eki",
        "üp": "Zarf-Fiil Eki",
        
        # Edilgen ekleri
        "ıl": "Edilgen Eki",
        "il": "Edilgen Eki",
        "ul": "Edilgen Eki",
        "ül": "Edilgen Eki",
        
        # Ettirgen ekleri
        "tır": "Ettirgen Eki",
        "tir": "Ettirgen Eki",
        "tur": "Ettirgen Eki",
        "tür": "Ettirgen Eki",
        
        # İşteşlik ekleri
        "ış": "İşteşlik Eki",
        "iş": "İşteşlik Eki",
        "uş": "İşteşlik Eki",
        "üş": "İşteşlik Eki",
        
        # Yönelme durumu ekleri
        "e": "Yönelme Eki",
        "a": "Yönelme Eki",
        
        # Belirtme durumu ekleri
        "i": "Belirtme Eki",
        "ı": "Belirtme Eki",
        "u": "Belirtme Eki",
        "ü": "Belirtme Eki",
        
        # Bulunma durumu ekleri
        "de": "Bulunma Eki",
        "da": "Bulunma Eki",
        "te": "Bulunma Eki",
        "ta": "Bulunma Eki",
        
        # Ayrılma durumu ekleri
        "den": "Ayrılma Eki",
        "dan": "Ayrılma Eki",
        "ten": "Ayrılma Eki",
        "tan": "Ayrılma Eki",
        
        # Ek eylem ekleri
        "dir": "Ek Eylem",
        "dır": "Ek Eylem",
        "dur": "Ek Eylem",
        "dür": "Ek Eylem"
    }
    
    # Çok anlamlı ekler
    multi_meanings = {
        # İsimden sıfat yapma ekleri
        "li": ["İsimden Sıfat Yapma Eki", "Bulunma Durumu"],
        "lı": ["İsimden Sıfat Yapma Eki", "Bulunma Durumu"],
        "lu": ["İsimden Sıfat Yapma Eki", "Bulunma Durumu"],
        "lü": ["İsimden Sıfat Yapma Eki", "Bulunma Durumu"],
        
        "siz": ["İsimden Sıfat Yapma Eki", "Bulunma Durumu"],
        "sız": ["İsimden Sıfat Yapma Eki", "Bulunma Durumu"],
        "suz": ["İsimden Sıfat Yapma Eki", "Bulunma Durumu"],
        "süz": ["İsimden Sıfat Yapma Eki", "Bulunma Durumu"],
        
        # İsimden isim yapma ekleri
        "ci": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "cı": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "cu": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "cü": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "çi": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "çı": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "çu": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "çü": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        
        # İsimden isim yapma ekleri (lik, lık, luk, lük)
        "lik": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "lık": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "luk": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        "lük": ["İsimden İsim Yapma Eki", "Bulunma Durumu"],
        
        # Kişi ekleri (y ile başlayan)
        "yim": ["1. Tekil Kişi", "İyelik Eki"],
        "yım": ["1. Tekil Kişi", "İyelik Eki"],
        "yum": ["1. Tekil Kişi", "İyelik Eki"],
        "yüm": ["1. Tekil Kişi", "İyelik Eki"],
        
        "yiz": ["1. Çoğul Kişi", "İyelik Eki"],
        "yız": ["1. Çoğul Kişi", "İyelik Eki"],
        "yuz": ["1. Çoğul Kişi", "İyelik Eki"],
        "yüz": ["1. Çoğul Kişi", "İyelik Eki"],
        
        # Şimdiki zaman ekleri
        "yor": ["Şimdiki Zaman", "Zaman Eki"],
        
        # Gelecek zaman ekleri
        "ceğ": ["Gelecek Zaman", "Zaman Eki"],
        "cağ": ["Gelecek Zaman", "Zaman Eki"]
    }
    
    # Tek anlamlı ekler için
    if suffix in single_meanings:
        meaning = single_meanings[suffix]
        return f"-{suffix} : {meaning}", meaning
    
    # Çok anlamlı ekler için
    elif suffix in multi_meanings:
        meanings = multi_meanings[suffix]
        display_text = f"-{suffix} : " + " / ".join(meanings)
        return display_text, meanings[0]  # İlk anlamı tooltip_text olarak kullan
    
    # Özel breakdown ekleri için
    if suffix == 'y (kaynaştırma)':
        return '-y : kaynaştırma harfi', 'Kaynaştırma Harfi'
    
    # Bilinmeyen ekler için
    else:
        return f"-{suffix} : {suffix}", suffix
