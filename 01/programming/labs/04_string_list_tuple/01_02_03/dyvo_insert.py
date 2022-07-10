def dyvo_insert(sentence, flag):
    """
    Inserting word "диво" before every word that starts with flag.
    (str, str) -> str
    Return the result.
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "ки")
    дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті
    """
    sentence = sentence.lower()
    repl = "дивоки"
    amount = sentence.count("ки")
    sentence = sentence.replace(flag, repl, amount)
    print(sentence)


dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "ки")
