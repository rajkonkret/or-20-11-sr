from pprint import pprint


class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


art = LongestKeyDict()
print(art)
art['tomasz'] = 12
art['abraham'] = 7
art['zen'] = 1
print(art)
pprint(art)
# {'tomasz': 12, 'abraham': 7, 'zen': 1}
# {'abraham': 7, 'tomasz': 12, 'zen': 1}

print(art.longest_key())  # abraham
