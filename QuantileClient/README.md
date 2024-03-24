# QuantileClientLib

QuantileClient is a Python client library designed to serve as a wrapper for the Quantile AI API. It simplifies the process of interacting with Quantile's LLM models, enabling developers to seamlessly integrate Quantile's capabilities into their Python applications.


```bash
pip install QuantileClient

```

```python

from QuantileClient import QuantileClient

base_url = "http://<api url>"  # Adjust to your server's base URL
api_key = "<your-api-quant-api-key>"

client = QuantileClient(base_url, api_key)
prompt = "what is an api"

# use any platform and model just change the func
openai_response = client.generate_openai_response(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "system", "content": prompt},
                  ],
        max_tokens=100
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

```
## Acess call cascading api 

```python

from QuantileClient import QuantileClient

base_url = "http://<api url>"  # Adjust to your server's base URL
api_key = "<your-api-quant-api-key>"

client = QuantileClient(base_url, api_key)
prompt = "what is an api"

# No neeed to specify model 

callcascade = client.call_cascading(
    prompt="tell me the word news and something abt apis",
    max_tokens=100
    
)

```
### Contributing
Contributions are welcome! Feel free to open issues, submit pull requests, or provide feedback.

### License

MIT