import time
import concurrent.futures


def process_task(task_id):
    print(f"Tentando processar a tarefa {task_id}...")
    if task_id % 2 == 0:
        raise Exception(f"Erro na tarefa {task_id}")


def retry_task(task_id, max_retries=3):
    for attempt in range(max_retries):
        try:
            process_task(task_id)
            print(f"Tarefa {task_id} concluída com sucesso.")
            return
        except Exception as e:
            print(f"{e}. Tentativa {attempt + 1} de {max_retries}.")
            time.sleep(1)
    print(f"Tarefa {task_id} falhou após {max_retries} tentativas.")


def main():
    tasks = range(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(retry_task, task_id) for task_id in tasks]
        concurrent.futures.wait(futures)


if __name__ == "__main__":
    main()
