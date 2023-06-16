from enum import Enum

class ContractType(str, Enum):
    FORWARD: str = 'FORWARD'
    EUROPEANOPTION: str = 'EUROPEANOPTION'
    AMERICANOPTION: str = 'AMERICANOPTION'
    EUROPEANDIGITALOPTION: str = 'EUROPEANDIGITALOPTION'
    ASIANOPTION: str = 'ASIANOPTION'
    EUROPEANBARRIEROPTION: str = 'EUROPEANBARRIEROPTION'


class Stock(str, Enum):
    # todo: replace EXAMPLE stocks with meaningful names
    EXAMPLE1: str = 'EXAMPLE1'
    EXAMPLE2: str = 'EXAMPLE2'


class PutCallFwd(str, Enum):
    PUT: str = 'PUT'
    CALL: str = 'CALL'
    FWD: str = 'FWD'


class Measure(str, Enum):
    FAIR_VALUE: str = 'FAIR_VALUE'
    DELTA: str = 'DELTA'
    GAMMA: str = 'GAMMA'
    VEGA: str = 'VEGA'
    THETA: str = 'THETA'
    RHO: str = 'RHO'


class GreekMethod(str, Enum):
    ANALYTIC: str = 'ANALYTIC'
    BUMP: str = 'BUMP'


class LongShort(str, Enum):
    LONG: str = 'LONG'
    SHORT: str = 'SHORT'


class UpDown(str, Enum):     # for Barrier Contract
    UP: str = 'UP'
    DOWN: str = 'DOWN'


class InOut(str, Enum):     # for Barrier Contract
    IN: str = 'IN'
    OUT: str = 'OUT'




>>>>>>>>> Temporary merge branch 2
