from enum import Enum


class TipeMargin(str, Enum):
    ISOLATED = "ISOLATED"
    CROSSED = "CROSSED"


class Posisi(str, Enum):
    LONG = "LONG"
    SHORT = "SHORT"


class Sisi(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class TipeOrder(str, Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"


class Tindakan(str, Enum):
    BUKA = "BUKA"
    TUTUP = "TUTUP"
