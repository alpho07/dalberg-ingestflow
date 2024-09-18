from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from services.data_ingestion.ingestion_service import extract_data
from services.data_loading.load_service import load_data_to_db
from services.data_transformation.transform_service import transform_data
from services.data_visualization.visualization_service import visualize_data

app = FastAPI()


@app.get("/ingest")
async def ingest_data(api_url: str, api_key: str):
    """
    API endpoint to trigger data ingestion from an external API.

    Args:
        api_url (str): The URL of the API to extract data from.
        api_key (str): The API key used for authentication.

    Returns:
        dict: Status and extracted data.

    Raises:
        HTTPException: If the data ingestion process fails.
    """
    try:
        raw_data = extract_data(api_url, api_key)
        return {"status": "Data successfully extracted", "data": raw_data}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error in data ingestion: {str(e)}"
        )


@app.post("/load")
async def load_data(data: list, table_name: str):
    """
    API endpoint to load data into the database.

    Args:
        data (list): The raw data to be loaded into the database.
        table_name (str): The name of the database table.

    Returns:
        dict: Status message of the loading process.

    Raises:
        HTTPException: If the data loading process fails.
    """
    try:
        load_status = await load_data_to_db(data, table_name)
        return {"status": load_status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading data: {str(e)}")


@app.get("/transform")
async def transform_data_route(query: str):
    """
    API endpoint to trigger data transformation.

    Args:
        query (str): The SQL query to execute for data transformation.

    Returns:
        dict: Transformed data.

    Raises:
        HTTPException: If the data transformation process fails.
    """
    try:
        transformed_data = await transform_data(query)
        return {"status": "Data successfully transformed", "data": transformed_data}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error in data transformation: {str(e)}"
        )


@app.get("/visualize-data", response_class=HTMLResponse)
async def visualize_data_route(
    query: str, x_axis: str, y_axis: str, chart_type: str = "bar"
):
    """
    API endpoint to generate a data visualization.

    Args:
        query (str): The SQL query used to fetch the data for visualization.
        x_axis (str): The column to use for the x-axis.
        y_axis (str): The column to use for the y-axis.
        chart_type (str, optional): The type of chart to generate (bar, line, scatter). Defaults to 'bar'.

    Returns:
        str: HTML content containing the generated chart.

    Raises:
        HTTPException: If the chart generation process fails.
    """
    try:
        chart_html = await visualize_data(query, x_axis, y_axis, chart_type)
        return HTMLResponse(content=chart_html, status_code=200)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating visualization: {str(e)}"
        )
