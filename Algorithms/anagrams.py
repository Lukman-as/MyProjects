def anagrams(S):
    d = {}
    for word in S:
        s = ''.join(sorted(word))
        if s in d:
            d[s].append(word)
        else:
            d[s] = [word]
    return([d[s] for s in d if len(d[s]) > 1])
# the above function has a time complexity of O(n*klog k)

string = "listen silent enlist inlets rat tar art god dog evil live veil vile"
words = [word.strip(",") for word in string.split()]
print(anagrams(words))
