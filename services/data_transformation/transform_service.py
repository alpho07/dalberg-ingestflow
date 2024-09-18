import pandas as pd
from sqlalchemy.ext.asyncio import create_async_engine
from utils.config import DATABASE_URL
from utils.logger import logger

async_engine = create_async_engine(DATABASE_URL)


async def transform_data(query: str) -> list:
    """
    Transforms the raw data stored in the database based on the provided SQL query.

    Args:
        query (str): The SQL query used to transform the data.

    Returns:
        list: A list of transformed data.

    Raises:
        Exception: If there is an error during the data transformation process.
    """
    try:
        async with async_engine.connect() as conn:
            # Execute the transformation query
            result = await conn.execute(query)
            transformed_data = pd.DataFrame(result.fetchall(), columns=result.keys())

        logger.info("Data successfully transformed.")
        return transformed_data.to_dict(orient="records")

    except Exception as e:
        logger.error(f"Failed to transform data: {str(e)}")
        raise e
