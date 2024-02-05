
# Generador de historias con género literario a partir de procesamiento de lenguaje natural NLP y detección de imágenes utilizando Computer Vision

Este proyecto es una demostración de implementación del API en un Web App creado para la generación de historias a partir de imágenes

## Authors

- [@ReneVentura](https://github.com/ReneVentura)


## Run Locally

Clone the project

```bash
  git clone https://github.com/ReneVentura/grad-prod
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies


Start the frontend

```bash
  npm run start
```

Start the backend

```bash
  ./run-backend.sh
```


## Installation

Install virtual enviroment python 3.10
(on Mac)
```bash 
  virtualenv -p python3.10 env
  source env/bin/activate
```
Install frontend dependencies with npm

```bash
  cd frontend
  npm install 
  
```

Install backend dependencies with pip

```bash
  cd backend
  pip install -r requeriments.txt 
  
```
## Deployment

To deploy this project run

```bash
  npm run deploy
```

```bash
  ./run-backend.sh
```
## API Reference

#### Get all items

```http
  POST /upload
```

| Payload | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `request.files` | `*.jpg,.jpeg,.png` | **Required**. Your Image |
| `request.form` | `json` | **Required**. Your Parameters |



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_KEY` OpenAI private user Key

`HUGGING_KEY` Huggin Face private user Key


## Demo



[demo](https://www.veed.io/view/68ec9c6e-c255-4583-97a1-bace0d7054b4?panel=share)
