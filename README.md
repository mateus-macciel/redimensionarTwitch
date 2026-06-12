# Twitch Resizer 🎮

Ferramenta simples em Python para gerar automaticamente os tamanhos exigidos pela Twitch para **Badges** e **Emotes**.

A partir de uma única imagem quadrada, o programa cria todas as versões necessárias prontas para upload.

---

## ✨ Funcionalidades

### Badges

Gera:

- 72x72
- 36x36
- 18x18

### Emotes

Gera:

- 112x112
- 56x56
- 28x28

---

## 📦 Requisitos

- Python 3.10+
- Pillow

Instalação:

```bash
pip install pillow
```

Ou:

```bash
pip install -r requirements.txt
```

---

# 🇧🇷 Português

## Uso

### Gerar Badges

```bash
python main.py imagem.png badge
```

Saída:

```text
output/
├── badge_72x72.png
├── badge_36x36.png
└── badge_18x18.png
```

### Gerar Emotes

```bash
python main.py imagem.png emote
```

Saída:

```text
output/
├── emote_112x112.png
├── emote_56x56.png
└── emote_28x28.png
```

### Utilizando o Executável

Após gerar o `.exe` com PyInstaller:

```bash
main.exe imagem.png badge
```

ou

```bash
main.exe imagem.png emote
```

---

## Estrutura do Projeto

```text
twitch-resizer/
│
├── main.py
├── requirements.txt
├── README.md
├── imagem.png
│
└── output/
```

---

## Observações

- A imagem de entrada deve ser quadrada.
- Os arquivos são exportados em PNG.
- A pasta `output` é criada automaticamente.
- Arquivos existentes serão sobrescritos.

---

# 🇺🇸 English

## Usage

### Generate Badges

```bash
python main.py image.png badge
```

Output:

```text
output/
├── badge_72x72.png
├── badge_36x36.png
└── badge_18x18.png
```

### Generate Emotes

```bash
python main.py image.png emote
```

Output:

```text
output/
├── emote_112x112.png
├── emote_56x56.png
└── emote_28x28.png
```

### Using the Executable

After building the `.exe` with PyInstaller:

```bash
main.exe image.png badge
```

or

```bash
main.exe image.png emote
```

---

## Project Structure

```text
twitch-resizer/
│
├── main.py
├── requirements.txt
├── README.md
├── image.png
│
└── output/
```

---

## Notes

- The input image must be square.
- All generated files are exported as PNG.
- The `output` folder is created automatically.
- Existing files with the same name will be overwritten.

---

## 🔨 Building the Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build:

```bash
pyinstaller --onefile main.py
```

The executable will be generated inside:

```text
dist/
└── main.exe
```
