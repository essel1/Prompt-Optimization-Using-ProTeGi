from transformers import AutoTokenizer, AutoModelForCausalLM

# Load Falcon 7B model and tokenizer
model_id = "tiiuae/falcon-7b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map = "auto",
    torch_dtype = "auto"
    )

prompt = "Heyyyyyy!'"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda") # Use GPU if available

outputs = model.generate(
    **inputs,
    do_sample = False,     # Enable Sampling to use 'temperature' or 'top_p'
    max_new_tokens = 100, # limit the output length
    pad_token_id=tokenizer.eos_token_id
)

output = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(output.json())