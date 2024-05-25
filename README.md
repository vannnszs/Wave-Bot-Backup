# Wave-Bot

Wave-Bot adalah skrip otomatisasi menggunakan Selenium WebDriver untuk mengotomatisasi interaksi dengan sebuah situs web. Skrip ini mengotomatiskan proses login, klaim, dan pengecekan waktu berikutnya untuk melakukan klaim lagi.

## Prasyarat

- Python 3.x
- Selenium
- ChromeDriver yang sesuai dengan versi Google Chrome Anda

## Instalasi

1. Clone repositori ini ke direktori lokal Anda:

    ```bash
    git clone https://github.com/vannszs/Wave-Bot.git
    ```

2. Install dependencies yang diperlukan:

    ```bash
    pip install selenium
    ```

3. Download dan pasang [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) yang sesuai dengan versi Google Chrome yang terpasang di komputer Anda. Pastikan `ChromeDriver` ada di PATH atau tempatkan di direktori yang sesuai dan sesuaikan jalur di dalam skrip jika perlu.

## Penggunaan

1. Atur path ke ChromeDriver dan direktori sesi pengguna di dalam skrip jika diperlukan:

    ```python
    session_path = "C:/selenium"  # Sesuaikan dengan path Anda
    ```

2. Jalankan skrip:

    ```bash
    python script_name.py
    ```

3. Skrip akan meminta Anda untuk memasukkan autentikasi web dan pharse untuk login:

    ```plaintext
    Masukan Web Auth anda :
    Masukan Pharse anda untuk login :
    ```

    Untuk mendapatkan "Masukan Web Auth anda", ikuti langkah-langkah berikut:

    - Buka [Telegram Web](https://web.telegram.org/) menggunakan Chrome.
    - Login ke akun Telegram Anda.
    - Cari dan buka WaveWallet.
    - Tunggu sampai iframe popup muncul, kemudian inspect element dan cari link berawalan "waveapp" dengan cara ctrl + F.
         <div align="center">
        <img src="https://i.postimg.cc/j5W9S5FN/Screenshot-2024-05-20-001438.png" alt="Screenshot" style="width: 80%; margin: 50px;">
    </div>

    - Salin link tersebut dan masukkan ke dalam skrip ketika diminta.

## Penjelasan Skrip

- Mengatur opsi ChromeDriver untuk menggunakan user-agent mobile, mengurangi logging, dan menjalankan browser dalam mode headless.
- Mengotomatiskan proses login dengan memasukkan pharse pengguna.
- Mengklaim item di halaman web secara berkala dan menunggu waktu tertentu sebelum melakukan klaim berikutnya.

## Catatan

- Pastikan Anda memiliki izin untuk mengotomatiskan interaksi dengan situs web yang Anda targetkan.
- Gunakan skrip ini dengan bijak dan sesuai dengan kebijakan situs web.

## Kontribusi

Kontribusi sangat diterima. Silakan fork repositori ini dan ajukan pull request dengan perubahan yang Anda rasa dapat memperbaiki proyek ini.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT. Lihat file `LICENSE` untuk informasi lebih lanjut.
