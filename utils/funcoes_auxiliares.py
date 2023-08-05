def return_menu_principal():
    resposta = input("\nDeseja retornar ao menu principal [sim/não]? ")
    if resposta == 'sim':
        return True
    else:
        print("Obrigada por utilizar nosso programa.")
        return False

def format_text():
    nome = input('Nome: ')
    nome_formatado = nome.title()
    return nome_formatado