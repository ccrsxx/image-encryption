import os
import base64


def encrypt_image(image_path: str) -> str:
    if not os.path.exists("result"):
        os.makedirs("result")

    encrypted_filename = os.path.basename(image_path + ".base64")
    encrypted_filename_path = os.path.join("result", encrypted_filename)

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        encoded_bytes = base64.b64encode(image_bytes)
        encoded_string = encoded_bytes.decode("utf-8")

        with open(encrypted_filename_path, "w") as encoded_file:
            encoded_file.write(encoded_string)

    return encrypted_filename_path


def decrypt_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        encoded_bytes = base64.b64decode(image_bytes)

        original_filename = ".".join(os.path.basename(image_path).split(".")[:-1])

        decrypted_filename_path = os.path.join("result", original_filename)

        with open(decrypted_filename_path, "wb") as new_image_file:
            new_image_file.write(encoded_bytes)

    return decrypted_filename_path


def main() -> None:
    image_path = "image/waifu.jpg"

    encrypted_image_path = encrypt_image(image_path)
    decrypted_image_path = decrypt_image(encrypted_image_path)

    print(f"Encrypted image: {encrypted_image_path}")
    print(f"Decrypted image: {decrypted_image_path}")


if __name__ == "__main__":
    main()
