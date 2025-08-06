import sys
sys.path.append('TurkishMorphologicalAnalysis')
from TurkishMorphologicalAnalysis.MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from analyzer.analyzer_core import analyze_sentence

# Test words
test_words = ['olan', 'çıktısı', 'raporlar', 'kesinlikle', 'ile', 'düzgün', 'doygun', 'yazılacak', 'olacak', 've', 'çizilecektir', 'edilmeyecektir']

print("Comparing Terminal vs Web Application Analyzers:")
print("=" * 60)

# Terminal analyzer
terminal_morph = FsmMorphologicalAnalyzer()

for word in test_words:
    print(f"\nWord: {word}")
    print("-" * 30)
    
    # Terminal analyzer result
    print("Terminal Analyzer:")
    try:
        terminal_result = terminal_morph.morphologicalAnalysis(word)
        if terminal_result and terminal_result.size() > 0:
            terminal_parse = terminal_result.getFsmParse(0)
            print(f"  Result: {terminal_parse}")
        else:
            print("  No analysis found")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Web application analyzer result
    print("Web Application Analyzer:")
    try:
        web_result = analyze_sentence(word)
        if web_result and len(web_result) > 0:
            web_analysis = web_result[0]
            print(f"  Root: {web_analysis['root']}")
            print(f"  Root Type: {web_analysis['root_type']}")
            print(f"  Morphological Breakdown: {web_analysis['morphological_breakdown']}")
            print(f"  Surface Suffix: {web_analysis['surface_suffix']}")
        else:
            print("  No analysis found")
    except Exception as e:
        print(f"  Error: {e}")

print("\n" + "=" * 60)
print("Comparison completed!") 