import sys
sys.path.append('TurkishMorphologicalAnalysis')
from TurkishMorphologicalAnalysis.MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

# Debug edilmeyecektir
word = 'edilmeyecektir'
morph = FsmMorphologicalAnalyzer()

print(f"Debugging word: {word}")
print("=" * 40)

try:
    result = morph.morphologicalAnalysis(word)
    if result and result.size() > 0:
        parse = result.getFsmParse(0)
        print(f"Parse: {parse}")
        print(f"Root: {parse.getWord().getName()}")
        print(f"Surface Form: {parse.getSurfaceForm()}")
        
        for i in range(parse.size()):
            group = parse.getInflectionalGroup(i)
            print(f"Group {i}: {group}")
    else:
        print("No analysis found")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 40) 