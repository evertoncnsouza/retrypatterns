import time

# Função que simula uma tarefa que sempre falha
def process_task():
    """Simula uma tarefa que pode falhar."""
    print("Tentando executar a tarefa...")
    raise Exception("Erro no processamento")

# Função que implementa retry com número máximo de tentativas e tempo fixo entre elas
def retry_with_max_attempts(func, max_retries=5, wait_time=2):
    """
    Executa uma função com retry até atingir o número máximo de tentativas.

    :param func: Função que será executada com retry.
    :param max_retries: Quantidade máxima de tentativas antes de desistir.
    :param wait_time: Tempo fixo (em segundos) entre cada tentativa.
    """
    for attempt in range(1, max_retries + 1):
        try:
            func()  # Tenta executar a função
            print("Operação concluída com sucesso!")
            return  # Encerra se for bem-sucedida
        except Exception as e:
            if attempt >= max_retries:
                # Se atingir o número máximo de tentativas, encerra com erro
                print(f"Erro: {e}. Limite de {max_retries} tentativas atingido. Encerrando retries.")
                return
            # Exibe mensagem de erro e aguarda antes da próxima tentativa
            print(f"Erro: {e}. Tentativa {attempt}/{max_retries}. Tentando novamente em {wait_time} segundos...")
            time.sleep(wait_time)  # Aguarda antes de tentar novamente


def main():
    retry_with_max_attempts(process_task, max_retries=5, wait_time=2)


if __name__ == "__main__":
    main()
