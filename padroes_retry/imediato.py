def process_task():
    print("Tentando processar a tarefa...")
    raise Exception("Erro no processamento")


def main():
    while True:
        try:
            process_task()
            break  # Sucesso, sai do loop
        except Exception as e:
            print(f"Erro: {e}. Tentando novamente...")  # Retry imediato, sem pausa


if __name__ == "__main__":
    main()
