# API de Clima

Uma API RESTful desenvolvida com Flask que fornece informações meteorológicas de diferentes cidades, integrando com OpenWeatherMap API e incluindo tradução automática das descrições do clima para português.

## 📋 Funcionalidades

- Consulta de dados meteorológicos por cidade
- Conversão automática de temperatura de Kelvin para Celsius
- Tradução automática da descrição do clima de inglês para português
- Retorno de dados em formato JSON incluindo:
  - Temperatura atual
  - Sensação térmica
  - Descrição do clima
  - Umidade relativa do ar

## 🔧 Tecnologias Utilizadas

- Python
- Flask
- OpenWeatherMap API
- Google Translate API (googletrans)
- python-dotenv

## 📦 Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)
- Chave de API do OpenWeatherMap

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/api-clima.git
cd api-clima
```

2. Instale as dependências:
```bash
pip install flask requests googletrans==3.1.0a0 python-dotenv
```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave API do OpenWeatherMap:
```
API_KEY=sua_chave_api_aqui
```

## 🚀 Como Usar

1. Inicie o servidor:
```bash
python app.py
```

2. Faça uma requisição GET para o endpoint `/clima` com o parâmetro `cidade`:
```
http://localhost:5000/clima?cidade=Londres
```

### Exemplo de Resposta:
```json
{
    "Cidade": "Londres",
    "Temperatura": "18.52°C",
    "Sensação": "17.85°C",
    "Descrição": "céu limpo",
    "Umidade": "65%"
}
```

## 📝 Configuração da API

O serviço utiliza as seguintes APIs:
- OpenWeatherMap para dados meteorológicos
- Google Translate para tradução das descrições

É necessário obter uma chave API gratuita do OpenWeatherMap em: https://openweathermap.org/api

## 🔒 Variáveis de Ambiente

- `API_KEY`: Sua chave de API do OpenWeatherMap
