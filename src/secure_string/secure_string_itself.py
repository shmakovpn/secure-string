from typing import Optional, Tuple, Union, Iterable, List, TypeVar, Mapping, Sequence, Iterator, Any
from functools import wraps
from .secure_string_context import SecureStringContextManager
from .secure_string_exceptions import SecureStringDoesNotSupportError
from .secure_string_strict_context import SecureStringStrictDecorator

__all__ = (
    'SecureString',
)

_T = TypeVar('_T')


class SecureStringDoesNotSupportDecorator:
    """
    Decorator for disallowed method in SecureString
    """
    def __init__(self, message: Optional[str] = None):
        self._message: Optional[str] = message
        """custom message, if is None, default message will be used"""

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if SecureStringContextManager.is_protected():
                message: str
                if self._message:
                    message = self._message
                else:
                    message = f'Method "{func.__name__}" does not allowed in SecureString'
                raise SecureStringDoesNotSupportError(message)
            return func(*args, **kwargs)

        return wrapper


class SecureStringBehaviourDecorator:
    """
    Decorator, wrap a magic method to switch between a fake and an orig behavior
    """
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            self_: 'SecureString' = args[0]

            if SecureStringContextManager.is_protected():
                # noinspection PyProtectedMember
                return getattr(self_._fake_value, func.__name__)(*args[1:], **kwargs)
            else:
                # noinspection PyProtectedMember
                right_args = [(str(a) if isinstance(a, SecureString) else a) for a in args[1:]]
                right_kwargs = {
                    (str(k) if isinstance(k, SecureString) else k): (str(v) if isinstance(v, SecureString) else v)
                    for k, v in kwargs.items()
                }
                # noinspection PyProtectedMember
                return getattr(self_._orig_value, func.__name__)(*right_args, **right_kwargs)

        return wrapper


class SecureString(str):
    """String that protects passwords from accidentally getting into logs """
    _fake_value: str = '***'
    _orig_value: str = ''

    def __new__(cls, *args, **kwargs):
        str_ = super().__new__(cls, cls._fake_value)
        str_._orig_value = args[0]
        return str_

    @property
    def value(self) -> str:
        """
        the real value

        :raise AttributeError:
        """
        if SecureStringContextManager.is_protected():
            return self._orig_value

        return getattr(super(), 'value')

    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def __add__(self, other) -> str:
        # Why not raise an error?
        # Sometimes one uses 's1 + s2 + s2' to format log messages and etc., instead of interpolation or f-strings
        return ''  # fake return  # pragma: no cover

    # __class__ not needed

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def __contains__(self, item) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator(message='SecureString can not be compared (==)')
    @SecureStringBehaviourDecorator()
    def __eq__(self, other) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def __format__(self, format_spec):
        pass  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator(message='SecureString can not be compared (>=)')
    @SecureStringBehaviourDecorator()
    def __ge__(self, other) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def __getitem__(self, item):
        pass  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def __getnewargs__(self):
        pass  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator(message='SecureString can not be compared (>)')
    @SecureStringBehaviourDecorator()
    def __gt__(self, other):
        pass  # pragma: no cover

    @SecureStringStrictDecorator()
    def __hash__(self) -> int:
        """A secure string can be a dict key"""
        return self._orig_value.__hash__()

    # __init__ not needed
    # __init_subclass__  not needed

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator(message='SecureString does not support __iter__')
    @SecureStringBehaviourDecorator()
    def __iter__(self) -> Iterator[str]:
        return iter([])  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator(message='SecureString can not be compared (<=)')
    @SecureStringBehaviourDecorator()
    def __le__(self, other) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def __len__(self) -> int:
        return 0  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator(message='SecureString can not be compared (<)')
    @SecureStringBehaviourDecorator()
    def __lt__(self, other) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def __mod__(self, other):
        pass  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def __mul__(self, n: int) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator(message='SecureString can not be compared (!=)')
    @SecureStringBehaviourDecorator()
    def __ne__(self, other) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    def __radd__(self, other) -> str:
        # A string does not have __radd__, method, but it need to be added
        # Why not raise an error?
        # Sometimes one uses 's1 + s2 + s2' to format log messages and etc., instead of interpolation or f-strings
        if SecureStringContextManager.is_protected():
            return other + self._fake_value

        return other + self._orig_value

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def __reduce__(self):
        pass  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def __reduce_ex__(self):
        pass  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def __repr__(self) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def __rmod__(self, other):
        pass  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def __rmul__(self, n: int) -> str:
        # A string does not have __rmul__ but it need to be added
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def __sizeof__(self) -> int:
        return 0  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def __str__(self) -> str:
        return ''  # fake return  # pragma: no cover

    # __subclasscheck__ not needed
    # __subclasshook__ not needed

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def capitalize(self) -> str:
        return ''  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def casefold(self) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def center(self) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def count(self, x: str, __start: Optional[int] = None, __end: Optional[int] = None) -> int:
        return 0  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def encode(self, *args, **kwargs) -> bytes:
        return b''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def endswith(
        self,
        suffix: Union[str, Tuple[str, ...]], start: Optional[int] = None, end: Optional[int] = None
    ) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def expandtabs(self, tabsize: int = 8) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def find(self, sub: str, __start: Optional[int] = None, __end: Optional[int] = None) -> int:
        return 0  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def format(self, *args: object, **kwargs: object) -> str:
        return ''  # fake return  # pragma: no cover

    # noinspection PyShadowingBuiltins
    @SecureStringStrictDecorator()
    @SecureStringBehaviourDecorator()
    def format_map(self, map) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def index(self, sub: str, __start: Optional[int] = None, __end: Optional[int] = None) -> int:
        return 0  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isalnum(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isalpha(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isascii(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isdecimal(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isdigit(self) -> bool:
        return False  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isidentifier(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def islower(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isnumeric(self) -> bool:
        return False  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isprintable(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isspace(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def istitle(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def isupper(self) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def join(self, __iterable: Iterable[str]) -> str:
        return ''  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def ljust(self, __width: int, __fillchar: str = ' ') -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def lower(self) -> str:
        return ''  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def lstrip(self, __chars: Optional[str] = None) -> str:
        return ''  # fake return  # pragma: no cover

    # skip maketrans

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def partition(self, __sep: str) -> Tuple[str, str, str]:
        return '', '', ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def replace(self, __old: str, __new: str, __count: int = -1) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def rfind(self, sub: str, __start: Optional[int] = None, __end: Optional[int] = None) -> int:
        return 0  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def rindex(self, sub: str, __start: Optional[int] = None, __end: Optional[int] = None) -> int:
        return 0  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def rjust(self, __width: int, __fillchar: str = ' ') -> str:
        return ''  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def rpartition(self, __sep: str) -> Tuple[str, str, str]:
        return '', '', ''  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def rsplit(self, sep: Optional[str] = None, maxsplit: int = -1) -> List[str]:
        return []  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def rstrip(self, __chars: Optional[str] = None) -> str:
        return ''  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def split(self, sep: Optional[str] = None, maxsplit: int = -1) -> List[str]:
        return []  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def splitlines(self, keepends: bool = False) -> List[str]:
        return []  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def startswith(
        self, prefix: Union[str, Tuple[str, ...]], start: Optional[int] = None, end: Optional[int] = None
    ) -> bool:
        return False  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def strip(self, __chars: Optional[str] = None) -> str:
        return ''  # fake return  # pragma: no cover

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def swapcase(self) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def title(self) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def translate(self, __table: Union[Mapping[int, Union[int, str, None]], Sequence[Union[int, str, None]]]) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def upper(self) -> str:
        return ''  # fake return  # pragma: no cover

    @SecureStringStrictDecorator()
    @SecureStringDoesNotSupportDecorator()
    @SecureStringBehaviourDecorator()
    def zfill(self, __width: int) -> str:
        return ''  # fake return  # pragma: no cover

    # region copy
    @SecureStringStrictDecorator()
    def __copy__(self):
        if SecureStringContextManager.is_protected():
            return SecureString(self.value)

        return self._orig_value

    # noinspection SpellCheckingInspection
    @SecureStringStrictDecorator()
    def __deepcopy__(self, memodict=None):
        if SecureStringContextManager.is_protected():
            return SecureString(self.value)

        return self._orig_value
    # endregion copy
