import os
import base64

from parse import parse_argv


def encrypt_image(image_path: str) -> str:
    if image_path.endswith(".base64"):
        print("Invalid file format. Please provide a non .base64 file.")
        quit()

    os.makedirs("result", exist_ok=True)

    encrypted_filename = os.path.basename(image_path + ".base64")
    encrypted_filename_path = os.path.join("result", encrypted_filename)

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        encoded_bytes = base64.b64encode(image_bytes)
        encoded_string = encoded_bytes.decode("utf-8")

        with open(encrypted_filename_path, "w") as encoded_file:
            encoded_file.write(encoded_string)

    return encrypted_filename_path


def main() -> None:
    image_path = parse_argv()

    encrypted_image_path = encrypt_image(image_path)

    print(f"Encrypted image: {encrypted_image_path}")


if __name__ == "__main__":
    main()
