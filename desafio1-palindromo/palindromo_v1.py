def is_palindrome(checker):
    checker = checker.replace(" ", "").lower() # Formatação: remove os espaços em branco e torna a frase em letras minúsculas.

    return checker == checker[::-1] # Retorna para o verificador "checker" se a frase/sequência é igual à sua reversão.

##
cmd = input("Digite uma frase/sequência para verificar se é um palíndromo: ") 
##

# Validação se é um palíndromo ou não.
if is_palindrome(cmd):
    print("A frase/sequência fornecida É um palíndromo!")
else:
    print("A frase/sequência fornecida NÃO é um palíndromo.")
