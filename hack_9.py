"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(d):
    result = {}
    
    for key, value in d.items():
        # Convertir la primera letra de la clave a mayúscula
        new_key = key.capitalize()
        
        # Verificar si el valor comienza con la clave original
        if value.startswith(key):
            # Formatear el nuevo valor
            new_value = new_key + value[len(key):]
            # Insertar en el diccionario resultado solo si cumple el criterio
            if new_key not in result:
                result[new_key] = new_value
    
    # Asegurarse de que el resultado final cumpla con las expectativas
    # Eliminamos cualquier entrada que no cumpla el criterio
    final_result = {k: v for k, v in result.items() if v.startswith(k)}
    
    return final_result

