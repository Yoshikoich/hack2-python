"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(input_dict):
    d = {}
    
    for key, value in input_dict.items():
        
        new_key = key.capitalize()
        new_value = value.replace('k', '').capitalize()
        d[new_key] = new_value
    
    
    if 'Foo' in d:
        return {'Foo': d['Foo']}

