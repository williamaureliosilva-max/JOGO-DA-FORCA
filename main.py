from jogo import ESTADOS_FORCA, inicializar_jogo, processar_chute

def executar():
    palavra_secreta, letras_descobertas, tentativas, letras_tentadas = inicializar_jogo()
    
    print("--- JOGO DA FORCA (MODULAR) ---")
    
    while tentativas > 0 and "_" in letras_descobertas:
        print(ESTADOS_FORCA[tentativas])
        print(f"Palavra: {' '.join(letras_descobertas)}")
        print(f"Tentativas: {tentativas}")
        
        chute = input("Digite uma letra: ").upper().strip()
        
        if len(chute) == 1 and chute.isalpha():
            tentativas, acerto, msg = processar_chute(chute, palavra_secreta, letras_descobertas, tentativas, letras_tentadas)
            print(msg)
        else:
            print("Entrada inválida!")

    if "_" not in letras_descobertas:
        print(f"\nParabéns! Ganhaste. A palavra era: {palavra_secreta}")
    else:
        print(ESTADOS_FORCA[0])
        print(f"\nPerdeste! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    executar() 
