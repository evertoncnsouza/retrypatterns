import time


class CircuitBreaker:
    def __init__(self, failure_threshold, recovery_timeout):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time = 0
        self.state = 'CLOSED'

    def call(self, func):
        if self.state == 'OPEN':
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = 'HALF-OPEN'
            else:
                raise Exception("Circuit is open, request denied")

        try:
            result = func()
            self.state = 'CLOSED'
            self.failures = 0
            return result
        except Exception as e:
            self.failures += 1
            if self.failures >= self.failure_threshold:
                self.state = 'OPEN'
                self.last_failure_time = time.time()
            raise e


def potentially_failing_task():
    print("Tentando realizar a tarefa...")
    raise Exception("Erro na tarefa")


def main():
    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=5)

    for _ in range(10):
        try:
            cb.call(potentially_failing_task)
        except Exception as e:
            print(e)
            time.sleep(1)


if __name__ == "__main__":
    main()
