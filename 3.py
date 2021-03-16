from collections import defaultdict 
def anagram(words):
    gw = defaultdict(list)
    for word in words:
        gw["".join(sorted(word))].append(word)
    for group in gw.values():
        print(" ".join(group))      

data=["nir","dha","ahd","irn"] 
anagram(data)