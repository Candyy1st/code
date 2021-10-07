"""
Aplikasi deteksi Gempa
MOdularisasi dengan Function
"""


def ekstraksi_data():
    hasil = dict()
    hasil['tanggal'] = '10 Oktober 2021'
    hasil['waktu'] = '11:51:52 WIB'
    hasil['magnitudo'] = 4.3
    hasil['lokasi'] = {'ls': 1.48, 'bt': 123}
    hasil['pusat'] = 'Pusat gempa berada di darat 18km barat laut'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III'
    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)