import hashlib # Importa a biblioteca hashlib, nativa do python, que fornece funções de hash. https://docs.python.org/3/library/hashlib.html
import PySimpleGUI as sg # Importa a biblioteca pysimplegui para fazer interfaces, não é nativa do python. https://www.pysimplegui.org/en/latest/

# Função para criar um hash da mensagem
def create_hash_message(message):
    sha256 = hashlib.sha256()  # Inicializa um objeto de hash SHA-256
    sha256.update(message.encode('utf-8'))  # Atualiza o hash com a mensagem codificada em UTF-8
    return sha256.hexdigest()  # Retorna o hash da mensagem em formato hexadecimal

# Função para criptografar a mensagem
def encrypted_message_func(message, key):
    encrypted_msg = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]  # Seleciona o caractere correspondente da chave
        encrypted_char = chr(ord(char) + ord(key_char))  # Realiza a criptografia substituindo o caractere
        encrypted_msg += encrypted_char
    return encrypted_msg

# Função para criar o layout da interface gráfica da janela principal
def create_main_layout():
    return [
        [sg.Text("Mensagem original:"), sg.InputText(key='-ORIGINAL-')],
        [sg.Text("Chave de criptografia:"), sg.InputText(key='-ENCRYPTION_KEY-')],
        [sg.Button("Criptografar"), sg.Button("Informações")],
        [sg.Text("", key='-RESULT-', size=(40, 2))],
    ]

# Função para criar o layout da interface gráfica da janela de informações
def create_info_layout(original_message, encryption_key, message_hash, encrypted_message):
    return [
        [sg.Text(f"Mensagem original: {original_message}")],
        [sg.Text(f"Chave de criptografia: {encryption_key}")],
        [sg.Text(f"Mensagem criptografada: {encrypted_message}")],
        [sg.Text(f"Hash da mensagem: {message_hash}")],
        [sg.Text(f"Mensagem descriptografada: {original_message}")],
        [sg.Button("Voltar")],
    ]

main_window = sg.Window("Criptografia").Layout(create_main_layout())  # Cria a janela principal
info_window = None  # Inicializa a janela de informações como nula

while True:
    event, values = main_window.Read()  # Aguarda eventos da janela principal
    if event == sg.WIN_CLOSED:  # Verifica se a janela principal foi fechada
        break
    elif event == "Criptografar":  # Se o botão "Criptografar" for clicado
        original_message = values['-ORIGINAL-']  # Obtém a mensagem original do campo de entrada
        encryption_key = values['-ENCRYPTION_KEY-']  # Obtém a chave de criptografia do campo de entrada

        message_hash = create_hash_message(original_message)  # Calcula o hash da mensagem
        encrypted_msg = encrypted_message_func(original_message, encryption_key)  # Criptografa a mensagem

        main_window['-RESULT-'].update(f'''
            Mensagem criptografada: {encrypted_msg}
        ''')  # Atualiza a janela principal com a mensagem criptografada

    elif event == "Informações":  # Se o botão "Informações" for clicado
        original_message = values['-ORIGINAL-']  # Obtém a mensagem original do campo de entrada
        encryption_key = values['-ENCRYPTION_KEY-']  # Obtém a chave de criptografia do campo de entrada

        message_hash = create_hash_message(original_message)  # Calcula o hash da mensagem

        if info_window is not None:
            info_window.Close()  # Fecha a janela de informações anterior, se estiver aberta

        # Atualize o valor de encrypted_message com a mensagem criptografada
        encrypted_message = encrypted_message_func(original_message, encryption_key)

        info_layout = create_info_layout(original_message, encryption_key, message_hash, encrypted_message)  # Cria o layout da janela de informações
        info_window = sg.Window("Informações").Layout(info_layout)  # Cria a janela de informações

    if info_window is not None:
        info_event, _ = info_window.Read()  # Aguarda eventos da janela de informações
        if info_event == sg.WIN_CLOSED or info_event == "Voltar":  # Se a janela de informações for fechada ou o botão "Voltar" for clicado
            info_window.Close()  # Fecha a janela de informações

main_window.close()  # Fecha a janela principal ao sair do loop
