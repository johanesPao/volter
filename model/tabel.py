from sqlmodel import SQLModel, Field
from sqlalchemy import Enum as SQLEnum
from datetime import datetime, timezone, timedelta

from konfigurasi.pengaturan import TZ
from utilitas.enums import Posisi, Sisi


def tz():
    tz = timezone(timedelta(hours=TZ))
    return datetime.now(tz)


class Transaksi(SQLModel, table=True):
    __tablename__ = "Transaksi"

    id: int | None = Field(default=None, primary_key=True)
    simbol: str
    posisi: Posisi = Field(sa_column=SQLEnum(Posisi))
    sisi: Sisi = Field(sa_column=SQLEnum(Sisi))
    kuantitas: float
    harga: float
    timestamp: datetime = Field(default_factory=tz)


class PergerakanHarga(SQLModel, table=True):
    __tablename__ = "PergerakanHarga"

    id: int | None = Field(default=None, primary_key=True)
    simbol: str
    harga: float
    persen_perubahan: float
    posisi: Posisi | None = Field(sa_column=SQLEnum(Posisi))
    timestamp: datetime = Field(default_factory=tz)
