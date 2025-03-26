import time
import concurrent.futures


# Processamento de uma tarefa
def process_task(task_id):
    print(f"Tentando processar a tarefa {task_id}...")

    # Simula uma falha para tarefas com ID par
    if task_id % 2 == 0:
        raise Exception(f"Erro na tarefa {task_id}")

    print(f"Tarefa {task_id} concluída com sucesso.")


# Processamento de uma tarefa com retry
def retry_task(task_id, max_retries=3):
    for attempt in range(max_retries):
        try:
            # Tenta executar a tarefa
            process_task(task_id)
            return f"Tarefa {task_id} finalizada com sucesso."
        except Exception as e:
            # Em caso de erro, exibe a tentativa e espera 1 segundo antes de tentar de novo
            print(f"{e}. Tentativa {attempt + 1} de {max_retries}.")
            time.sleep(1)  # Aqui poderíamos aplicar estratégia de backoff
    return f"Tarefa {task_id} falhou após {max_retries} tentativas."


def main():
    # Lista de tarefas com alta e baixa prioridade
    high_priority_tasks = range(0, 5)  # Tarefas mais críticas
    low_priority_tasks = range(5, 10)  # Tarefas menos críticas

    # Criação de dois pools de threads separados, um para cada prioridade
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as high_priority_executor, \
            concurrent.futures.ThreadPoolExecutor(max_workers=3) as low_priority_executor:
        # Submete as tarefas de alta prioridade para execução com retry
        high_priority_futures = [high_priority_executor.submit(retry_task, task) for task in high_priority_tasks]

        # Submete as tarefas de baixa prioridade para execução com retry
        low_priority_futures = [low_priority_executor.submit(retry_task, task) for task in low_priority_tasks]

        # Aguarda todas as tarefas serem concluídas
        concurrent.futures.wait(high_priority_futures + low_priority_futures)

        # Imprime o resultado de cada tarefa (sucesso ou falha)
        for future in high_priority_futures + low_priority_futures:
            print(future.result())


if __name__ == "__main__":
    main()
