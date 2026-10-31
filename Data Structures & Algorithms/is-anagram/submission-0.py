class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = self.count(s)
        t_counter = self.count(t)
        is_anagram = self.check(s_counter, t_counter) and self.check(t_counter, s_counter)
        return is_anagram

    def count(self, s):
        counter = {}
        for c in s:
            if c in counter.keys():
                counter[c] += 1
            else:
                counter[c] = 1
        return counter

    def check(self, counter_1, counter_2):
        for c in counter_1.keys():
            if c not in counter_2.keys() or counter_1[c] != counter_2[c]:
                return False
            else:
                continue
        return True
