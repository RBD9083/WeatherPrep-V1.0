
import requests #Agar bisa terhubung ke API
vAPI_KEY="Place your Meteosource apin key here" #Mengambil kunci api
import sys #Untuk keluar jika eror 

def MintaData(kota):
    #membuat url berdasarkan input kota pengguna
    url = f'https://www.meteosource.com/api/v1/free/point?place_id={kota}&sections=hourly&language=en&units=metric&key={vAPI_KEY}'
    try:
        hasil = requests.get(url)
    except: #Berarti internet gak nyambung
        print("Periksa kondisi internet")
        main()
    if hasil.status_code == 200: #Kode 200 berarti sukses
        data=hasil.json() #memformat data
        return data
    elif hasil.status_code == 403: #API KEY invalid
        print("Pastikan sudah membuat folder dan variabel kunci API dan mengimportnya ke MainForecast.py")
        sys.exit(1)
    elif hasil.status_code == 402 or hasil.status_code == 429: #Jatah sudah habis
        print('Jatah penggunaan cuaca hari/menit ini sudah habis, mohon maaf. Tunggu sebentar/esok hari untuk menggunakannya kembali')
        sys.exit(1)
    elif hasil.status_code == 400: #Nama kota salah/tidak support
        print("Nama kota tidak resmi atau Kota tidak ada datanya di API")
        main()
    
    
def GarisBesarCuaca3jam(Data): #Memproses data dan mengembalikan antara "Badai""Terik","Berawan","Hujan" dari data 3 jam pertama
    
    Prakiraan3Jam = [jam['weather'] for jam in Data['hourly']['data'][:3]] #Hanya mengambil data 'cuaca' di 3 jam pertama
    if any('thunderstorm' == cuaca for cuaca in Prakiraan3Jam): #badai
        return 'BADAI'
    elif any('rain' == cuaca for cuaca in Prakiraan3Jam): #hujan
        return 'HUJAN'
    elif any(cuaca in ['cloudy', 'overcast'] for cuaca in Prakiraan3Jam): #berawan
        return 'BERAWAN'
    else:
        return "CERAH" #selain itu berarti cerah
    
def MembuatRekomendasi(cuaca):
    if cuaca == 'BADAI':
        return """PERINGATAN: Batalkan rencana jika tidak terlalu penting/mendesak. Jika kebutuhan memang mendesak, maka:
                  -SANGAT DIREKOMENDASIKAN menggunakan kendaraan mobil agar terlindung dari angin dan hujan deras badai
                  -Cek kondisi mobil seperti tekanan ban, aki, bahan bakar penuh
                  -Pakailah pakaian yang hangat mengantisipasi suhu dingin (Jika terpaksa memakai motor, pakailah jaket anti air)
                  -Bawa selimut dan senter darurat, P3K sederhana, power bank + charger dalam tas kedap air
                  -Gunakanlah sepatu anti-licin
                  -Ingatlah untuk memprioritaskanlah keselamatan
                """
    elif cuaca == 'HUJAN':
        return """-Gunakan kendaraan mobil jika memungkinkan, nyalakan lampu, dan pastikan wiper berfungsi baik
                  -Jika memakai motor, gunakan jas hujan yang tertutup rapat serta helm dengan visor bening
                  -Pakailah pakaian yang cepat kering atau anti air, hindari bahan tebal yang menyerap air
                  -Bawalah payung atau jas hujan cadangan, serta tas kedap air untuk melindungi barang elektronik
                  -Gunakan sepatu tertutup agar kaki tetap kering dan aman dari jalanan licin
                  -Siapkan powerbank dan plastik pelindung untuk HP atau dokumen penting"
                """
    elif cuaca == 'BERAWAN':
        return """
                -Gunakan kendaraan seperti biasa namun tetap waspada jika terlihat tanda-tanda hujan
                -Pakailah pakaian yang nyaman dengan lapisan tipis seperti jaket ringan atau sweater
                -Bawalah payung lipat atau jas hujan ringan sebagai antisipasi perubahan cuaca mendadak
                -Siapkan botol minum secukupnya agar tubuh tetap terhidrasi
                -Gunakan sepatu yang nyaman untuk berjalan dan tidak licin jika jalan mulai basah"
                """
    elif cuaca == 'CERAH':
        return """-Gunakan kendaraan yang memiliki ventilasi atau AC yang baik
                  -Pakailah pakaian berbahan ringan dan menyerap keringat, hindari pakaian gelap yang menyerap panas
                  -Gunakan tabir surya (sunscreen) dan kacamata hitam untuk melindungi kulit serta mata
                  -Bawalah topi atau payung untuk perlindungan dari sinar matahari langsung
                  -Siapkan botol air minum untuk mencegah dehidrasi, bisa ditambah elektrolit jika perjalanan panjang
                  -Gunakan alas kaki yang nyaman agar tidak mudah berkeringat dan tetap aman saat bepergian"
                """
    else:
        print("WEATHER nilainya tidak masuk perkiraan")
        sys.exit(1)


def main():
    print('Selamat datang di program rekomendasi persiapan berbasis prakiraan cuaca')
    print('\n')
    try: #meminta input kota dengan error handling
        Kota = str(input('Masukkan nama kota dengan nama resminya (masukkan Yogyakarta, bukan jogja): ')).lower()
    except:
        print("Masukkan nama kota dengan benar")
        main()
    DataMentah = MintaData(Kota) #meminta prakiraan cuaca dengan API Meteosource
    print("Meminta prakiraan cuaca ke API....")
    Cuaca = GarisBesarCuaca3jam(DataMentah) #Meyimpulkan cuaca jam kedepan
    Rekomendasi = MembuatRekomendasi(Cuaca) #Membuat rekomendasi persiapan
    Hasil= f'Berdasarkan data, Cuaca {Kota} dalam 3 jam diprakirakan {Cuaca}, Kita merekomendasikan user:\n{Rekomendasi}' #Menambah pembukaan default
    print(Hasil, '\n\n') #Memberikan hasil
    Lagi = input("Mau menggunakan program lagi? (Y/N): ")
    if Lagi == 'Y':
        main()
    elif Lagi == 'N':
        print('Terimakasih telah menggunakan program')
        sys.exit(1)
    else:
        sys.exit(1)
if __name__ == "__main__":

    main()
