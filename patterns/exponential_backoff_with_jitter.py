import time
import random


def process_task():
    print("Attempting to process the task...")
    raise Exception("Processing error")


def main():
    max_retries = 5
    base_delay = 1  # Base time in seconds

    for attempt in range(max_retries):
        try:
            process_task()
            break  # Success, exit the loop
        except Exception as e:
            wait_time = base_delay * (2 ** attempt)  # Exponential backoff
            wait_time += random.uniform(0, 1)  # Jitter to avoid collisions
            print(f"Error: {e}. Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)


if __name__ == "__main__":
    main()
