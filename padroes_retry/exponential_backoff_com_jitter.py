import time
import random


def process_task():
    print("Tentando processar a tarefa...")
    raise Exception("Erro no processamento")


def main():
    max_retries = 5
    base_delay = 1  # Tempo base em segundos

    for attempt in range(max_retries):
        try:
            process_task()
            break  # Sucesso, sai do loop
        except Exception as e:
            wait_time = base_delay * (2 ** attempt)  # Backoff exponencial
            wait_time += random.uniform(0, 1)  # Jitter para evitar colisões
            print(f"Erro: {e}. Tentando novamente em {wait_time:.2f} segundos...")
            time.sleep(wait_time)


if __name__ == "__main__":
    main()
