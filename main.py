import sys
from pathlib import Path
from PIL import Image


BADGE_SIZES = [72, 36, 18]
EMOTE_SIZES = [112, 56, 28]


def resize_image(image_path, mode):
    image = Image.open(image_path)

    width, height = image.size

    if width != height:
        raise ValueError("A imagem precisa ser quadrada.")

    if mode.lower() == "badge":
        sizes = BADGE_SIZES
    elif mode.lower() == "emote":
        sizes = EMOTE_SIZES
    else:
        raise ValueError("Modo inválido. Use 'badge' ou 'emote'.")

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    for size in sizes:
        resized = image.resize((size, size), Image.Resampling.LANCZOS)

        output_file = output_dir / f"{mode}_{size}x{size}.png"
        resized.save(output_file)

        print(f"Criado: {output_file}")


def main():
    if len(sys.argv) != 3:
        print("Uso:")
        print("python main.py <imagem> <badge|emote>")
        sys.exit(1)

    image_path = sys.argv[1]
    mode = sys.argv[2]

    try:
        resize_image(image_path, mode)
        print("Concluído.")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()