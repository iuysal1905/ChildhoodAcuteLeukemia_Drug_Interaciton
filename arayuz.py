import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import pip
pip.main(["install", "openpyxl"])

# Set header title
st.title('XAI ile İlaç Yeniden Kullanım Çalışmaları için Benzetim Ortamı')
st.text('Biyoaktivite Standart Türleri Frekans Dağılımı')
st.image('bioactivite_units.png')
# Define list of selection options and sort alphabetically
sec1 = ['IC50','Inhibition']
sec1.sort()
sec2=['Biyoaktivite','XAI','Model Performansları']
sec3=['Biyoaktivite Sınıfı','LogP','MW','NumHAcceptors','NumHDonors','PIC50']
sec4=['WaterFall','Bar','BeeSwarm','HeatMap','Decision-1','Decision-2','Force','Scatter','Violin','Important Features']
sec5=['RMSE','R-Kare','Adjusted R-Kare','Time Taken','Confusion Matrix','Diğer Performans Metrikleri','Accuracy','F1 Score','ROC-AUC','Smiles Gösterimleri']

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
        elif (selected_4=='Decision-1'):
            st.image('inhibition_decision_0.png')
        elif (selected_4=='Decision-2'):
            st.image('inhibition_decision.png')
        elif (selected_4=='Force'):
            st.image('inhibition_force_0.png')
        elif (selected_4=='Scatter'):
            st.image('inhibition_scatter.png')
        elif (selected_4=='Violin'):
            st.image('inhibition_violin.png')
        elif (selected_4=='Important Features'):
            st.image('inhibition_importantfeatures.png')
    elif (selected_2=='Model Performansları'):
        selected_5 = st.selectbox('Lütfen model değerlendirme seçeneklerinden birini seçiniz', sec5)
        if (selected_5=='RMSE'):
            st.image('inhibition_rmse2.png',caption="En başarılı model Gradient Boosted Trees")
            st.image('inhibition_rmse.png', caption="En başarılı model DecisionTreeRegressor")
            st.balloons() 
        elif (selected_5=='R-Kare'):
            st.image('inhibition_r2.png', caption="En başarılı model DecisionTreeRegressor")
        elif (selected_5=='Adjusted R-Kare'):
            st.image('inhibition_adjusted_rkare.png', caption="En başarılı model DecisionTreeRegressor")
        elif (selected_5=='Time Taken'):
            st.image('inhibition_timetaken.png')
        elif (selected_5=='Confusion Matrix'):
            st.image('cfmatrix.png')
        elif (selected_5=='Diğer Performans Metrikleri'):
            st.image('diger1.png')
        elif (selected_5=='Accuracy'):
            st.image('accuracy_train.png', caption="DecisionTree en başarılı modellerden birisi olmuştur")
        elif (selected_5=='F1 Score'):
            st.image('f1score_train.png', caption="DecisionTree en başarılı modellerden birisi olmuştur")
        elif (selected_5=='ROC-AUC'):
            st.image('roc_auc_train.png',caption="DecisionTree en başarılı modellerden birisi olmuştur")
        elif (selected_5=='Smiles Gösterimleri'):
            st.image('smiles.png')
    
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
        elif (selected_4=='Decision-1'):
            st.image('ic50_decision_0.png')
        elif (selected_4=='Decision-2'):
            st.image('ic50_decision.png')
        elif (selected_4=='Force'):
            st.image('ic50_force_0.png')
        elif (selected_4=='Scatter'):
            st.image('ic50_scatter.png')
        elif (selected_4=='Violin'):
            st.image('ic50_violin.png')
        elif (selected_4=='Important Features'):
            st.image('ic50_importantfeatures.png')
    elif (selected_2=='Model Performansları'):
        selected_5 = st.selectbox('Lütfen model değerlendirme seçeneklerinden birini seçiniz', sec5)
        if (selected_5=='RMSE'):
            st.image('ic50_rmse_2.png',caption="En başarılı model Gradient Boosted Trees")
            st.image('ic50_rmse.png',caption="En başarılı model DecisionTreeRegressor")
            st.balloons()
        elif (selected_5=='R-Kare'):
            st.image('ic50_rkare.png',caption="En başarılı model DecisionTreeRegressor")
        elif (selected_5=='Adjusted R-Kare'):
            st.image('ic50_adjusted_rkare.png',caption="En başarılı model DecisionTreeRegressor")
        elif (selected_5=='Time Taken'):
            st.image('ic50_timetaken.png')
        elif (selected_5=='Confusion Matrix'):
            st.image('cfmatrix.png')
            st.write("Gerçek pozitif sınıfı doğru bir şekilde pozitif olarak tahmin edilen örnek sayısı 3196, gerçek negatif sınıfı yanlış bir şekilde pozitif olarak tahmin edilen örnek sayısı 32, gerçek pozitif sınıfı yanlış bir şekilde negatif olarak tahmin edilen örnek sayısı 14 ve gerçek negatif sınıfı doğru bir şekilde negatif olarak tahmin edilen örnek sayısı 600 olarak elde edilmiştir.")
        elif (selected_5=='Diğer Performans Metrikleri'):
            st.image('diger1.png',caption="Genel olarak, verilen metrikler sonucunda modelin yüksek doğruluk, hassasiyet ve özgünlük değerlerine sahip olduğu görülmektedir")
            st.write("ACC Macro, tüm sınıfların doğru sınıflandırma oranlarının ortalamasıdır ve 0.98803 olarak hesaplanmıştır. ARI - Ayarlanmış Rand Endeksi, kümeleme algoritmasının gerçek sınıflandırmaya ne kadar yakın olduğunu gösteren bir ölçüttür. Değer ne kadar yüksekse, modelin daha iyi bir kümeleme performansı olduğunu göstermektedir ve 0.94022 olarak hesaplanmıştır. AUNP, pozitif sınıfın altında kalan alanın normalleştirilmiş versiyonudur. Değer ne kadar yüksekse, modelin pozitif sınıfı iyi bir şekilde sınıflandırdığını göstermektedir. 0.9725 olarak hesaplanmıştır. AUNU, negatif sınıfın altında kalan alanın normalleştirilmiş versiyonudur. Değer ne kadar yüksekse, modelin negatif sınıfı iyi bir şekilde sınıflandırdığını göstermektedir ve 0.9725 olarak hesaplanmıştır. F1 Macro - Makro F1 skoru, tüm sınıfların F1 skorlarının ortalamasıdır. F1 skoru, hassasiyet (precision) ve duyarlılık (recall) metriklerinin harmonik ortalaması olarak ifade edilmektedir ve 0.97797 olarak hesaplanmıştır.  Mikro F1 skoru, tüm sınıfların TP, FP ve FN değerlerinin toplamı üzerinden hesaplanan bir F1 skorudur ve 0.98803 olarak hesaplanmıştır. Hamming Loss - Hamming kaybı, doğru sınıflandırılmayan etiketlerin toplam sayısının, toplam etiket sayısına oranıdır ve 0.01197 olarak hesaplanmıştır. Kappa, modelin gerçek sınıfları rastgele tahmin etme olasılığına karşı düzeltilmiş bir sınıflandırma doğruluğu ölçüsüdür. Değer 1'e ne kadar yakınsa, modelin daha iyi bir sınıflandırma performansı olduğunu göstermektedir ve 0.95594 olarak bulunmuştur. Matthews korelasyonu, doğru ve yanlış pozitif/negatif sınıflandırmalar arasındaki dengeli bir ölçüdür. Değer ne kadar yüksekse, modelin daha iyi bir sınıflandırma performansı olduğunu göstermektedir ve 0.95608 olarak elde edilmiştir. A1 (Landis & Koch), Landis ve Koch tarafından önerilen ölçüte göre, modelin sınıfları neredeyse mükemmel bir şekilde sınıflandırdığını göstermektedir.")
        elif (selected_5=='Accuracy'):
            st.image('accuracy_test.png',caption="En başarılı model ExtraTreesRegressor")
        elif (selected_5=='F1 Score'):
            st.image('f1score_test.png',caption="En başarılı model ExtraTreesRegressor")
        elif (selected_5=='ROC-AUC'):
            st.image('roc_auc_test.png',caption="En başarılı model ExtraTreesRegressor")
        elif (selected_5=='Smiles Gösterimleri'):
            st.image('smiles.png')
# Footer
st.markdown(
    
    """
    <br>
    <h6><a href="https://iuysal1905-streamlit-leukemia-dnhrmb.streamlit.app/" target="_blank">Lösemi İlaç-İlaç Etkileşim Ağ Grafiği</a></h6>
    <h6>Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.</h6>
    """, unsafe_allow_html=True
    )
