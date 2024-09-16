import streamlit as st
import joblib
import numpy as np
import sklearn



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

model = joblib.load('model3.pkl')


st.title("Forest Cover Type Prediction")



elevation = st.number_input('Elevation', value=0)
aspect = st.number_input('Aspect', value=0)
slope = st.number_input('Slope', value=0)
hordt_hyd = st.number_input('Horizontal Distance to Hydrology', value=0)
verdt_hyd = st.number_input('Vertical Distance to Hydrology', value=0)
hordt_road = st.number_input('Horizontal Distance to Roadways', value=0)
hillshade9 = st.number_input('Hillshade 9am', value=0)
hillshade12 = st.number_input('Hillshade Noon', value=0)
hillshade3 = st.number_input('Hillshade 3pm', value=0)
hordt_fire = st.number_input('Horizontal Distance to Fire Points', value=0)



soil_type = st.selectbox('Soil Type', [
    "Cathedral family - Rock outcrop complex, extremely stony",
    "Vanet - Ratake families complex, very stony",
    "Haploborolis - Rock outcrop complex, rubbly",
    "Ratake family - Rock outcrop complex, rubbly",
    "Vanet family - Rock outcrop complex complex, rubbly",
    "Vanet - Wetmore families - Rock outcrop complex, stony",
    "Gothic family",
    "Supervisor - Limber families complex",
    "Troutville family, very stony",
    "Bullwark - Catamount families - Rock outcrop complex, rubbly",
    "Bullwark - Catamount families - Rock land complex, stony",
    "Legault family - Rock land complex, stony",
    "Catamount family - Rock land - Bullwark family complex, rubbly",
    "Pachic Argiborolis - Aquolis complex",
    "Unspecified in the USFS Soil and ELU Survey",
    "Cryaquolis - Cryoborolis complex",
    "Gateview family - Cryaquolis complex",
    "Rogert family, very stony",
    "Typic Cryaquolis - Borohemists complex",
    "Typic Cryaquepts - Typic Cryaquolls complex",
    "Typic Cryaquolls - Leighcan family, till substratum complex",
    "Leighcan family, till substratum, extremely bouldery",
    "Leighcan family, till substratum - Typic Cryaquolls complex",
    "Leighcan family, till substratum, stony",
    "Typic Cryaquepts - Typic Cryaquolls complex",
    "Typic Cryaquepts - Typic Cryaquolls complex",
])

soil_types_dict = {
    "Cathedral family - Rock outcrop complex, extremely stony": "1000000000000000000000000000000000000000",
    "Vanet - Ratake families complex, very stony": "0100000000000000000000000000000000000000",
    "Haploborolis - Rock outcrop complex, rubbly": "0010000000000000000000000000000000000000",
    "Ratake family - Rock outcrop complex, rubbly": "0001000000000000000000000000000000000000",
    "Vanet family - Rock outcrop complex complex, rubbly": "0000100000000000000000000000000000000000",
    "Vanet - Wetmore families - Rock outcrop complex, stony": "0000010000000000000000000000000000000000",
    "Gothic family": "0000001000000000000000000000000000000000",
    "Supervisor - Limber families complex": "0000000100000000000000000000000000000000",
    "Troutville family, very stony": "0000000010000000000000000000000000000000",
    "Bullwark - Catamount families - Rock outcrop complex, rubbly": "0000000001000000000000000000000000000000",
    "Bullwark - Catamount families - Rock land complex, stony": "0000000000100000000000000000000000000000",
    "Legault family - Rock land complex, stony": "0000000000010000000000000000000000000000",
    "Catamount family - Rock land - Bullwark family complex, rubbly": "0000000000001000000000000000000000000000",
    "Pachic Argiborolis - Aquolis complex": "0000000000000100000000000000000000000000",
    "Unspecified in the USFS Soil and ELU Survey": "0000000000000010000000000000000000000000",
    "Cryaquolis - Cryoborolis complex": "0000000000000001000000000000000000000000",
    "Gateview family - Cryaquolis complex": "0000000000000000100000000000000000000000",
    "Rogert family, very stony": "0000000000000000010000000000000000000000",
    "Typic Cryaquolis - Borohemists complex": "0000000000000000001000000000000000000000",
    "Typic Cryaquepts - Typic Cryaquolls complex": "0000000000000000000100000000000000000000",
    "Typic Cryaquolls - Leighcan family, till substratum complex": "0000000000000000000010000000000000000000",
    "Leighcan family, till substratum, extremely bouldery": "0000000000000000000001000000000000000000",
    "Leighcan family, till substratum - Typic Cryaquolls complex": "0000000000000000000000100000000000000000",
    "Leighcan family, till substratum, stony": "0000000000000000000000010000000000000000",
    "Typic Cryaquepts - Typic Cryaquolls complex": "0000000000000000000000001000000000000000",
    "Typic Cryaquepts - Typic Cryaquolls complex": "0000000000000000000000000100000000000000",
}
soil_type_encoded = [int(x) for x in soil_types_dict.get(soil_type, "0000000000000000000000000000000000000000")]


inputs = np.array([elevation, aspect, slope, hordt_hyd, verdt_hyd, hordt_road,
                   hillshade9, hillshade12, hillshade3, hordt_fire]+ soil_type_encoded).reshape(1, -1)


if st.button('Predict'):
    prediction = model.predict(inputs)
    outputs = ["Spruce/Fir", "Lodgepole Pine", "Ponderosa Pine", "Cottonwood/Willow", "Aspen", "Douglas-fir", "Krummholz"]
    st.write(f"The predicted forest cover type is: {outputs[prediction[0]]}")
