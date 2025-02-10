import pytest
import pickle
import copy
import json
import secure_string.secure_string_itself as tm
from secure_string.secure_string_strict_exceptions import SecureStringStrictError
from secure_string import SecureStringStrictContextManager


class TestSecureString:
    def test_inheritance(self):
        assert issubclass(tm.SecureString, str)
        assert isinstance(tm.SecureString('hello'), str)

    def test_value(self):
        """test getting the real value of SecureString"""
        assert tm.SecureString('hello').value == 'hello'

        with tm.SecureStringContextManager(False):
            with pytest.raises(AttributeError):
                _value = tm.SecureString('hello').value

        with SecureStringStrictContextManager(True):
            assert tm.SecureString('hello').value == 'hello'

    def test__add(self):
        assert tm.SecureString('hello') + ' Bob' == tm.SecureString._fake_value + ' Bob'

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello') + ' Bob' == 'hello Bob'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello') + ' Bob'

    def test__contains(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            assert 'e' in tm.SecureString('hello')

        with tm.SecureStringContextManager(False):
            assert 'e' in tm.SecureString('hello')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                assert 'e' in tm.SecureString('hello')

    def test__eq(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            assert tm.SecureString('hello') == 'hello'

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello') == 'hello'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello') == 'hello'

    def test__format(self):
        assert tm.SecureString('hello').__format__('') == tm.SecureString._fake_value.__format__('')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').__format__('') == 'hello'.__format__('')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').__format__('')

    def test__ge(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            assert tm.SecureString('d') >= 'c'

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('d') >= 'c'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                assert tm.SecureString('d') >= 'c'

    def test__getitem(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello')[0]

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello')[0] == 'h'
            assert tm.SecureString('hello')[:2] == 'he'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello')[0]

    def test__getnewargs(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').__getnewargs__()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').__getnewargs__() == ('hello', )

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').__getnewargs__()

    def test__gt(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            assert tm.SecureString('b') > 'a'

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('b') > 'a'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                assert tm.SecureString('b') > 'a'

    def test__hash(self):
        assert hash(tm.SecureString('hello')) == hash('hello')

        with tm.SecureStringContextManager(False):
            assert hash(tm.SecureString('hello')) == hash('hello')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = hash(tm.SecureString('hello'))

    # __init_subclass__  not needed

    def test__iter(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = iter(tm.SecureString('hello'))

        with tm.SecureStringContextManager(False):
            assert list(iter(tm.SecureString('hello'))) == [s for s in 'hello']

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = iter(tm.SecureString('hello'))

    def test__le(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            assert tm.SecureString('c') <= 'd'

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('c') <= 'd'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                assert tm.SecureString('c') <= 'd'

    def test__len(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = len(tm.SecureString('hello'))

        with tm.SecureStringContextManager(False):
            assert len(tm.SecureString('hello')) == len('hello')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = len(tm.SecureString('hello'))

    def test__lt(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            assert tm.SecureString('a') < 'b'

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('a') < 'b'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                assert tm.SecureString('a') < 'b'

    def test__mod(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('a %s a') % 'hello'

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('b %s b') % 'hello' == 'b hello b'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('a %s a') % 'hello'

    def test__mul(self):
        assert tm.SecureString('hello') * 2 == tm.SecureString._fake_value * 2

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello') * 2 == 'hello' * 2

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello') * 2

    def test__ne(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            assert tm.SecureString('hello') != 'hello'

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello') != 'foo'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello') != 'foo'

    def test__radd(self):
        assert 'say ' + tm.SecureString('hello') == 'say ' + tm.SecureString._fake_value

        with tm.SecureStringContextManager(False):
            assert 'say ' + tm.SecureString('hello') == 'say hello'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = 'say ' + tm.SecureString('hello')

    def test__reduce(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').__reduce__()

        with tm.SecureStringContextManager(False):
            with pytest.raises(TypeError):
                _r = tm.SecureString('hello').__reduce__()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').__reduce__()

    def test__reduce_ex(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').__reduce_ex__(pickle.DEFAULT_PROTOCOL)

        with tm.SecureStringContextManager(False):
            with pytest.raises(TypeError):
                _r = tm.SecureString('hello').__reduce__(pickle.DEFAULT_PROTOCOL)

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').__reduce__(pickle.DEFAULT_PROTOCOL)

    def test__repr(self):
        assert repr(tm.SecureString('hello')) == repr(tm.SecureString._fake_value)

        with tm.SecureStringContextManager(False):
            assert repr(tm.SecureString('hello')) == repr('hello')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = repr(tm.SecureString('hello'))

    def test__rmod(self):
        # this test the same as test_interpolation,
        # but explicit is better than implicit
        assert 'z %s z' % tm.SecureString('hello') == f'z {tm.SecureString._fake_value} z'

        with tm.SecureStringContextManager(False):
            assert 'z %s z' % tm.SecureString('hello') == f'z hello z'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                'z %s z' % tm.SecureString('hello')

    def test__rmul(self):
        assert 2 * tm.SecureString('hello') == 2 * tm.SecureString._fake_value

        with tm.SecureStringContextManager(False):
            assert 2 * tm.SecureString('hello') == 2 * 'hello'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = 2 * tm.SecureString('hello')

    def test__sizeof(self):
        assert tm.SecureString('hello').__sizeof__()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').__sizeof__() == 'hello'.__sizeof__()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').__sizeof__()

    def test__str(self):
        assert str(tm.SecureString('hello')) == str(tm.SecureString._fake_value)

        with tm.SecureStringContextManager(False):
            assert str(tm.SecureString('hello')) == str('hello')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = str(tm.SecureString('hello'))

    # __subclasscheck__ not needed
    # __subclasshook__ not needed

    def test_capitalize(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').capitalize()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hellO').capitalize() == 'Hello'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').capitalize()

    # noinspection SpellCheckingInspection
    def test_casefold(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').casefold()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hellO').casefold() == 'hello'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').casefold()

    def test_center(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').center(10)

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').center(10) == 'hello'.center(10)

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').center(10)

    def test_count(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').count('l')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').count('l') == 'hello'.count('l')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').count('l')

    def test_encode(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').encode()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').encode() == 'hello'.encode()

    def test_endswith(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').endswith('o')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').endswith('o') is True

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').endswith('o')

    def test_expandtabs(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').expandtabs(2)

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').expandtabs(2) == 'hello'.expandtabs(2)

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').expandtabs(2)

    def test_find(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').find('e')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').find('e') == 'hello'.find('e')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').find('e')

    def test_format(self):
        assert 'c {} c'.format(tm.SecureString('hello')) == f'c {tm.SecureString._fake_value} c'

        with tm.SecureStringContextManager(False):
            assert 'c {} c'.format(tm.SecureString('hello')) == 'c hello c'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = 'c {} c'.format(tm.SecureString('hello'))

    def test_format_map(self):
        assert tm.SecureString('e {v} e').format_map({'v': 't'}) == tm.SecureString._fake_value

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('e {v} e').format_map({'v': 't'}) == 'e t e'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('e {v} e').format_map({'v': 't'})

    def test_index(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').index('e')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').index('e') == 1

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').index('e')

    def test_isalnum(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isalnum()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isalnum() == 'hello'.isalnum()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isalnum()

    def test_isalpha(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isalpha()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isalpha() == 'hello'.isalpha()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isalpha()

    def test_isascii(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isascii()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isascii() == 'hello'.isascii()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isascii()

    def test_isdecimal(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isdecimal()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isdecimal() == 'hello'.isdecimal()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isdecimal()

    def test_isdigit(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isdigit()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isdigit() == 'hello'.isdigit()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isdigit()

    # noinspection SpellCheckingInspection
    def test_isidentifier(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isidentifier()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isidentifier() == 'hello'.isidentifier()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isidentifier()

    def test_islower(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').islower()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').islower() == 'hello'.islower()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').islower()

    def test_isnumeric(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isnumeric()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isnumeric() == 'hello'.isnumeric()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isnumeric()

    # noinspection SpellCheckingInspection
    def test_isprintable(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isprintable()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isprintable() == 'hello'.isprintable()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isprintable()

    def test_isspace(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isspace()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isspace() == 'hello'.isspace()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isspace()

    def test_istitle(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').istitle()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').istitle() == 'hello'.istitle()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').istitle()

    def test_isupper(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').isupper()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').isupper() == 'hello'.isupper()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').isupper()

    def test_join(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('.').join(['a', 'b'])

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('.').join(['a', 'b']) == '.'.join(['a', 'b'])

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('.').join(['a', 'b'])

    # noinspection SpellCheckingInspection
    def test_ljust(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').ljust(2, 'x')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').ljust(2, 'x') == 'hello'.ljust(2, 'x')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').ljust(2, 'x')

    def test_lower(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').lower()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hellO').lower() == 'hello'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').lower()

    # noinspection SpellCheckingInspection
    def test_lstrip(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').lstrip()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').lstrip() == 'hello'.lstrip()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').lstrip()

    def test_partition(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').partition('l')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').partition('l') == 'hello'.partition('l')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').partition('l')

    def test_replace(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').replace('e', 'x')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').replace('e', 'x') == 'hello'.replace('e', 'x')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').replace('e', 'x')

    def test_rfind(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').rfind('e')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').rfind('e') == 'hello'.rfind('e')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').rfind('e')

    # noinspection SpellCheckingInspection
    def test_rindex(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').rindex('e')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').rindex('e') == 'hello'.rindex('e')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').rindex('e')

    # noinspection SpellCheckingInspection
    def test_rjust(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').rjust(2)

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').rjust(2) == 'hello'.rjust(2)

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').rjust(2)

    # noinspection SpellCheckingInspection
    def test_rpartition(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').rpartition('l')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').rpartition('l') == 'hello'.rpartition('l')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').rpartition('l')

    def test_rsplit(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').rsplit('l')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').rsplit('l') == 'hello'.rsplit('l')

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').rsplit('l')

    # noinspection SpellCheckingInspection
    def test_rstrip(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').rstrip()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').rstrip() == 'hello'.rstrip()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').rstrip()

    def test_split(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('a,b').split(',')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('a,b').split(',') == ['a', 'b']

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('a,b').split(',')

    def test_splitlines(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').splitlines()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').splitlines() == 'hello'.splitlines()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').splitlines()

    def test_startswith(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').startswith('h')

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').startswith('h') is True

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').startswith('h')

    def test_strip(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').strip()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').strip() == 'hello'.strip()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').strip()

    # noinspection SpellCheckingInspection
    def test_swapcase(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').swapcase()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').swapcase() == 'hello'.swapcase()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').swapcase()

    def test_title(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').title()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').title() == 'hello'.title()

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').title()

    def test_translate(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').translate({})

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').translate({}) == 'hello'.translate({})

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').translate({})

    def test_upper(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').upper()

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hellO').upper() == 'HELLO'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').upper()

    def test_zfill(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = tm.SecureString('hello').zfill(1)

        with tm.SecureStringContextManager(False):
            assert tm.SecureString('hello').zfill(1) == 'hello'.zfill(1)

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = tm.SecureString('hello').zfill(1)

    # region interpolation
    def test_interpolation(self):
        assert 'x %s x' % tm.SecureString('hello') == f'x {tm.SecureString._fake_value} x'

        with tm.SecureStringContextManager(False):
            assert 'x %s x' % tm.SecureString('hello') == 'x hello x'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = 'x %s x' % tm.SecureString('hello')

    def test_f_interpolation(self):
        assert f'y {tm.SecureString("hello")} y' == f'y {tm.SecureString._fake_value} y'

        with tm.SecureStringContextManager(False):
            assert f'y {tm.SecureString("hello")} y' == 'y hello y'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = f'y {tm.SecureString("hello")} y'
    # endregion interpolation

    def test_json_dumps(self):
        ss = tm.SecureString('hello')
        ss_dumped = json.dumps(ss)
        assert ss_dumped == json.dumps(tm.SecureString._fake_value)

        # json.dumps default encoder uses `encode_basestring_ascii`, this function written on C
        # thus `SecureStringContextManager` is useless.
        # But `json.dumps` protected strings is a bad practice

    def test_dict_key(self):
        dict_ = {tm.SecureString('hello'): '_hello', tm.SecureString('bye'): '_bye'}
        assert len(dict_) == 2

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = {tm.SecureString('hello'): '_hello', tm.SecureString('bye'): '_bye'}

    # region copy
    def test_copy(self):
        assert isinstance(copy.copy(tm.SecureString('hello')), tm.SecureString)
        assert str(copy.copy(tm.SecureString('hello'))) == tm.SecureString._fake_value

        with tm.SecureStringContextManager(False):
            assert copy.copy(tm.SecureString('hello')) == 'hello'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = copy.copy(tm.SecureString('hello'))

    def test_deepcopy(self):
        assert isinstance(copy.deepcopy(tm.SecureString('hello')), tm.SecureString)
        assert str(copy.deepcopy(tm.SecureString('hello'))) == tm.SecureString._fake_value

        with tm.SecureStringContextManager(False):
            assert copy.deepcopy(tm.SecureString('hello')) == 'hello'

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = copy.deepcopy(tm.SecureString('hello'))
    # endregion copy

    def test_reversed(self):
        with pytest.raises(tm.SecureStringDoesNotSupportError):
            _r = reversed(tm.SecureString('hello'))

        with tm.SecureStringContextManager(False):
            assert list(reversed(tm.SecureString('hello'))) == list(reversed('hello'))

        with SecureStringStrictContextManager(True):
            with pytest.raises(SecureStringStrictError):
                _r = reversed(tm.SecureString('hello'))
