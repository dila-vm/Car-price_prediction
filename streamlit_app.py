import streamlit as st
import numpy as np
import pandas as pd
import joblib
import util

ml_model = joblib.load('./xgb_model.joblib')
st.title('How much Is this car? :car: :dollar:')

brand_mapping = {
    "Acura": 0,
    "Alfa": 1,
    "Aston": 2,
    "Audi": 3,
    "BMW": 4,
    "Bentley": 5,
    "Cadillac": 6,
    "Chevrolet": 7,
    "Dodge": 8,
    "Ford": 9,
    "GMC": 10,
    "Honda": 11,
    "Hummer": 12,
    "Hyundai": 13,
    "INFINITI": 14,
    "Jaguar": 15,
    "Jeep": 16,
    "Kia": 17,
    "Land": 18,
    "Lexus": 19,
    "Lincoln": 20,
    "MINI": 21,
    "Maserati": 22,
    "Mercedes-Benz": 23,
    "Nissan": 24,
    "Pontiac": 25,
    "Porsche": 26,
    "RAM": 27,
    "Rivian": 28,
    "Rolls-Royce": 29,
    "Subaru": 30,
    "Tesla": 31,
    "Toyota": 32,
    "Volkswagen": 33
}


def get_input():
    inputs = []
    cols = st.columns(3)
    input_index = 0

    with cols[input_index % 3]:
        brand = st.selectbox('Brand', options=list(brand_mapping.keys()))
        brand_numeric = brand_mapping[brand]
        inputs.append(brand_numeric)
    input_index += 1

    with cols[input_index % 3]:
        model = st.selectbox('Model', options=list(util.model_mapping.keys()))
        model_numeric = util.model_mapping[model]
        inputs.append(model_numeric)
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
        transmission = st.selectbox('Transmission', options=list(util.transmission_mapping.keys()))
        transmission_numaric = util.transmission_mapping[transmission]
        inputs.append(transmission_numaric)
    input_index += 1

    with cols[input_index % 3]:
        speed = st.number_input('Speed', min_value=0.0, step=0.1)
        inputs.append(speed)
    input_index += 1

    with cols[input_index % 3]:
        exterior_color = st.selectbox('Exterior Color', options=list(util.exterior_color.keys()))
        exterior_color_numeric = util.exterior_color[exterior_color]
        inputs.append(exterior_color_numeric)
    input_index += 1

    with cols[input_index % 3]:
        interior_color = st.selectbox('Interior Color', options=list(util.interior_color_mapping.keys()))
        interior_color_numeric = util.interior_color_mapping[interior_color]
        inputs.append(interior_color_numeric)
    input_index += 1

    with cols[input_index % 3]:
        accident = st.selectbox('Accident', options=list(util.accident_mapping.keys()))
        accident_numeric = util.accident_mapping[accident]
        inputs.append(accident_numeric)
    input_index += 1

    with cols[input_index % 3]:
        clean_title = st.selectbox('Clean Title', options=list(util.clean_tile_mapping.keys()))
        clean_title_numeric = util.clean_tile_mapping[clean_title]
        inputs.append(clean_title_numeric)
    input_index += 1

    with cols[input_index % 3]:
        cylinder = st.selectbox('Cylinder', options=list(util.cylinder_mapping.keys()))
        cylinder_numeric = util.cylinder_mapping[cylinder]
        inputs.append(cylinder_numeric)
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
        hp = st.selectbox('HP', options=list(util.hp_mapping.keys()))
        hp_numeric = util.hp_mapping[hp]
        inputs.append(hp_numeric)
    input_index += 1

    with cols[input_index % 3]:
        v = st.selectbox('V', options=list(util.v_mapping.keys()))
        v_numeric = util.v_mapping[v]
        inputs.append(v_numeric)
    input_index += 1

    with cols[input_index % 3]:
        pdi = st.selectbox('PDI', ['true', 'false'])
        pdi_numeric = 1 if pdi == 'true' else 0
        inputs.append(pdi_numeric)
    input_index += 1

    with cols[input_index % 3]:
        tfsi = st.checkbox('TFSI')
        inputs.append(1 if tfsi else 0)
    input_index += 1

    with cols[input_index % 3]:
        gdi = st.checkbox('GDI')
        inputs.append(1 if gdi else 0)
    input_index += 1

    with cols[input_index % 3]:
        sohc = st.checkbox('SOHC')
        inputs.append(1 if sohc else 0)
    input_index += 1

    with cols[input_index % 3]:
        dohc = st.checkbox('DOHC')
        inputs.append(1 if dohc else 0)
    input_index += 1

    with cols[input_index % 3]:
        straight = st.checkbox('Straight')
        inputs.append(1 if straight else 0)
    input_index += 1

    with cols[input_index % 3]:
        a_t = st.checkbox('A/T')
        inputs.append(1 if a_t else 0)
    input_index += 1

    with cols[input_index % 3]:
        automatic = st.checkbox('Automatic')
        inputs.append(1 if automatic else 0)
    input_index += 1

    with cols[input_index % 3]:
        auto_shift = st.checkbox('Auto-Shift')
        inputs.append(1 if auto_shift else 0)
    input_index += 1

    with cols[input_index % 3]:
        dual_shift_mode = st.checkbox('Dual Shift Mode')
        inputs.append(1 if dual_shift_mode else 0)
    input_index += 1

    with cols[input_index % 3]:
        cvt = st.checkbox('CVT')
        inputs.append(1 if cvt else 0)
    input_index += 1

    with cols[input_index % 3]:
        overdrive = st.checkbox('Overdrive')
        inputs.append(1 if overdrive else 0)
    input_index += 1

    with cols[input_index % 3]:
        m_t = st.checkbox('M/T')
        inputs.append(1 if m_t else 0)
    input_index += 1

    return np.array(inputs).reshape(1, -1)


def main():
    user_inputs = get_input()
    prediction = ml_model.predict(user_inputs)

    # Display prediction highlighted
    st.write("")
    st.markdown(
        "<h3 style='text-align: center; background-color: #ff4b4b;'>Predicted Price: " + str(prediction) + "</h3>",
        unsafe_allow_html=True)


if __name__ == '__main__':
    main()
