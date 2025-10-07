import schedule
import time
from strategi.volatility import VolatilityHunter
from konfigurasi.pengaturan import INTERVAL_CEK, ENV_MODE

strategi = VolatilityHunter()

if ENV_MODE == "development":
    schedule.every(10).seconds.do(strategi.koin_volatilitas_tinggi)
else:
    schedule.every().day.at("07:00").do(strategi.koin_volatilitas_tinggi)

schedule.every(INTERVAL_CEK).seconds.do(strategi.evaluasi_harga)

print("Scheduler dimulai. Menunggu pukul 07:00 (GMT+7)...")
while True:
    schedule.run_pending()
    time.sleep(30)
