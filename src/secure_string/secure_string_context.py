from typing import Optional
from global_manager import GlobalManager

__all__ = (
    'SecureStringContextManager',
)


class SecureStringContextManager(GlobalManager[bool]):
    """
    What if we are working with someone else's code or code that we cannot change?
    In such cases, protected strings should behave like normal strings.
    In other words, we want to be able to switch modes: normal strings or protected strings.

    ```py
    from secure_string import SecureString, SecureStringContextManager

    ss = SecureString('my password')
    print(ss)  # '***'

    with SecureStringContextManager(False):
        print(ss)  # 'my_password'
    ```
    """
    @classmethod
    def is_protected(cls) -> bool:
        """
        Current protection context.

        :return: True enable protection (default), False - disable protection
        """
        is_protected: Optional[bool] = super().get_current_context()

        if is_protected is True or is_protected is None:
            return True  # by default the protection is on

        return False
