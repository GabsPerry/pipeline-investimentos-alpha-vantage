# Importando bibliotecas 

import requests                         # requisição de API
import json                             # trabalhar com Json
from pathlib import Path                # manipular caminhos de arquivos e pastas 
from datetime import datetime as dt     # pegar data atual
import time 
from config import API_KEY, VOLUME_PATH
from src.utils.logger import get_logger

logger = get_logger('Ingestão')

# Criando campos chave 
# Minha API Key (estou buscando do meu arquivo config.py)
apiKey = API_KEY
output_dir = VOLUME_PATH

# sourceCurrency
#srcCur = 'BTC'               # Moeda/Cripto origem que vou extrair os dados 

# convertedCurrency 
convCur = 'USD'              # Moeda/Cripto para qual a origem será convertida

repository = 'data_lake/raw'

# Lista de cryptos 
cryptos = ["BTC", "ETH", "SOL", "ADA", "XRP", "BNB", "DOT", "DOGE", "TRX", "LTC"]

for srcCur in cryptos:

    logger.info(f'Fazendo nova requisição na API para {srcCur}...')
    #print('Fazendo nova requisição na API...')

    # Fazendo requisição da API 
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={srcCur}&to_currency={convCur}&apikey={apiKey}'
    
    try:

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Convertendo resposta da API em json
        data = response.json()

        # Validando reposta da API
        if "Realtime Currency Exchange Rate" not in data:
            logger.error(f'Resposta inválida para {srcCur}: {data}')
            continue

        # Salvando a response da API num arquivo json, na minha pasta local 

        # currentDate
        curDate = dt.today().strftime('%Y-%m-%d')

        #output_dir = '/Volumes/workspace/default/lago_do_mago/raw_data'
        #'J8M9P0B2JCPHH1PM'

        #file = output_dir / f"{srcCur}_{curDate}.json" 
        file = Path(f"{output_dir}/{srcCur}_{curDate}.json")

        with file.open("w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        logger.info(f'Arquivo criado com sucesso: {file}')
        #print(f'file created: {file}')

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro de requisição para {srcCur}: {e}")
    
    except Exception as e:
        logger.exception(f'Erro inesperado ao processar {srcCur}: {e}')

    time.sleep(12)

logger.info('Extração finalizada...')
#print('Extração finalizada...')
#print(data)
