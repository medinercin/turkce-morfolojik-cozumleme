import sys
sys.path.append('TurkishMorphologicalAnalysis')
from TurkishMorphologicalAnalysis.MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from analyzer.analyzer_core import analyze_sentence

# Test the web application's analyzer
test_words = ['olan', 'çıktısı', 'raporlar', 'kesinlikle', 'ile', 'düzgün', 'doygun', 'yazılacak', 'olacak', 've', 'çizilecektir', 'edilmeyecektir']

print("Testing web application's morphological analyzer:")
print("=" * 50)

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