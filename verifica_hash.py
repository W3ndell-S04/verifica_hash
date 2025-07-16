import hashlib
import argparse
import os
import sys

def calcular_sha256(arquivo):
    """Calcula o hash SHA256 de um arquivo"""
    sha256 = hashlib.sha256()
    try:
        with open(arquivo, 'rb') as f:
            for bloco in iter(lambda: f.read(4096), b''):
                sha256.update(bloco)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{arquivo}' não encontrado.")
        sys.exit(1)

def verificar_integridade(arquivo, hash_original):
    """Verifica se o hash do arquivo corresponde ao fornecido"""
    hash_calculado = calcular_sha256(arquivo)
    print(f"Hash calculado:  {hash_calculado}")
    print(f"Hash fornecido:  {hash_original}")

    if hash_calculado.lower() == hash_original.lower():
        print("✅ Integridade verificada: os hashes coincidem!")
    else:
        print("❌ Integridade comprometida: os hashes são diferentes!")

def main():
    parser = argparse.ArgumentParser(description="Verificador de integridade SHA256")
    parser.add_argument("arquivo", help="Caminho para o arquivo a ser verificado")
    parser.add_argument("hash", help="Hash SHA256 original para comparação")

    args = parser.parse_args()
    verificar_integridade(args.arquivo, args.hash)

if __name__ == "__main__":
    main()
