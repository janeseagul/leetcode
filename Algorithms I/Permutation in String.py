def checkInclusion(self, s1: str, s2: str) -> bool:
    freq1 = {}
    for c in s1:
        freq1[c] = freq1.get(c, 0) + 1
    s2_window = s2[:len(s1)]
    freq2 = {}
    for c in s2_window:
        freq2[c] = freq2.get(c, 0) + 1
    if freq1 == freq2:
        return True

    for i in range(len(s1), len(s2)):
        freq2[s2_window[0]] -= 1
        if freq2[s2_window[0]] == 0:
            del freq2[s2_window[0]]
        s2_window = s2_window[1:] + s2[i]
        freq2[s2[i]] = freq2.get(s2[i], 0) + 1
        if freq1 == freq2:
            return True
    return False