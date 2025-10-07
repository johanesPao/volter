from binance.client import Client
from konfigurasi.pengaturan import API
from utilitas.enums import Sisi, TipeOrder

klien = Client(API.KEY, API.SECRET_KEY)


def ticker_24_jam(simbol: str = None) -> dict:
    if simbol:
        return klien.get_symbol_ticker(symbol=simbol)
    return klien.get_ticker()


def buat_order_future(
    simbol: str, sisi: Sisi, tipe_order: TipeOrder, kuantitas: float, reduce_only=False
) -> dict:
    return klien.futures_create_order(
        symbol=simbol,
        side=sisi,
        type=tipe_order,
        quantity=kuantitas,
        reduceOnly=reduce_only,
    )
