import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
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
selected_1 = st.selectbox('Lütfen standart türlerden birini seçiniz', sec1)

# Set info message on initial site load
if len(selected_1) == 0:
    st.text('Lütfen listeden birini seçiniz')
elif (selected_1=='Inhibition'):
    selected_2 = st.selectbox('Lütfen değerlendirme türlerinden birini seçiniz', sec2)
    if len(selected_2) == 0:
        st.text('Lütfen listeden birini seçiniz')
    elif (selected_2=='Biyoaktivite'):
        selected_3 = st.selectbox('Lütfen biyoaktivite türlerinden birini seçiniz', sec3)
        if (selected_3=='Biyoaktivite Sınıfı'):
            st.image('inhibition_bioactivitiy_class.png')
        elif (selected_3=='LogP'):
            st.image('inhibition_logp.png')
        elif (selected_3=='MW'):
            st.image('inhibition_mw.png')
        elif (selected_3=='NumHAcceptors'):
            st.image('inhibition_numhacceptors.png')
        elif (selected_3=='NumHDonors'):
            st.image('inhibition_numhdonors.png')
        elif (selected_3=='PIC50'):
            st.image('inhibition_pic50_bioclass.png')
    elif (selected_2=='XAI'):
        selected_4 = st.selectbox('Lütfen grafik türlerinden birini seçiniz', sec4)
        if (selected_4=='WaterFall'):
            st.image('inhibition_waterfall.png')
        elif (selected_4=='Bar'):
            st.image('inhibition_bar.png')
        elif (selected_4=='BeeSwarm'):
            st.image('inhibition_beeswarm.png')
        elif (selected_4=='HeatMap'):
            st.image('inhibition_heatmap.png')
        elif (selected_4=='Important Features'):
            st.image('inhibition_importantfeatures.png')
    elif (selected_2=='Model Performansı'):
        selected_5 = st.selectbox('Lütfen model değerlendirme seçeneklerinden birini seçiniz', sec5)
        if (selected_5=='RMSE'):
            st.image('inhibition_rmse.png')
        elif (selected_5=='Time Taken'):
            st.image('inhibition_timetaken.png')
    
elif (selected_1=='IC50'):

    selected_2 = st.selectbox('Lütfen değerlendirme türlerinden birini seçiniz', sec2)
    if len(selected_2) == 0:
        st.text('Lütfen listeden birini seçiniz')
    elif (selected_2=='Biyoaktivite'):
        selected_3 = st.selectbox('Lütfen biyoaktivite türlerinden birini seçiniz', sec3)
        if (selected_3=='Biyoaktivite Sınıfı'):
            st.image('ic50_bioactivitiy_class.png')
        elif (selected_3=='LogP'):
            st.image('ic50_logp.png')
        elif (selected_3=='MW'):
            st.image('ic50_mw.png')
        elif (selected_3=='NumHAcceptors'):
            st.image('ic50_numhacceptors.png')
        elif (selected_3=='NumHDonors'):
            st.image('ic50_numhdonors.png')
        elif (selected_3=='PIC50'):
            st.image('ic50_pic50_bioclass.png')
    elif (selected_2=='XAI'):
        selected_4 = st.selectbox('Lütfen grafik türlerinden birini seçiniz', sec4)
        if (selected_4=='WaterFall'):
            st.image('ic50_waterfall.png')
        elif (selected_4=='Bar'):
            st.image('ic50_bar.png')
        elif (selected_4=='BeeSwarm'):
            st.image('ic50_beeswarm.png')
        elif (selected_4=='HeatMap'):
            st.image('ic50_heatmap.png')
        elif (selected_4=='Important Features'):
            st.image('ic50_importantfeatures.png')
    elif (selected_2=='Model Performansı'):
        selected_5 = st.selectbox('Lütfen model değerlendirme seçeneklerinden birini seçiniz', sec5)
        if (selected_5=='RMSE'):
            st.image('ic50_rmse.png')
        elif (selected_5=='Time Taken'):
            st.image('ic50_timetaken.png')
# Footer
    if st.button("Lösemi İlaç-İlaç Etkileşim Ağ Grafiği"):
        link = "https://iuysal1905-streamlit-leukemia-dnhrmb.streamlit.app/"
        js_code = f"window.open('{link}')"
        st.write("<script>{}</script>".format(js_code), unsafe_allow_html=True)

    st.markdown("Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.")
st.markdown(
    
    """
    <br>
    <h6><a href="https://iuysal1905-streamlit-leukemia-dnhrmb.streamlit.app/" target="_blank">Lösemi İlaç-İlaç Etkileşim Ağ Grafiği</a></h6>
    <h6>Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.</h6>
    """, unsafe_allow_html=True
    )
