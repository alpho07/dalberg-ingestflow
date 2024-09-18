# services/data_ingestion/ingestion_service.py

import os
import requests
from dotenv import load_dotenv
from utils.logger import logger

load_dotenv()

def extract_data(api_url: str, api_key: str) -> list:
    """
    Extracts raw data from an external API.

    Args:
        api_url (str): The URL of the API to extract data from.
        api_key (str): The API key used for authentication.

    Returns:
        list: The raw data extracted from the API.

    Raises:
        Exception: If there is an error during the data extraction process.
    """
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        logger.info("Data successfully extracted from the API.")
        return response.json()

    except Exception as e:
        logger.error(f"Failed to extract data: {str(e)}")
        raise e
    
    
    
    # implementing code reuse
    # Another project reusing the extract_data method

from services.data_ingestion.ingestion_service import extract_data

# Example usage
api_url = "https://api.example.com/data"
api_key = "example-api-key"

data = extract_data(api_url, api_key)
print(data)
    
    
