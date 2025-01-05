def longest_consec(strarr, k):
    o = 0
    joined = []
    strarr.sort(key=len, reverse=True)
    if k <= 0 or k > len(strarr):
        return ""
    else:
        joined.extend(strarr[:k])
        joined = ''.join(joined)
        return joined
        
        
