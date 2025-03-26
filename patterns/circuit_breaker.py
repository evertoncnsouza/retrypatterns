import time

# Classe que implementa o padrão Circuit Breaker
class CircuitBreaker:
    def __init__(self, failure_threshold, recovery_timeout):
        self.failure_threshold = failure_threshold  # Quantidade de falhas consecutivas antes de "abrir" o circuito
        self.recovery_timeout = recovery_timeout  # Tempo (em segundos) que o circuito ficará aberto antes de tentar se recuperar
        self.failures = 0  # Contador de falhas consecutivas
        self.last_failure_time = 0  # Momento da última falha registrada
        self.state = 'CLOSED'  # Estados possíveis: CLOSED (normal), OPEN (bloqueando chamadas), HALF-OPEN (teste de recuperação)

    # função protegida pelo circuit breaker
    def call(self, func):
        # Se o estado for OPEN, verifica se já passou o tempo de recuperação
        if self.state == 'OPEN':
            if time.time() - self.last_failure_time > self.recovery_timeout:
                # Transiciona para HALF-OPEN para testar se o sistema se recuperou
                print("Circuit breaker está mudando para o estado HALF-OPEN.")
                self.state = 'HALF-OPEN'
            else:
                # Ainda dentro do tempo de recuperação — nega a execução
                raise Exception("Circuito está OPEN, requisição bloqueada.")

        try:
            # Tenta executar a função
            result = func()
            # Se funcionar, fecha o circuito e zera o contador de falhas
            self.state = 'CLOSED'
            self.failures = 0
            return result
        except Exception as e:
            # Incrementa o número de falhas consecutivas
            self.failures += 1
            print(f"Falha detectada: {e}. Contador de falhas: {self.failures}")

            if self.state == 'HALF-OPEN':
                # Se falhar no modo de teste, volta para o estado OPEN imediatamente
                print("Falha no estado HALF-OPEN, voltando para OPEN.")
                self.state = 'OPEN'
                self.last_failure_time = time.time()
            elif self.failures >= self.failure_threshold:
                # Se atingir o limite de falhas, abre o circuito
                print("Limite de falhas atingido, circuito agora está OPEN.")
                self.state = 'OPEN'
                self.last_failure_time = time.time()

            raise e  # Repassa a exceção para o chamador

# Tarefa que pode falhar aleatoriamente
def potentially_failing_task():
    print("Tentando executar a tarefa...")
    if time.time() % 2 < 1:  # Simula falhas intermitentes com base no relógio
        raise Exception("Erro na tarefa")
    print("Tarefa executada com sucesso.")

def main():
    # Cria um circuit breaker que permite até 3 falhas consecutivas e espera 5 segundos para tentar se recuperar
    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=5)

    # Simula 10 tentativas de execução da tarefa
    for i in range(10):
        try:
            print(f"\nTentativa {i+1}:")
            cb.call(potentially_failing_task)
        except Exception as e:
            print(e)
        time.sleep(1)  # Aguarda 1 segundo entre as execuções

if __name__ == "__main__":
    main()
