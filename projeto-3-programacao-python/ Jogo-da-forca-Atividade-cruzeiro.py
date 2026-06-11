import random                                                 # Importa a biblioteca random para selecionar palavras aleatoriamente da lista


def mostrar_forca(tentativas, letras_descobertas):
    """
    Exibe visualmente a forca e o estado atual da palavra.

    Args:
        tentativas: número de tentativas restantes.
        letras_descobertas: lista contendo as letras descobertas da palavra.

    Returns:
        Nenhum retorno.
    """

    erros = 6 - tentativas                                    # Calcula o número de erros com base nas tentativas restantes

    cabeca = "o" if erros >= 1 else " "                       # estrura condicional para mostrar a cabeça do boneco
    tronco = "|" if erros >= 2 else " "
    braco_esquerdo = "/" if erros >= 3 else " "
    braco_direito = "\\" if erros >= 4 else " "         
    perna_esquerda = "/" if erros >= 5 else " "
    perna_direita = "\\" if erros >= 6 else " "

    print("\n ______")
    print(" |    |")                                                # visualização da forca, utilizando a estrutura condicional para mostrar o boneco de acordo com o número de erros
    print(f" |    {cabeca}")                                                                   
    print(f" |   {braco_esquerdo}{tronco}{braco_direito}")
    print(f" |   {perna_esquerda} {perna_direita}")                
    print(" |")
    print("_|_")
    print("Palavra:", " ".join(letras_descobertas))                  # Mostra a palavra atual

def iniciar_jogo(palavras):                                
    """
    Inicializa os dados principais do jogo.

    Args:
        palavras: lista contendo as palavras possíveis para sorteio.

    Returns:
        palavra_secreta, letras_descobertas, palavras_tentadas e tentativas.
    """                        

    palavra_secreta = random.choice(palavras)                                       # Seleciona aleatoriamente uma palavra da lista para ser a palavra secreta do jogo
    letras_descobertas = ["_"] * len(palavra_secreta)                               # Cria uma lista de "_" com o mesmo comprimento da palavra secreta para representar as letras ainda não descobertas
    palavras_tentadas = set()                                                       # Foi escolhido set porque não permite letras repetidas, facilitando o controle das tentativas
    tentativas = 6                                                                  # Define o número de tentativas que o usuário tem para adivinhar a palavra, começando com 6 tentativas
    return palavra_secreta, letras_descobertas, palavras_tentadas, tentativas       # Retorna os elementos necessários para o jogo: a palavra secreta, a lista de letras descobertas, o conjunto de palavras tentadas e o número de tentativas restantes
    
def start_forca():
    """
    Exibe a tela inicial e as regras básicas do jogo.

    Args:
        Nenhum argumento.

    Returns:
        Nenhum retorno.
    """

    print("\n==============================")             
    print("       JOGO DA FORCA")                                     # Exibe o título do jogo, para visualização do usuário
    print("==============================")
    print("Adivinhe a palavra secreta.")                              # Exibe uma breve descrição do objetivo do jogo, para visualização do usuário
    print("Você tem 6 tentativas.")
    print("Digite uma letra por vez.")
    print("==============================\n")

    input("Pressione ENTER para iniciar...")

def processar_tentativa(letra_usuario, palavra_secreta, letras_descobertas):
    """
    Verifica se a letra digitada existe na palavra secreta.

    Args:
        letra_usuario: letra digitada pelo usuário.
        palavra_secreta: palavra escolhida pelo sistema.
        letras_descobertas: lista com letras já descobertas.

    Returns:
        True se a letra existir na palavra e False caso contrário.
    """

    acertou = False                                                   # Variável para controlar se o usuário acertou a letra ou não, inicialmente definida como False

    for posicao, letra in enumerate(palavra_secreta):                 # Loop que percorre cada letra da palavras secreta
        if letra == letra_usuario:                                    # Verifica se a letra digitada pelo usuário é igual à letra atual da palavra secreta
            letras_descobertas[posicao] = letra_usuario               # Atualiza a letra na possição correspondente dela na lista de letras descobertas 
            acertou = True                                            # Se a letra digitada for correta o valor de acertou é atualizado para True, indicando que o usuário acertou a letra

    return acertou                                                    # Retorna o valor de acertou, indicando se o usuário acertou ou não a letra digitada

# Lista das palavras do jogo, neste formato para boa visualização
palavras = [
    "PYTHON",                                                         # Lista contendo as possíveis palavras secretas do jogo
    "PROGRAMACAO",
    "ESTRUTURA",
    "DEPURACAO",
    "SNAKECASE"
]

jogar_novamente = "s"                                                 # Variável para controlar se o usuário deseja jogar novamente

# Loop principal do jogo, que continua enquanto o usuário desejar jogar novamente
while jogar_novamente == "s":

    palavra_secreta, letras_descobertas, palavras_tentadas, tentativas = iniciar_jogo(palavras)     # Chama a função iniciar_jogo para configurar o jogo e obter os elementos necessários para o jogo, como a palavra secreta, as letras descobertas, as palavras tentadas e as tentativas restantes

    start_forca()                                                                    # Chama a função start_forca para mostrar as regras do jogo e iniciar a interface do jogo, preparando o usuário para começar a jogar

    while tentativas > 0 and "_" in letras_descobertas:                              # Loop que continua enquanto o usuário tiver tentativas restantes, permitindo que o jogo continue até que o usuário vença ou perca

        mostrar_forca(tentativas, letras_descobertas)                                # Mostra ao usuário o estado atual do jogo, incluindo as tentativas restantes e as letras descobertas até o momento
        print(f"Tentativas restantes: {tentativas}")                                 # Exibe o número de tentativas restantes para o usuário, informando-o sobre quantas chances ainda tem para adivinhar a palavra secreta

        letra_usuario = input("Digite uma letra: ").upper()                          # Solicita ao usuário que digite uma letra e converte a entrada para maiúscula, e se minuscula ele converte para maiúscula

        if letra_usuario in palavras_tentadas:                                       # Verifica se a letra digitada pelo usuário já foi tentada anteriormente
            print(f"Você já tentou a letra {letra_usuario}, tente outra.")
            continue

        palavras_tentadas.add(letra_usuario)                                         #Adiciona a letra digitada pelo usuário ao conjunto de palavras tentadas, evita repetições

        acertou = processar_tentativa(letra_usuario, palavra_secreta, letras_descobertas)          # Chama a função para verificar se a letra digitada pelo usario está presente na palavra secreta e atualiza as letras descobertas e retorna se acertou ou não

        if not acertou:                                                                    # Lógica se a letra estiver incorreta
            tentativas -= 1                                                                   # Reduz  o número de tentativas restantes em 1
            print("\n--------------------------------")
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")            # Mensagem de erro , para visulização do usuário
            print("--------------------------------")

        else:                                                                              # Lógica se a letra estiver correta
            print("\n--------------------------------")
            print(f"Boa! A letra '{letra_usuario}' existe na palavra.")                       # Mensagem de acerto, para visualização do usuário
            print("--------------------------------")
   
    if "_" not in letras_descobertas:                                                      # Verifica se o usuário venceu, ou seja, se todas as letras foram descobertas
        mostrar_forca(tentativas, letras_descobertas)                                      # Mostra a forca final, com a palavra completamente descoberta, para visualização do usuário
        print(f"\nParabéns! Você venceu! Com {tentativas} tentativas restantes.")          # Mensagem de vitória, para visualização do usuário
        print("A palavra era:", palavra_secreta)                                           # Exibe a palavra secreta para o usuário

    else:                                                                                  # Verifica se o usuário perdeu, ou seja, se as tentativas acabaram e ainda há letras não descobertas
        mostrar_forca(tentativas, letras_descobertas)                                      # Mostra a forca final, com a palavra completamente descoberta, para visualização do usuário
        print("\nGame Over! Você perdeu! Tente novamente!")                                # Mensagem de derrota, para visualização do usuário
        print("A palavra era:", palavra_secreta)                                           # Exibe a palavra secreta para o usuário

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()                   # Pergunta ao usuário se deseja jogar novamente, e converte a resposta para minúscula para facilitar a comparação, controlando o loop principal do jogo
