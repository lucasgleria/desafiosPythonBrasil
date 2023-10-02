# Estou usando a versão 3.9.9 do python, caso haja erros ou conflítuos ao executar o programa, mude sua versão python.
# Caso for executar localmente, não esqueça de fazer a importação da bilbioteca, escreva no seu terminal, powershell ou cmd: 'pip install pysimplegui'

# Importação da biblioteca, é necessário fazer antes de utilizar a bilbiotexa em seu programa, são boas práticas fazer todas as suas importações, logo no início do programa
import PySimpleGUI as sg # A expressão "as sg" é uma boa prática também e facilita a utilização da bilbioteca. É como se estivesse dizendo ao python que "PySimpleGUI" == "sg"
# Vale acrescentar que você pode chamar a bibliotca do que quiser, mas por boas práticas siga as convensões para todos entenderem seu código. 

def is_palindrome(checker):
    checker = checker.replace(" ", "").lower()
    return checker == checker[::-1]

layout = [ # "Layout" é da biblioteca pysimplegui, para gerar uma interface grafica (GUI)
    [sg.Text("Digite uma frase/sequência para verificar se é um palíndromo:")], # "sg.Text" imprime na GUI um texto estático.
    [sg.InputText(key='-INPUT-')], # "sg.InputText" imprime na GUI um input vazio, "key" nesse contexto é como se fosse o id do input
    [sg.Button("Verificar"), sg.Exit()] # Nessa linha, imprimirá dois botões na GUI, o botão de verificação "Verificar" e o botão de exclusão da janela "Exit"
]

window = sg.Window("Verificador de Palíndromo", layout) # Estou chamando o "layout" através de "window" -- "Verificador de Palíndromo" será o "title" da GUI

while True: # Para manter o programa em execução mesmo após uma verificação, fazemos um laço
    event, values = window.read() # A função "read" nos fornecerá a comunicação entre nossa GUI e o "backend"

    if event in (sg.WIN_CLOSED, 'Exit'): # Caso clique no "X" da GUI ou em Exit
        break # Terminar a execução.
    elif event == 'Verificar': # Caso o botão "Verificar" seja clicado
        cmd = values['-INPUT-'] # pegar o valor fornecido pelo "ID" -INPUT- e guardar na variável "cmd"
        # Validação se é um palíndromo ou não.
        if is_palindrome(cmd): 
            sg.popup("A frase/sequência fornecida É um palíndromo!") # Exibe um popup na tela
        else:
            sg.popup("A frase/sequência fornecida NÃO é um palíndromo.") # Exibe um popup na tela

window.close() # Fim do programa 
