import torch
from TTS.api import TTS


models = TTS().list_models()
print(models.list_models())
