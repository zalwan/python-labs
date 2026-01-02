import pandas as pd
from tabulate import tabulate

# Dataset awal
data = {
    "nama": ["Andi", "Budi", "Citra", "Dedi", "Eka"],
    "umur": [25, 30, 22, 28, 35],
    "gaji": [50000, 45000, 60000, 55000, 40000],
    "departemen": ["IT", "HR", "IT", "Finance", "HR"]
}

# Save buat reset dataset
dataset_asli = pd.DataFrame(data)
df = dataset_asli.copy()


def tampilkan_dataset():
    print("\nCurrent Dataset:")
    print(tabulate(df, headers="keys", tablefmt="grid", showindex=True))
    print(f"Shape: {df.shape}")


while True:
    print("\n" + "=" * 55)
    print("DATASET SORTING PROGRAM")
    print("=" * 55)
    print("1. Tampilkan dataset")
    print("2. Sort by single column")
    print("3. Sort by multiple columns")
    print("4. Reset dataset")
    print("5. Keluar")

    pilihan = input("\nPilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_dataset()

    elif pilihan == "2":
        kolom = input("Masukkan nama kolom: ")
        if kolom in df.columns:
            ascending = input("Ascending? (y/n): ").lower() == "y"
            df = df.sort_values(by=kolom, ascending=ascending)
            print("\nDataset berhasil di-sort!")
            tampilkan_dataset()
        else:
            print("Kolom tidak ditemukan!")

    elif pilihan == "3":
        kolom = input("Masukkan kolom (pisahkan dengan koma): ").split(",")
        kolom = [k.strip() for k in kolom]

        if all(k in df.columns for k in kolom):
            df = df.sort_values(by=kolom)
            print("\nDataset berhasil di-sort (multiple columns)!")
            tampilkan_dataset()
        else:
            print("Salah satu kolom tidak ditemukan!")

    elif pilihan == "4":
        df = dataset_asli.copy()
        print("\nDataset berhasil di-reset ke kondisi awal.")
        tampilkan_dataset()

    elif pilihan == "5":
        print("Program selesai. Terima kasih 👋")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih 1-5.")
