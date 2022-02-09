'''
Given a pattern and a string ``s``, find if s follows the same pattern.

Here follow means a full match: there is a bijection (unique one-to-one relationship) between a letter in pattern and a non-empty word in s.

For every word, there is a letter in pattern.
Patterns can be up to 300 length.
There are no leading or trailing spaces in s.
All words are separated by a single space.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """The keyword here is 'bijection' """
        tokens = s.split()

        if len(tokens) != len(pattern):
            return False

        bijection = {}
        seen = set()

        for i in range(len(pattern)):
            key = pattern[i]

            if key not in bijection:
                if tokens[i] not in seen:
                    bijection[key] = tokens[i]
                    seen.add(tokens[i])
                else:
                    return False

            elif bijection[key] != tokens[i]:
                    return False
        
        return True
