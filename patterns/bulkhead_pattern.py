import time
import concurrent.futures


def process_task(task_id):
    print(f"Attempting to process task {task_id}...")
    if task_id % 2 == 0:
        raise Exception(f"Error in task {task_id}")


def retry_task(task_id, max_retries=3):
    for attempt in range(max_retries):
        try:
            process_task(task_id)
            print(f"Task {task_id} completed successfully.")
            return
        except Exception as e:
            print(f"{e}. Attempt {attempt + 1} of {max_retries}.")
            time.sleep(1)
    print(f"Task {task_id} failed after {max_retries} attempts.")


def main():
    tasks = range(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(retry_task, task_id) for task_id in tasks]
        concurrent.futures.wait(futures)


if __name__ == "__main__":
    main()
