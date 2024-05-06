from parse import parse_argv

from encrypt import encrypt_image
from decrypt import decrypt_image


def main() -> None:
    image_path = parse_argv()

    encrypted_image_path = encrypt_image(image_path)
    decrypt_image_path = decrypt_image(encrypted_image_path)

    print(f"Encrypted image: {encrypted_image_path}")
    print(f"Decrypted image: {decrypt_image_path}")


if __name__ == "__main__":
    main()
