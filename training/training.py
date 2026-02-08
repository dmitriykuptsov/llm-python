from transformers import AutoTokenizer, AutoModelForCausalLM

import json
import torch
from torch.utils.data import Dataset

model_name = "gpt2-medium"

class GPT2Dataset(Dataset):
    def __init__(self, json_path, tokenizer, max_length=512):
        with open(json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        enc = self.tokenizer(
            self.data[idx]["text"],
            truncation=True,
            max_length=self.max_length,
            padding=False,
            return_tensors="pt"
        )

        input_ids = enc["input_ids"].squeeze(0)
        attention_mask = enc["attention_mask"].squeeze(0)

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask
        }

from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token


model = GPT2LMHeadModel.from_pretrained(model_name)
model.config.pad_token_id = tokenizer.eos_token_id
model.resize_token_embeddings(len(tokenizer))


dataset = GPT2Dataset("../dataset/gpt2_training_data.json", tokenizer)

from transformers import TrainingArguments
from transformers import Trainer, DataCollatorForLanguageModeling

training_args = TrainingArguments(
    output_dir="./gpt2-networking",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    learning_rate=2e-5,
    lr_scheduler_type = "cosine",
    #warmup_steps = 100,
    #logging_steps=100,
    optim = "adamw_torch",
    #save_steps=1000,
    #save_total_limit=2,
    max_steps=10000,
    fp16=False,              # set False if no GPU
    report_to="none"
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False   # GPT-2 is causal
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=data_collator
)

model.config.use_cache = False
model.gradient_checkpointing_enable()

trainer.train()

model.save_pretrained("./gpt2-networking")
tokenizer.save_pretrained("./gpt2-networking")
