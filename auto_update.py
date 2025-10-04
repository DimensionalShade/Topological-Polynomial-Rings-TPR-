import time

def interpret(text, modulus):
    support = [i for i, c in enumerate(text) if ord(c) % modulus != 0]
    tags = {i: f"char:{text[i]}" for i in support}
    print(f"\nTPR AutoUpdate:")
    for i in support:
        print(f"  ▓ index {i} → {tags[i]}")
    print(f"Total support: {len(support)}")

def watch(path, modulus):
    last = ""
    while True:
        try:
            with open(path) as f:
                text = f.read()
            if text != last:
                interpret(text, modulus)
                last = text
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2)

if __name__ == "__main__":
    watch("input.txt", 17)
