import cv2
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
            image = cv2.imread("inhibition_bioactivitiy_class.png")
            cv2.imshow(image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()   
        elif (selected_3=='LogP'):
            print('inhibition_logp.png')
        elif (selected_3=='MW'):
            print('inhibition_mw.png')
        elif (selected_3=='NumHAcceptors'):
            print('inhibition_numhacceptors')
        elif (selected_3=='NumHDonors'):
            print('inhibition_numhdonors')
        elif (selected_3=='PIC50'):
            print('inhibition_pic50_bioclass')
    elif (selected_2=='XAI'):
        selected_4 = st.selectbox('Lütfen grafik türlerinden birini seçiniz', sec4)
        if (selected_4=='WaterFall'):
            print('inhibition_waterfall.png')
        elif (selected_4=='Bar'):
            print('inhibition_bar.png')
        elif (selected_4=='BeeSwarm'):
            print('inhibition_mw.png')
        elif (selected_4=='HeatMap'):
            print('inhibition_heatmap')
        elif (selected_4=='Important Features'):
            print('inhibition_importantfeatures')
    elif (selected_2=='Model Performansı'):
        selected_5 = st.selectbox('Lütfen model değerlendirme seçeneklerinden birini seçiniz', sec5)
        if (selected_5=='RMSE'):
            print('inhibition_rmse.png')
        elif (selected_5=='Time Taken'):
            print('inhibition_timetaken.png')
    
elif (selected_1=='IC50'):

    selected_2 = st.selectbox('Lütfen değerlendirme türlerinden birini seçiniz', sec2)
    if len(selected_2) == 0:
        st.text('Lütfen listeden birini seçiniz')
    elif (selected_2=='Biyoaktivite'):
        selected_3 = st.selectbox('Lütfen biyoaktivite türlerinden birini seçiniz', sec3)
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
        selected_4 = st.selectbox('Lütfen grafik türlerinden birini seçiniz', sec4)
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
        selected_5 = st.selectbox('Lütfen model değerlendirme seçeneklerinden birini seçiniz', sec5)
        if (selected_5=='RMSE'):
            print('ic50_rmse.png')
        elif (selected_5=='Time Taken'):
            print('ic50_timetaken.png')
# Footer
st.markdown(
    """
    <br>
    <h6><a href="https://iuysal1905-streamlit-leukemia-dnhrmb.streamlit.app/" target="_blank">Lösemi İlaç-İlaç Etkileşim Ağ Grafiği</a></h6>
    <h6>Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.</h6>
    """, unsafe_allow_html=True
    )
