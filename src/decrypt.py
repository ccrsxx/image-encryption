import os
import base64

from parse import parse_argv


def decrypt_image(image_path: str) -> str:
    if not image_path.endswith(".base64"):
        print("Invalid file format. Please provide a .base64 file.")
        quit()

    os.makedirs("result", exist_ok=True)

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        encoded_bytes = base64.b64decode(image_bytes)

        original_filename = ".".join(os.path.basename(image_path).split(".")[:-1])

        decrypted_filename_path = os.path.join(
            "result", "decrypted-" + original_filename
        )

        with open(decrypted_filename_path, "wb") as new_image_file:
            new_image_file.write(encoded_bytes)

    return decrypted_filename_path


def main() -> None:
    image_path = parse_argv()

    decrypted_image_path = decrypt_image(image_path)

    print(f"Decrypted image: {decrypted_image_path}")


if __name__ == "__main__":
    main()
