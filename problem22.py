'''For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

def sentence_split(s, words):
    
    word_set = set(words)
    sentence_words = list()
    for i in range(len(s)):
        if s[0:i + 1] in word_set:
            sentence_words.append(s[0:i + 1])
            word_set.remove(s[0:i + 1])
            sentence_words += sentence_split(s[i + 1:], word_set)
            break

    return sentence_words

print(sentence_split("thequickbrownfox", ['quick', 'brown', 'the', 'fox']))
    
print(sentence_split("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))

