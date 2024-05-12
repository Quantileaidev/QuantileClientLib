# QuantileClientLib

QuantileClient is a Python client library designed to serve as a wrapper for the Quantile AI API. It simplifies the process of interacting with Quantile's AI supported platfroms LLMs, enabling developers to seamlessly integrate Quantile's capabilities into their Python applications.

[Offical Documentation](https://quantileai.in/documentation)

## All New Rag Chat
Introducing Rag Chat 1.0 – your go-to solution for seamless file uploads and effortless chatting! No more cumbersome links or complicated interfaces. It's as easy as upload, chat, and connect.

With Rag Chat 1.0, simplicity is key. Just upload your files with a click and dive straight into conversation. No more endless waiting for links to load or struggling with tangled chains of language its
*Simple*,
*effictive*,
*Easy to integrate*

```bash
pip install QuantileClient

```
**File upload**

```python

from QuantileClient import QuantileClient

base_url = "http://<api url>"  # Replace with quantileai api base URL
api_key = "<your-api-quant-api-key>"

client = QuantileClient(base_url, api_key)

rag_upload = client.rag_data_upload(
    db_name = "mytest",  #name the db here always remember this
    pdf_file ="test2.pdf", #path to pdf
    chunk_size=100, 
    chunk_overlap=10,
    embedding_model="text-embedding-3-small",
)
print(rag_upload)

```
**Rag Chat**

```python

from QuantileClient import QuantileClient

base_url = "http://<api url>"  # Replace with quantileai api base URL
api_key = "<your-api-quant-api-key>"

client = QuantileClient(base_url, api_key)

rag_assitant = client.rag_chat(
    db_name="mytest",
    description="talk in slang", #give deep desc for how it will act
    question = "My question is why quantILE Ai is soo cool",
    embedding_model="text-embedding-3-small",
    inference_model="gpt-3.5-turbo-0125",
    temperature=0,
    max_token = 1000,
    k=2  
)
print(rag_assitant)

```

## Chat with varoius model
Start conversing with different LLM models using just one Key. Say goodbye to the inconvenience of juggling multiple platforms or creating numerous accounts

```python


from QuantileClient import QuantileClient

base_url = "http://<api url>"  # Replace with quantileai api base URL
api_key = "<your-api-quant-api-key>"

client = QuantileClient(base_url, api_key)
prompt = "what is an api"

# use any platform and model just change the func
openai_response = client.generate_openai_response(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "system", "content": prompt},
                  ],
        max_tokens=100,
        parsed_output=True #to give just the output not whole response
    )

anthropic_response = client.generate_anthropic_response(
        model="claude-2.1",
        messages=[{"role": "system", "content": prompt},
                  ],
        max_tokens=100,
        parsed_output=True #to give just the output not whole response

    )

cohere_respose = client.generate_cohere_response(
        max_tokens=100,
        message = prompt , 
        chat_history=[
            {"role": "CHATBOT", "message": "you are an api expert"}
            ]
        connectors=[{"id": "web-search"}]
    )


print(f"My openai response is {openai_response}")
print(f"My cohere response is {cohere_response}")
print(f"My anthropic response is {anthropic_response}")


```
## Access call cascading api 

```python

from QuantileClient import QuantileClient

base_url = "http://<api url>"  # Adjust to quantile api base URL
api_key = "<your-api-quant-api-key>"

client = QuantileClient(base_url, api_key)
prompt = "what is an api"

# No neeed to specify model 

callcascade = client.call_cascading(
    prompt="tell me the word news and something abt apis",
    max_tokens=100,
    parsed_output=True #to give just the output not whole response
    
)
print(f"My callcascade response is {callcascade}")


```

## Generate AI Images 

```python

from QuantileClient import QuantileClient

base_url = "http://<api url>"  # Adjust to quantile api base URL
api_key = "<your-api-quant-api-key>"

client = QuantileClient(base_url, api_key)
prompt = "ai robots controlling the whole world"

image_gen_response = client.image_gen(
    prompt=prompt,
    model = "dall-e-2",
    width=1024,
    height=1024,
    num_images=1,
    quality="Standard"
    )
print(f"My image gen response is {image_gen_response}")

```

| Provider      | Completion | Async Completion | rag_chat | image generation |
| ------------- | ---------- | ---------------- | -------- | ---------------- |
| OpenAI        | ✅         | ✅               | ✅       | ✅               |
| deepinfra     | ✅         | ✅               | ✅       | ✅               |
| perplexity-ai | ✅         | ✅               |          |                  |
| anthropic     | ✅         | ✅               | ✅       |                  |
| cohere        | ✅         |                  |          |                  |
| huggingface   | ✅         |                  |          | ✅               |


### License
MIT