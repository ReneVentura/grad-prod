

# %%
from PIL import Image
image =  "monstruo.jpg"
im = Image.open(image)
im

# %%
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_KEY")
ai_api_key = os.getenv("HUGGING_KEY")


# %%
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": ai_api_key}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query(image)
print(output[0]['generated_text'])
caption1 = output[0]['generated_text']

# %%
import requests

API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": ai_api_key}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query(image)
print(output[0]['generated_text'])
caption2 = output[0]['generated_text']

# %%
import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/git-large-coco"
headers = {"Authorization": ai_api_key}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query(image)
print(output[0]['generated_text'])
caption3 = output[0]['generated_text']

# %%
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-mpnet-base-v2"
headers = {"Authorization": ai_api_key}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
	"inputs": {
		"source_sentence": "a purple monster teddy bear sitting on a bed with a green tongue and yellow eyes",
		"sentences": [
			caption1,
			caption2,
			caption3
		]
	},
})

print(output)

# %%
import pandas as pd
pd.set_option('display.max_colwidth', None)
data = {
    'Modelo': ['Humano', 'BLIP', 'GIT', 'VIT'],
    
    'Sentence': ['a purple monster teddy bear sitting on a bed with a green tongue and yellow eyes', 
                 caption1, 
                 caption2,
                 caption3],
    'SBERT sentence similarity': [1,output[0], output[1],output[2]]
}

df = pd.DataFrame(data)

df




# %%
import os
import openai
import sys




# %%
def generate_literature(genre = "romantic", inspiration = "romanticism", caption = "the sunset", length = "100", type_of_literature = "poem"):

    '''
        @PARAMS
        length (int): length of the generated literature, the minimum is 10 and the max is 400
        genre (str): genre of the generated literature, has to be either romantic, gothic or fantastic-realism
        inspiration(str): the movement that will define the literature, has to be either, Romanticism, Realism or Naturalism
        caption (str): the generated caption obtained from the image
        type_of_literature (str): the type of the literary text to be generated, has to be either, fable, story or poem
    '''
    content_system = "You are a "+ genre+  " spanish writter from the, "+ inspiration
    content_user = "make a "+ length+ "Words "+ type_of_literature+ " of this caption "+ caption
    openai.organization = "org-X9t5LSUVjPl0ceRHpyGWv4ts"
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": content_system},
        {"role": "user", "content": content_user}
        ]
    )
    return completion.choices[0].message

# %%
data = {
    "genre":["romantic"],
    "inspiration":["romanticism"],
    "length":["100"],
    "literature":["poem"]
}
df = pd.DataFrame(data)
df

# %%
def ultimate_caption(caption, caption2, caption3):
    content_system = "you are a literature teacher"
    content_user = "enhance the first: "+caption + " ,sentence with these other two, "+ caption2+", "+caption3+ " and make a simple and more coherent sentence of 10 words from that"
    openai.organization = "org-X9t5LSUVjPl0ceRHpyGWv4ts"
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": content_system},
        {"role": "user", "content": content_user}
        ]
    )
    return completion.choices[0].message

# %%
data = ultimate_caption(caption=caption1, caption2=caption2, caption3=caption3)
# Accede directamente al valor de "content" desde el objeto de respuesta
definitive_caption = data["content"]

# Imprime el valor
print(definitive_caption)

# %%
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-mpnet-base-v2"
headers = {"Authorization": ai_api_key}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
	"inputs": {
		"source_sentence": "a purple monster teddy bear sitting on a bed with a green tongue and yellow eyes",
		"sentences": [
			
			caption1,
			caption2,
			caption3,
			definitive_caption
		]
	},
})

print(output)
import pandas as pd
pd.set_option('display.max_colwidth', None)
data = {
    'Modelo': ['Humano', 'BLIP', 'GIT', 'VIT', 'GPT-4 Transformed sentence'],
    
    'Sentence': ['a purple monster teddy bear sitting on a bed with a green tongue and yellow eyes', 
                 caption1, 
                 caption2,
                 caption3,
				 definitive_caption],
    'SBERT sentence similarity': [1,output[0], output[1],output[2], output[3]]
}

df = pd.DataFrame(data)

df


# %%
data = generate_literature(caption=definitive_caption)
# Accede directamente al valor de "content" desde el objeto de respuesta
content_value = data["content"]

# Imprime el valor
print(content_value)


