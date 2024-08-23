from huggingface_hub import HfFolder
import requests
import spacy

# Load the spaCy model for sentence segmentation
nlp = spacy.load("en_core_web_sm")

# Function to query the LLM and process the response
def generate_response(text):
    model_id = "tiiuae/falcon-7b-instruct"
    api_url = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {"Authorization": f"Bearer {HfFolder().get_token()}"}
    payload = {"inputs": text, "parameters": {"max_new_tokens": 50}}  # Restrict to 50 tokens

    print(f"Querying...: {text}")
    response = requests.post(api_url, headers=headers, json=payload)
    generated_text = response.json()[0]["generated_text"]

    # Use spaCy to split sentences
    doc = nlp(generated_text.replace(text,""))
    sentences = [sent.text for sent in doc.sents]
    
    # Join the first 2 sentences
    return ' '.join(sentences[:2])

if __name__ == "__main__":
    model_response = generate_response("Tell me about Robert Downey Jr.")
    print(model_response)
