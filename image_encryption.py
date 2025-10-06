from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save("encrypted_image.png")
    print("✅ Image encrypted successfully!")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save("decrypted_image.png")
    print("✅ Image decrypted successfully!")

if __name__ == "__main__":
    path = input("Enter image path: ")
    key = int(input("Enter encryption key (number): "))
    choice = input("Encrypt or Decrypt (E/D): ").upper()

    if choice == "E":
        encrypt_image(path, key)
    else:
        decrypt_image(path, key)
