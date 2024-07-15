import streamlit as st
import pickle
import numpy as np

# Load the pickled model
def load_model():
    try:
        model_path = os.path.join(os.getcwd(), 'model.pkl')
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        print(f"Error: 'model.pkl' not found in directory: {os.getcwd()}")
        return None
    except Exception as e:
        print(f"Error loading 'model.pkl': {e}")
        return None

# Function to predict housing prices
def predict_price(model, input_data):
    # Reshape input data for prediction
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction[0]

def main():
    # Load the model
    model = load_model()

    # Title of the web app
    st.title('California Housing Price Prediction')

    # Input features for prediction
    MedInc = st.number_input('MedInc (median income in block)')
    HouseAge = st.number_input('HouseAge (median house age in block)')
    AveRooms = st.number_input('AveRooms (average number of rooms)')
    AveBedrms = st.number_input('AveBedrms (average number of bedrooms)')
    Population = st.number_input('Population (block population)')
    AveOccup = st.number_input('AveOccup (average house occupancy)')
    Latitude = st.number_input('Latitude (house block latitude)')
    Longitude = st.number_input('Longitude (house block longitude)')

    # Predict button
    if st.button('Predict Price'):
        input_data = [MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]
        prediction = predict_price(model, input_data)
        st.success(f'Predicted Price: ${prediction:,.2f}')

if __name__ == '__main__':
    main()
