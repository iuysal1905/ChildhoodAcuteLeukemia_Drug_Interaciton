import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
import pip
pip.main(["install", "openpyxl"])

# Set header title
st.title('XAI ile İlaç Yeniden Kullanım Çalışmaları için Benzetim Ortamı')

# Define list of selection options and sort alphabetically
sec1 = ['IC50','Inhibition']
sec1.sort()
sec2=['Biyoaktivite','XAI','Model Performansı']
sec3=['Biyoaktivite Sınıfı','LogP','MW','NumHAcceptors','NumHDonors','PIC50']
sec4=['WaterFall','Bar','BeeSwarm','HeatMap','Important Features']
sec5=['RMSE','Time Taken']

# Implement multiselect dropdown menu for option selection (returns a list)
selected_1 = st.multiselect('Lütfen standart türlerden birini seçiniz', sec1)

# Set info message on initial site load
if len(selected_1) == 0:
    st.text('Lütfen listeden birini seçiniz')

# Create network graph when user selects >= 1 item
elif (selected_1=='IC50'):

    selected_2 = st.multiselect('Lütfen değerlendirme türlerinden birini seçiniz', sec2)
    if len(selected_2) == 0:
        st.text('Lütfen listeden birini seçiniz')
    elif (selected_2=='Biyoaktivite'):
        selected_3 = st.multiselect('Lütfen biyoaktivite türlerinden birini seçiniz', sec3)
        if (selected_3=='Biyoaktivite Sınıfı'):
            print('ic50_bioactivitiy_class.png')
        elif (selected_3=='LogP'):
            print('ic50_logp.png')
        elif (selected_3=='MW'):
            print('ic50_mw.png')
        elif (selected_3=='NumHAcceptors'):
            print('ic50_numhacceptors')
        elif (selected_3=='NumHDonors'):
            print('ic50_numhdonors')
        elif (selected_3=='PIC50'):
            print('ic50_pic50_bioclass')
    elif (selected_2=='XAI'):
        selected_4 = st.multiselect('Lütfen grafik türlerinden birini seçiniz', sec4)
        if (selected_4=='WaterFall'):
            print('ic50_waterfall.png')
        elif (selected_4=='Bar'):
            print('ic50_bar.png')
        elif (selected_4=='BeeSwarm'):
            print('ic50_mw.png')
        elif (selected_4=='HeatMap'):
            print('ic50_heatmap')
        elif (selected_4=='Important Features'):
            print('ic50_importantfeatures')
    elif (selected_2=='Model Performansı'):
        selected_5 = st.multiselect('Lütfen model değerlendirme seçeneklerinden birini seçiniz', sec5)
        if (selected_5=='RMSE'):
            print('ic50_rmse.png')
        elif (selected_5=='Time Taken'):
            print('ic50_timetaken.png')
    
    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(G)

    # Generate network with specific layout settings
    drug_net.repulsion(
                        node_distance=420,
                        central_gravity=0.33,
                        spring_length=110,
                        spring_strength=0.10,
                        damping=0.95
                       )

    

# Footer
st.markdown(
    """
    <br>
    <h6><a href="https://iuysal1905-streamlit-leukemia-dnhrmb.streamlit.app/" target="_blank">Lösemi İlaç-İlaç Etkileşim Ağ Grafiği</a></h6>
    <h6>Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.</h6>
    """, unsafe_allow_html=True
    )
