import streamlit as st
import numpy as np
import pandas as pd
import joblib

ml_model = joblib.load('./xgb_model.joblib')
st.title('How much Is this car?')

car_brands = [
    'Mercedes-Benz', 'INFINITI', 'Chevrolet', 'RAM', 'Honda', 'Rivian', 'BMW',
    'Dodge', 'Jeep', 'MINI', 'Porsche', 'Audi', 'Lexus', 'Cadillac', 'Jaguar',
    'Ford', 'Toyota', 'Tesla', 'Volkswagen', 'GMC', 'Land', 'Nissan', 'Maserati',
    'Kia', 'Lincoln', 'Hummer', 'Acura', 'Bentley', 'Hyundai', 'Alfa', 'Aston',
    'Pontiac', 'Rolls-Royce', 'Subaru'
]

def get_input():
    inputs = []
    cols = st.columns(3)
    input_index = 0

    with cols[input_index % 3]:
        brand = st.number_input('Brand', min_value=0, max_value=100)
        inputs.append(brand)
    input_index += 1

    with cols[input_index % 3]:
        model = st.number_input('Model', min_value=0, max_value=1000)
        inputs.append(model)
    input_index += 1

    with cols[input_index % 3]:
        model_year = st.number_input('Model Year', min_value=1900, max_value=2024)
        inputs.append(model_year)
    input_index += 1

    with cols[input_index % 3]:
        mileage = st.number_input('Mileage', min_value=0)
        inputs.append(mileage)
    input_index += 1

    with cols[input_index % 3]:
        fuel_type = st.number_input('Fuel Type', min_value=0, max_value=10)
        inputs.append(fuel_type)
    input_index += 1

    with cols[input_index % 3]:
        liter = st.number_input('Liter', min_value=0.0, step=0.1)
        inputs.append(liter)
    input_index += 1

    with cols[input_index % 3]:
        transmission = st.number_input('Transmission', min_value=0, max_value=100)
        inputs.append(transmission)
    input_index += 1

    with cols[input_index % 3]:
        speed = st.number_input('Speed', min_value=0.0, step=0.1)
        inputs.append(speed)
    input_index += 1

    with cols[input_index % 3]:
        exterior_color = st.number_input('Exterior Color', min_value=0, max_value=100)
        inputs.append(exterior_color)
    input_index += 1

    with cols[input_index % 3]:
        interior_color = st.number_input('Interior Color', min_value=0, max_value=100)
        inputs.append(interior_color)
    input_index += 1

    with cols[input_index % 3]:
        accident = st.number_input('Accident', min_value=0, max_value=1)
        inputs.append(accident)
    input_index += 1

    with cols[input_index % 3]:
        clean_title = st.number_input('Clean Title', min_value=0, max_value=1)
        inputs.append(clean_title)
    input_index += 1

    with cols[input_index % 3]:
        cylinder = st.number_input('Cylinder', min_value=0)
        inputs.append(cylinder)
    input_index += 1

    with cols[input_index % 3]:
        turbo = st.number_input('Turbo', min_value=0, max_value=1)
        inputs.append(turbo)
    input_index += 1

    with cols[input_index % 3]:
        engine_type = st.number_input('Engine Type', min_value=0, max_value=100)
        inputs.append(engine_type)
    input_index += 1

    with cols[input_index % 3]:
        hp = st.number_input('HP', min_value=0)
        inputs.append(hp)
    input_index += 1

    with cols[input_index % 3]:
        v = st.number_input('V', min_value=0)
        inputs.append(v)
    input_index += 1

    with cols[input_index % 3]:
        pdi = st.selectbox('PDI', ['true', 'false'])
        pdi_numeric = 1 if pdi == 'true' else 0
        inputs.append(pdi_numeric)
    input_index += 1

    with cols[input_index % 3]:
        tfsi = st.number_input('TFSI', min_value=0, max_value=1)
        inputs.append(tfsi)
    input_index += 1

    with cols[input_index % 3]:
        gdi = st.number_input('GDI', min_value=0, max_value=1)
        inputs.append(gdi)
    input_index += 1

    with cols[input_index % 3]:
        sohc = st.number_input('SOHC', min_value=0, max_value=1)
        inputs.append(sohc)
    input_index += 1

    with cols[input_index % 3]:
        dohc = st.number_input('DOHC', min_value=0, max_value=1)
        inputs.append(dohc)
    input_index += 1

    with cols[input_index % 3]:
        straight = st.number_input('Straight', min_value=0, max_value=1)
        inputs.append(straight)
    input_index += 1

    with cols[input_index % 3]:
        a_t = st.number_input('A/T', min_value=0, max_value=1)
        inputs.append(a_t)
    input_index += 1

    with cols[input_index % 3]:
        automatic = st.number_input('Automatic', min_value=0, max_value=1)
        inputs.append(automatic)
    input_index += 1

    with cols[input_index % 3]:
        auto_shift = st.number_input('Auto-Shift', min_value=0, max_value=1)
        inputs.append(auto_shift)
    input_index += 1

    with cols[input_index % 3]:
        dual_shift_mode = st.number_input('Dual Shift Mode', min_value=0, max_value=1)
        inputs.append(dual_shift_mode)
    input_index += 1

    with cols[input_index % 3]:
        cvt = st.number_input('CVT', min_value=0, max_value=1)
        inputs.append(cvt)
    input_index += 1

    with cols[input_index % 3]:
        overdrive = st.number_input('Overdrive', min_value=0, max_value=1)
        inputs.append(overdrive)
    input_index += 1

    with cols[input_index % 3]:
        m_t = st.number_input('M/T', min_value=0, max_value=1)
        inputs.append(m_t)
    input_index += 1

    return np.array(inputs).reshape(1, -1)

def main():
    user_inputs = get_input()
    prediction = ml_model.predict(user_inputs)

    # Display prediction highlighted
    st.write("")
    st.markdown("<h3 style='text-align: center; background-color: lightgreen;'>Predicted Price: " + str(prediction) +"</h3>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
