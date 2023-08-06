class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if not self.queue:
            raise IndexError(
                "A fila está vazia, não é possível remover elementos."
                )
        return self.queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if not (0 <= index < len(self.queue)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
