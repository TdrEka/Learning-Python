
translations = {
    "hola": {"en": "hello", "de": "hallo"},
    "patata": {"en": "potato", "de": "kartoffel"},
    "ambulancia": {"en": "ambulance", "de": "krankenwagen"}
}

def translate(word, language = "en"):
    if word.lower() not in translations:
        return "nu-uh"
    elif language.lower() not in translations[word]:
        return "terrible"
    else:
        return translations[word.lower()][language.lower()]

