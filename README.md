# secure-string

![Tests](https://github.com/shmakovpn/secure-string/actions/workflows/python-package.yml/badge.svg)
[![codecov](https://codecov.io/github/shmakovpn/secure-string/graph/badge.svg?token=744XXMAKOZ)](https://codecov.io/github/shmakovpn/secure-string)
![Mypy](https://github.com/shmakovpn/secure-string/actions/workflows/mypy.yml/badge.svg)

Protects passwords from accidentally getting into logs

## Installation

```bash
pip install secure-strings  # not secure-string, but secure-strings
```

## Examples

```py
from secure_string import SecureString, SecureStringContextManager, SecureStringStrictContextManager


password = SecureString('my password')
print(password)  # this will prints '***' to stdout
print(password.value)  # this will prints 'my password', use the `value` property to get real value

# we can disable string protection
with SecureStringContextManager(False):
    print(password)  # 'my password'


# we can also enable strict mode when we need to find a place where the password can be displayed
with SecureStringStrictContextManager(True):
    print(password)  # SecureStringStrictError, Method "__str__" does not allowed in strict mode context
```
