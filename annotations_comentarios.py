import math

def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

print(circunferencia(8))
# 50.26548245743669

# É recomendado não fazer type hint no comentário, pois o mypy não pega

def cabecalho1(texto,  alinhamento=True)
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

def cabecalho2(
        texto,  # type: str
        alinhamento=True,  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

nome = 'Geek University'  # type: str


