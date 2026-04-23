class MessMindNode:
    def __init__(self, node_id, neighbors, data_partition):
        self.id = node_id
        self.neighbors = neighbors
        self.model = SimpleCNN()
        self.data = data_partition
        self.round = 0

    def train_local(self, epochs=1):
        # стандартный PyTorch цикл обучения
        pass

    def send_weights(self, target_url):
        # POST /weights с сериализованными весами (numpy.tolist() или torch.save)
        pass

    def receive_weights(self):
        # Flask эндпоинт для приёма весов
        pass

    def aggregate_weights(self, received_weights_list):
        # усреднение: self.model.load_state_dict(среднее)
        pass

    def run_round(self):
        self.train_local()
        for neighbor in self.neighbors:
            self.send_weights(neighbor)
        # дождаться ответов от соседей (async или очередь)
        self.aggregate_weights(полученные_веса)
