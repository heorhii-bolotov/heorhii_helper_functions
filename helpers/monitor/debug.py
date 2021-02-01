from datetime import datetime
from icecream import ic


def set_prefix(s: str) -> None: ic.configureOutput(prefix=f'{s}|')


def set_time_prefix() -> None: ic.configureOutput(prefix=lambda: f'{datetime.now()}|')


def set_context() -> None: ic.configureOutput(includeContext=True)


def p(*args, **kwargs) -> None: print(*args, **kwargs)

