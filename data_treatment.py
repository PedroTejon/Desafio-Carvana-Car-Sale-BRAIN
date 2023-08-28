from pandas import read_csv
from re import sub


def main():
    dados = read_csv('carvana.csv')
    
    # Exclusão de dados duplicados
    dados = dados.drop_duplicates()
    
    # Tratamento de nomes
    dados['Name'] = dados['Name'].apply(lambda x: sub(r' {2,}', ' ', x.strip().lower()))
    
    # Definição de códigos de modelos e marcas 
    models = {}
    brands = []
    brand_codes = []
    model_codes = []
    for name in dados['Name']:
        if name.count(' ') >= 1:
            brand, model = name.split(' ', maxsplit=1)    
        else:
            brand, model = name, name
        
        if brand in models:
            if model not in models[brand]:
                models[brand].append(model)
            model_code = models[brand].index(model)
        else:
            models[brand] = [model]
            model_code = 0
        model_codes.append(model_code)
        
        if brand not in brands:
            brands.append(brand)
        brand_codes.append(brands.index(brand))

    dados['Brand'] = brand_codes
    dados['Model'] = model_codes

    # Definição de colunas de categoria de carro/tipos populares
    categorias_extras = ['cross', 'grand', 'passenger', 'sport', 'cab', 'sportback', 'regular', 'coupe', 'limited', 'hybrid', 'crew', 'town',  'double', 'electric', 'plug-in']
    
    for categoria in categorias_extras:
        dados[categoria] = [categoria in nome.split(' ') for nome in dados['Name']]

    # Exclusão de coluna name
    dados = dados.drop('Name', axis=1, )

    # Correção de anos mais longos do que o normal
    dados['Year'] = dados['Year'].astype('str').str[:4].astype('int')

    dados.to_csv('carvana_treated.csv', index=False)


if __name__ == '__main__':
    main()