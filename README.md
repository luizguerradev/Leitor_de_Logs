# Leitor de Logs com Contexto

Este projeto é um **programa em Python** para analisar arquivos de log em uma pasta, destacando mensagens de **ERRO** e **Tracebacks**, junto com as últimas 10 linhas de contexto antes do erro. Ele também salva os resultados em um arquivo `.txt` para consulta posterior.

---

## 🔹 Funcionalidades

- Lê todos os arquivos de log dentro de uma pasta.
- Detecta:
  - Linhas com `ERROR`.
  - Blocos de `Traceback` completos (incluindo Exception final).
- Exibe **as 10 linhas anteriores** ao erro para fornecer contexto.
- Salva todos os erros detectados em um arquivo `.txt`.
- Mantém a janela aberta após execução para facilitar visualização.

---

## 🔹 Pré-requisitos

- Python 3.x instalado
  - Verifique no terminal:
    ```bash
    python --version
    ```
- Sistema operacional: Windows, Linux ou MacOS

---

## 🔹 Estrutura de pastas

```bash
LeitorLogs/
│
├── leitor_logs.py # Script principal
├── logs/ # Pasta contendo arquivos de log
└── README.md # Este arquivo
```

---

## 🔹 Como rodar o programa

### 1️⃣ Método padrão (pasta `logs` e saída padrão)
Abra o terminal na pasta do projeto e digite:
```bash
python leitor_logs.py
```
  - Os resultados serão mostrados no console.
  - Um arquivo erros_encontrados.txt será criado na mesma pasta.

### 2️⃣ Método avançado (especificando pasta e arquivo de saída)

```bash
python leitor_logs.py <caminho_da_pasta> <nome_arquivo_saida.txt>
```

Exemplo:

```bash
python leitor_logs.py logs resultado.txt
```
## 🔹 Como funciona

  - O script percorre todos os arquivos na pasta de logs.

  - Para cada arquivo:
    - Procura por ERROR e Traceback.
    - Captura as últimas 10 linhas antes do erro como contexto.
    - Imprime no console e escreve no arquivo de saída.

## 🔹 Exemplo de saída

📄 Lendo: app.log
```bash
🔴 ERROR encontrado:
   Contexto (últimas 10 linhas):
   INFO: Conectando ao banco
   DEBUG: Preparando consulta
   ...
   >> 2025-09-12 10:22:33 ERROR: Falha ao conectar ao banco

🔴 Traceback encontrado:
   Contexto (últimas 10 linhas):
   INFO: Iniciando função dividir
   ...
   --- Início Traceback ---
   Traceback (most recent call last):
   File "main.py", line 10, in <module>
       dividir()
   ZeroDivisionError: division by zero
   --- Fim Traceback ---
```

## 🔹 Observações

  - Arquivos muito grandes podem levar alguns segundos para processar.
  - A pasta de logs deve existir; caso contrário, o programa retorna erro.
  - Mantive um input() no final para que a janela não feche automaticamente no Windows.
