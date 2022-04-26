"""For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal]."""

def match(s,l):
    results = set()
    l = set(l)
    for word in l:
        if word.startswith(s):
            results.add(word)
    return results

sub = 'de'
arr= ['dog', 'deer', 'deal']
res=match(sub,arr)
print(list(res))
