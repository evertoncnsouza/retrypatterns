from padroes_retry import imediato
from padroes_retry import com_intervalo_fixo
from padroes_retry import exponential_backoff_sem_jitter
from padroes_retry import exponential_backoff_com_jitter
from padroes_retry import circuit_breaker
from padroes_retry import fibonacci_backoff
from padroes_retry import com_limite_tentativas
from padroes_retry import baseado_status_code
from padroes_retry import bulkhead_pattern
from padroes_retry import token_bucket_retry
from padroes_retry import rate_limit

if __name__ == "__main__":
    imediato.main()
    com_intervalo_fixo.main()
    exponential_backoff_sem_jitter.main()
    exponential_backoff_com_jitter.main()
    circuit_breaker.main()
    fibonacci_backoff.main()
    com_limite_tentativas.main()
    baseado_status_code.main()
    bulkhead_pattern.main()
    token_bucket_retry.main()
    rate_limit.main()
