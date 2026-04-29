import os
import glob

"""
Script para dividir arquivos TXT grandes em partes menores
para upload no NotebookLM (limite ~3MB por arquivo)
"""

# CONFIGURAÇÕES
INPUT_DIR = "../output/txt_partes"
OUTPUT_DIR = "../output/txt_partes_notebooklm"
MAX_SIZE_MB = 3

def dividir_arquivos():
    """Divide arquivos TXT em partes de até 3MB"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    txt_files = glob.glob(os.path.join(INPUT_DIR, "*.txt"))

    if not txt_files:
        print("❌ Nenhum arquivo TXT encontrado em txt_partes/")
        return

    print(f"📂 Encontrados {len(txt_files)} arquivos para processar")

    parte_global = 1

    for txt_file in txt_files:
        print(f"\n📄 Processando: {os.path.basename(txt_file)}")

        with open(txt_file, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        tamanho_atual = 0
        buffer = []

        for linha in linhas:
            tamanho_linha = len(linha.encode('utf-8'))

            # Se adicionar essa linha ultrapassar 3MB, salvar arquivo
            if tamanho_atual + tamanho_linha > MAX_SIZE_MB * 1024 * 1024:
                output_path = os.path.join(OUTPUT_DIR, f'lore_parte_{parte_global}.txt')
                with open(output_path, 'w', encoding='utf-8') as f_out:
                    f_out.writelines(buffer)

                print(f"✅ Criado: lore_parte_{parte_global}.txt ({tamanho_atual / (1024*1024):.2f} MB)")

                parte_global += 1
                buffer = []
                tamanho_atual = 0

            buffer.append(linha)
            tamanho_atual += tamanho_linha

        # Salvar o que sobrou
        if buffer:
            output_path = os.path.join(OUTPUT_DIR, f'lore_parte_{parte_global}.txt')
            with open(output_path, 'w', encoding='utf-8') as f_out:
                f_out.writelines(buffer)

            print(f"✅ Criado: lore_parte_{parte_global}.txt ({tamanho_atual / (1024*1024):.2f} MB)")
            parte_global += 1

    print(f"\n🎉 Processamento concluído! Total de arquivos criados: {parte_global - 1}")
    print(f"📂 Arquivos salvos em: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    dividir_arquivos()
