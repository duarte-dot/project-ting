import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write("Formato inválido\n")
        return []

    try:
        with open(path_file, 'r') as file:
            lines = file.read().split('\n')
            return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return []


def process(path_file, instance):
    """Transforma o conteúdo do arquivo em um dicionário e adiciona na fila."""
    # Verifica se o arquivo já foi processado anteriormente
    for file in instance.queue:
        if file["nome_do_arquivo"] == path_file:
            sys.stdout.write(
                f"Arquivo {path_file} já processado. Ignorando.\n"
                )
            return

    # Importa as linhas do arquivo usando a função txt_importer
    lines = txt_importer(path_file)

    # Cria o dicionário com os dados processados do arquivo
    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    # Adiciona o dicionário na fila
    instance.enqueue(file_data)

    # Mostra os dados processados via stdout
    sys.stdout.write(f"{file_data}\n")


def remove(instance):
    """Remove o primeiro arquivo processado da fila."""
    try:
        # Remover o primeiro arquivo da fila
        removed_file = instance.dequeue()
        sys.stdout.write(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso\n"
            )
    except IndexError:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        # Buscar o arquivo na posição especificada
        file_data = instance.search(position)
        sys.stdout.write(f"{file_data}\n")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
