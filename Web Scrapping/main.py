import cotacoes as ct
import atualizar_tabela as at

def main():
    dolar,euro, ouro = ct.pega_cotacoes()
    at.atualiza_tabela(dolar,euro,ouro)

if __name__ == '__main__':
   main()