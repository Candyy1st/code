"""
Aplikasi deteksi Gempa
MOdularisasi dengan Function
"""
from deteksi_gempa import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)