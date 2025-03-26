import time
import threading

# Classe que implementa o algoritmo Token Bucket
class TokenBucket:
    """
    Implementa o algoritmo Token Bucket para limitar a taxa de chamadas a uma função.
    """

    def __init__(self, rate, capacity):
        self.rate = rate  # Tokens gerados por segundo
        self.capacity = capacity  # Capacidade máxima do bucket
        self.tokens = capacity  # Começa cheio
        self.lock = threading.Lock()  # Garante acesso thread-safe
        self.last_checked = time.time()  # Última verificação
        self.running = True

        # Cria uma thread para reabastecer os tokens ao longo do tempo
        self.thread = threading.Thread(target=self.refill_tokens, daemon=True)
        self.thread.start()

    def refill_tokens(self):
        """Thread que reabastece tokens continuamente com base no tempo e taxa."""
        while self.running:
            with self.lock:
                now = time.time()
                elapsed = now - self.last_checked  # Tempo desde a última recarga
                self.last_checked = now
                new_tokens = elapsed * self.rate  # Calcula quantos tokens devem ser adicionados
                self.tokens = min(self.capacity, self.tokens + new_tokens)  # Não passa da capacidade
            time.sleep(0.1)  # Intervalo para evitar uso excessivo da CPU

    def consume_token(self, timeout=10):
        """
        Tenta consumir um token. Se não houver, espera até o timeout.

        :param timeout: Tempo máximo de espera por um token.
        :return: True se conseguiu um token, False se atingiu o timeout.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            with self.lock:
                if self.tokens >= 1:
                    self.tokens -= 1
                    return True
            time.sleep(0.1)  # Espera antes de tentar de novo
        return False  # Não conseguiu dentro do tempo

    def stop(self):
        """Encerra a thread de recarga de tokens."""
        self.running = False
        self.thread.join()

# Simula o processamento de uma tarefa que pode falhar
def process_task(task_id):
    """Simula um processamento que pode falhar."""
    print(f"🔄 Tentando processar a tarefa {task_id}...")
    if task_id % 2 == 0:  # Tarefas com ID par falham
        raise Exception(f"⚠️ Erro na tarefa {task_id}")

# Função que aplica retry controlado pelo token bucket
def retry_task(task_id, bucket, max_retries=5, retry_interval=1):
    """
    Tenta executar uma tarefa com retry usando Token Bucket.

    :param task_id: ID da tarefa.
    :param bucket: Instância do TokenBucket.
    :param max_retries: Máximo de tentativas permitidas.
    :param retry_interval: Tempo fixo de espera entre tentativas.
    """
    for attempt in range(1, max_retries + 1):
        if bucket.consume_token(timeout=10):  # Tenta obter um token (espera até 10s)
            try:
                process_task(task_id)
                print(f"✅ Tarefa {task_id} concluída com sucesso.")
                return
            except Exception as e:
                print(f"{e}. Tentativa {attempt}/{max_retries}. Tentando novamente em {retry_interval} segundos...")
                time.sleep(retry_interval)
        else:
            print(f"❌ Tarefa {task_id} não conseguiu um token a tempo. Ignorando.")
            return
    print(f"❌ Tarefa {task_id} excedeu o número máximo de tentativas. Desistindo.")


def main():
    token_bucket = TokenBucket(rate=1, capacity=5)  # Gera 1 token por segundo, até 5 tokens acumulados
    tasks = range(10)  # 10 tarefas
    threads = []

    # Executa cada tarefa em uma thread separada
    for task_id in tasks:
        t = threading.Thread(target=retry_task, args=(task_id, token_bucket))
        t.start()
        threads.append(t)

    # Aguarda todas as tarefas terminarem
    for t in threads:
        t.join()

    token_bucket.stop()  # Encerra a thread do token bucket


if __name__ == "__main__":
    main()
