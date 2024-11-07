from abc import ABC, abstractmethod

# Interface untuk Transportasi
class Transportasi(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def drive(self):
        pass

# Kelas untuk AutoCarRPL, yang mengimplementasikan Transportasi
class AutoCarRPL(Transportasi):
    def __init__(self, bahan_bakar, kecepatan, roda2, setir, mesin2, fuel):
        self.bahan_bakar = bahan_bakar
        self.kecepatan = kecepatan
        self.roda2 = roda2  # Daftar objek Roda
        self.setir = setir  # Daftar objek Setir
        self.mesin2 = mesin2  # Objek Mesin
        self.fuel = fuel  # Objek Fuel

    def start(self):
        print(f"AutoCarRPL dimulai dengan bahan bakar {self.bahan_bakar}")

    def drive(self):
        print(f"AutoCarRPL sedang melaju dengan kecepatan: {self.kecepatan} km/jam")
        self.fuel.konsumsi_bahan_bakar()

# Kelas untuk Roda
class Roda:
    def __init__(self, ukuran, bahan):
        self.ukuran = ukuran  # Ukuran roda
        self.bahan = bahan  # Bahan roda (contoh: karet)

    def berputar(self):
        print(f"Roda dengan ukuran {self.ukuran} sedang berputar.")

# Kelas untuk Setir
class Setir:
    def __init__(self, jenis, bahan):
        self.jenis = jenis  # Jenis setir (contoh: manual, power)
        self.bahan = bahan  # Bahan setir (contoh: kulit)

    def mengemudi(self):
        print(f"Mengemudi dengan kontrol {self.jenis} sedang berbelok.")

# Kelas untuk Mesin
class Mesin:
    def __init__(self, daya, tipe):
        self.daya = daya  # Daya mesin (dalam HP)
        self.tipe = tipe  # Jenis mesin (contoh: bensin, listrik)

    def hidupkan_mesin(self):
        print(f"Mesin tipe {self.tipe} dengan {self.daya} HP sedang hidup.")

# Kelas untuk Fuel (Bahan Bakar)
class Fuel:
    def __init__(self, jenis, kapasitas):
        self.jenis = jenis  # Jenis bahan bakar (contoh: Bensin, Solar)
        self.kapasitas = kapasitas  # Kapasitas dalam liter
        self.level = kapasitas  # Level bahan bakar saat ini

    def konsumsi_bahan_bakar(self):
        if self.level > 0:
            self.level -= 1  # Mengonsumsi 1 liter bahan bakar
            print(f"Mengonsumsi bahan bakar. Sisa bahan bakar: {self.level} liter.")
        else:
            print("Bahan bakar habis!")

# Kelas untuk Mio yang memperpanjang AutoCarRPL
class Mio(AutoCarRPL):
    def __init__(self, bahan_bakar, kecepatan, roda2, setir, mesin2, fuel):
        super().__init__(bahan_bakar, kecepatan, roda2, setir, mesin2, fuel)

    def drive(self):
        print("Mio siap untuk dikemudikan.")
        super().drive()

# Contoh penggunaan kelas-kelas
if __name__ == "__main__":
    # Membuat instance untuk komponen-komponen
    roda_list = [Roda(15, "Karet") for _ in range(4)]  # Membuat 4 objek Roda
    setir_list = [Setir("Power", "Kulit")]  # Membuat daftar dengan satu objek Setir
    mesin = Mesin(120, "Bensin")  # Membuat objek Mesin dengan daya 120 HP
    fuel = Fuel("Bensin", 50)  # Membuat objek Fuel dengan kapasitas 50 liter

    # Membuat instance AutoCarRPL
    mobil = AutoCarRPL("Bensin", 80, roda_list, setir_list, mesin, fuel)
    mobil.start()
    mobil.drive()

    # Membuat instance Mio
    mio = Mio("Bensin", 60, roda_list, setir_list, mesin, fuel)
    mio.start()
    mio.drive()
