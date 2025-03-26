import time

# Função que retorna o n-ésimo número da sequência de Fibonacci
def fibonacci(n):
    """Retorna o n-ésimo número da sequência de Fibonacci de forma eficiente."""
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b  # Geração da sequência: 1, 1, 2, 3, 5, 8, ...
    return a

# Função que aplica estratégia de retry com Fibonacci Backoff
def fibonacci_backoff_with_retry(func, max_retries=10, max_wait=30):
    """
    Executa uma função com retry utilizando Fibonacci Backoff.

    :param func: A função que será executada.
    :param max_retries: Número máximo de tentativas.
    :param max_wait: Tempo máximo de espera entre tentativas.
    """
    for attempt in range(1, max_retries + 1):  # Começa da tentativa 1
        try:
            func()  # Tenta executar a função
            print("Operação concluída com sucesso!")
            return  # Sai da função se der certo
        except Exception as e:
            # Calcula o tempo de espera com base na sequência de Fibonacci
            wait_time = min(fibonacci(attempt), max_wait)
            print(f"Erro: {e}. Tentativa {attempt}/{max_retries}. Tentando novamente em {wait_time} segundos...")
            time.sleep(wait_time)  # Aguarda antes da próxima tentativa

    # Se todas as tentativas falharem
    print("Operação falhou após o número máximo de tentativas.")

# Função que simula uma tarefa instável, que pode falhar dependendo do tempo
def potentially_failing_task():
    """Simula uma tarefa que pode falhar."""
    print("Tentando executar a tarefa...")
    if time.time() % 2 < 1:  # Simula falha com base na variação de tempo
        raise Exception("Erro na tarefa")
    print("Tarefa executada com sucesso.")


def main():
    fibonacci_backoff_with_retry(potentially_failing_task)

if __name__ == "__main__":
    main()
