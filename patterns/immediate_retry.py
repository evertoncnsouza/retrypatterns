# Função que simula uma tarefa que sempre falha
def process_task():
    """Simula uma tarefa que pode falhar."""
    print("Tentando processar a tarefa...")
    raise Exception("Erro no processamento")  # Falha garantida para fins de exemplo

# Função que aplica retry imediato (sem nenhum tempo de espera entre tentativas)
def immediate_retry(func, max_retries=10):
    """
    Executa uma função com retry imediato em caso de falha.

    :param func: Função a ser executada com retry.
    :param max_retries: Número máximo de tentativas antes de desistir.
    """
    for attempt in range(1, max_retries + 1):
        try:
            func()  # Tenta executar a função
            print("Operação concluída com sucesso!")
            return  # Encerra se funcionar
        except Exception as e:
            # Em caso de erro, tenta novamente imediatamente (sem delay)
            print(f"Erro: {e}. Tentativa {attempt}/{max_retries}. Tentando novamente imediatamente...")

    # Se todas as tentativas falharem
    print("Operação falhou após o número máximo de tentativas.")


def main():
    immediate_retry(process_task)

if __name__ == "__main__":
    main()
