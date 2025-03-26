import time
import collections

# Classe que implementa um limitador de taxa simples (Rate Limiter)
class RateLimiter:
    """
    Implementa um limitador de taxa baseado em número máximo de chamadas dentro de uma janela de tempo.
    """

    def __init__(self, max_calls, time_window):
        self.max_calls = max_calls  # Número máximo de chamadas permitidas
        self.time_window = time_window  # Janela de tempo em segundos
        self.call_times = collections.deque()  # Fila que armazena os horários das chamadas

    # Verifica se uma nova requisição pode ser feita dentro do limite
    def allow_request(self):
        current_time = time.time()

        # Remove registros antigos que já saíram da janela de tempo
        while self.call_times and self.call_times[0] < current_time - self.time_window:
            self.call_times.popleft()

        # Se ainda estiver dentro do limite, permite a chamada
        if len(self.call_times) < self.max_calls:
            self.call_times.append(current_time)
            return True
        else:
            return False

    # Aguarda até que uma nova requisição seja permitida
    def wait_until_allowed(self):
        while not self.allow_request():
            # Calcula quanto tempo falta para liberar uma nova chamada
            sleep_time = max(0, self.call_times[0] + self.time_window - time.time())
            print(f"Limite de requisições atingido. Aguardando {sleep_time:.2f} segundos...")
            time.sleep(sleep_time)

# Função que simula uma tarefa instável
def process_task():
    """Simula uma tarefa que pode falhar."""
    print("Tentando executar a tarefa...")
    if time.time() % 2 < 1:  # Simula falhas de forma intermitente
        raise Exception("Erro no processamento")
    print("Tarefa concluída com sucesso!")

# Retry com controle de taxa (rate limit)
def retry_with_rate_limit(task, max_retries=5, max_calls=3, time_window=10):
    """
    Executa uma função com retry, respeitando um limitador de taxa.

    :param task: Função que será executada.
    :param max_retries: Quantidade máxima de tentativas.
    :param max_calls: Quantas chamadas são permitidas dentro do período de tempo.
    :param time_window: Período de tempo (em segundos) para o rate limit.
    """
    rate_limiter = RateLimiter(max_calls, time_window)
    retry_count = 0

    while retry_count < max_retries:
        try:
            rate_limiter.wait_until_allowed()  # Aguarda até que seja permitido fazer a chamada
            task()
            print("Operação concluída com sucesso!")
            return
        except Exception as e:
            retry_count += 1
            if retry_count >= max_retries:
                print(f"Erro: {e}. Número máximo de tentativas atingido. Encerrando retries.")
                return
            print(f"Erro: {e}. Tentativa {retry_count}/{max_retries}. Tentando novamente...")


def main():
    retry_with_rate_limit(process_task, max_retries=5, max_calls=3, time_window=10)


if __name__ == "__main__":
    main()
