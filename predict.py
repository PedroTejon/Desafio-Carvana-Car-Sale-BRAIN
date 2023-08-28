from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet, Lars, LassoLars
# from sklearn.svm import SVR
# from sklearn.tree import DecisionTreeRegressor,ExtraTreeRegressor
# from sklearn.ensemble im1port RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor, HistGradientBoostingRegressor, VotingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor


def main():
    dados = read_csv('carvana_treated.csv')
    dados_treino, dados_teste, labels_treino, labels_teste = train_test_split(dados.drop('Price', axis=1), dados['Price'], test_size=0.2, random_state=1)
    
    scaler = StandardScaler()
    dados_treino = scaler.fit_transform(dados_treino)
    dados_teste = scaler.transform(dados_teste)

    # modelos = [
    #     SVR(kernel='linear',C=1),
    #     LinearRegression(n_jobs=-1),
    #     DecisionTreeRegressor(random_state=1),
    #     ExtraTreeRegressor(random_state=1),
    #     RandomForestRegressor(random_state=1, n_estimators=100, n_jobs=-1),
    #     GradientBoostingRegressor(random_state=1, n_estimators=100),
    #     AdaBoostRegressor(random_state=1, estimator=LinearRegression(n_jobs=-1),n_estimators=100),
    #     Lasso(random_state=1),
    #     Ridge(random_state=1),
    #     ElasticNet(random_state=1),
    #     Lars(random_state=1),
    #     LassoLars(random_state=1),
    #     HistGradientBoostingRegressor(interaction_cst=None, learning_rate=0.3, loss='poisson', max_depth=10, min_samples_leaf=10, random_state=1),
    # ]

    modelo = HistGradientBoostingRegressor(interaction_cst=None, learning_rate=0.3, loss='poisson', max_depth=10, min_samples_leaf=10, random_state=1)
    
    modelo.fit(dados_treino, labels_treino)
    previsao = modelo.predict(dados_teste)

    print(mean_absolute_percentage_error(labels_teste, previsao))


if __name__ == '__main__':
    main()