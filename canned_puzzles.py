

def easy_1():
    rawdata = [None,None,None,2,6,None,7,None,1,
            6,8,None,None,7,None,None,9,None,
            1,9,None,None,None,4,5,None,None,
            8,2,None,1,None,None,None,4,None,
            None,None,4,6,None,2,9,None,None,
            None,5,None,None,None,3,None,2,8,
            None,None,9,3,None,None,None,7,4,
            None,4,None,None,5,None,None,3,6,
            7,None,3,None,1,8,None,None,None,]
    data = []
    for ii in rawdata:
        if ii is None:
            data.append(ii)
        else:
            data.append(ii - 1)
    return data

def easy_1_answer():
    rawdata = [4,3,5,2,6,9,7,8,1,
            6,8,2,5,7,1,4,9,3,
            1,9,7,8,3,4,5,6,2,
            8,2,6,1,9,5,3,4,7,
            3,7,4,6,8,2,9,1,5,
            9,5,1,7,4,3,6,2,8,
            5,1,9,3,2,6,8,7,4,
            2,4,8,9,5,7,1,3,6,
            7,6,3,4,1,8,2,5,9,]
    return list(map(lambda k: k-1, rawdata))

def hard_1():
    """provides "Vegard Hanssen puzzle 2155141"
    """
    rawdata = [
        None,None,None, 6,None,None, 4,None,None,
        7,None,None, None,None,3, 6,None,None,
        None,None,None, None,9,1, None,8,None,

        None,None,None,None,None,None,None,None,None,
        None,5,None, 1,8,None, None,None,3,
        None,None,None, 3,None,6, None,4,5,

        None,4,None, 2,None,None, None,6,None,
        9,None,3, None,None,None, None,None,None,
        None,2,None, None,None,None, 1,None,None]
    data = []
    for ii in rawdata:
        if ii is None:
            data.append(ii)
        else:
            data.append(ii - 1)
    return data

def hard_1_answer():
    """solution to the "Vegard Hanssen puzzle 2155141"
    """
    rawdata = [
        5,8,1, 6,7,2, 4,3,9,
        7,9,2, 8,4,3, 6,5,1,
        3,6,4, 5,9,1, 7,8,2,

        4,3,8, 9,5,7, 2,1,6,
        2,5,6, 1,8,4, 9,7,3,
        1,7,9, 3,2,6, 8,4,5,

        8,4,5, 2,1,9, 3,6,7,
        9,1,3, 7,6,8, 5,2,4,
        6,2,7, 4,3,5, 1,9,8]
    return list(map(lambda k:k-1, rawdata))
