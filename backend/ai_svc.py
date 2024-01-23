

# %%
from PIL import Image
import requests
import os
import openai
import sys
# Access the API key
api_key = os.getenv("OPENAI_KEY")
ai_api_key = os.getenv("HUGGING_KEY")
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": ai_api_key}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
def blip_caption(image):
    output = query(image)
    print(output[0]['generated_text'])
    caption1 = output[0]['generated_text']
    return caption1

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
    content_user = "make a "+ length+ "Words "+ type_of_literature+ " of this caption "+ caption + " in spanish"
    openai.organization = "org-X9t5LSUVjPl0ceRHpyGWv4ts"
    openai.api_key = api_key
    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": content_system},
        {"role": "user", "content": content_user}
        ]
    )
    return completion.choices[0].message


def ultimate_caption(caption):
    content_system = "you are a literature teacher"
    content_user = "enhance the : "+caption + " ,sentence with these other two, and make a simple and more coherent sentence of 10 words from that"
    openai.organization = "org-X9t5LSUVjPl0ceRHpyGWv4ts"
    openai.api_key = api_key
    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": content_system},
        {"role": "user", "content": content_user}
        ]
    )
    return completion.choices[0].message

def create_fragment_from_image(params, image):
    caption1 = blip_caption(image=image)

    data = ultimate_caption(caption = caption1)
    definitive_caption = data.content
    print(definitive_caption)
    data = generate_literature(genre=params['genero'], inspiration=params['inspiracion'], type_of_literature=params['tipo'], length=params['longitud'], caption=definitive_caption)
    content_value = data.content
    print(content_value)
    return content_value


