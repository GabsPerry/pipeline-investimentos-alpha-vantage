# Importando bibliotecas 

import requests                         # requisição de API
import json                             # trabalhar com Json
from pathlib import Path                # manipular caminhos de arquivos e pastas 
from datetime import datetime as dt     # pegar data atual
import time 
#from dotenv import load_dotenv
#import os 

# Criando campos chave 

# Importando variáveis de ambiente do arquivo .env 
#load_dotenv()

# Sua API Key
#apiKey = os.getenv("ALPHA_VANTAGE_KEY")
apiKey = 'J8M9P0B2JCPHH1PM'

# sourceCurrency
#srcCur = 'BTC'               # Moeda/Cripto origem que vou extrair os dados 

# convertedCurrency 
convCur = 'USD'              # Moeda/Cripto para qual a origem será convertida

repository = 'data_lake/raw'

# Lista de cryptos 
cryptos = ["BTC", "ETH", "SOL", "ADA", "XRP", "BNB", "DOT", "DOGE", "TRX", "LTC"]

for srcCur in cryptos:

    print('Fazendo nova requisição na API...')

    # Fazendo requisição da API 
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={srcCur}&to_currency={convCur}&apikey={apiKey}'
    
    response = requests.get(url)

    #print(response)

    data = response.json()


    # Salvando a response da API num arquivo json, na minha pasta local 

    # currentDate
    curDate = dt.today().strftime('%Y-%m-%d')

    #output_dir = Path(repository) / srcCur 
    #output_dir.mkdir(parents=True, exist_ok=True)

    #output_dir = os.getenv("VOLUME_DBX")
    output_dir = '/Volumes/workspace/default/lago_do_mago/raw_data'

    #file = output_dir / f"{srcCur}_{curDate}.json" 
    file = Path(f"{output_dir}/{srcCur}_{curDate}.json")

    with file.open("w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f'file created: {file}')

    time.sleep(12)

print('Extração de hoje finalizada...')
#print(data)
