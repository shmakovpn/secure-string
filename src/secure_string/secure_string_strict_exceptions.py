class SecureStringStrictError(TypeError):
    """
    In protected mode, all attempts to access a SecureString instance other than
    explicitly through the `value` property will throw a SecureStringStrictError.
    """
    pass
