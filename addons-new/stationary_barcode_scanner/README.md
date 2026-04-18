# Stationary Barcode Scanner

Addon Odoo 18 untuk mempermudah dan mempercepat input barang-barang stationary ke dalam document Sales Order.
Dikarenakan barang stationary ukurannya kecil-kecil dan banyak jenisnya, addon ini memungkinkan user langsung melakukan **scan barcode** dari hardware scanner atau mengetiknya manual.

## Fitur:
1. Input auto-focus pada form Sales Order untuk menangkap scan barcode.
2. Otomatis menambahkan product ke Order Lines jika product baru di-scan.
3. Menambahkan quantity (+1) otomatis jika product sudah ada dalam order.
4. UI feedback notifikasi sukses dan gagal secara langsung saat update order line.

## Cara Penggunaan:
1. Pindah ke modul **Sales**.
2. Buat Quotation / Order Baru atau buka Order yang stavenya Draft / Sent.
3. Di panel detail Form, di sebelum list product ada input *Scan stationary barcode here*.
4. Arahkan scanner dan tembak barcode, atau ketik via keyboard lalu tekan Enter.
5. Notifikasi akan keluar jika scan sukses atau produk tidak ditemukan.

## Instalasi
Letakkan di addons path, update app list, dan install `stationary_barcode_scanner`.
Modul ini requires modul `sale` (Sales) dan `barcodes`.

Fixes #1
