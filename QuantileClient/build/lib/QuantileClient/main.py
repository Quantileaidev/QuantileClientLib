import os
from dotenv import load_dotenv
import requests
import json
class QuantileClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = self.load_api_key_from_env()

    def load_api_key_from_env(self):
        load_dotenv()
        return os.getenv("API_KEY")

    def save_api_key_to_env(self, api_key):
        with open(".env", "w") as f:
            f.write(f"API_KEY={api_key}")

    def generate_openai_response(self, model, messages, tools=None, tool_choice=None, max_tokens=None,
                                 temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None,parsed_output=False):
        messages_json = json.dumps(messages)
        url = f"{self.base_url}/generate_openai_response"
        headers = {
            "accept": "application/json",
            "quant-api-key": self.api_key
        }
        payload = {
            "model": model,
            "messages": messages_json,
            "tools": tools,
            "tool_choice": tool_choice,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
            "parese_output": parsed_output
        }
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

    def generate_anthropic_response(self, messages, model=None, max_tokens=None, temperature=None,parsed_output=False):
        url = f"{self.base_url}/generate_anthropic_response"
        messages_json = json.dumps(messages)

        headers = {
            "accept": "application/json",
            "quant-api-key": self.api_key
        }
        payload = {
            "messages": messages_json,
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "parese_output": parsed_output
        }
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

    def generate_deepinfra_response(self, messages, model=None, max_tokens=None, temperature=None,parsed_output=False):
        url = f"{self.base_url}/generate_deepinfra_response"
        messages_json = json.dumps(messages)

        headers = {
            "accept": "application/json",
            "quant-api-key": self.api_key
        }
        payload = {
            "messages":messages_json,
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "parese_output":parsed_output
        }
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

    def generate_perplexity_response(self, messages, model=None, max_tokens=None, temperature=None):
        url = f"{self.base_url}/generate_perplexity_response"
        messages_json = json.dumps(messages)

        headers = {
            "accept": "application/json",
            "quant-api-key": self.api_key
        }
        payload = {
            "messages": messages_json,
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        response = requests.get(url, headers=headers, params=payload)
        return response.json()

    def generate_cohere_response(self, message, chat_history, model=None, max_tokens=None, temperature=None,
                                 connectors=None):
        chat_history = json.dumps(chat_history)
        connectors = json.dumps(connectors)
        print(chat_history)

        url = f"{self.base_url}/generate_cohere_response"

        headers = {
            "accept": "application/json",
            "quant-api-key": self.api_key
        }
        payload = {
            "message": message,
            "chat_history": chat_history,
            "model": model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "connectors": connectors
        }
        response = requests.get(url, headers=headers, params=payload)
        return response.json()
    
    def call_cascading(self,prompt, max_tokens=None,temperature=None,parsed_output=False):
        
        url = f"{self.base_url}/call_cascading"
        headers = {
            "accept": "application/json",
            "quant-api-key": self.api_key
        }
        params = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature":temperature,
            "parese_output":parsed_output
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    
    def image_gen(self,prompt,model,width,height,num_images,quality):
        url = f"{self.base_url}/image_generation"
        headers = {
            "accept": "application/json",
            "quant-api-key": self.api_key
        }
        params = {
            "prompt": prompt,
            "model": model,
            "width": width,
            "height": height,
            "num_images": num_images,
            "quality": quality
        
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    def rag_data_upload(self, db_name, pdf_file, chunk_size=100, chunk_overlap=10, embedding_model="text-embedding-3-small"):
        url = f"{self.base_url}/rag_data_upload"
        
        headers = {
            "accept": "application/json",
            "quant-api-key": self.api_key
        }
        
        params = {
            "db_name": db_name,
            "pdf_file": pdf_file,
            "chunk_size": chunk_size,
            "chunk_overlap": chunk_overlap,
            "embedding_model": embedding_model
        }
        if not os.path.exists(pdf_file):
            return {"error": "File not found"}
        
        with open(pdf_file, 'rb') as file:
            files = {'pdf_file': (os.path.basename(pdf_file), file)}
            response = requests.post(url, headers=headers, params=params, files=files)
        
        return response.json()
    def rag_chat(self,db_name,description,question,embedding_model="text-embedding-3-small",inference_model="gpt-3.5-turbo-0125",temperature=0):
        url = f"{self.base_url}/rag_assistant"
        
        headers = {
            "accept": "application/json",
            "quant-api-key": self.api_key
        }
        params = {
            "db_name": db_name,
            "description": description,
            "question": question,
            "embedding_model": embedding_model,
            "inference_model": inference_model,
            "temperature": temperature
        }
        
        response = requests.get(url, headers=headers, params=params)
        return response.json()

        
 
        

        
    
