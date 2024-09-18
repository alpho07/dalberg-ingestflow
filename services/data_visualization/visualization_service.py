import plotly.express as px
import pandas as pd
from sqlalchemy.ext.asyncio import create_async_engine
from utils.config import DATABASE_URL
from utils.logger import logger

async_engine = create_async_engine(DATABASE_URL)

async def visualize_data(query: str, x_axis: str, y_axis: str, chart_type: str = 'bar') -> str:
    """
    Generates a chart visualization based on the query and axes provided.

    Args:
        query (str): The SQL query used to retrieve the data for visualization.
        x_axis (str): The column to use for the x-axis of the chart.
        y_axis (str): The column to use for the y-axis of the chart.
        chart_type (str, optional): The type of chart to generate. Defaults to 'bar'.

    Returns:
        str: HTML content of the generated chart.

    Raises:
        Exception: If there is an error during data retrieval or chart generation.
    """
    try:
        async with async_engine.connect() as conn:
            # Execute the query to fetch data
            result = await conn.execute(query)
            df = pd.DataFrame(result.fetchall(), columns=result.keys())

            # Generate the chart based on the specified chart type
            if chart_type == 'bar':
                fig = px.bar(df, x=x_axis, y=y_axis)
            elif chart_type == 'line':
                fig = px.line(df, x=x_axis, y=y_axis)
            elif chart_type == 'scatter':
                fig = px.scatter(df, x=x_axis, y=y_axis)
            else:
                raise ValueError("Unsupported chart type. Choose between 'bar', 'line', or 'scatter'.")

            logger.info(f"Generated {chart_type} chart for {x_axis} vs {y_axis}")
            return fig.to_html()

    except Exception as e:
        logger.error(f"Error generating chart: {str(e)}")
        raise Exception(f"Error generating chart: {str(e)}")
