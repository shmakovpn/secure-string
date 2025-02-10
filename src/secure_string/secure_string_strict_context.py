from typing import Optional
from functools import wraps
from global_manager import GlobalManager
from .secure_string_strict_exceptions import SecureStringStrictError

__all__ = (
    'SecureStringStrictContextManager',
    'SecureStringStrictDecorator',
)


class SecureStringStrictContextManager(GlobalManager[bool]):
    """
    In the strict mode
    """
    @classmethod
    def is_strict(cls) -> bool:
        """
        Current protection strict mode context.

        :return: True enable strict mode, False - disable strict mode (default)
        """
        is_strict: Optional[bool] = super().get_current_context()

        if is_strict:
            return True

        return False


class SecureStringStrictDecorator:
    """
    Decorator for disallow a decorated method in strict mode context
    """
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if SecureStringStrictContextManager.is_strict():
                raise SecureStringStrictError(f'Method "{func.__name__}" does not allowed in strict mode context')
            return func(*args, **kwargs)

        return wrapper
