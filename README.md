# verifica_hash
# 🔐 Verificador de Hash SHA256

Ferramenta simples em Python para calcular o hash SHA256 de arquivos e verificar sua integridade, comparando com um hash original.

## ✅ Funcionalidades

- Calcula o hash SHA256 de qualquer arquivo.
- Compara o hash calculado com um hash original informado.
- Interface de linha de comando (CLI) com `argparse`.

---

## 🧠 Como funciona

O script lê o arquivo em blocos, calcula o hash SHA256 e compara com o hash original fornecido pelo usuário. Se os hashes coincidirem, a integridade está garantida.

---

## 💻 Como usar

### 1. Execute no terminal:

```bash
python verifica_hash.py caminho/do/arquivo.ext HASH_ORIGINAL
2. Exemplo:
bash
Copiar
Editar
python verifica_hash.py exemplo.txt 3a7bd3e2360a3d29eea436fcfb9aa6e6d3f3d0dd7b4e3f2dba7797f75f2e3c09
📦 Requisitos
Python 3.6 ou superior

Biblioteca hashlib (já incluída no Python)

📁 Estrutura do projeto
python
Copiar
Editar
verifica-hash/
├── verifica_hash.py
└── README.md
🚀 Objetivo do Projeto
Criar uma ferramenta simples e eficiente para:

Garantir a integridade de arquivos transmitidos ou baixados.

Aprender e aplicar conceitos de segurança e hashing.

Praticar o uso de Python em CLIs.

🧩 Licença
Este projeto está licenciado sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.

✍️ Autor
Desenvolvido por Wendell Lago Soares
