class Solution:
    off = [6, -7, 6, 8]

    def encode(self, strs: List[str]) -> str:
        e_strs = []
        for s in strs:
            e_s = ""
            for i in range(len(s)):
                e_c = chr(ord(s[i]) + self.off[i % len(self.off)])
                e_s += e_c
            e_strs.append(e_s)
        if e_strs == []:
            return "prazno"
        e_str = "presledek".join(e_strs)
        return e_str

    def decode(self, s: str) -> List[str]:
        if s == "prazno":
            return []
        d_strs = []
        e_strs = s.split("presledek")
        for e_s in e_strs:
            d_s = ""
            for i in range(len(e_s)):
                d_c = chr(ord(e_s[i]) - self.off[i % len(self.off)])
                d_s += d_c
            d_strs.append(d_s)
        return d_strs
