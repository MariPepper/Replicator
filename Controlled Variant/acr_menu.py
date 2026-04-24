import os
import shutil
import random
from pathlib import Path
from datetime import datetime
from cryptography.fernet import Fernet

REPLICA_TAG = "__REPLICA__"

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

# ============================
#  PERCENTAGE SELECTION
# ============================

def choose_percentage():
    while True:
        try:
            pct = int(input("Enter replication percentage (1–100): "))
            if 1 <= pct <= 100:
                return pct
        except:
            pass
        print("Invalid value.")

# ============================
#  EXTENSION SELECTION
# ============================

def choose_extensions():
    print("\nSelect file extensions to replicate.")
    print("Example: pdf,epub,docx,png")
    raw = input("Extensions (comma-separated): ").strip()
    return [("." + ext.strip().lower()) for ext in raw.split(",") if ext.strip()]

# ============================
#  FILE LISTING
# ============================

def list_target_files(base_path, extensions):
    files = []
    for root, dirs, fs in os.walk(base_path):
        for f in fs:
            if any(f.lower().endswith(ext) for ext in extensions):
                files.append(Path(root) / f)
    return files

# ============================
#  REPLICATION
# ============================

def replicate_files(files, percentage):
    if not files:
        log("No eligible files found.")
        return []

    count = max(1, int(len(files) * (percentage / 100)))
    selected = random.sample(files, count)

    created = []
    for f in selected:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        new_name = f"{f.stem}{REPLICA_TAG}_{timestamp}{f.suffix}"
        dest = f.parent / new_name
        try:
            shutil.copy2(f, dest)
            created.append(dest)
        except Exception as e:
            log(f"Error replicating {f}: {e}")

    log(f"Created {len(created)} replicas.")
    return created

# ============================
#  CLEANUP
# ============================

def cleanup_replicas(base_path):
    removed = 0
    for root, dirs, fs in os.walk(base_path):
        for f in fs:
            if REPLICA_TAG in f:
                try:
                    os.remove(Path(root) / f)
                    removed += 1
                except:
                    pass
    log(f"Removed {removed} replicated files.")

# ============================
#  ENCRYPTION (SAFE)
# ============================

def encrypt_replicas(base_path):
    key = Fernet.generate_key()
    cipher = Fernet(key)

    encrypted = 0

    for root, dirs, fs in os.walk(base_path):
        for f in fs:
            if REPLICA_TAG in f:
                file_path = Path(root) / f
                enc_path = file_path.with_suffix(file_path.suffix + ".enc")

                try:
                    with open(file_path, "rb") as original:
                        data = original.read()

                    encrypted_data = cipher.encrypt(data)

                    with open(enc_path, "wb") as encrypted_file:
                        encrypted_file.write(encrypted_data)

                    encrypted += 1

                except Exception as e:
                    log(f"Error encrypting {file_path}: {e}")

    log(f"Encrypted {encrypted} replica files.")

    print("\n=== ENCRYPTION KEY (SAVE THIS) ===")
    print(key.decode())
    print("==================================\n")

# ============================
#  MENU
# ============================

def pause():
    input("\nPress ENTER to continue...")

def menu():
    base = Path.cwd()
    percentage = 100
    extensions = [".pdf", ".epub", ".docx"]

    while True:
        print("\n" + "="*50)
        print("=== Anti‑Censorship Replicator ===")
        print("="*50)
        print(f"Current percentage: {percentage}%")
        print(f"Extensions: {', '.join(extensions)}")
        print("-"*50)
        print("1) Change replication percentage")
        print("2) Change file extensions")
        print("3) Start replication cycle")
        print("4) Cleanup replicas")
        print("5) Encrypt replicas (generate password)")
        print("6) Exit")
        print("-"*50)

        choice = input("> ").strip()
        print("\n" + "-"*50)

        if choice == "1":
            percentage = choose_percentage()
            print(f"\n✔ Replication percentage updated to {percentage}%.")
            pause()

        elif choice == "2":
            extensions = choose_extensions()
            print(f"\n✔ Extensions updated to: {', '.join(extensions)}")
            pause()

        elif choice == "3":
            files = list_target_files(base, extensions)
            created = replicate_files(files, percentage)
            print(f"\n✔ Replication cycle complete. {len(created)} replicas created.")
            pause()

        elif choice == "4":
            cleanup_replicas(base)
            print("\n✔ Cleanup complete.")
            pause()

        elif choice == "5":
            encrypt_replicas(base)
            print("\n✔ Encryption complete.")
            pause()

        elif choice == "6":
            log("Exiting.")
            break

        else:
            print("Invalid option.")
            pause()

if __name__ == "__main__":
    menu()
