import time
import random

# Função que simula uma tarefa com alta probabilidade de falhar
def process_task():
    """Simula um processo que pode falhar."""
    print("Tentando processar a tarefa...")
    if random.random() < 0.8:  # Simula uma falha em 80% das vezes
        raise Exception("Erro no processamento")
    print("Tarefa processada com sucesso!")

# Função que aplica estratégia de retry com exponential backoff + jitter
def exponential_backoff_with_jitter(func, max_retries=5, base_delay=1, max_delay=10):
    """
    Executa uma função com retry utilizando backoff exponencial com jitter.

    :param func: A função que será executada com retry.
    :param max_retries: Quantidade máxima de tentativas antes de desistir.
    :param base_delay: Valor base do tempo de espera (em segundos).
    :param max_delay: Tempo máximo de espera permitido entre tentativas.
    """
    for attempt in range(max_retries):
        try:
            func()  # Tenta executar a função
            print("Operação concluída com sucesso!")
            return  # Encerra se der certo
        except Exception as e:
            # Calcula o tempo de espera com base exponencial
            wait_time = base_delay * (2 ** attempt)  # Ex: 1, 2, 4, 8...
            # Adiciona aleatoriedade (jitter) para evitar picos simultâneos
            wait_time += random.uniform(0, 1)
            # Garante que não ultrapasse o limite máximo de espera
            wait_time = min(wait_time, max_delay)

            print(f"Erro: {e}. Tentativa {attempt + 1}/{max_retries}. Tentando novamente em {wait_time:.2f} segundos...")
            time.sleep(wait_time)  # Aguarda antes da próxima tentativa

    # Se todas as tentativas falharem
    print("Operação falhou após o número máximo de tentativas.")


def main():
    exponential_backoff_with_jitter(process_task)


if __name__ == "__main__":
    main()
