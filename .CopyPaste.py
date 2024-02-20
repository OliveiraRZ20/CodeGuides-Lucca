# finalização de codigo que roda no CMD

choice = input("Deseja ir de novo [S/N]")
while choice not in ("s", "n"):
    print("Escolha Inválida, tente novamente.")
    choice = input("Deseja ir de novo [S/N]:\n")
if choice.lower() == "n":
    break
    print("saindo")

# função check numero primo


def e_primo(n):
    if n < 2:
        return "O número tem que ser maior que 2 seu bobão."
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False
    return True


# funcao contador de palavras com frequencia

from collections import *


def wordcountfreq(text):
    content = text
    content = content.lower()
    sem_espaco = content.split()
    contador = Counter(sem_espaco)
    resultado = []
    for palavra, frequencia in contador.most_common():
        resultado.append(f"{palavra}: {frequencia}")
    return resultado


# funcao contador de caracteres com frequencia

from collections import *


def charcountfreq(text):
    content = text
    content = content.lower()
    contador = Counter(content)
    resultado = []
    for letra, frequencia in contador.most_common():
        if letra == " ":
            continue
        if letra in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            continue
        resultado.append(f"{letra}: {frequencia}")
    return resultado
