import time

# Função que simula uma tarefa que pode falhar de forma intermitente
def process_task():
    """Simula uma tarefa que pode falhar."""
    print("Tentando processar a tarefa...")
    if time.time() % 2 < 1:  # Simula falha com base no tempo (probabilidade de 50%)
        raise Exception("Erro no processamento")
    print("Tarefa concluída com sucesso!")

# Função que aplica retry com intervalo fixo
def fixed_interval_retry(func, max_retries=5, interval=5):
    """
    Executa uma função com retry usando intervalo fixo entre tentativas.

    :param func: Função a ser executada com retry.
    :param max_retries: Número máximo de tentativas permitidas.
    :param interval: Tempo fixo (em segundos) entre uma tentativa e outra.
    """
    for attempt in range(1, max_retries + 1):
        try:
            func()  # Tenta executar a função
            print("Operação concluída com sucesso!")
            return  # Encerra se for bem-sucedida
        except Exception as e:
            # Em caso de erro, exibe a tentativa atual e aguarda um tempo fixo
            print(f"Erro: {e}. Tentativa {attempt}/{max_retries}. Tentando novamente em {interval} segundos...")
            time.sleep(interval)  # Espera antes da próxima tentativa

    # Caso todas as tentativas falhem
    print("Operação falhou após o número máximo de tentativas.")

def main():
    fixed_interval_retry(process_task)

if __name__ == "__main__":
    main()
