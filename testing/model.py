import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = (
    "mps" if torch.backends.mps.is_available()
    else "cuda" if torch.cuda.is_available()
    else "cpu"
)

model_path = "../training/gpt2-networking"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

model.to(device)
model.eval()

prompt = "Host identity protocol is"

inputs = tokenizer(prompt, return_tensors="pt").to(device)

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.8,
        top_p=0.9
    )

print(tokenizer.decode(output[0], skip_special_tokens=True))

