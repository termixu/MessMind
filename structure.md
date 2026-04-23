MessMind/
├── README.md
├── docker-compose.yml
├── requirements.txt
├── config/
│   └── nodes.yaml              # Список IP соседей для каждого узла
├── messmind/
│   ├── __init__.py
│   ├── node.py                 # Главный класс узла
│   ├── model.py                # Архитектура нейросети
│   ├── trainer.py              # Локальное обучение
│   ├── communicator.py         # Отправка/получение весов
│   └── consensus.py            # Усреднение весов (FedAvg)
├── scripts/
│   ├── start_node.sh
│   └── simulate_local.py       # Запуск 3 узлов на одном ПК (разные порты)
└── tests/
    └── test_comm.py
