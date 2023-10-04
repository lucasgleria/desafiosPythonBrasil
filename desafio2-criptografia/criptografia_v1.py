# Gostaria de agradecer pelo desafio, precisei pesquisar muita coisa que só conhecia na teoria para por isso em prática!

import hashlib  # Importa a biblioteca hashlib, nativa do python, que fornece funções de hash. https://docs.python.org/3/library/hashlib.html

# Função para criar um hash da mensagem
def create_hash_message(message):
    sha256 = hashlib.sha256()  # Inicializa um objeto sha256 da biblioteca hashlib.
    sha256.update(message.encode('utf-8'))  # Atualiza o hash com a mensagem codificada em UTF-8.
    return sha256.hexdigest()  # Retorna o valor do hash em formato hexadecimal.

# Função para criptografar a mensagem
def encrypted_message(message, key):
    encrypted_message = ""  # Inicializa uma string vazia para armazenar a mensagem criptografada.
    for i in range(len(message)):
        char = message[i]  # Pega um caractere da mensagem original.
        key_char = key[i % len(key)]  # Pega um caractere da chave de criptografia, repetindo-a, se necessário.
        encrypted_char = chr(ord(char) + ord(key_char))  # Realiza a criptografia do caractere.
        encrypted_message += encrypted_char  # Adiciona o caractere criptografado à mensagem.
    return encrypted_message  # Retorna a mensagem criptografada.

# Função para descriptografar a mensagem
def decrypt_message(encrypted_message, key):
    decrypted_message = ""  # Inicializa uma string vazia para armazenar a mensagem descriptografada.
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]  # Pega um caractere da mensagem criptografada.
        key_char = key[i % len(key)]  # Pega um caractere da chave de descriptografia, repetindo-a, se necessário.
        decrypted_char = chr(ord(char) - ord(key_char))  # Realiza a descriptografia do caractere.
        decrypted_message += decrypted_char  # Adiciona o caractere descriptografado à mensagem.
    return decrypted_message  # Retorna a mensagem descriptografada.

# Solicita a entrada do usuário para a mensagem original e a chave de criptografia.
original_message = input("Digite a mensagem que quer encriptar: ")
encryption_key = input("Digite a chave de criptografia: ")

# Cria um hash da mensagem original.
message_hash = create_hash_message(original_message)

# Criptografa a mensagem original.
encrypted_message = encrypted_message(original_message, encryption_key)

# Imprime os resultados na tela.
print(f'''
        Mensagem original: {original_message}

        Hash da mensagem: {message_hash}

        Mensagem criptografada: {encrypted_message}

''')

# Solicita a chave de descriptografia do usuário.
decryption_key = input("Insira a chave de descriptografia: ")

# Descriptografa a mensagem criptografada.
decrypted_message = decrypt_message(encrypted_message, decryption_key)

# Verifica a integridade da mensagem comparando o hash da mensagem descriptografada com o hash original.
if create_hash_message(decrypted_message) == message_hash:
    print(f"Mensagem descriptografada: {decrypted_message}")
    print("Integridade da mensagem verificada.")
else:
    print("Erro: A mensagem foi alterada ou a chave está incorreta.")
