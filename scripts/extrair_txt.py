import ijson
import os
import glob

"""
Script para extrair mensagens de JSON exportado do Discord
e converter em arquivos TXT organizados por chunks
"""

# CONFIGURAÇÕES
INPUT_DIR = "../output"
OUTPUT_DIR = "../output/txt_partes"
CHUNK_SIZE = 10000  # número de mensagens por arquivo

def detectar_prefix(json_path):
    """Detecta automaticamente a estrutura do JSON"""
    with open(json_path, 'r', encoding='utf-8') as f:
        parser = ijson.parse(f)
        for prefix, event, value in parser:
            if event == 'start_array':
                return prefix + '.item' if prefix else 'item'
    return 'messages.item'

def extrair_mensagens(input_file):
    """Extrai mensagens do JSON e salva em arquivos TXT"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"📂 Arquivo de entrada: {input_file}")

    prefix = detectar_prefix(input_file)
    print(f"🔍 Estrutura detectada. Lendo mensagens em: {prefix}")

    msg_count = 0
    chunk_count = 1
    total_msgs = 0
    f_out = None

    with open(input_file, 'r', encoding='utf-8') as f_in:
        for item in ijson.items(f_in, prefix):
            total_msgs += 1
            if total_msgs % 500 == 0:
                print(f"📨 {total_msgs} mensagens processadas...")

            # Abrir novo arquivo por chunk
            if msg_count == 0:
                if f_out:
                    f_out.close()
                output_path = os.path.join(OUTPUT_DIR, f'conversas_parte_{chunk_count}.txt')
                f_out = open(output_path, 'w', encoding='utf-8')
                print(f"🪶 Criando {output_path}...")

            # Extrair dados
            author = item.get('author', {})
            author_name = author.get('nickname') or author.get('name', 'Desconhecido')
            author_id = author.get('id', 'Sem ID')
            timestamp = item.get('timestamp', 'Sem data')
            content = item.get('content', '').strip()

            # Escrever no TXT
            if content:
                f_out.write(f"[{timestamp}] {author_name} ({author_id}): {content}\n")

            # Atualizar contadores
            msg_count += 1
            if msg_count >= CHUNK_SIZE:
                msg_count = 0
                chunk_count += 1
                f_out.flush()

    if f_out:
        f_out.close()

    print(f"\n✅ Processamento concluído! Total de mensagens extraídas: {total_msgs}")
    print(f"📂 Arquivos salvos em: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    # Procura o primeiro arquivo JSON na pasta de output
    json_files = glob.glob(os.path.join(INPUT_DIR, "*.json"))

    if not json_files:
        print("❌ Nenhum arquivo JSON encontrado na pasta output/")
        print(f"   Procurado em: {os.path.abspath(INPUT_DIR)}")
        exit(1)

    input_file = json_files[0]
    extrair_mensagens(input_file)
