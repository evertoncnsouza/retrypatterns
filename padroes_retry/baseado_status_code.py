import time
import requests


def should_retry(status_code):
    # Define os códigos de status que devem acionar um retry
    retry_statuses = [500, 502, 503, 504]
    return status_code in retry_statuses


def make_request_with_retry(url, max_retries=5):
    retry_count = 0
    while retry_count < max_retries:
        response = requests.get(url)
        if response.status_code == 200:
            print("Requisição bem-sucedida")
            return response
        elif should_retry(response.status_code):
            retry_count += 1
            wait_time = 2 ** retry_count  # Backoff exponencial
            print(
                f"Erro {response.status_code}: Tentativa {retry_count} de {max_retries}. Tentando novamente em {wait_time} segundos...")
            time.sleep(wait_time)
        else:
            print(f"Erro {response.status_code}: Não é possível tentar novamente.")
            return response
    print("Número máximo de tentativas alcançado.")
    return None


def main():
    url = "https://exemplo.com/api"
    response = make_request_with_retry(url)
    if response:
        print("Resposta:", response.content)


if __name__ == "__main__":
    main()
