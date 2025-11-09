import os, keyboard, pygame

pygame.mixer.init()

SOUNDS_DIR = "sounds"
files = [f for f in os.listdir(SOUNDS_DIR) if f.lower().endswith((".wav", ".mp3", ".ogg"))]
files.sort()

# Use F1–F12
key_map = ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12"]
sounds = {}

for k, fname in zip(key_map, files):
    sounds[k] = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, fname))
    print(f"{k.upper()} -> {fname}")

print("Press ESC to quit.")

def make_player(k):
    def _play(event):
        sounds[k].play()
    return _play

for k in sounds:
    keyboard.on_press_key(k, make_player(k), suppress=True)

keyboard.wait("esc")
