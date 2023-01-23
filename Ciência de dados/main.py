import importa_base as ib
import inteligencia_artificial as ia
import visualizar_previsoes as vp

def main():
    tabela = ib.importa_base()
    y_teste, previsao_arvoredecisao, previsao_regressaolinear = ia.inteligencia_artificial(tabela)
    vp.visualizar_previsoes(y_teste, previsao_arvoredecisao, previsao_regressaolinear)

if __name__ == '__main__':
   main()