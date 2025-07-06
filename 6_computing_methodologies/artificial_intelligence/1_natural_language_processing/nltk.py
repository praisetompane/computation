from nltk.corpus import wordnet as wn

poses = {"n": "noun", "v": "verb"}

# synset = synonym set
# nltk = natural language tool kit

for synset in wn.synsets("good"):
    print(
        "{}: {}".format(
            poses[synset.pos()], ", ".join([lm.name() for lm in synset.lenmas()])
        )
    )
