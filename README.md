# WeatherPrep 1.0:Program Python Memberikan rekomendasi bepergian sebelum bepergian dengan prakiraan cuaca 3 jam kedepan
Program Python ini memberikan rekomendasi kendaraan, pakaian, dan barang bawaan yang relevan untuk membantu pengguna mempersiapkan diri sebelum bepergian berdasarkan prakiraan cuaca di kota pengguna (dari input pengguna).
Data Prakiraan Cuaca didapatkan dari API Meteosource (https://www.meteosource.com) free plan(gratis)

# Cara penggunaan
-Jalankan program python dengan terminal "python MainForecast.py"
-Masukkan nama kota sesuai nama resmi, contoh: 'Yogyakarta' bukan 'jogja'

# Contoh
-Input: "Yogyakarta"
-Output:"""-Gunakan kendaraan mobil jika memungkinkan, nyalakan lampu, dan pastikan wiper berfungsi baik
                  -Jika memakai motor, gunakan jas hujan yang tertutup rapat serta helm dengan visor bening
                  -Pakailah pakaian yang cepat kering atau anti air, hindari bahan tebal yang menyerap air
                  -Bawalah payung atau jas hujan cadangan, serta tas kedap air untuk melindungi barang elektronik
                  -Gunakan sepatu tertutup agar kaki tetap kering dan aman dari jalanan licin
                  -Siapkan powerbank dan plastik pelindung untuk HP atau dokumen penting"
                """
# Batasan:
-Hanya Kota yang ada di data Meteosource yang bisa diprakirakan
-Perekomendasian terbatas pada 4 cuaca yaitu Sunny/Terik,Cloudy/Berawan,Rain/Hujan, Thunderstorm/Badai
-Karna API menggunakan Free Plan, setiap hari dibatasi 400 request, 1 prakiraan memakan 1 request

# Algoritma
-Minta input nama kota resmi(Jakarta/Jakarta/dll), verifikasi agar benar
-Meminta data prakiraan cuaca di kota input dari API meteosource
-Mengambil data 3 jam kedepan dan menyimpulkan cuaca secara garis besar
-memberi output berupa rekomendasi persiapan
-menanyakan penggunaan ulang progam(Y/N)
# Spesifikasi
-Bahasa pyhton versi 3.8+
-library eksternal 'request'
-membutuhkan kunci API meteosource (free plan) yang disimpan di 'fAPI_KEY.py' dengan nama variabel 'vAPI_KEY'
-Sistem operasi windows/macOS versi 8.1+/10.9 Mavericks+
-Koneksi internet untuk API
# Error Handling
Input bukan string -> pesan plus ulangi program
Intenet putus -> memberi pesan, ulangi program
Kunci APi salah -> memberi pesan, hentikan program
Kouta API habis -> memberi pesan, hentikan program
Kota salah ejaan/gak ada di data API -> memberi pesan, ulangi program

# Pseudo-code:
IMPOR API_KEY,request,dll
FUNGSI MintaData(kota):
    buat URL API menggunakan kota dan API_KEY
    coba kirim request HTTP GET
        jika gagal koneksi -> tampilkan "Periksa internet" dan panggil main()
    jika status_code 200 -> kembalikan data JSON
    jika 403 -> tampilkan error API KEY, keluar
    jika 402/429 -> tampilkan kuota habis, keluar
    jika 400 -> tampilkan kota tidak valid, kembali ke main()

FUNGSI GarisBesarCuaca3jam(Data):
    ambil 3 data pertama dari 'hourly'
    jika ada 'thunderstorm' -> kembalikan BADAI
    jika ada 'rain' -> kembalikan HUJAN
    jika ada 'cloudy' atau 'overcast' -> kembalikan BERAWAN
    selain itu -> CERAH

FUNGSI MembuatRekomendasi(cuaca):
    jika BADAI -> tampilkan rekomendasi darurat
    jika HUJAN -> tampilkan rekomendasi hujan
    jika BERAWAN -> rekomendasi antisipasi
    jika CERAH -> rekomendasi cuaca panas

FUNGSI main():
    minta input kota dari user
    panggil MintaData dengan parameter kota
    panggil GarisBesarCuaca3jam dengan parameter data
    panggil MembuatRekomendasi dengan parameter Garisbesar cuaca
    tampilkan hasil
    tanya mau ulang atau keluar

END

# Set-Up program (1 kali)
-Install python versi 3.8+
-Install library request
-Di folder program, buat file 'fAPI_KEY.py' dengan isi variabel string 'vAPI_KEY' berisi kunci API Meteosource

# Versi & Pengembang
-WeatherPrep v1.0
-Pengembang:Rafael Bentara D. atau Username: RBD9083 at Github
-Lisensi:MIT License

