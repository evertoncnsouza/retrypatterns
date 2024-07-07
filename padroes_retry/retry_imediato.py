
import time


def process_task():
    print("Tentando processar a tarefa...")
    raise Exception("Erro no processamento")


def main():
    while True:
        try:
            process_task()
            break  # Sucesso, sai do loop
        except Exception as e:
            print(f"Erro: {e}. Tentando novamente...")
            time.sleep(1)  # Retry imediato


if __name__ == "__main__":
    main()
