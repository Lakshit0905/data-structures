"""
SDET Problem: Retry Logic for Flaky Tests
==========================================
Implement a retry mechanism that retries a failed function call
up to N times with optional delay between attempts.

Interview Explanation:
    In test automation, network timeouts and race conditions cause
    intermittent failures ("flaky tests"). A retry decorator or utility
    makes tests more resilient. Key parameters: max_retries, delay_seconds,
    and which exceptions to catch.

SDET Use Case:
    Retry an API call that times out, retry a DB query during
    connection issues, or retry a Selenium element click that fails.
"""

import time
import random
import functools


def retry(max_retries: int = 3, delay_seconds: float = 1.0, exceptions=(Exception,)):
    """
    Decorator factory for retrying functions on failure.

    Args:
        max_retries:    Maximum number of retry attempts
        delay_seconds:  Seconds to wait between retries
        exceptions:     Tuple of exception types to catch and retry
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_retries + 1):
                try:
                    result = func(*args, **kwargs)
                    if attempt > 1:
                        print(f"  ✓ Succeeded on attempt {attempt}/{max_retries}")
                    return result
                except exceptions as e:
                    last_exception = e
                    print(f"  ✗ Attempt {attempt}/{max_retries} failed: {e}")
                    if attempt < max_retries:
                        print(f"    Retrying in {delay_seconds}s...")
                        time.sleep(delay_seconds)
            raise last_exception  # Re-raise the last exception after all retries
        return wrapper
    return decorator


def retry_with_result(func, max_retries: int = 3, delay_seconds: float = 0.5):
    """
    Non-decorator version: wrap any callable with retry logic.
    Returns (success: bool, result_or_error).
    """
    for attempt in range(1, max_retries + 1):
        try:
            result = func()
            return True, result
        except Exception as e:
            print(f"  Attempt {attempt}/{max_retries} failed: {e}")
            if attempt < max_retries:
                time.sleep(delay_seconds)
    return False, None


# ── Example functions to demonstrate retry ─────────────────

# Simulate a flaky API call
call_count = 0

def flaky_api_call():
    """Simulates an API call that fails the first 2 times."""
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError(f"Timeout on attempt {call_count}")
    return {"status": 200, "data": "Success!"}


@retry(max_retries=4, delay_seconds=0, exceptions=(ConnectionError,))
def api_call_with_retry():
    """Same flaky function but wrapped with the @retry decorator."""
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError(f"Timeout on attempt {call_count}")
    return {"status": 200, "data": "Success via decorator!"}


if __name__ == "__main__":
    print("=" * 60)
    print("SDET: Retry Logic for Flaky Tests")
    print("=" * 60)

    # Test 1: Non-decorator retry
    print("\nTest 1: retry_with_result() wrapper")
    call_count = 0
    success, result = retry_with_result(flaky_api_call, max_retries=4, delay_seconds=0)
    print(f"  Outcome: success={success}, result={result}")

    # Test 2: Decorator retry
    print("\nTest 2: @retry decorator")
    call_count = 0
    try:
        result = api_call_with_retry()
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  All retries exhausted: {e}")

    # Test 3: Exhaust all retries
    print("\nTest 3: Exhaust all retries (always fails)")

    @retry(max_retries=3, delay_seconds=0)
    def always_fails():
        raise ValueError("Always broken")

    try:
        always_fails()
    except ValueError as e:
        print(f"  Expected failure after retries: {e}")
