def return_menu_principal():
    return_menu_principal = input("Deseja retornar ao menu principal [sim/não]? ")
    if return_menu_principal == 'sim':
        return_menu = True
    else:
        print("Obrigada por utilizar nosso programa.")
        return_menu = False
    return return_menu

def format_text(texto):
    nome_formatado = texto.title()
    return nome_formatado