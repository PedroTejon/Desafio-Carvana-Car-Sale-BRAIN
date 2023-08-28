from pandas import read_csv
import sktester


def main():
    dados = read_csv('carvana_treated.csv')

    # print(SKTester.mean_absolute_percentage_error())
    test_regression(dados)
    


if __name__ == '__main__':
    main()