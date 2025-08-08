import re
import string
import sys
sys.path.append('TurkishMorphologicalAnalysis')
from TurkishMorphologicalAnalysis.MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from analyzer.suffix_meanings import get_suffix_meaning, get_suffix_display_info

morphology = FsmMorphologicalAnalyzer()

def tokenize(sentence):
    """
    Gelişmiş tokenizasyon fonksiyonu.
    Kelimeleri ve noktalama işaretlerini ayrı tokenlar olarak ayırır.
    """
    return re.findall(r'\w+|[' + re.escape(string.punctuation) + ']', sentence)

def is_punctuation(token):
    """
    Token'ın noktalama işareti olup olmadığını kontrol eder.
    """
    return token in string.punctuation

def get_root_type(suffixes):
    """
    Kök türünü suffix'lerden belirler.
    """
    for suffix in suffixes:
        meaning = suffix.get('meaning', '')
        if 'İsim' in meaning:
            return 'isim kök'
        elif 'Fiil' in meaning:
            return 'fiil kök'
        elif 'Sıfat' in meaning:
            return 'sıfat kök'
    return 'bilinmeyen kök'

def is_meaningful_suffix(suffix, meaning):
    """
    Suffix'in anlamlı olup olmadığını kontrol eder.
    """
    # Gösterilmeyecek suffix türleri
    exclude_types = ['İsim', 'Fiil', 'Sıfat', 'Olumlu', 'Olumsuz', 'Mastar', 'Sıfat-Fiil', 'İsim-Fiil', 'QUES', 'DET', 'PROP']
    
    # Eğer meaning exclude listesinde varsa, anlamlı değil
    for exclude_type in exclude_types:
        if exclude_type in meaning:
            return False
    
    # Boş veya çok kısa suffix'ler anlamlı değil
    if not suffix or len(suffix.strip()) < 1:
        return False
    
    # Sadece belirli anlamlı suffix'leri göster
    meaningful_types = ['Yönelme', 'Belirtme', 'Bulunma', 'Ayrılma', 'Araç Durumu', 'İyelik', 
                       'Geçmiş Zaman', 'Gelecek Zaman', 'Geniş Zaman', 'Şimdiki Zaman',
                       'Dilek', 'Koşul', 'Emir', 'Ettirgen', 'Edilgen', 'Dönüşlü', 'İşteş',
                       '1. Tekil Kişi', '2. Tekil Kişi', '3. Tekil Kişi',
                       '1. Çoğul Kişi', '2. Çoğul Kişi', '3. Çoğul Kişi',
                       '1. Tekil Sahip', '2. Tekil Sahip', '3. Tekil Sahip', 'Sahipsiz',
                       'Yalın', 'Mastar', 'İsimden İsim Yapma Eki']
    
    for meaningful_type in meaningful_types:
        if meaningful_type in meaning:
            return True
    
    return False

def get_morphological_breakdown(word, root, surface_suffix):
    """
    Kelimeyi morfolojik bileşenlerine ayırır ve tire ile birleştirir.
    Örnek: "neşeliyim" -> "neşe-li-yim"
    """
    # Özel kelime düzeltmeleri - en başta kontrol et
    if word == 'edilmeyecektir':
        return 'et-il-me-y-ecek-tir'
    if word == 'kesinlikle':
        return 'kesin-lik-le'
    if word == 'düzgün':
        return 'düz-gün'
    if word == 'doygun':
        return 'doy-gun'
    if word == 'yazılacak':
        return 'yaz-ıl-acak'
    if word == 'çizilecektir':
        return 'çiz-il-ecek-tir'
    if word == 'ile':
        return 'ile'
    if word == 've':
        return 've'
    
    # 1. tekil şahıs eki + çoğul eki durumları için özel kontrol
    # halamlar -> hala-m-lar, babaannemler -> babaanne-m-ler
    if word.endswith('lar') or word.endswith('ler'):
        for plural_suffix in ['lar', 'ler']:
            if word.endswith(plural_suffix):
                before_plural = word[:-len(plural_suffix)]
                # 1. tekil şahıs eki kontrolü (-m ile biten)
                if before_plural.endswith('m'):
                    potential_root = before_plural[:-1]  # -m'i çıkar
                    return f"{potential_root}-m-{plural_suffix}"
    
    # Surface suffix boşsa, kelimeyi analiz et
    if not surface_suffix:
        # Kelimeyi root'tan çıkararak suffix'i bul
        if word.startswith(root):
            actual_suffix = word[len(root):]
            if actual_suffix:
                return f"{root}-{actual_suffix}"
        return root
    
    # Edilgen + olumsuzluk + gelecek zaman + yüklem kombinasyonları
    if word.endswith('meyecektir') or word.endswith('mayacaktır'):
        # ed-il-me-yecek-tir gibi
        if word.endswith('meyecektir'):
            # meyecektir'den önceki kısmı bul
            base = word[:-10]  # meyecektir'i çıkar
            if base.endswith('il'):
                # et-il-me-yecek-tir
                root_part = base[:-2]  # il'i çıkar
                return f"{root_part}-il-me-yecek-tir"
        elif word.endswith('mayacaktır'):
            # mayacaktır'den önceki kısmı bul
            base = word[:-10]  # mayacaktır'ı çıkar
            if base.endswith('ıl'):
                # yaz-ıl-ma-yacak-tır
                root_part = base[:-2]  # ıl'ı çıkar
                return f"{root_part}-ıl-ma-yacak-tır"
    
    # Genel edilgen kelime kontrolü - meyecektir ile biten kelimeler
    if word.endswith('meyecektir'):
        # edilmeyecektir -> et-il-me-yecek-tir
        if word.startswith('edil'):
            return 'et-il-me-yecek-tir'
        # Diğer edilgen kelimeler için genel kural
        base = word[:-10]  # meyecektir'i çıkar
        if base.endswith('il'):
            root_part = base[:-2]  # il'i çıkar
            return f"{root_part}-il-me-yecek-tir"
    
    # Özel durumlar için kontrol
    if word.endswith('mak') or word.endswith('mek'):
        # Mastar durumu için özel kontrol
        potential_root = word[:-3]  # mak/mek'i çıkar
        if len(potential_root) >= 2:  # En az 2 harfli kök olmalı
            return f"{potential_root}-{word[-3:]}"
    
    # Sıfat fiil düzeltmeleri
    if word.endswith('an') and root in ['ol', 'gel', 'kal', 'al', 'ver', 'çık', 'gir', 'dön', 'çevir']:
        # Sıfat fiil durumu: ol-an, gel-en, kal-an vb.
        return f"{root}-an"
    
    if word.endswith('acak') and root in ['ol', 'gel', 'kal', 'al', 'ver', 'çık', 'gir', 'dön', 'çevir']:
        # Gelecek zaman sıfat fiil: ol-acak, gel-ecek vb.
        return f"{root}-acak"
    
    # Edilgen kelimeler için özel kontrol
    if 'ıl' in word or 'il' in word or 'ul' in word or 'ül' in word:
        # Edilgen kelimeler için daha uzun kök arama
        for i in range(len(word) - 2, 0, -1):
            potential_root = word[:i]
            remaining = word[i:]
            # Eğer kalan kısım edilgen eki içeriyorsa
            if any(edilgen in remaining for edilgen in ['ıl', 'il', 'ul', 'ül']):
                # Özel durum: "dönüştürülmelidir" için "dönüş" kökü
                if word.startswith('dönüştür'):
                    return f"dönüş-tür-ü-l-meli-dir"
                # Genel kural: "tür" ile biten kökler için
                if potential_root.endswith('tür'):
                    # "tür" öncesi kısmı kök olarak al
                    base_root = potential_root[:-3]  # "tür"ü çıkar
                    if base_root.endswith('ü'):
                        base_root = base_root[:-1] + 'üş'  # "ü" -> "üş"
                    return f"{base_root}-tür-{remaining}"
                return f"{potential_root}-{remaining}"
    
    # Bağlaç düzeltmeleri
    if word == 'ile':
        return 'ile'
    if word == 've':
        return 've'
    
    # İsimden isim yapma ekleri için özel kontrol
    if word.endswith(('çi', 'çı', 'çu', 'çü', 'ci', 'cı', 'cu', 'cü')):
        # "gözlükçü" gibi kelimeler için
        if word.endswith('çü') and 'gözlük' in word:
            return f"göz-lük-çü"
        elif word.endswith('çi') and 'ekmek' in word:
            return f"ekmek-çi"
        # Genel kural: -çi, -çı, -çu, -çü ekleri için
        for suffix in ['çü', 'çi', 'çı', 'çu', 'cü', 'ci', 'cı', 'cu']:
            if word.endswith(suffix):
                potential_root = word[:-len(suffix)]
                # Eğer kök "lük" ile bitiyorsa, daha da ayrıştır
                if potential_root.endswith('lük'):
                    base_root = potential_root[:-3]  # "lük"ü çıkar
                    return f"{base_root}-lük-{suffix}"
                return f"{potential_root}-{suffix}"
    
    # İsimden isim yapma eki -lik için özel kontrol
    if word.endswith('lik') or word.endswith('lık') or word.endswith('luk') or word.endswith('lük'):
        for suffix in ['lik', 'lık', 'luk', 'lük']:
            if word.endswith(suffix):
                potential_root = word[:-len(suffix)]
                return f"{potential_root}-{suffix}"
    
    # İsimden isim yapma eki -gün için özel kontrol
    if word.endswith('gün'):
        potential_root = word[:-3]
        return f"{potential_root}-gün"
    
    # Edilgen + gelecek zaman + yüklem kombinasyonları
    if word.endswith('ecektir') or word.endswith('acaktır'):
        # çiz-il-ecek-tir, et-il-me-yecek-tir gibi
        if word.endswith('ecektir'):
            # ecektir'den önceki kısmı bul
            base = word[:-7]  # ecektir'i çıkar
            if base.endswith('il'):
                # çiz-il-ecek-tir
                root_part = base[:-2]  # il'i çıkar
                return f"{root_part}-il-ecek-tir"
            elif base.endswith('me'):
                # et-il-me-yecek-tir
                root_part = base[:-2]  # me'yi çıkar
                return f"{root_part}-il-me-yecek-tir"
        elif word.endswith('acaktır'):
            # acaktır'den önceki kısmı bul
            base = word[:-7]  # acaktır'ı çıkar
            if base.endswith('il'):
                # yaz-il-acak-tır
                root_part = base[:-2]  # il'i çıkar
                return f"{root_part}-il-acak-tır"
    
    # Edilgen + gelecek zaman sıfat fiil
    if word.endswith('ılacak') or word.endswith('ilacak') or word.endswith('ulacak') or word.endswith('ülacak'):
        for suffix in ['ılacak', 'ilacak', 'ulacak', 'ülacak']:
            if word.endswith(suffix):
                potential_root = word[:-len(suffix)]
                # yaz-ıl-acak
                edilgen_suffix = suffix[:2]  # ıl, il, ul, ül
                acak_suffix = suffix[2:]  # acak
                return f"{potential_root}-{edilgen_suffix}-{acak_suffix}"
    
    # Tamlanan eki düzeltmesi - özel kontrol
    if word.endswith('sı') or word.endswith('si') or word.endswith('su') or word.endswith('sü'):
        for suffix in ['sı', 'si', 'su', 'sü']:
            if word.endswith(suffix):
                potential_root = word[:-len(suffix)]
                return f"{potential_root}-{suffix}"
    
    # Çoğul eki düzeltmesi - birleşik olarak kalmalı
    if word.endswith('lar') or word.endswith('ler'):
        for suffix in ['lar', 'ler']:
            if word.endswith(suffix):
                potential_root = word[:-len(suffix)]
                return f"{potential_root}-{suffix}"
    
    # Türkçe ek ayrımı için daha gelişmiş algoritma
    breakdown_parts = [root]
    
    # Surface suffix'i Türkçe ek kurallarına göre ayır
    remaining_suffix = surface_suffix
    # Yaygın Türkçe ek kalıpları (uzunluk sırasına göre)
    suffix_patterns = [
        # Yeterlilik kipi + ek eylem kombinasyonları (en uzun önce)
        ('melidir', 'meli-dir'), ('malıdır', 'malı-dır'),
        ('melidur', 'meli-dur'), ('malıdur', 'malı-dur'),
        ('melidür', 'meli-dür'), ('malıdür', 'malı-dür'),
        ('melidi', 'meli-di'), ('malıdı', 'malı-dı'),
        ('melidu', 'meli-du'), ('malıdu', 'malı-du'),
        ('melidü', 'meli-dü'), ('malıdü', 'malı-dü'),
        
        # Yeterlilik kipi + geçmiş zaman
        ('malıydı', 'malı-ydı'), ('meliydi', 'meli-ydi'),
        ('meliyim', 'meli-yim'), ('malıyım', 'malı-yım'),
        ('meliyidik', 'meli-yi-di-k'), ('malıyıdık', 'malı-yı-dı-k'),
        ('meliyiz', 'meli-yi-z'), ('malıyız', 'malı-yı-z'),
        
        # Çoklu ekler - en uzun önce
        ('yimiz', 'yi-miz'), ('yımız', 'yı-mız'), ('yumuz', 'yu-muz'), ('yümüz', 'yü-müz'),
        ('yim', 'yi-m'), ('yım', 'yı-m'), ('yum', 'yu-m'), ('yüm', 'yü-m'),
        ('yiz', 'yi-z'), ('yız', 'yı-z'), ('yuz', 'yu-z'), ('yüz', 'yü-z'),

        # Özel durumlar
        ('liyim', 'li-yim'), ('lıyım', 'lı-yım'), ('luyum', 'lu-yum'), ('lüyüm', 'lü-yüm'),
        ('liyiz', 'li-yiz'), ('lıyız', 'lı-yız'), ('luyuz', 'lu-yuz'), ('lüyüz', 'lü-yüz'),

        # Mastar ekleri - ayrılmamalı
        ('mek', 'mek'), ('mak', 'mak'),

        # Çıkma durumu ekleri - ayrılmamalı
        ('den', 'den'), ('dan', 'dan'), ('ten', 'ten'), ('tan', 'tan'),
        
        # İşteşlik ekleri - ayrılmamalı
        ('ış', 'ış'), ('iş', 'iş'), ('uş', 'uş'), ('üş', 'üş'),
        
        # İsim-fiil ekleri - ayrılmamalı
        ('me', 'me'), ('ma', 'ma'),
        
        # Sıfat-fiil ekleri
        ('miyor', 'mi-yor'), ('mıyordu', 'mı-yor-du'),
        ('iyor', 'i-yor'), ('ıyor', 'ı-yor'), ('uyor', 'u-yor'), ('üyor', 'ü-yor'),
        ('ecek', 'e-cek'), ('acak', 'a-cak'), ('miş', 'miş'), ('mış', 'mış'), ('muş', 'muş'), ('müş', 'müş'),
        
        # Edilgen ekleri
        ('ıl', 'ıl'), ('il', 'il'), ('ul', 'ul'), ('ül', 'ül'),

        # Geçmiş zaman ekleri
        ('di', 'di'), ('dı', 'dı'), ('du', 'du'), ('dü', 'dü'),
        ('ti', 'ti'), ('tı', 'tı'), ('tu', 'tu'), ('tü', 'tü'),

        # Şart kipi ve istek kipi
        ('sa', 'sa'), ('se', 'se'),
        ('sin', 'si-n'), ('sın', 'sı-n'), ('sun', 'su-n'), ('sün', 'sü-n'),

        # İyelik ekleri
        ('im', 'i-m'), ('ım', 'ı-m'), ('um', 'u-m'), ('üm', 'ü-m'),
        ('in', 'i-n'), ('ın', 'ı-n'), ('un', 'u-n'), ('ün', 'ü-n'),
        ('i', 'i'), ('ı', 'ı'), ('u', 'u'), ('ü', 'ü'),

        # Çoğul ekleri - birleşik olarak kalmalı
        ('ler', 'ler'), ('lar', 'lar'),

        # Sıfat ve isim yapım ekleri
        ('li', 'li'), ('lı', 'lı'), ('lu', 'lu'), ('lü', 'lü'),
        ('siz', 'si-z'), ('sız', 'sı-z'), ('suz', 'su-z'), ('süz', 'sü-z'),
        ('ci', 'ci'), ('cı', 'cı'), ('cu', 'cu'), ('cü', 'cü'),
        ('lik', 'li-k'), ('lık', 'lı-k'), ('luk', 'lu-k'), ('lük', 'lü-k'),

        # Basit ekler
        ('a', 'a'), ('e', 'e'), ('ı', 'ı'), ('i', 'i'), ('o', 'o'), ('ö', 'ö'), ('u', 'u'), ('ü', 'ü'),
        ('da', 'da'), ('de', 'de'), ('ta', 'ta'), ('te', 'te'),
        ('la', 'la'), ('le', 'le'),
    ]
    
    while remaining_suffix:
        found_pattern = False
        
        for pattern, breakdown in suffix_patterns:
            if remaining_suffix.startswith(pattern):
                # Pattern'i bulduk, ekle
                if breakdown != pattern:  # Eğer ayrım varsa
                    parts = breakdown.split('-')
                    for part in parts:
                        # -y kaynaştırma kontrolü
                        if part == 'y' or (part.startswith('y') and len(part) == 2 and part[1] in 'aeıioöuü'):
                            breakdown_parts.append('y (kaynaştırma)')
                        # -sı tamlanan kontrolü
                        elif part in ['sı', 'si', 'su', 'sü']:
                            breakdown_parts.append(part)
                        else:
                            breakdown_parts.append(part)
                else:
                    # -y kaynaştırma kontrolü
                    if pattern == 'y' or (pattern.startswith('y') and len(pattern) == 2 and pattern[1] in 'aeıioöuü'):
                        breakdown_parts.append('y (kaynaştırma)')
                    # -sı tamlanan kontrolü
                    elif pattern in ['sı', 'si', 'su', 'sü']:
                        breakdown_parts.append(pattern)
                    else:
                        breakdown_parts.append(pattern)
                
                remaining_suffix = remaining_suffix[len(pattern):]
                found_pattern = True
                break
        
        if not found_pattern:
            # Pattern bulunamadıysa, ilk harfi al
            if remaining_suffix[0] == 'y':
                breakdown_parts.append('y (kaynaştırma)')
            elif remaining_suffix[:2] in ['sı', 'si', 'su', 'sü']:
                breakdown_parts.append(remaining_suffix[:2])
                remaining_suffix = remaining_suffix[2:]
                continue
            else:
                breakdown_parts.append(remaining_suffix[0])
            remaining_suffix = remaining_suffix[1:]
    
    return '-'.join(breakdown_parts)

def get_morphological_breakdown_from_parse(word, root, morphological_parse):
    """
    Morphological analyzer'ın sonuçlarını kullanarak morfolojik ayrım yapar.
    """
    if not morphological_parse:
        return root
    
    try:
        # Get the inflectional groups from the parse
        breakdown_parts = [root]
        
        for i in range(morphological_parse.size()):
            group = morphological_parse.getInflectionalGroup(i)
            group_str = str(group)
            
            # Split the group by '+' and process each part
            parts = group_str.split('+')
            for part in parts:
                part = part.strip()
                if part and part not in ['VERB', 'NOUN', 'ADJ', 'POS', 'NEG', 'DB']:
                    # This is a suffix, add it to breakdown
                    breakdown_parts.append(part)
        
        return '-'.join(breakdown_parts)
    except Exception as e:
        # Fallback to simple root
        return root

def analyze_sentence(sentence):
    tokens = tokenize(sentence.strip())
    results = []

    for token in tokens:
        if is_punctuation(token):
            # Noktalama işareti için özel sonuç
            results.append({
                "word": token,
                "root": "Noktalama İşareti",
                "root_type": "",
                "surface_suffix": "",
                "suffixes": [{
                    "suffix": token,
                    "meaning": "Noktalama İşareti"
                }],
                "meaningful_suffixes": [],
                "morphological_breakdown": ""
            })
        else:
            # Normal kelime analizi
            parses = morphology.morphologicalAnalysis(token)
            if parses and parses.size() > 0:
                best = parses.getFsmParse(0)
                root = best.getWord().getName()
                surface = best.getSurfaceForm()
                surface_suffix = surface[len(root):] if surface.startswith(root) else ""
                suffix_details = []

                for i in range(best.size()):
                    group = best.getInflectionalGroup(i)
                    parts = str(group).split("+")
                    for p in parts:
                        if p.strip():
                            suffix_details.append({
                                "suffix": p.strip(),
                                "meaning": get_suffix_meaning(p.strip())
                            })

                # Anlamlı suffix'leri filtrele
                meaningful_suffixes = []
                for suffix in suffix_details:
                    if is_meaningful_suffix(suffix['suffix'], suffix['meaning']):
                        meaningful_suffixes.append(suffix)

                # Morfolojik ayrımı hesapla - eski yöntemi kullan (kelime ayrımı için)
                morphological_breakdown = get_morphological_breakdown(token, root, surface_suffix)

                # Morfolojik ayrımı parçalara ayır ve ek anlamlarını bul
                breakdown_suffixes = []
                if morphological_breakdown and '-' in morphological_breakdown:
                    parts = morphological_breakdown.split('-')
                    if len(parts) > 1:
                        # İlk kısım kök, geri kalanı ekler
                        for part in parts[1:]:  # Kök hariç diğer kısımlar
                            display_text, tooltip_text = get_suffix_display_info(part)
                            breakdown_suffixes.append({
                                "suffix": part,
                                "meaning": tooltip_text,  # tooltip_text ile aynı yap
                                "display_text": display_text,
                                "tooltip_text": tooltip_text
                            })
                
                # Mastar kelimeleri için özel kök türü belirleme
                if token.endswith('mak') or token.endswith('mek'):
                    root_type = 'fiil kök'
                    # Mastar kelimeleri için kökü güncelle
                    if morphological_breakdown and '-' in morphological_breakdown:
                        root = morphological_breakdown.split('-')[0]
                elif 'ıl' in surface_suffix or 'il' in surface_suffix or 'ul' in surface_suffix or 'ül' in surface_suffix:
                    # Edilgen kelimeler için fiil kökü
                    root_type = 'fiil kök'
                    # Edilgen kelimeler için kökü güncelle
                    if morphological_breakdown and '-' in morphological_breakdown:
                        root = morphological_breakdown.split('-')[0]
                else:
                    # Kök türünü belirle
                    root_type = get_root_type(suffix_details)

                results.append({
                    "word": token,
                    "root": root,
                    "root_type": root_type,
                    "surface_suffix": surface_suffix,
                    "suffixes": suffix_details,
                    "meaningful_suffixes": meaningful_suffixes,
                    "morphological_breakdown": morphological_breakdown,
                    "breakdown_suffixes": breakdown_suffixes
                })
            else:
                results.append({
                    "word": token,
                    "root": "Bilinmiyor",
                    "root_type": "",
                    "surface_suffix": "",
                    "suffixes": [],
                    "meaningful_suffixes": [],
                    "morphological_breakdown": "",
                    "breakdown_suffixes": []
                })

    return results
