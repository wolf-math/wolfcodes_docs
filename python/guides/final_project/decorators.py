from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from models import RecordCollection


P = ParamSpec("P")
R = TypeVar("R")


def action_banner(title: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(function: Callable[P, R]) -> Callable[P, R]:
        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            print(f"\n{title}")
            print("-" * len(title))
            return function(*args, **kwargs)

        return wrapper

    return decorator


def require_owned_records(
    action_name: str,
) -> Callable[[Callable[P, R | None]], Callable[P, R | None]]:
    def decorator(function: Callable[P, R | None]) -> Callable[P, R | None]:
        @wraps(function)
        def wrapper(
            collection: RecordCollection,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> R | None:
            if collection.record_count() == 0:
                print(f"There are no records to {action_name}.")
                return None

            return function(collection, *args, **kwargs)

        return wrapper

    return decorator
