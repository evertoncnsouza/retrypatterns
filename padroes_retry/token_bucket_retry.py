import time
import threading


class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.lock = threading.Lock()
        self.last_checked = time.time()

    def add_tokens(self):
        with self.lock:
            now = time.time()
            elapsed = now - self.last_checked
            self.last_checked = now
            new_tokens = elapsed * self.rate
            self.tokens = min(self.capacity, self.tokens + new_tokens)

    def consume_token(self):
        with self.lock:
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            else:
                return False


def process_task(task_id):
    print(f"Tentando processar a tarefa {task_id}...")
    if task_id % 2 == 0:
        raise Exception(f"Erro na tarefa {task_id}")


def retry_task(task_id, bucket):
    while True:
        if bucket.consume_token():
            try:
                process_task(task_id)
                print(f"Tarefa {task_id} concluída com sucesso.")
                return
            except Exception as e:
                print(f"{e}. Tentando novamente.")
                time.sleep(1)
        else:
            print(f"Sem tokens disponíveis para a tarefa {task_id}. Aguardando...")
            time.sleep(1)
            bucket.add_tokens()


def main():
    token_bucket = TokenBucket(rate=1, capacity=5)  # 1 token por segundo, capacidade máxima de 5 tokens
    tasks = range(10)
    threads = []
    for task_id in tasks:
        t = threading.Thread(target=retry_task, args=(task_id, token_bucket))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
