import time


def process_task():
    print("Attempting to perform the task...")
    raise Exception("Processing error")


def retry_with_rate_limit(task, max_retries=5, rate_limit=2):
    retry_count = 0
    while retry_count < max_retries:
        try:
            task()
            print("Task completed successfully.")
            return
        except Exception as e:
            retry_count += 1
            if retry_count >= max_retries:
                print(f"Error: {e}. Maximum attempts reached, stopping retries.")
                return
            print(
                f"Error: {e}. Attempt {retry_count} of {max_retries}. Retrying in {rate_limit} seconds...")
            time.sleep(rate_limit)


def main():
    retry_with_rate_limit(process_task, max_retries=5, rate_limit=2)


if __name__ == "__main__":
    main()
