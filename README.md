
## 🚀 Cara #1: Jalankan Otomatis (GitHub Actions)

1. Klik tombol **"Use this template"** di atas.
2. Masuk ke tab **Settings → Secrets → Actions**
3. Klik **"New repository secret"**:
   - **Name**: `WALLET_ADDRESS`
   - **Value**: alamat wallet kamu (contoh: `0x1234abcd...`)
4. Buka tab **Actions**, jalankan workflow manual 1x untuk test.
5. Faucet akan otomatis diklaim setiap hari jam **14:00 WIB** (07:00 UTC)

---

## 🖥️ Cara #2: Jalankan di Laptop Sendiri (Local)

1. Clone repo ini:

```bash
git clone https://github.com/UpTo1M/eth-faucet-claimer.git
cd eth-faucet-claimer
