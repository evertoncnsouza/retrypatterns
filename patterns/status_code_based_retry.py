import time
import requests

# Define quais códigos de status HTTP devem acionar retry
def should_retry(status_code):
    """Define quais status HTTP devem ser tratados com retry."""
    retry_statuses = {500, 502, 503, 504}  # Erros típicos de servidor e indisponibilidade temporária
    return status_code in retry_statuses

# Função que faz requisições HTTP com retry baseado em status code
def retry_request(url, max_retries=5, max_wait_time=30):
    """
    Faz uma requisição HTTP com retry baseado em status code.

    :param url: URL para fazer a requisição.
    :param max_retries: Número máximo de tentativas antes de desistir.
    :param max_wait_time: Tempo máximo de espera entre tentativas (em segundos).
    :return: Objeto Response do requests, ou None se todas as tentativas falharem.
    """
    retry_count = 0
    start_time = time.time()  # Marca o início da operação (para medir tempo total)

    while retry_count < max_retries:
        try:
            # Tenta fazer a requisição GET com timeout de 10 segundos
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                # Sucesso! Retorna a resposta
                print(f"✅ Requisição bem-sucedida. Tempo total: {time.time() - start_time:.2f} segundos.")
                return response

            elif should_retry(response.status_code):
                # Caso o código esteja entre os que justificam retry
                retry_count += 1
                wait_time = min(2 ** retry_count, max_wait_time)  # Exponential backoff com limite
                print(f"⚠️ Erro {response.status_code}: Tentativa {retry_count}/{max_retries}. Tentando novamente em {wait_time} segundos...")
                time.sleep(wait_time)

            else:
                # Para outros erros (ex: 400 ou 404), não tenta novamente
                print(f"❌ Erro {response.status_code}: Retry não aplicável.")
                return response

        except requests.exceptions.RequestException as e:
            # Em caso de falha de rede (timeout, DNS, etc.), também aplica retry
            retry_count += 1
            wait_time = min(2 ** retry_count, max_wait_time)
            print(f"🌐 Erro de rede: {e}. Tentativa {retry_count}/{max_retries}. Tentando novamente em {wait_time} segundos...")
            time.sleep(wait_time)

    # Se todas as tentativas falharem
    print(f"❌ Máximo de tentativas atingido ({max_retries}). Tempo total: {time.time() - start_time:.2f} segundos.")
    return None


def main():
    url = "https://example.com/api"  # URL de exemplo, altere para testar com uma real
    response = retry_request(url, max_retries=5, max_wait_time=30)
    if response:
        # Mostra os primeiros 200 caracteres do corpo da resposta
        print("📥 Resposta:", response.text[:200])


if __name__ == "__main__":
    main()
