MBLENGTH: dict[int, int]

class Charset:
    id: int
    name: str
    collation: str
    is_default: bool
    def __init__(self, id: int, name: str, collation: str, is_default: str) -> None: ...
    @property
    def encoding(self) -> str: ...
    @property
    def is_binary(self) -> bool: ...

class Charsets:
    def __init__(self) -> None: ...
    def add(self, c: Charset) -> None: ...
    def by_id(self, id: int) -> Charset: ...
    def by_name(self, name: str) -> Charset: ...

def charset_by_name(name: str) -> Charset: ...
def charset_by_id(id: str) -> Charset: ...
