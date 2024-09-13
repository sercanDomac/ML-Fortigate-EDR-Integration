# ml_model.py
import torch
import torch.nn as nn
import numpy as np

class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(6, 4),
            nn.ReLU(),
            nn.Linear(4, 2),
            nn.ReLU())
        
        self.decoder = nn.Sequential(
            nn.Linear(2, 4),
            nn.ReLU(),
            nn.Linear(4, 6),
            nn.Sigmoid())
    
    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

def train_autoencoder(train_data):
    model = Autoencoder()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    train_data = torch.tensor(train_data, dtype=torch.float32)
    epochs = 100
    for epoch in range(epochs):
        output = model(train_data)
        loss = criterion(output, train_data)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    print(f"Eğitim tamamlandı. Son kayıp: {loss.item()}")
    return model

def detect_anomalies_with_autoencoder(model, new_data):
    new_data = torch.tensor(new_data, dtype=torch.float32)
    output = model(new_data)
    loss = torch.mean((output - new_data) ** 2).item()
    print(f"Anomali skoru: {loss}")
    return loss
