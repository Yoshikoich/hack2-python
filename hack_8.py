"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""



def fn_hack_8(s):
    result = []
    length = len(s)
    
    # Manejar el caso cuando hay más de un elemento
    if length > 1:
        for i in range(length):
            result.append(str(length - i))
    else:
        result.append(str(length))

    return result