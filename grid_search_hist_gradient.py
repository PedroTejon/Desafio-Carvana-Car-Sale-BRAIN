from pandas import read_csv
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import HistGradientBoostingRegressor


def main():
    dados = read_csv('carvana_treated.csv')
    dados_treino, labels_treino = dados.drop('Price', axis=1), dados['Price']

    parametros = {
        'interaction_cst': ['pairwise', 'no interaction', None],
        'max_depth': [x for x in range(10, 40, 10)] + [None],
        'min_samples_leaf': [10, 20, 40],
        'learning_rate': [0.1, 0.3, 0.5, 1],
        'loss': ['squared_error', 'absolute_error', 'friedman_mse', 'poisson']
    }

    gds = GridSearchCV(HistGradientBoostingRegressor(
            random_state=1), param_grid=parametros, verbose=50, n_jobs=-1)

    gds.fit(dados_treino, labels_treino)

    print(gds.best_params_)


if __name__ == '__main__':
    main()
