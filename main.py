import os
import requests
from datetime import datetime


WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

if not WALLET_ADDRESS:
    raise ValueError("Wallet address not found.")


FAUCET_URL = f"https://faucet.quicknode.com/faucet-sepolia/token/{WALLET_ADDRESS}"

def claim():
    print(f"[{datetime.now()}] 🚀 Mengirim request klaim ke: {FAUCET_URL}")
    response = requests.get(FAUCET_URL)
    if response.status_code == 200:
        print(f"[{datetime.now()}] berhasil: {response.text.strip()}")
    else:
        print(f"[{datetime.now()}] Gagal: {response.status_code}: {response.text.strip()}")

if __name__ == "__main__":
    claim()