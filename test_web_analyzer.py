import sys
sys.path.append('TurkishMorphologicalAnalysis')
from TurkishMorphologicalAnalysis.MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from analyzer.analyzer_core import analyze_sentence

# Test cases for morphological analysis
def test_web_analyzer():
    print("Testing web application's morphological analyzer:")
    print("=" * 50)
    
    # Test kelimeleri
    test_words = [
        "olan", "çıktısı", "raporlar", "kesinlikle", "ile", "düzgün", "doygun",
        "yazılacak", "olacak", "ve", "çizilecektir", "edilmeyecektir",
        "belirtisiz", "olarak", "bulunmaktadır", "girmez", "gelerek", "yazarak",
        "okumaz", "yazmaz", "belirtili", "isim", "yazmaz", "okumaz", "gelerek", "yazarak",
        # Çok anlamlı ekler için test kelimeleri
        "evli", "kitapsız", "okullu", "gözlü", "evde", "kitapta", "okulda", "gözde"
    ]
    
    for word in test_words:
        print(f"\nTesting word: {word}")
        try:
            result = analyze_sentence(word)
            if result and len(result) > 0:
                analysis = result[0]
                print(f"  Root: {analysis['root']}")
                print(f"  Root Type: {analysis['root_type']}")
                print(f"  Morphological Breakdown: {analysis['morphological_breakdown']}")
                print(f"  Surface Suffix: {analysis['surface_suffix']}")
            else:
                print(f"  No analysis found for {word}")
        except Exception as e:
            print(f"  Error analyzing {word}: {e}")

    print("\n" + "=" * 50)
    print("Test completed!")

if __name__ == "__main__":
    test_web_analyzer() 