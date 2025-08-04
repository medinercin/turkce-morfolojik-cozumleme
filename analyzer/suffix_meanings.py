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
        "ıl": "Edilgen",
        "il": "Edilgen",
        "ul": "Edilgen",
        "ül": "Edilgen",
        
        # Fiilimsi ekleri
        "INF": "Mastar", 
        "PART": "Sıfat-Fiil", 
        "GER": "İsim-Fiil",
        "mak": "Mastar",
        "mek": "Mastar",
        
        # Diğer ekler
        "QUES": "Soru", 
        "DET": "Belirteç", 
        "PROP": "Özel İsim",
        
        # İsimden isim yapma ekleri
        "çi": "İsimden İsim Yapma Eki",
        "çı": "İsimden İsim Yapma Eki", 
        "çu": "İsimden İsim Yapma Eki",
        "çü": "İsimden İsim Yapma Eki",
        "ci": "İsimden İsim Yapma Eki",
        "cı": "İsimden İsim Yapma Eki",
        "cu": "İsimden İsim Yapma Eki", 
        "cü": "İsimden İsim Yapma Eki",
        
        # İsimden isim yapma ekleri (lük, lik, lık, luk)
        "lük": "İsimden İsim Yapma Eki",
        "lik": "İsimden İsim Yapma Eki",
        "lık": "İsimden İsim Yapma Eki",
        "luk": "İsimden İsim Yapma Eki",
        
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
