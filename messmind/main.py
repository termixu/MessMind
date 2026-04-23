import argparse
import yaml
from messmind.node import MessMindNode

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--node_id", type=int, required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--config", type=str, default="config/nodes.yaml")
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    node_cfg = config['nodes'][args.node_id]
    node = MessMindNode(
        node_id=args.node_id,
        neighbors=node_cfg['neighbors'],
        data_partition=None  # загрузите свою часть MNIST
    )
    node.run()  # бесконечный цикл раундов (например, 10 раундов)
