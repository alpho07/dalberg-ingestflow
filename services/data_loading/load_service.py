import pandas as pd
from sqlalchemy.ext.asyncio import create_async_engine
from utils.config import DATABASE_URL
from utils.logger import logger

async_engine = create_async_engine(DATABASE_URL)


async def load_data_to_db(data: list, table_name: str) -> str:
    """
    Loads the raw data into the PostgreSQL database.

    Args:
        data (list): The raw data to be loaded into the database.
        table_name (str): The name of the database table where the data will be loaded.

    Returns:
        str: A message confirming successful data loading.

    Raises:
        Exception: If there is an error during the data loading process.
    """
    try:
        # Convert the data to a DataFrame
        df = pd.DataFrame(data)

        # Load the data into the specified database table
        async with async_engine.begin() as conn:
            await conn.run_sync(
                lambda conn: df.to_sql(
                    table_name, conn, if_exists="replace", index=False
                )
            )

        logger.info("Data successfully loaded into the database.")
        return f"Data successfully loaded into {table_name}"

    except Exception as e:
        logger.error(f"Failed to load data into the database: {str(e)}")
        raise e
