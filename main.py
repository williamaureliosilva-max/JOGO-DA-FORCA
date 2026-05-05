from jogo import ESTADOS_FORCA, inicializar_jogo, processar_chute

def executar():
    palavra_secreta, letras_descobertas, tentativas, letras_tentadas = inicializar_jogo()
    
    print("--- JOGO DA FORCA (ROBUSTO) ---")
    
    while tentativas > 0 and "_" in letras_descobertas:
        print(ESTADOS_FORCA[tentativas])
        print(f"Palavra: {' '.join(letras_descobertas)}")
        print(f"Tentativas restantes: {tentativas}")
        
        try:
            chute = input("\nDigite uma letra: ").upper().strip()
            
            # Testes de robustez (Tratamento de erros)
            if not chute:
                raise ValueError("O campo não pode estar vazio!")
            if len(chute) > 1:
                raise ValueError("Introduz apenas uma única letra!")
            if not chute.isalpha():
                raise ValueError("Introduz apenas letras (A-Z)!")

            # Se passar nos testes acima, o jogo processa a letra
            tentativas, acerto, msg = processar_chute(chute, palavra_secreta, letras_descobertas, tentativas, letras_tentadas)
            print(msg)
            
        except ValueError as erro:
            print(f">> ERRO DETETADO: {erro}")

    if "_" not in letras_descobertas:
        print(f"\nPARABÉNS! Ganhaste. A palavra era: {palavra_secreta}")
    else:
        print(ESTADOS_FORCA[0])
        print(f"\nGAME OVER! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    executar()
