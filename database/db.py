from sqlmodel import Session, create_engine, SQLModel
from konfigurasi.pengaturan import DATABASE_URL
from model.tabel import Transaksi, PergerakanHarga
from utilitas.enums import Posisi, Sisi

db_engine = create_engine(DATABASE_URL, echo=False)
SQLModel.metadata.create_all(db_engine)


def simpan_transaksi(
    simbol: str, posisi: Posisi, sisi: Sisi, kuantitas: float, harga: float
) -> None:
    with Session(db_engine) as sesi:
        transaksi = Transaksi(
            simbol=simbol, posisi=posisi, sisi=sisi, kuantitas=kuantitas, harga=harga
        )
        sesi.add(transaksi)
        sesi.commit()
        print(f"Transaksi disimpan: {simbol} {posisi} {sisi} {kuantitas} @ {harga}")


def simpan_harga(
    simbol: str, harga: float, persen_perubahan: float, posisi: Posisi
) -> None:
    with Session(db_engine) as sesi:
        pergerakan_harga = PergerakanHarga(
            simbol=simbol, harga=harga, persen_perubahan=persen_perubahan, posisi=posisi
        )
        sesi.add(pergerakan_harga)
        sesi.commit()
