import random
import datetime
import os
import sys

def get_commit_count_today(file_path):
    """Menghitung berapa kali aktivitas dicatat untuk hari ini."""
    if not os.path.exists(file_path):
        return 0
    
    today_str = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "r") as f:
        content = f.readlines()
        # Menghitung baris yang mengandung tanggal hari ini
        return sum(1 for line in content if today_str in line)

def main():
    file_log = "activity_log.md"
    
    # 1. Tentukan target harian secara acak (misal: antara 2 sampai 12 commit)
    # Kita gunakan seed berdasarkan tanggal agar target tetap konsisten sepanjang hari tersebut
    today_seed = datetime.datetime.now().strftime("%Y%m%d")
    random.seed(today_seed)
    daily_target = random.randint(2, 12) 
    
    # 2. Cek berapa banyak commit yang sudah dilakukan hari ini
    current_count = get_commit_count_today(file_log)
    
    # 3. Logika pengambilan keputusan
    # Jika sudah mencapai target, atau berdasarkan probabilitas (agar tidak berurutan terus)
    random.seed() # Reset seed agar benar-benar acak untuk probabilitas per jam
    chance_to_skip = random.random() < 0.3 # 30% peluang skip meski belum target (biar lebih natural)

    if current_count >= daily_target:
        print(f"Target hari ini ({daily_target}) sudah tercapai. Melewatkan.")
        sys.exit(1) # Keluar dengan error agar action berhenti
    
    if chance_to_skip:
        print("Keputusan acak: Melewatkan jadwal ini agar jeda waktu terlihat natural.")
        sys.exit(1)

    # 4. Eksekusi penulisan log jika lolos filter
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_log, "a") as f:
        f.write(f"- **{timestamp}**: Automated Sync ({current_count + 1}/{daily_target})\n")
    
    print(f"Berhasil mencatat aktivitas ke-{current_count + 1} dari target {daily_target} hari ini.")

if __name__ == "__main__":
    main()
