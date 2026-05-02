import random

# Visualização da Forca (Saída/Output)
ESTADOS_FORCA = [
    """
       +---+

       |   |
       O   |
      /|\\  |
      / \\  |

           |
    =========""",  # 0 tentativas restantes
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |

           |
    =========""",  # 1 tentativa restante
    """
       +---+
       |   |
       O   |
      /|\\  |

           |
           |
    =========""",  # 2 tentativas restantes
    """
       +---+

       |   |
       O   |
      /|   |

           |
           |
    =========""",  # 3 tentativas restantes
    """
       +---+

       |   |
       O   |

       |   |
           |

           |
    =========""",  # 4 tentativas restantes
    """
       +---+
       |   |
       O   |

           |
           |
           |
    =========""",  # 5 tentativas restantes
    """
       +---+

       |   |
           |

           |
           |
           |
    ========="""   # 6 tentativas restantes (Início)
]

def jogar():
    # Configuração Inicial
    palavras = ["PYTHON", "GITHUB", "ALGORITMO", "PROGRAMACAO", "COMPUTADOR", "VARIAVEL"]
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra_secreta]
    tentativas = 6
    letras_tentadas = []

    print("="*30)
    print("      JOGO DA FORCA")
    print("="*30)

    while tentativas > 0 and "_" in letras_descobertas:
        print(ESTADOS_FORCA[tentativas])
        print(f"\nPalavra: {' '.join(letras_descobertas)}")
        print(f"Tentativas: {tentativas}")
        print(f"Letras já usadas: {', '.join(letras_tentadas)}")
        
        # Entrada do Utilizador (Input)
        chute = input("\nDigite uma letra: ").upper().strip()

        # Validação básica
        if len(chute) != 1 or not chute.isalpha():
            print(">> ERRO: Digite apenas UMA letra!")
            continue

        if chute in letras_tentadas:
            print(f">> Já tentaste a letra {chute}!")
            continue
        
        letras_tentadas.append(chute)

        # Processamento do palpite
        if chute in palavra_secreta:
            print(f">> BOA! A letra {chute} existe na palavra.")
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[i] = chute
        else:
            print(f">> QUE PENA! A letra {chute} não existe.")
            tentativas -= 1

    # Resultado Final
    if "_" not in letras_descobertas:
        print("\n" + "="*30)
        print(f"PARABÉNS! Ganhaste!\nA palavra era: {palavra_secreta}")
        print("="*30)
    else:
        print(ESTADOS_FORCA[0])
        print("\n" + "="*30)
        print(f"GAME OVER! Perdeste.\nA palavra era: {palavra_secreta}")
        print("="*30)

if __name__ == "__main__":
    jogar()


