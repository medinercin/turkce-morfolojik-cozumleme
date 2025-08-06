import sys
sys.path.append('TurkishMorphologicalAnalysis')
from TurkishMorphologicalAnalysis.MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from analyzer.analyzer_core import get_morphological_breakdown

# Debug edilmeyecektir
word = 'edilmeyecektir'
morph = FsmMorphologicalAnalyzer()

print(f"Debugging word: {word}")
print("=" * 40)

try:
    result = morph.morphologicalAnalysis(word)
    if result and result.size() > 0:
        parse = result.getFsmParse(0)
        root = parse.getWord().getName()
        surface = parse.getSurfaceForm()
        surface_suffix = surface[len(root):] if surface.startswith(root) else ""
        
        print(f"Root: {root}")
        print(f"Surface Form: {surface}")
        print(f"Surface Suffix: '{surface_suffix}'")
        
        # Test our breakdown function
        breakdown = get_morphological_breakdown(word, root, surface_suffix)
        print(f"Our Breakdown: {breakdown}")
        
    else:
        print("No analysis found")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 40) 