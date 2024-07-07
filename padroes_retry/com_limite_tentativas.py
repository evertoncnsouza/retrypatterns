import time


def process_task():
    print("Tentando realizar a tarefa...")
    raise Exception("Erro no processamento")


def main():
    max_retries = 5
    retry_count = 0

    while retry_count < max_retries:
        try:
            process_task()
            break  # Sucesso, sai do loop
        except Exception as e:
            retry_count += 1
            if retry_count >= max_retries:
                print(f"Erro: {e}. Tentativas máximas alcançadas, parando retries.")
                break
            print(f"Erro: {e}. Tentativa {retry_count} de {max_retries}. Tentando novamente em 2 segundos...")
            time.sleep(2)  # Intervalo fixo


if __name__ == "__main__":
    main()
