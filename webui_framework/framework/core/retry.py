from typing import Callable, TypeVar

T = TypeVar("T")


def retry_call(func: Callable[[], T], retries: int = 3) -> T:
    last_error = None
    for _ in range(retries):
        try:
            return func()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
    raise last_error  # type: ignore[misc]
