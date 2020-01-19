def isreverse(s1, s2):

    # Case 1: Parameters must be the same length
    s1Length = len(s1)
    s2Length = len(s2)
    s1List = list(s1)
    s2List = list(s2)
    done = False
    result = False
    if s1Length == s2Length:
        # Case 2: If parameters are the same 1 letter string, or nothing return true
        if s1Length == 0 or (s1Length == 1 and s1 == s2):
            done = True
            result = True
        # Case 3: Check if external letters are the same, then pop them and loop
        elif s1List[0] == s2List[len(s2List)-1] and done is not True:
            s1List.pop(0)
            s2List.pop(len(s2List)-1)
            isreverse(s1List, s2List)
            result = True
    return result
