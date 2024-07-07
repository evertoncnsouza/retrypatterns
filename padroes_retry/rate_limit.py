import time


def process_task():
    print("Tentando realizar a tarefa...")
    raise Exception("Erro no processamento")


def retry_with_rate_limit(task, max_retries=5, rate_limit=2):
    retry_count = 0
    while retry_count < max_retries:
        try:
            task()
            print("Tarefa concluída com sucesso.")
            return
        except Exception as e:
            retry_count += 1
            if retry_count >= max_retries:
                print(f"Erro: {e}. Tentativas máximas alcançadas, parando retries.")
                return
            print(
                f"Erro: {e}. Tentativa {retry_count} de {max_retries}. Tentando novamente em {rate_limit} segundos...")
            time.sleep(rate_limit)


def main():
    retry_with_rate_limit(process_task, max_retries=5, rate_limit=2)


if __name__ == "__main__":
    main()
