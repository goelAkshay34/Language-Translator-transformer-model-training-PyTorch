from config import get_config
cfg = get_config()
cfg['batch_size'] = 4
cfg['preload'] = None
cfg['num_epochs'] = 30

from train import train_model

train_model(cfg)