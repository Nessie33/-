def single_root_words(root_words, *other_words):
    same_words = []
    root = root_words.lower()
    other = [x.lower() for x in other_words]
    for i in other:
        if i in root or root in i:
            same_words.append(i)
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
