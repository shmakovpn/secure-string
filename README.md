# secure-string

![Tests](https://github.com/shmakovpn/secure-string/actions/workflows/python-package.yml/badge.svg)
[![codecov](https://codecov.io/github/shmakovpn/secure-string/graph/badge.svg?token=744XXMAKOZ)](https://codecov.io/github/shmakovpn/secure-string)
![Mypy](https://github.com/shmakovpn/secure-string/actions/workflows/mypy.yml/badge.svg)
[![pypi](https://img.shields.io/pypi/v/secure-strings.svg)](https://pypi.python.org/pypi/secure-strings)
[![downloads](https://static.pepy.tech/badge/secure-strings/month)](https://pepy.tech/project/secure-strings)
[![versions](https://img.shields.io/pypi/pyversions/secure-strings.svg)](https://github.com/shmakovpn/secure-string)

Protects passwords from accidentally getting into logs

## Installation

```bash
pip install secure-strings  # not secure-string, but secure-strings
```

## Examples

```py
from secure_string import SecureString, SecureStringContextManager, SecureStringStrictContextManager


password = SecureString('my password')
print(password)  # this will print '***' to stdout
print(password.value)  # this will print 'my password', use the `value` property to get real value

# we can disable string protection
with SecureStringContextManager(False):
    print(password)  # 'my password'


# we can also enable strict mode when we need to find a place where the password can be displayed
with SecureStringStrictContextManager(True):
    print(password)  # SecureStringStrictError, Method "__str__" does not allowed in strict mode context
```
