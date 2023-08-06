import re


def exists_word(word: str, instance):
    words_found = []
    word_lower = word.lower()

    for obj in instance.queue:
        nome_do_arquivo = obj['nome_do_arquivo']
        linhas_do_arquivo = obj['linhas_do_arquivo']
        ocorrencias = []

        for index, line in enumerate(linhas_do_arquivo):
            words = re.findall(word_lower, line, re.IGNORECASE)
            word_counter = len(words)
            if word_counter > 0:
                line_found = {"linha": index + 1}
                ocorrencias.append(line_found)

        if ocorrencias:
            result = {
                "palavra": word,
                "arquivo": nome_do_arquivo,
                "ocorrencias": ocorrencias,
            }
            words_found.append(result)

    return words_found


def search_by_word(word: str, instance):
    words_found = []
    word_lower = word.lower()

    for obj in instance.queue:
        nome_do_arquivo = obj['nome_do_arquivo']
        linhas_do_arquivo = obj['linhas_do_arquivo']
        ocorrencias = []

        for index, line in enumerate(linhas_do_arquivo):
            words = re.findall(word_lower, line, re.IGNORECASE)
            word_counter = len(words)
            if word_counter > 0:
                line_found = {
                    "linha": index + 1,
                    "conteudo": line,
                }
                ocorrencias.append(line_found)

        if ocorrencias:
            result = {
                "palavra": word,
                "arquivo": nome_do_arquivo,
                "ocorrencias": ocorrencias,
            }
            words_found.append(result)

    return words_found
