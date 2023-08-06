from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()

    queue.enqueue({"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 5})
    assert len(queue) == 1
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 5}
    assert len(queue) == 0

    queue.enqueue({"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 2})
    queue.enqueue({"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 1})
    queue.enqueue({"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 10})
    queue.enqueue({"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 4})

    assert queue.search(2) == {
        "nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 4}

    with pytest.raises(IndexError):
        queue.search(4)
