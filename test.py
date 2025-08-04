from TurkishMorphologicalAnalysis.TurkishMorphology import TurkishMorphology

morph = TurkishMorphology.createWithDefaults()
result = morph.analyzeSentence("geldiler").getBestAnalysis()
print(result[0].formatLong())
