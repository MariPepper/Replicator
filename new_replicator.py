import os
import shutil
from pathlib import Path
from datetime import datetime

# ============== CONFIGURATION ==============
# ===========================================

def log(message):
    """Log messages to console"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    print(log_message)

def daemon_replication():
    current_folder = Path.cwd()
    cycle = 0
    total_files_replicated = 0
    
    log("=" * 50)
    log("INFINITE REPLICATION DAEMON STARTED")
    log(f"Target folder: {current_folder}")
    log(f"Check interval: {CHECK_INTERVAL} seconds")
    log("=" * 50)
    
    try:
        while True:
            cycle += 1
            
            log(f"\n--- Cycle {cycle} ---")
            cycle_replicated = 0
            
            try:
                for root, dirs, files in os.walk(current_folder):
                    root_path = Path(root)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
                    
                    for file in files:
                        # Skip scripts and log files
                        if file.endswith((".py", ".txt")):
                            continue
                        
                        file_path = root_path / file
                        
                        try:
                            ext = file_path.suffix
                            base_name = file_path.stem
                            
                            # Create one copy per cycle
                            new_name = f"{base_name}_{timestamp}_{cycle}{ext}"
                            dest = root_path / new_name
                            
                            shutil.copy2(file_path, dest)
                            cycle_replicated += 1
                            total_files_replicated += 1
                            
                        except Exception as e:
                            log(f"Error copying {file}: {e}")
                            continue
                
                log(f"Replicated {cycle_replicated} files | Total: {total_files_replicated}")
                
            except Exception as e:
                log(f"Error in cycle {cycle}: {e}")
    
    except KeyboardInterrupt:
        log("\nSTOPPING: Keyboard interrupt (Ctrl+C)")
    
    except Exception as e:
        log(f"FATAL ERROR: {e}")
    
    finally:
        log("=" * 50)
        log(f"DAEMON STOPPED - Total replicated: {total_files_replicated}")
        log("=" * 50)

if __name__ == "__main__":
    daemon_replication()