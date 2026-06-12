# Twitch Resize Tool

Twitch Resize Tool é uma ferramenta simples em Python para gerar automaticamente os tamanhos exigidos pela Twitch para badges e emotes a partir de uma única imagem quadrada.

O usuário fornece uma imagem de entrada e escolhe o tipo de saída desejado (`badge` ou `emote`). O programa gera automaticamente todas as versões necessárias.

## Funcionalidades

* Geração automática de badges da Twitch.
* Geração automática de emotes da Twitch.
* Mantém transparência em imagens PNG.
* Interface simples via linha de comando.
* Saída organizada em pasta dedicada.
* Compatível com Windows, Linux e macOS.

## Requisitos

* Python 3.10+
* Pillow

## Instalação

### Clonar o repositório

```bash
git clone git@github.com:SEU-USUARIO/twitch-resize-tool.git
cd twitch-resize-tool
```

### Criar ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

```text
twitch-resize-tool/
│
├── input/
├── output/
│
├── main.py
├── requirements.txt
└── README.md
```

## Dependências

**requirements.txt**

```txt
Pillow
```

## Formatos Suportados

Entrada:

```text
PNG
JPG
JPEG
WEBP
```

Recomendado:

```text
PNG com fundo transparente
```

## Uso

### Gerar Badges

Comando:

```bash
python main.py input/imagem.png badge
```

Arquivos gerados:

```text
output/
├── badge_72x72.png
├── badge_36x36.png
└── badge_18x18.png
```

Tamanhos:

| Arquivo         | Dimensão |
| --------------- | -------- |
| badge_72x72.png | 72×72    |
| badge_36x36.png | 36×36    |
| badge_18x18.png | 18×18    |

---

### Gerar Emotes

Comando:

```bash
python main.py input/imagem.png emote
```

Arquivos gerados:

```text
output/
├── emote_112x112.png
├── emote_56x56.png
└── emote_28x28.png
```

Tamanhos:

| Arquivo           | Dimensão |
| ----------------- | -------- |
| emote_112x112.png | 112×112  |
| emote_56x56.png   | 56×56    |
| emote_28x28.png   | 28×28    |

## Exemplos

### Badge

Entrada:

```bash
python main.py input/logo.png badge
```

Saída:

```text
output/
├── badge_72x72.png
├── badge_36x36.png
└── badge_18x18.png
```

### Emote

Entrada:

```bash
python main.py input/smile.png emote
```

Saída:

```text
output/
├── emote_112x112.png
├── emote_56x56.png
└── emote_28x28.png
```

## Regras de Entrada

A imagem deve ser:

* Quadrada (largura igual à altura).
* Preferencialmente PNG.
* Preferencialmente com fundo transparente.
* Preferencialmente em alta resolução para melhor qualidade após o redimensionamento.

Exemplo recomendado:

```text
1024x1024 PNG transparente
```

## Estrutura de Saída

```text
output/
├── badge_72x72.png
├── badge_36x36.png
├── badge_18x18.png
│
├── emote_112x112.png
├── emote_56x56.png
└── emote_28x28.png
```

## Tratamento de Erros

O programa valida:

* Existência do arquivo informado.
* Tipo de saída (`badge` ou `emote`).
* Formato da imagem.
* Dimensões da imagem.

Exemplos:

```bash
python main.py imagem.png
```

Retorno:

```text
Uso:
python main.py <imagem> <badge|emote>
```

```bash
python main.py imagem.png teste
```

Retorno:

```text
Tipo inválido.
Use: badge ou emote
```
