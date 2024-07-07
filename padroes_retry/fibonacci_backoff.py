import time


def fibonacci_backoff(attempt):
    fib_sequence = [1, 1]
    for i in range(2, attempt + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[attempt]


def main():
    max_retries = 10
    for attempt in range(max_retries):
        try:
            print("Tentando realizar a tarefa...")
            raise Exception("Erro na tarefa")
        except Exception as e:
            wait_time = fibonacci_backoff(attempt)
            print(f"Erro: {e}. Tentando novamente em {wait_time} segundos...")
            time.sleep(wait_time)


if __name__ == "__main__":
    main()
