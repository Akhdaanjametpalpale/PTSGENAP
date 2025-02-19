import random

def sapa_acak():
    sapaan = ["Assalamualaikum", "Halo", "Selamat pagi"]
    nama = ["teman-teman", "kawan", "rekan-rekan", "sobat"]

    pilihan_sapaan = random.choice(sapaan)
    pilihan_nama = random.choice(nama)

    pesan = f"{pilihan_sapaan}, {pilihan_nama}! Semangat belajar Python!"
    return pesan

print(sapa_acak())

#Baris 1 mengimpor modul random
#baris 3 mend-define atau mendefinisikan sapa-acak
#baris 4 menyebutkan kalimat list yang sudah di beri tanda petik ke dalam terminal ketika di run
# baris 5 menyebutkan kalimat list yang sudah diberikan tanda petik juga ke dalam terminal
# Baris 7 Memilih satu sapaan secara acak
# Baris 8 memilih secara acak salah satu elemen atau kata dari list sapaan dan menyimpan di dalam variabel pilihan_nama (bedanaya hanya dari nama dan sapaan saja)
# baris 10 memberikan dua string yaitu pilihan_sapaan dan pilihan_nama dengan huruf f sebelum string dimasukkan untuk memanggil string
# baris 11 pada barisan yang ini adalah untuk mengembalikan nilai dari fungsi sapa_acak
# baris 13 Memanggil fungsi dan mencetak hasilnya