import os

from agents import SoftwareDevDataset
import litellm
from agents.optimization.trainer import Trainer, TrainerConfig

if os.environ.get("OPENAI_API_KEY") is None:
    os.environ["OPENAI_API_KEY"] = ""
if os.environ.get("OPENAI_BASE_URL") is None:
    os.environ["OPENAI_BASE_URL"] = ""

litellm.set_verbose = False

if __name__ == "__main__":
    # Prepare the data
    dataset = SoftwareDevDataset()

    # Trainer training
    trainer_config_path = "examples/software_dev/configs/trainer_config.json"
    trainer = Trainer(config=TrainerConfig(trainer_config_path), dataset=dataset)
    trainer.train()
