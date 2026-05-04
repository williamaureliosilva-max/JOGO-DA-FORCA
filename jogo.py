# Núcleo funcional do jogo da forca
import random

ESTADOS_FORCA = [
    """\n +---+\n |   |\n O   |\n/|\\  |\n/ \\  |\n     |\n=========""",
    """\n +---+\n |   |\n O   |\n/|\\  |\n/    |\n     |\n=========""",
    """\n +---+\n |   |\n O   |\n/|\\  |\n     |\n     |\n=========""",
    """\n +---+\n |   |\n O   |\n/|   |\n     |\n     |\n=========""",
    """\n +---+\n |   |\n O   |\n |   |\n     |\n     |\n=========""",
    """\n +---+\n |   |\n O   |\n     |\n     |\n     |\n=========""",
    """\n +---+\n |   |\n     |\n     |\n     |\n     |\n========="""
]

def inicializar_jogo():
    palavras = ["PYTHON", "GITHUB", "ALGORITMO", "MODULARIZACAO"]
    palavra = random.choice(palavras)
    return palavra, ["_" for _ in palavra], 6, []

def processar_chute(chute, palavra_secreta, letras_descobertas, tentativas, letras_tentadas):
    if chute in letras_tentadas:
        return tentativas, False, "Já tentaste essa letra!"
    
    letras_tentadas.append(chute)
    
    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_descobertas[i] = chute
        return tentativas, True, "Boa! A letra existe."
    else:
        return tentativas - 1, False, "Errado! Perdeste uma vida." 
