import os
import time

def type_line(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Simulated hacking intro
type_line("Initializing encrypted connection...")
time.sleep(0.5)
type_line("Accessing high-security data vaults...")
time.sleep(0.5)
type_line("Verifying biometric credentials...")
time.sleep(0.5)
type_line("Override protocols accepted.")
time.sleep(0.5)
type_line("Injecting system command hooks...")
time.sleep(0.5)
type_line("Trace blockers engaged...")
time.sleep(0.5)
type_line("Secure channel established.")
time.sleep(1)

# Dramatic pause
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

# BIG welcome banner
print("\n" * 5)
print("=" * 90)
print(" " * 20 + "███ WELCOME MR. SYED SALMAN ALI ███")
print("=" * 90)
print("\n" * 2)
time.sleep(5)
