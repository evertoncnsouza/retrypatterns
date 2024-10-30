import time
import requests


def should_retry(status_code):
    # Define the status codes that should trigger a retry
    retry_statuses = [500, 502, 503, 504]
    return status_code in retry_statuses


def make_request_with_retry(url, max_retries=5):
    retry_count = 0
    while retry_count < max_retries:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successful request")
            return response
        elif should_retry(response.status_code):
            retry_count += 1
            wait_time = 2 ** retry_count  # Exponential backoff
            print(
                f"Error {response.status_code}: Attempt {retry_count} of {max_retries}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print(f"Error {response.status_code}: Retry not possible.")
            return response
    print("Maximum retry attempts reached.")
    return None


def main():
    url = "https://example.com/api"
    response = make_request_with_retry(url)
    if response:
        print("Response:", response.content)


if __name__ == "__main__":
    main()
