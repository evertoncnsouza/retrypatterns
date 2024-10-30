def process_task():
    print("Attempting to process the task...")
    raise Exception("Processing error")


def main():
    while True:
        try:
            process_task()
            break  # Success, exit the loop
        except Exception as e:
            print(f"Error: {e}. Retrying...")  # Immediate retry, no pause


if __name__ == "__main__":
    main()
