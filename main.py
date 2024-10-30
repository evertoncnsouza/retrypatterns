from patterns import immediate_retry
from patterns import fixed_interval_retry
from patterns import exponential_backoff_with_jitter
from patterns import circuit_breaker
from patterns import fibonacci_backoff
from patterns import retry_with_max_attempts
from patterns import status_code_based_retry
from patterns import bulkhead_pattern
from patterns import token_bucket_retry
from patterns import rate_limit

if __name__ == "__main__":
    bulkhead_pattern.main()
    circuit_breaker.main()
    exponential_backoff_with_jitter.main()
    fibonacci_backoff.main()
    fixed_interval_retry.main()
    immediate_retry.main()
    rate_limit.main()
    retry_with_max_attempts.main()
    status_code_based_retry.main()
    token_bucket_retry.main()
