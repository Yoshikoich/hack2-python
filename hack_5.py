"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(s):
    result = []
    length = len(s)
    
    # Iterar en pares de caracteres
    for i in range(0, length, 2):
        # Añadir el par de caracteres (o el carácter solo si es el final)
        result.append(s[i:i+2])
    
    # Manejar el caso en el que queda un solo carácter al final
    if length % 2 != 0:
        result[-1] = result[-1][0] + '-'  # Reemplazar el último carácter con el carácter seguido de un guion
    
    # Convertir la lista en una cadena con guiones entre los pares
    return '-'.join(result)