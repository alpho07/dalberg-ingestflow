from sklearn.linear_model import LinearRegression
import pandas as pd
from sqlalchemy.ext.asyncio import create_async_engine
from utils.config import DATABASE_URL

async_engine = create_async_engine(DATABASE_URL)

async def apply_linear_regression():
    """
    Applies a simple linear regression model on the transformed data to predict farm size.

    Returns:
        dict: Predicted farm sizes for the next dataset entries.
    """
    try:
        async with async_engine.connect() as conn:
            # Fetch transformed data (example: farm size and location data)
            query = "SELECT farm_size, location_index FROM raw_data"
            result = await conn.execute(query)
            df = pd.DataFrame(result.fetchall(), columns=result.keys())

            # Prepare the data
            X = df[['location_index']]  # Features (e.g., location)
            y = df['farm_size']          # Target (farm size)

            # Train a linear regression model
            model = LinearRegression()
            model.fit(X, y)

            # Predict future farm sizes
            predictions = model.predict(X)
            df['predicted_farm_size'] = predictions

            return df.to_dict(orient='records')

    except Exception as e:
        raise Exception(f"Error applying linear regression: {str(e)}")
    
    
 #Route   
app.get("/apply-machine-learning")
async def apply_ml_route():
    """
    API endpoint to apply machine learning on the data and return predictions.
    
    Returns:
        dict: Predicted values from the machine learning model.
    """
    try:
        predictions = await apply_linear_regression()
        return {"status": "Success", "data": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error applying machine learning: {str(e)}")
    
