
import requests
def obter_previsao_tempo(API_KEY, cidade, estado):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': f"{cidade},{estado},Brasil",
        'appid': API_KEY,
        'units': 'metric'  # Unidade Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Lança uma exceção para erros HTTP
        dados_previsao = response.json()
        return dados_previsao
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None


def exibir_previsao_tempo(dados_previsao):
    if dados_previsao is not None:
        temperatura = dados_previsao['main']['temp']
        descricao = dados_previsao['weather'][0]['description']
        print(f"Temperatura: {temperatura}°C")
        print(f"Condição: {descricao}")
    else:
        print("Não foi possível obter a previsão do tempo.")


def main():
    api_key = "" #colocar sua api
    cidade = input("Digite o nome da cidade: ")
    estado = input("Digite a sigla do estado: ")

    dados_previsao = obter_previsao_tempo(api_key, cidade, estado)

    exibir_previsao_tempo(dados_previsao)


if __name__ == "__main__":
    main()

