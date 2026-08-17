# Treinamento de Visão Computacional com YOLO

Este repositório reúne os materiais do **Treinamento de Visão Computacional com YOLO**, incluindo os **slides das 10 aulas**, os **códigos práticos para execução local no VS Code** e os **notebooks executáveis no Google Colab**.

Os exemplos foram organizados para acompanhar diretamente os slides. Quando uma aula possui mais de uma prática, cada código fica separado em uma pasta identificada pelo **número e pelo título do slide correspondente**.

> **Observação:** os notebooks do Google Colab não estão armazenados neste repositório. Eles podem ser acessados diretamente pelos botões **Open in Colab** disponíveis neste README.

---

## Estrutura do repositório

```text
.
├── Slides/
│   ├── Aula_01.pdf
│   ├── Aula_02.pdf
│   ├── Aula_03.pdf
│   ├── Aula_04.pdf
│   ├── Aula_05.pdf
│   ├── Aula_06.pdf
│   ├── Aula_07.pdf
│   ├── Aula_08.pdf
│   ├── Aula_09.pdf
│   └── Aula_10.pdf
│
├── VSCode/
│   ├── Aula 01/
│   ├── Aula 02/
│   ├── Aula 04/
│   ├── Aula 06/
│   ├── Aula 07/
│   ├── Aula 08/
│   ├── Aula 09/
│   ├── Aula 10/
│   └── requirements.txt
│
└── README.md
```

As **Aulas 03 e 05** estão disponíveis normalmente na pasta `Slides/`, mas não possuem pastas em `VSCode/`, pois são aulas predominantemente conceituais e não possuem práticas executáveis separadas.

Quando uma aula possui várias práticas, a organização segue este padrão:

```text
VSCode/
└── Aula 02/
    ├── Slide 04 - Redimensionamento/
    │   └── slide_04_redimensionamento.py
    ├── Slide 06 - Conversão para tons de cinza/
    │   └── slide_06_tons_de_cinza.py
    ├── Slide 09 - Suavização e redução de ruído/
    │   └── slide_09_gaussian_blur.py
    └── ...
```

Nos arquivos Python, trechos adicionados apenas para facilitar a execução ou a visualização são identificados por comentários como:

```python
# APOIO PARA EXECUÇÃO — não faz parte do trecho original do slide
```

```python
# PLOT / VISUALIZAÇÃO — apoio didático
```

---

## Slides das aulas

Os slides completos das **10 aulas** ficam disponíveis na pasta `Slides/`. Eles podem ser abertos diretamente pelo GitHub ou baixados junto com o restante do repositório.

| Aula | Conteúdo | Slides |
|:---:|---|:---:|
| **Aula 01** | Introdução à Visão Computacional | [Ver slides](./Slides/Aula_01.pdf) |
| **Aula 02** | Processamento básico de imagens com OpenCV | [Ver slides](./Slides/Aula_02.pdf) |
| **Aula 03** | Do processamento clássico ao Aprendizado de Máquina | [Ver slides](./Slides/Aula_03.pdf) |
| **Aula 04** | Redes Neurais Convolucionais | [Ver slides](./Slides/Aula_04.pdf) |
| **Aula 05** | Detecção de Objetos | [Ver slides](./Slides/Aula_05.pdf) |
| **Aula 06** | Conhecendo YOLO | [Ver slides](./Slides/Aula_06.pdf) |
| **Aula 07** | Utilizando YOLO na prática | [Ver slides](./Slides/Aula_07.pdf) |
| **Aula 08** | Dataset próprio | [Ver slides](./Slides/Aula_08.pdf) |
| **Aula 09** | Treinando nosso próprio YOLO | [Ver slides](./Slides/Aula_09.pdf) |
| **Aula 10** | Do modelo ao sistema | [Ver slides](./Slides/Aula_10.pdf) |

---

## Notebooks no Google Colab

Os notebooks podem ser executados diretamente no navegador. Eles **não fazem parte da estrutura de pastas do repositório**; o acesso é feito pelos links abaixo.

| Aula | Conteúdo | Notebook |
|:---:|---|:---:|
| **Aula 01** | Introdução à Visão Computacional | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mVBE_j56IxhpDzfy34hfbr858gA_AnMQ?authuser=1) |
| **Aula 02** | Processamento básico de imagens com OpenCV | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lvAgi6HBgRvf6n23CuiTZAjqKPQIgK1o?authuser=1#scrollTo=uGZsf40fnqKR) |
| **Aula 04** | Redes Neurais Convolucionais | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11fuIlOyFWQZSkuSb1kCLUQwA3GXqNVvY?authuser=1) |
| **Aula 06** | Conhecendo YOLO | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yg9PmKh6-r8WfAniS9kEfxqmsnqRQnET?authuser=1) |
| **Aula 07** | Utilizando YOLO na prática | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13BFP47dyoNHsYH2lAHqVxXXU7qzCjbTv?authuser=1) |
| **Aula 08** | Dataset próprio | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wJqY5qI56vnhPeDXjzYWX-IL-raEzUQT?authuser=1) |
| **Aula 09** | Treinando nosso próprio YOLO | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1VF0DWZ2HTQIJwxQb1guIBx65Lpdk7sfT?authuser=1) |
| **Aula 10** | Do modelo ao sistema | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11yIRa-XkgK406Sxf8mtSIJIl_rpFq10N?authuser=1) |

> **Observação:** práticas que dependem de **vídeo, webcam ou tracking em tempo real** permanecem apenas na versão local para VS Code.

---

## Aulas com material prático

| Aula | Conteúdo |
|---|---|
| **Aula 01** | Introdução à Visão Computacional |
| **Aula 02** | Processamento básico de imagens com OpenCV |
| **Aula 04** | Redes Neurais Convolucionais |
| **Aula 06** | Conhecendo YOLO |
| **Aula 07** | Utilizando YOLO na prática |
| **Aula 08** | Dataset próprio |
| **Aula 09** | Treinando nosso próprio YOLO |
| **Aula 10** | Do modelo ao sistema |

---

## Preparando o ambiente local

### 1. Requisitos

Para executar os códigos localmente, recomenda-se ter instalado:

- **Python 3.x**;
- **Visual Studio Code**;
- extensão **Python** para o VS Code;
- `pip` disponível no ambiente Python.

---

### 2. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

Também é possível utilizar **Code > Download ZIP** na página do repositório.

---

### 3. Criar um ambiente virtual

O uso de um ambiente virtual é recomendado para manter as bibliotecas do treinamento separadas das demais instalações do sistema.

#### Windows — PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### Windows — Prompt de Comando

```cmd
py -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Depois de ativar o ambiente, atualize o `pip`:

```bash
python -m pip install --upgrade pip
```

---

## Bibliotecas necessárias

As dependências utilizadas nos códigos estão listadas em:

```text
VSCode/requirements.txt
```

Principais bibliotecas:

| Biblioteca | Utilização |
|---|---|
| `opencv-python` | leitura, manipulação e processamento de imagens e vídeos |
| `matplotlib` | visualização de imagens, comparações e gráficos |
| `torch` | operações com redes neurais utilizando PyTorch |
| `ultralytics` | inferência, treinamento, validação, tracking e exportação com YOLO |

### Instalação recomendada

A partir da raiz do repositório:

```bash
pip install -r VSCode/requirements.txt
```

Ou entre primeiro na pasta `VSCode`:

```bash
cd VSCode
pip install -r requirements.txt
```

### Instalação manual

```bash
pip install opencv-python matplotlib torch ultralytics
```

Para instalar ou atualizar apenas a Ultralytics:

```bash
pip install -U ultralytics
```

---

## Executando uma prática

Você pode abrir toda a pasta `VSCode` no Visual Studio Code ou executar diretamente pelo terminal.

Exemplo:

```bash
cd "VSCode/Aula 02/Slide 04 - Redimensionamento"
python slide_04_redimensionamento.py
```

Em Linux ou macOS, dependendo da configuração:

```bash
python3 slide_04_redimensionamento.py
```

---

## Arquivos utilizados nas práticas

Alguns códigos precisam de imagens, vídeos ou modelos auxiliares. Quando solicitado pelo script, coloque o arquivo na mesma pasta da prática correspondente.

| Arquivo | Uso |
|---|---|
| `imagem.jpg` | leitura, visualização e inferência com YOLO |
| `objetos.jpg` | processamento de imagens com OpenCV |
| `binaria.png` | morfologia, contornos e bounding boxes |
| `video.mp4` | práticas locais de inferência e tracking em vídeo |
| `data.yaml` | configuração do dataset |
| `best.pt` | checkpoint de um modelo treinado |
| `yolo26n.pt` | checkpoint pré-treinado utilizado nos exemplos |

Exemplo:

```text
VSCode/
└── Aula 02/
    └── Slide 04 - Redimensionamento/
        ├── objetos.jpg
        └── slide_04_redimensionamento.py
```

---

## Visualização dos resultados

As práticas utilizam **Matplotlib** sempre que uma saída visual ajuda a acompanhar o processamento.

Entre os exemplos estão:

- imagem original e imagem redimensionada;
- conversão para tons de cinza;
- suavização;
- limiarização;
- detecção de bordas;
- operações morfológicas;
- contornos e bounding boxes;
- imagens anotadas pelo YOLO;
- gráficos produzidos durante treinamento e validação.

---

## Observações sobre VS Code e Google Colab

A versão local em `VSCode/` é a versão mais completa das práticas.

O Google Colab é utilizado como alternativa para execução em navegador, especialmente quando não há necessidade de acessar dispositivos locais.

Por esse motivo, práticas envolvendo:

- webcam;
- vídeo local em tempo real;
- tracking contínuo;
- janelas gráficas do OpenCV;

são mantidas apenas na versão para **VS Code**.

---

## Organização didática

Os códigos foram mantidos próximos ao conteúdo apresentado nos slides. Sempre que foi necessário acrescentar algum trecho apenas para carregar arquivos, exibir resultados ou facilitar a execução, esse trecho foi identificado por comentários no próprio código.

O objetivo é permitir que cada prática seja executada isoladamente e relacionada de forma direta ao slide correspondente.
