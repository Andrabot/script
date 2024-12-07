import os
import time
import random
import secrets
from colorama import Fore, init

# Inisialisasi Colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Menampilkan banner dengan efek arc Anonymous yang menarik."""
    arc_art = '''
 ____   _____   ______    _______  __   __   _____   _____
|    \\ |     | |      |  |       |  \\_/  | |     | |     |
|  _  ||  _  | |  ____|  |  ___  |   |   | |  _  | |  ___|
| | | ||  |  | | |__     | |__| |    |   | |  |  | | |__
| | | ||  |  | |  __|    |  ___  |   |   | |  |  | |  __|
| |_| ||  |  | | |___    | |   | |    |   | |  |  | | |___
|_____/|_____| |_____|   |_|   |_|    |___| |_____| |_____|
'''
    print(Fore.CYAN + "=" * 80)
    print(Fore.GREEN + arc_art)
    print(Fore.YELLOW + "=" * 80)
    print(Fore.MAGENTA + "        WELCOME TO FREE & PAID VPS  by Mozilla      ")
    print(Fore.CYAN + "=" * 80)

def loading_animation(message):
    """Animasi loading dengan efek titik yang lebih smooth dan interaktif."""
    loading_message = f"{message} "
    for i in range(10):
        print(f"\r{loading_message}{'.' * i}   ", end="", flush=True)
        time.sleep(0.5)
    print("\r" + " " * len(loading_message) + "   ", end="\r")  # Clear line

def main_menu():
    """Menampilkan menu utama dengan efek transisi lebih smooth."""
    clear_screen()
    print_banner()
    print(Fore.GREEN + "\nPilih jenis layanan VPS:")
    print(Fore.CYAN + "1. VPS Gratis (1 vCPU, 512 MB RAM, 10 GB SSD) - Gratis")
    print(Fore.BLUE + "2. VPS Berbayar (Spesifikasi Tinggi dan Premium)")
    print(Fore.MAGENTA + "3. Tentang Layanan")
    print(Fore.RED + "4. Keluar")
    print(Fore.CYAN + "=" * 80)

def choose_vps_specification():
    """Menampilkan pilihan spesifikasi VPS berbayar dengan efek visual menarik."""
    print(Fore.GREEN + "\nPilih spesifikasi VPS berbayar:")
    print(Fore.YELLOW + "1. VPS Standar (2 vCPU, 4 GB RAM, 40 GB SSD) - Rp 2.000/bulan")
    print(Fore.CYAN + "2. VPS Premium (4 vCPU, 8 GB RAM, 100 GB SSD) - Rp 10.000/bulan")
    print(Fore.RED + "3. VPS Super (8 vCPU, 16 GB RAM, 200 GB SSD) - Rp 15.000/bulan")
    print(Fore.MAGENTA + "4. Kembali ke menu utama")
    print(Fore.CYAN + "=" * 80)

def activate_vps(vps_type, paid=False):
    """Aktivasi VPS dengan QR code jika berbayar, dan spek VPS pilihan untuk berbayar."""
    clear_screen()
    loading_animation("Sedang memproses VPS Anda")

    if paid:
        choose_vps_specification()  # Memilih spesifikasi VPS berbayar

        choice = input(Fore.YELLOW + "Masukkan pilihan spesifikasi VPS [1-4]: ")

        if choice == "1":
            vps_spec = "VPS Standar (2 vCPU, 4 GB RAM, 40 GB SSD)"
            price = "Rp 10.000/bulan"
        elif choice == "2":
            vps_spec = "VPS Premium (4 vCPU, 8 GB RAM, 100 GB SSD)"
            price = "Rp 20.000/bulan"
        elif choice == "3":
            vps_spec = "VPS Super (8 vCPU, 16 GB RAM, 200 GB SSD)"
            price = "Rp 35.000/bulan"
        elif choice == "4":
            return  # Kembali ke menu utama
        else:
            print(Fore.RED + "Pilihan tidak valid. Kembali ke menu utama...")
            time.sleep(2)
            return

        print(Fore.GREEN + f"\nAnda memilih: {vps_spec}")
        print(Fore.YELLOW + f"Harga: {price}")
        print(Fore.RED + "\nUntuk VPS Berbayar, lakukan pembayaran terlebih dahulu.")
        print(Fore.YELLOW + "Pembayaran dapat dilakukan melalui halaman berikut:")

        # Halaman pembayaran Dana yang diberikan
        payment_url = "https://andrabot.github.io/qr/"
        
        # Perintah untuk membuka browser langsung di Android
        os.system(f"am start -a android.intent.action.VIEW -d {payment_url}")  # Membuka halaman pembayaran di browser Chrome

    else:
        print(Fore.GREEN + f"\nVPS {vps_type} berhasil diaktifkan!")
        print(Fore.CYAN + "===============================================")
        print(Fore.YELLOW + f"IP Address: 192.168.{random.randint(1, 254)}.{random.randint(1, 254)}")
        print(Fore.YELLOW + f"Username: user{random.randint(1000, 9999)}")
        print(Fore.YELLOW + f"Password: {secrets.token_urlsafe(10)}")
        print(Fore.CYAN + "===============================================")
        print(Fore.BLUE + "Silakan gunakan detail ini untuk mengakses VPS Anda.")

    print(Fore.CYAN + "=" * 80)
    input(Fore.CYAN + "\nTekan Enter untuk kembali ke menu utama...")

def about_service():
    """Menampilkan informasi tentang layanan VPS."""
    clear_screen()
    print_banner()
    print(Fore.YELLOW + "Tentang Layanan VPS:")
    print(Fore.GREEN + "- Layanan VPS Gratis cocok untuk kebutuhan ringan seperti testing atau belajar.")
    print(Fore.BLUE + "- Layanan VPS Berbayar menawarkan performa tinggi untuk kebutuhan profesional.")
    print(Fore.CYAN + "- Semua layanan VPS kami dilengkapi dengan dukungan teknis 24/7.")
    print(Fore.YELLOW + "Hubungi kami untuk informasi lebih lanjut: support@vpsprovider.com")
    print(Fore.MAGENTA + "=" * 80)
    input(Fore.CYAN + "\nTekan Enter untuk kembali ke menu utama...")

def contact_us():
    """Menampilkan halaman kontak."""
    clear_screen()
    print_banner()
    print(Fore.GREEN + "Hubungi Kami:")
    print(Fore.YELLOW + "- Email: support@vpsprovider.com")
    print(Fore.CYAN + "- Telepon: +6283139270060")
    print(Fore.MAGENTA + "- WhatsApp: wa.me/6283139270060")
    print(Fore.BLUE + "=" * 80)
    input(Fore.CYAN + "\nTekan Enter untuk kembali ke menu utama...")

def main():
    """Fungsi utama untuk menjalankan aplikasi."""
    while True:
        main_menu()
        choice = input(Fore.YELLOW + "Masukkan pilihan Anda [1-4]: ")

        if choice == "1":
            activate_vps("Gratis")
        elif choice == "2":
            activate_vps("Berbayar", paid=True)  # Menambahkan opsi untuk memilih spesifikasi VPS berbayar
        elif choice == "3":
            about_service()
        elif choice == "4":
            contact_us()  # Menambahkan halaman kontak
        elif choice == "5":
            print(Fore.CYAN + "\nTerima kasih telah menggunakan layanan kami!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
            time.sleep(2)

if __name__ == "__main__":
    main()
