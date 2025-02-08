#script to check if there is any existing keylogger

import psutil

def detect_keylogger(): #main fucntion

    suspicious_processes = ['pynput','hook','log','keylogger','logkeys','xinput'] #list of suspicious processes

    for proc in psutil.process_iter(['pid','name']):
        try:

            process_name = proc.info['name'].lower()
            if any(susp_name in process_name for susp_name in suspicious_processes):
                print(f"[!]Suspicious process detected:{process_name}(PID:{proc.info['pid']})") #if found keylogger
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess): #if not 
            pass

if __name__ == "__main__":
    print("[+] Running Keylogger detetcion...")
    detect_keylogger()
    print("[+] Scan Complete.")