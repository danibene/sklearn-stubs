from typing import Any, Callable

class CachedProperty:
    def __init__(self, func: Callable) -> None: ...
    def __get__(self, obj: Any, typ: Any) -> Any: ...
    def __set__(self, obj: Any, value: Any) -> None: ...

cache_readonly = CachedProperty

class AxisProperty:
    def __init__(self, axis: int = ..., doc: str = ...) -> None: ...
    def __get__(self, obj: Any, typ: Any) -> Any: ...
    def __set__(self, obj: Any, value: Any) -> None: ...
