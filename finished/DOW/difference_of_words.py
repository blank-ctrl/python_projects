def difference_of_words(w1, w2):
    if not w1.isalpha() or not w2.isalpha(): 
        return "\nOnly letters of the english alphabet please\n"

# listing
    l_both = []
    l_unique = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

# processing
    class word:
        def __init__(self, word) -> None:
            self.word = word
            self.lenght = len(self.word)
            self.characters = []
            self.value = 0
            self.most_occuring_letter = []
            self.lettercount = {}
            self.alphabetic = None

        def processing(self):
            for i in self.word.lower():
                if i not in self.characters: self.characters.append(i)
                self.value += alphabet.index(i)+1
                self.lettercount.update({i : self.word.lower().count(i)})
            
            self.most_occuring_letter = max(self.lettercount, key=self.lettercount.get)
            self.characters.sort()
            self.isalphabetic()

        def isalphabetic(self):
            val = 0
            for e in self.word.lower():
                if alphabet.index(e) < val: 
                    self.alphabetic = False
                    break
                val = alphabet.index(e)
                self.alphabetic = True

    word1 = word(w1)
    word2 = word(w2)

    word1.processing()
    word2.processing()
    
    for i in word1.characters:
        if i in word2.characters and i not in l_both: l_both.append(i)
        elif i not in word2.characters and i not in l_unique: l_unique.append(i)
    
    for e in word2.characters:
        if e in word1.characters and e not in l_both: l_both.append(e)
        elif e not in word1.characters and e not in l_unique: l_unique.append(e)

    l_both.sort()
    l_unique.sort()

# making it readable
    if word1.lenght > word2.lenght: wl = f"Word one is longer than word two by {word1.lenght-word2.lenght} character(s)."
    elif word1.lenght < word2.lenght: wl = f"Word two is longer than word one by {word2.lenght-word1.lenght} character(s)."
    else: wl = f"Both words are {word1.lenght} character(s) long."

    if word1.value > word2.value: vl = f"Word one has a higher value than word two by {word1.value-word2.value}."
    elif word1.value < word2.value: vl = f"Word two has a higher value than word one by {word2.value-word1.value}."
    else: vl = f"Both words have a value of {word1.value}."

    if len(l_both) > 1: bl = f"The letters that are in both words are: {l_both}."
    elif len(l_both) == 1: bl = f"The letter that is in both words is: '{''.join(l_both)}'."
    else: bl = "There are no letters that occur in either word."

    if len(l_unique) > 1: ul = f"The letters that are unique in either word are: {l_unique}."
    elif len(l_unique) == 1: ul = f"The letter that is unique in one word is: '{''.join(l_unique)}'."
    else: ul = "There are no letters that are unique in either word."

# return it
    return f"""
            Word one: 
            lenght: {word1.lenght}
            characters: {word1.characters}
            value: {word1.value}
            most prominent/occuring letter: '{word1.most_occuring_letter}' ({word1.lettercount.get(word1.most_occuring_letter)}x)
            letters are in alphabetical order: {word1.alphabetic}
            \n
            Word two: 
            lenght: {word2.lenght}
            characters: {word2.characters}
            value: {word2.value}
            most prominent/occuring letter: '{word2.most_occuring_letter}' ({word2.lettercount.get(word2.most_occuring_letter)}x)
            letters are in alphabetical order: {word2.alphabetic}
            \n
            Comparison:
            {wl}
            {vl}
            {bl}
            {ul}
            """

print(difference_of_words(input("Word one: \n"), input("Word two: \n")))