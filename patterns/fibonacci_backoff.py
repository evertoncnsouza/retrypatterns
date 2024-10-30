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
            print("Attempting to perform the task...")
            raise Exception("Task error")
        except Exception as e:
            wait_time = fibonacci_backoff(attempt)
            print(f"Error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)


if __name__ == "__main__":
    main()
