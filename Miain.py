import subprocess
import time

# Menentukan alamat wallet Binance Coin
wallet_address = "0x0123456789abcdef" #tambahkan wallet coin crypto kalian sesuai  dengan coin crypto pool kalian
# Menentukan alamat pool mining
mining_pool = "pool.binance.com:3333" #tambahkan pool pada 
# Menentukan perintah penambangan
mining_command = [
    "ethminer.exe", # Ubah ethminer menjadi ethminer.exe jika menggunakan sistem operasi Windows
    "--algo=ethash",
    "--server=" + mining_pool,
    "--user=" + wallet_address,
    "--no-precompute",
]
# Memulai proses penambangan
while True:
    try:
        completed_process = subprocess.run(mining_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = completed_process.stdout.decode().strip()
        if completed_process.returncode != 0:
            raise Exception("Mining process failed.")
        print(f"Mining output: {output}")
    except Exception as e:
        print(f"Mining error: {str(e)}")
    time.sleep(30) # Tunggu selama 30 detik sebelum memulai penambangan lagi
