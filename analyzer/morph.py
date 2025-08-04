from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

morphology = FsmMorphologicalAnalyzer()

def analyze_sentence(sentence):
    # Cümleyi kelimelere ve noktalama işaretlerine ayır
    tokens = split_sentence_into_tokens(sentence)
    results = []
    
    for token in tokens:
        # Noktalama işaretlerini kontrol et
        if is_punctuation(token):
            results.append({
                "word": token,
                "root": "Noktalama İşareti",
                "suffixes": []
            })
            continue
            
        parses = morphology.morphologicalAnalysis(token)
        if parses and parses.size() > 0:
            best = parses.getFsmParse(0)
            root = best.getWord().getName()
            suffix_details = []
            
            # Kelimeden kökü çıkararak gerçek ekleri bul
            actual_suffixes = extract_actual_suffixes(token, root)
            
            for i in range(best.size()):
                suffix_str = str(best.getInflectionalGroup(i))
                # Ekleri ayrıştır ve Türkçe karşılıklarını ekle
                suffix_parts = suffix_str.split('+')
                for j, part in enumerate(suffix_parts):
                    if part.strip():
                        actual_suffix = actual_suffixes[j] if j < len(actual_suffixes) else part.strip()
                        suffix_details.append({
                            'suffix': actual_suffix,
                            'meaning': get_suffix_meaning(part.strip())
                        })
            results.append({
                "word": token,
                "root": root,
                "suffixes": suffix_details
            })
        else:
            results.append({
                "word": token,
                "root": "Bilinmiyor",
                "suffixes": []
            })
    return results

def split_sentence_into_tokens(sentence):
    """Cümleyi kelimelere ve noktalama işaretlerine ayırır"""
    import re
    
    # Noktalama işaretlerini tanımla
    punctuation_pattern = r'[.,!?;:()[\]{}"\'-]'
    
    # Cümleyi noktalama işaretlerine göre böl
    parts = re.split(f'({punctuation_pattern})', sentence)
    
    tokens = []
    for part in parts:
        part = part.strip()
        if part:  # Boş string'leri atla
            tokens.append(part)
    
    return tokens

def extract_actual_suffixes(word, root):
    """Kelimeden kökü çıkararak gerçek ekleri bulur"""
    if not root or root == "Bilinmiyor":
        return []
    
    # Kökü kelimeden çıkar
    if word.startswith(root):
        remaining = word[len(root):]
        if remaining:
            # Kalan kısmı ekler olarak böl
            suffixes = []
            current_suffix = ""
            
            for char in remaining:
                current_suffix += char
                # Türkçe ek başlangıçları
                if current_suffix in ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü', 'da', 'de', 'ta', 'te', 'dan', 'den', 'tan', 'ten', 'la', 'le', 'ya', 'ye', 'yor', 'acak', 'ecek', 'dı', 'tı', 'du', 'tu', 'di', 'ti', 'dü', 'tü', 'mış', 'miş', 'muş', 'müş', 'malı', 'meli', 'se', 'sa', 'mı', 'mi', 'mu', 'mü', 'lar', 'ler', 'ın', 'in', 'un', 'ün', 'ım', 'im', 'um', 'üm', 'ız', 'iz', 'uz', 'üz', 'sınız', 'siniz', 'sunuz', 'sünüz', 'lar', 'ler']:
                    suffixes.append(current_suffix)
                    current_suffix = ""
            
            if current_suffix:
                suffixes.append(current_suffix)
            
            return suffixes
    
    return []

def is_punctuation(word):
    """Kelimenin noktalama işareti olup olmadığını kontrol eder"""
    punctuation_marks = ['.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '...', '?!', '!?', 'mu?', 'mı?', 'mi?', 'mü?', 'mı', 'mi', 'mü', 'mu']
    return word in punctuation_marks

def get_suffix_meaning(suffix):
    """Eklerin Türkçe karşılıklarını döndürür"""
    meanings = {
        # İsim ekleri
        'NOUN': 'İsim',
        'A3SG': '3. Tekil Şahıs',
        'A3PL': '3. Çoğul Şahıs',
        'A1SG': '1. Tekil Şahıs',
        'A1PL': '1. Çoğul Şahıs',
        'A2SG': '2. Tekil Şahıs',
        'A2PL': '2. Çoğul Şahıs',
        'PNON': 'Sahipsiz',
        'P1SG': '1. Tekil Sahip',
        'P1PL': '1. Çoğul Sahip',
        'P2SG': '2. Tekil Sahip',
        'P2PL': '2. Çoğul Sahip',
        'P3SG': '3. Tekil Sahip',
        'P3PL': '3. Çoğul Sahip',
        
        # Durum ekleri
        'NOM': 'Yalın Durum',
        'ACC': 'Belirtme Durumu',
        'DAT': 'Yönelme Durumu',
        'LOC': 'Bulunma Durumu',
        'ABL': 'Ayrılma Durumu',
        'INS': 'Araç Durumu',
        'GEN': 'İyelik Durumu',
        
        # Fiil ekleri
        'VERB': 'Fiil',
        'POS': 'Olumlu',
        'NEG': 'Olumsuz',
        'IMP': 'Emir Kipi',
        'PROG': 'Şimdiki Zaman',
        'FUT': 'Gelecek Zaman',
        'PAST': 'Geçmiş Zaman',
        'PRES': 'Geniş Zaman',
        'AOR': 'Geniş Zaman',
        'NEC': 'Gereklilik Kipi',
        'COND': 'Koşul Kipi',
        'PASS': 'Edilgen Çatı',
        'CAUS': 'Ettirgen Çatı',
        'RECP': 'İşteş Çatı',
        'REFL': 'Dönüşlü Çatı',
        
        # Sıfat ekleri
        'ADJ': 'Sıfat',
        'COMP': 'Karşılaştırma',
        'SUP': 'Üstünlük',
        
        # Zaman ekleri
        'TENSE': 'Zaman',
        'ASPECT': 'Görünüş',
        'MOOD': 'Kip',
        'VOICE': 'Çatı',
        
        # Diğer
        'INF': 'Mastar',
        'PART': 'Sıfat-Fiil',
        'GER': 'İsim-Fiil',
        'ADV': 'Zarf',
        'POSTP': 'Edat',
        'CONJ': 'Bağlaç',
        'INTERJ': 'Ünlem',
        'DET': 'Belirteç',
        'PRON': 'Zamir',
        'NUM': 'Sayı',
        'PUNCT': 'Noktalama',
        
        # Özel durumlar
        'DB': 'Türetme Sınırı',
        'IS_OA': 'Özel Ad',
        'IS_KESIR': 'Kesir',
        'IS_DATE': 'Tarih',
        'IS_PERCENT': 'Yüzde',
        'IS_ZAMAN': 'Zaman',
        'IS_RANGE': 'Aralık',
        'IS_SAYI': 'Sayı',
        'IS_REELSAYI': 'Reel Sayı',
        
        # Daha detaylı ekler
        'ABLE': 'Yeterlilik Eki',
        'NEGATIVE': 'Olumsuzluk Eki',
        'PROGRESSIVE': 'Şimdiki Zaman Eki',
        'PROG1': 'Şimdiki Zaman Eki',
        'PROG2': 'Şimdiki Zaman Eki',
        'FUTURE': 'Gelecek Zaman Eki',
        'PAST_TENSE': 'Geçmiş Zaman Eki',
        'PRESENT': 'Geniş Zaman Eki',
        'AORIST': 'Geniş Zaman Eki',
        'NECESSITY': 'Gereklilik Kipi',
        'CONDITIONAL': 'Koşul Kipi',
        'PASSIVE': 'Edilgen Çatı',
        'CAUSATIVE': 'Ettirgen Çatı',
        'RECIPROCAL': 'İşteş Çatı',
        'REFLEXIVE': 'Dönüşlü Çatı',
        'COMPARATIVE': 'Karşılaştırma Eki',
        'SUPERLATIVE': 'Üstünlük Eki',
        'INFINITIVE': 'Mastar Eki',
        'PARTICIPLE': 'Sıfat-Fiil Eki',
        'GERUND': 'İsim-Fiil Eki',
        'ADVERB': 'Zarf Eki',
        'POSTPOSITION': 'Edat',
        'CONJUNCTION': 'Bağlaç',
        'INTERJECTION': 'Ünlem',
        'DETERMINER': 'Belirteç',
        'PRONOUN': 'Zamir',
        'NUMBER': 'Sayı',
        'PUNCTUATION': 'Noktalama İşareti',
        'QUESTION': 'Soru Eki',
        'NEGATION': 'Olumsuzluk Eki',
        'ABILITY': 'Yeterlilik Eki',
        'CONTINUOUS': 'Sürekli Zaman',
        'PERFECT': 'Bitmiş Zaman',
        'IMPERFECT': 'Bitmemiş Zaman',
        'PLUPERFECT': 'Öncesi Zaman',
        'FUTURE_PERFECT': 'Gelecek Bitmiş Zaman',
        'PRESENT_PERFECT': 'Şimdiki Bitmiş Zaman',
        'PAST_PERFECT': 'Geçmiş Bitmiş Zaman',
        'SUBJUNCTIVE': 'Dilek Kipi',
        'OPTATIVE': 'İstek Kipi',
        'IMPERATIVE': 'Emir Kipi',
        'HORTATIVE': 'Öneri Kipi',
        'PROHIBITIVE': 'Yasaklama Kipi',
        'PERMISSIVE': 'İzin Kipi',
        'OBLIGATIVE': 'Zorunluluk Kipi',
        'DESIDERATIVE': 'İstek Kipi',
        'INCHOATIVE': 'Başlama Kipi',
        'ITERATIVE': 'Tekrarlama Kipi',
        'FREQUENTATIVE': 'Sık Tekrarlama Kipi',
        'DIMINUTIVE': 'Küçültme Eki',
        'AUGMENTATIVE': 'Büyütme Eki',
        'HONORIFIC': 'Saygı Eki',
        'PEJORATIVE': 'Küçümseme Eki',
        'AMELIORATIVE': 'İyileştirme Eki',
        'FEMININE': 'Dişil Eki',
        'MASCULINE': 'Eril Eki',
        'NEUTER': 'Nötr Eki',
        'ANIMATE': 'Canlı Eki',
        'INANIMATE': 'Cansız Eki',
        'HUMAN': 'İnsan Eki',
        'NON_HUMAN': 'İnsan Olmayan Eki',
        'COLLECTIVE': 'Topluluk Eki',
        'DISTRIBUTIVE': 'Dağıtım Eki',
        'ORDINAL': 'Sıra Eki',
        'CARDINAL': 'Asıl Sayı Eki',
        'FRACTIONAL': 'Kesir Eki',
        'MULTIPLICATIVE': 'Çarpım Eki',
        'REPETITIVE': 'Tekrar Eki',
        'REVERSIVE': 'Ters Çevirme Eki',
        'SIMULTANEOUS': 'Aynı Anda Eki',
        'SUCCESSIVE': 'Ardışık Eki',
        'CONSECUTIVE': 'Sıralı Eki',
        'SIMULTANEOUSLY': 'Aynı Anda',
        'SUCCESSIVELY': 'Ardışık',
        'CONSECUTIVELY': 'Sıralı',
        'SIMULTANEOUSNESS': 'Aynı Andalık',
        'SUCCESSIVENESS': 'Ardışıklık',
        'CONSECUTIVENESS': 'Sıralılık',
        'SIMULTANEOUSLY_AGAIN': 'Tekrar Aynı Anda',
        'SUCCESSIVELY_AGAIN': 'Tekrar Ardışık',
        'CONSECUTIVELY_AGAIN': 'Tekrar Sıralı',
        'SIMULTANEOUSNESS_AGAIN': 'Tekrar Aynı Andalık',
        'SUCCESSIVENESS_AGAIN': 'Tekrar Ardışıklık',
        'CONSECUTIVENESS_AGAIN': 'Tekrar Sıralılık',
        
        # Türkçe ekler için daha detaylı karşılıklar
        'LE': 'İsimden Fiil Yapma Eki',
        'LA': 'İsimden Fiil Yapma Eki',
        'LI': 'İsimden Fiil Yapma Eki',
        'LU': 'İsimden Fiil Yapma Eki',
        'BIL': 'Yeterlilik Eki',
        'BILI': 'Yeterlilik Eki',
        'YOR': 'Şimdiki Zaman Eki',
        'ACAK': 'Gelecek Zaman Eki',
        'ECEK': 'Gelecek Zaman Eki',
        'DI': 'Geçmiş Zaman Eki',
        'TI': 'Geçmiş Zaman Eki',
        'DU': 'Geçmiş Zaman Eki',
        'TU': 'Geçmiş Zaman Eki',
        'IR': 'Geniş Zaman Eki',
        'UR': 'Geniş Zaman Eki',
        'AR': 'Geniş Zaman Eki',
        'ER': 'Geniş Zaman Eki',
        'MALI': 'Gereklilik Kipi',
        'MELI': 'Gereklilik Kipi',
        'SE': 'Koşul Kipi',
        'SA': 'Koşul Kipi',
        'IL': 'Edilgen Çatı',
        'IN': 'Edilgen Çatı',
        'DIR': 'Ettirgen Çatı',
        'TIR': 'Ettirgen Çatı',
        'IS': 'İşteş Çatı',
        'US': 'İşteş Çatı',
        'IN': 'Dönüşlü Çatı',
        'UN': 'Dönüşlü Çatı',
        'CE': 'Karşılaştırma Eki',
        'CA': 'Karşılaştırma Eki',
        'EN': 'Üstünlük Eki',
        'MEK': 'Mastar Eki',
        'MAK': 'Mastar Eki',
        'AN': 'Sıfat-Fiil Eki',
        'EN': 'Sıfat-Fiil Eki',
        'ME': 'İsim-Fiil Eki',
        'MA': 'İsim-Fiil Eki',
        'CE': 'Zarf Eki',
        'CA': 'Zarf Eki',
        'MI': 'Soru Eki',
        'MU': 'Soru Eki',
        'MÜ': 'Soru Eki',
        'MIS': 'Soru Eki',
        'MUS': 'Soru Eki',
        'MÜS': 'Soru Eki',
        'MA': 'Olumsuzluk Eki',
        'ME': 'Olumsuzluk Eki',
        'MIZ': '1. Çoğul Şahıs',
        'MÜZ': '1. Çoğul Şahıs',
        'SINIZ': '2. Çoğul Şahıs',
        'SÜNÜZ': '2. Çoğul Şahıs',
        'LAR': 'Çoğul Eki',
        'LER': 'Çoğul Eki',
        'IN': 'İyelik Eki',
        'UN': 'İyelik Eki',
        'ÜN': 'İyelik Eki',
        'IN': 'Belirtme Durumu',
        'UN': 'Belirtme Durumu',
        'ÜN': 'Belirtme Durumu',
        'A': 'Yönelme Durumu',
        'E': 'Yönelme Durumu',
        'DA': 'Bulunma Durumu',
        'DE': 'Bulunma Durumu',
        'DAN': 'Ayrılma Durumu',
        'DEN': 'Ayrılma Durumu',
        'LA': 'Araç Durumu',
        'LE': 'Araç Durumu',
        'IN': 'İyelik Durumu',
        'UN': 'İyelik Durumu',
        'ÜN': 'İyelik Durumu'
    }
    
    # Eğer suffix meanings sözlüğünde yoksa, suffix'i olduğu gibi döndür
    return meanings.get(suffix, suffix)
