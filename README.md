
# IoT Dashboard REST API

## Deskripsi
Project Internet of Things (IoT) untuk monitoring sensor dan kontrol perangkat menggunakan REST API.

## Fitur
- Monitoring suhu.
- Monitoring kelembapan.
- Grafik monitoring suhu.
- Grafik monitoring kelembapan.
- Kontrol lampu ON dan OFF.
- Penyimpanan riwayat sensor menggunakan SQLite.
- Menampilkan 10 data sensor terakhir.

## Teknologi
- Node-RED
- REST API
- HTML
- CSS
- JavaScript
- Chart.js
- SQLite

## Endpoint API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | /api/suhu | Mengambil data sensor |
| GET | /api/history | Mengambil riwayat sensor |
| POST | /api/kontrol | Mengontrol perangkat |

## Cara Menjalankan
1. Jalankan Node-RED.
2. Import flow project.
3. Deploy flow.
4. Jalankan simulator sensor.
5. Buka file dashboard HTML melalui browser.
