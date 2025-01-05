def solution(flo):
    ans = str(flo)
    try:
        pos = ans.index(".")
        return int(ans[:pos])
    except: return flo