"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    texto = "fooziman".replace("o", "0").replace("i", "1").replace("a", "@")
    texto = texto.upper()
    return list(texto)
63
print(fn_hack_10())
