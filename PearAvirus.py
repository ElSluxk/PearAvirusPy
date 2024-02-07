import os
import hashlib
import shutil

# Lista de hashes de malware (MD5, SHA1 y SHA256)
MALWARE_HASHES = [
    "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",  # Ejemplo: Hash de un archivo malicioso
    "b6d767d2f8ed5d21a44b0e5886680cb9",  # Otro hash de malware
    "9e107d9d372bb6826bd81d3542a419d6",  # Y uno más
   "bbe8ccb5601525bd586d1f491299bc17145ee22e798af67e85c978e966a52d59",
   "2f1c897d81393d550fc1f2a10aaef1af4625740d4eef4ccb007e6226e13fd209",
   "3b1b39fe900810b510f065224cbce651d7a8c01bedbee298fa0f207fa8117cea83cbdf79d47d6d7b0923a1fb802a36ce",
   "707fa35bc4309ab6aefc9f63f55eb86e420fc684",
]

# Carpeta de cuarentena
QUARANTINE_FOLDER = "quarantine"

def scan_file(file_path):
    try:
        with open(file_path, "rb") as file:
            content = file.read()
            file_hash = hashlib.sha256(content).hexdigest()
            if file_hash in MALWARE_HASHES:
                print(f"Archivo sospechoso encontrado: {file_path}")
                move_to_quarantine(file_path)
                return True
            else:
                print(f"Archivo limpio: {file_path}")
                return False
    except Exception as e:
        print(f"Error al escanear {file_path}: {e}")
        return False

def move_to_quarantine(file_path):
    if not os.path.exists(QUARANTINE_FOLDER):
        os.mkdir(QUARANTINE_FOLDER)
    quarantine_path = os.path.join(QUARANTINE_FOLDER, os.path.basename(file_path))
    shutil.move(file_path, quarantine_path)
    print(f"Archivo movido a cuarentena: {quarantine_path}")

def main():
    target_directory = input("Ingresa la ruta del directorio a analizar: ")
    total_files = 0
    infected_files = 0

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_files += 1
            if scan_file(file_path):
                infected_files += 1

    print(f"Archivos revisados: {total_files}")
    print(f"Archivos infectados: {infected_files}")

if __name__ == "__main__":
    main()
