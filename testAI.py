

# %%
from PIL import Image
from dotenv import load_dotenv
import os
import requests
import openai
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
image =  "test5.jpg"
im = Image.open(image)

load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_KEY")
ai_api_key = os.getenv("HUGGING_KEY")



API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

while True:
    output = query(image)
    try:
        generated_text = output[0]['generated_text']
        print(generated_text)
        caption1 = generated_text
        break  # Si no hay KeyError, sal del bucle
    except KeyError:
        print("KeyError: 'generated_text' no se encontró en la respuesta. Intentando de nuevo...")



API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": ai_api_key}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

while True:
    output = query(image)
    try:
        generated_text = output[0]['generated_text']
        print(generated_text)
        caption2 = generated_text
        break  # Si no hay KeyError, sal del bucle
    except KeyError:
        print("KeyError: 'generated_text' no se encontró en la respuesta. Intentando de nuevo...")


API_URL = "https://api-inference.huggingface.co/models/microsoft/git-large-coco"
headers = {"Authorization": ai_api_key}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

while True:
    output = query(image)
    try:
        generated_text = output[0]['generated_text']
        print(generated_text)
        caption3 = generated_text
        break  # Si no hay KeyError, sal del bucle
    except KeyError:
        print("KeyError: 'generated_text' no se encontró en la respuesta. Intentando de nuevo...")




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
    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": content_system},
        {"role": "user", "content": content_user}
        ]
    )
    return completion.choices[0].message


def ultimate_caption(caption, caption2, caption3):
    content_system = "you are a literature teacher"
    content_user = "enhance the first: "+caption + " ,sentence with these other two, "+ caption2+", "+caption3+ " and make a more complex and more coherent sentence of 20 words from that"
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

def generate_title(fragment):
    content_system = "you are a literature teacher"
    content_user = "make a short title for this fragment: "+fragment
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
def make_file(title, content, image_path, output_path='fragment.txt'):
    with open(output_path, 'w') as file:
        # Escribir el título en el archivo de texto
        file.write(f' {title}\n\n')

        # Escribir el contenido en el archivo de texto
        file.write(f'\n{content}\n\n')

        # Escribir la ruta de la imagen en el archivo de texto
        if image_path:
            file.write(f'Ruta de la imagen: {image_path}\n')

data = ultimate_caption(caption=caption1, caption2=caption2, caption3=caption3)
# Accede directamente al valor de "content" desde el objeto de respuesta
definitive_caption = data.content

# Imprime el valor
print(definitive_caption)


data = generate_literature(caption=definitive_caption, length="200", genre="gothic", type_of_literature="history")
# Accede directamente al valor de "content" desde el objeto de respuesta
fragment = data.content
title = generate_title(fragment)

# Imprime el valor
make_file(title.content, fragment, image)


