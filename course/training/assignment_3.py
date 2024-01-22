# assignemnt_3.py

from tqdm import tqdm 
import torch
from transformers import AdamW

# ----Assuming the dataloader & model are already initialized--------

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)
model.train()


# initialize optimizer
optim = AdamW(model.parameters(), lr=5e-6)

epochs = 3

for epoch in range(epochs):

    loop = tqdm(loader, leave=True)
    for batch in loop:
        optim.zero_grad()

        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        token_type_ids = batch['token_type_ids'].to(device)
        labels = batch['labels'].to(device)
        
        outputs = model(
            input_ids, 
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            labels=labels
        )

        loss = outputs.loss
        loss.backward()
       
        optim.step()
        
        loop.set_description(f'Epoch {epoch}')
        loop.set_postfix(loss=loss.item())