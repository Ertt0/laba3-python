class CatalogError(Exception):
    pass


class InvalidEntity(CatalogError):
    pass


class DuplicateID(CatalogError):
    pass


class ObjectNotFound(CatalogError):
    pass


class UnsupportedFormatVersion(CatalogError):
    pass


class CorruptedFile(CatalogError):
    pass
