"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10(texto="fooziman"):
    result = "fooziman"
    reemplazos = {'f': 'F', 'o': '0', 'z': 'Z', 'i': '1', 'm': 'M', 'a': '@', 'n': 'N'}

    result = [reemplazos.get(caracter, caracter) for caracter in texto]

    return result