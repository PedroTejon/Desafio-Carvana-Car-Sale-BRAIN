from seaborn import lineplot
from matplotlib.pyplot import subplots
from pandas import read_csv
from re import sub


def main():
    dados = read_csv('carvana_treated.csv')

    _, axis = subplots(figsize=(12,10))
    lineplot(x='Miles', y='Price', data=dados, ax=axis, ci=None).figure.savefig('graficos/milesXprices')

    _, axis = subplots(figsize=(12,10))
    lineplot(x='Year', y='Price', data=dados, ax=axis, ci=None).figure.savefig('graficos/yearXprices')


    dados = read_csv('carvana.csv')
    palavrasPerten = {}

    for linha in dados['Name']:
        linha = sub(r' {2,}', ' ', linha.strip().lower())
        if linha.count(' ') >= 1:
            brand, modelo = linha.split(' ', maxsplit=1)    
        else:
            brand, modelo = linha, linha
        
        
        for palavra in modelo.split(' '):
            if palavra in palavrasPerten and brand not in palavrasPerten[palavra]:
                palavrasPerten[palavra].append(brand)
            elif palavra not in palavrasPerten:
                palavrasPerten[palavra] = [brand]

    print(list(filter(lambda x: len(palavrasPerten[x]) >= 2, palavrasPerten)))


if __name__ == '__main__':
    main()