#train.py
import torch
from opacus import PrivacyEngine
from torch import optim

def train_model_with_dp(model, train_loader):
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    privacy_engine = PrivacyEngine(model, batch_size=64, noise_multiplier=1.0, max_grad_norm=1.0)
    privacy_engine.attach(optimizer)

    for epoch in range(10):
        for batch in train_loader:
            optimizer.zero_grad()
            loss = model(batch['data']).loss
            loss.backward()
            optimizer.step()
