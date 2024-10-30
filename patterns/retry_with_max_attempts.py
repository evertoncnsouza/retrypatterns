import time


def process_task():
    print("Attempting to perform the task...")
    raise Exception("Processing error")


def main():
    max_retries = 5
    retry_count = 0

    while retry_count < max_retries:
        try:
            process_task()
            break  # Success, exit the loop
        except Exception as e:
            retry_count += 1
            if retry_count >= max_retries:
                print(f"Error: {e}. Maximum attempts reached, stopping retries.")
                break
            print(f"Error: {e}. Attempt {retry_count} of {max_retries}. Retrying in 2 seconds...")
            time.sleep(2)  # Fixed interval


if __name__ == "__main__":
    main()
