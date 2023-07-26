import re
def valida_rg(rg):
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

    while True:
        if len(rg) == 9:
            rg_formatado = f"{rg[0:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8]}"
            if re.match(padrao_rg, rg_formatado):
                return rg_formatado
            else:
                rg = input("RG inválido, digite novamente: ")
                continue
        else:
            rg = input("RG inválido, digite novamente: ")
            continue