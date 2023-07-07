import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import pip
pip.main(["install", "openpyxl"])

# Set header title
st.title('Simulation Environment for Drug Reuse Studies with XAI')
st.text('Frequency Distribution of Bioactivity Standard Types')
st.image('bioactivite_units.png')
# Define list of selection options and sort alphabetically
sec1 = ['IC50','Inhibition']
sec1.sort()
sec2=['Bioactivity','XAI','Model Performances']
sec3=['Bioactivity Class','LogP','MW','NumHAcceptors','NumHDonors','PIC50']
sec4=['WaterFall','Bar','BeeSwarm','HeatMap','Decision-1','Decision-2','Force','Scatter','Violin','Important Features']
sec5=['RMSE','RE-AE-SE','R-Square','Adjusted R-Square','Time Taken','Confusion Matrix','Other Performance Metrics','Accuracy','F1 Score','ROC-AUC','SMILES Images']

# Implement multiselect dropdown menu for option selection (returns a list)
selected_1 = st.selectbox('Please select one of the standard types', sec1)

# Set info message on initial site load
if len(selected_1) == 0:
    st.text('Please select one from the list')
elif (selected_1=='Inhibition'):
    selected_2 = st.selectbox('Please select one of the evaluation types', sec2)
    if len(selected_2) == 0:
        st.text('Please select one from the list')
    elif (selected_2=='Bioactivity'):
        selected_3 = st.selectbox('Please select one of the bioactivity types', sec3)
        if (selected_3=='Bioactiviy Class'):
            st.image('inhibition_bioactivity_class.png')
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
        selected_4 = st.selectbox('Please select one of the graphic types', sec4)
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
    elif (selected_2=='Model Performances'):
        selected_5 = st.selectbox('Please select one of the model evaluation options', sec5)
        if (selected_5=='RMSE'):
            st.image('inhibition_rmse.png', caption="The most successful model DecisionTreeRegressor")
            st.balloons() 
        elif (selected_5=='RE-AE-SE'):
            st.image('inhbt_rmse2.png', caption="The most successful model GradientBoostedTrees")
        elif (selected_5=='R-Square'):
            st.image('inhibition_r2.png', caption="The most successful model DecisionTreeRegressor")
        elif (selected_5=='Adjusted R-Square'):
            st.image('inhibition_adjusted_rkare.png', caption="The most successful model DecisionTreeRegressor")
        elif (selected_5=='Time Taken'):
            st.image('inhibition_timetaken.png')
        elif (selected_5=='Confusion Matrix'):
            st.image('cfmatrix.png')
        elif (selected_5=='Other Performance Metrics'):
            st.image('diger1.png')
        elif (selected_5=='Accuracy'):
            st.image('accuracy_train.png', caption="DecisionTree has been one of the most successful models")
        elif (selected_5=='F1 Score'):
            st.image('f1score_train.png', caption="DecisionTree has been one of the most successful models")
        elif (selected_5=='ROC-AUC'):
            st.image('roc_auc_train.png',caption="DecisionTree has been one of the most successful models")
        elif (selected_5=='SMILES Images'):
            st.image('smiles.png')
    
elif (selected_1=='IC50'):

    selected_2 = st.selectbox('Please select one of the evaluation types', sec2)
    if len(selected_2) == 0:
        st.text('Please select one from the list')
    elif (selected_2=='Bioactivity'):
        selected_3 = st.selectbox('Please select one of the bioactivity types', sec3)
        if (selected_3=='Bioactivity Class'):
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
        selected_4 = st.selectbox('Please select one of the graphic types', sec4)
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
    elif (selected_2=='Model Performances'):
        selected_5 = st.selectbox('Please select one of the model evaluation options', sec5)
        if (selected_5=='RMSE'):
            st.image('ic50_rmse.png',caption="The most successful DecisionTreeRegressor")
            st.balloons()
        elif (selected_5=='RE-AE-SE'):
            st.image('ic50_rmse2.png', caption="The most successful model GradientBoostedTrees")
        elif (selected_5=='R-Square'):
            st.image('ic50_rkare.png',caption="The most successful DecisionTreeRegressor")
        elif (selected_5=='Adjusted R-Square'):
            st.image('ic50_adjusted_rkare.png',caption="The most successful model DecisionTreeRegressor")
        elif (selected_5=='Time Taken'):
            st.image('ic50_timetaken.png')
        elif (selected_5=='Confusion Matrix'):
            st.image('cfmatrix.png')
            st.write("The number of samples whose true positive class was correctly predicted as positive was 3196, the number of samples whose true negative class was incorrectly predicted as positive was 32, the number of samples whose true positive class was incorrectly predicted as negative was 14 and the number of samples whose true negative class was correctly predicted as negative was 600.")
        elif (selected_5=='Other Performance Metrics'):
            st.image('diger1.png',caption="In general, it is seen that the model has high accuracy, precision and specificity values as a result of the given metrics")
            st.write("ACC Macro is the average of the correct classification rates of all classes and is calculated as 0.98803. ARI - Adjusted Rand Index is a measure of how close the clustering algorithm is to the true classification. The higher the value, the better clustering performance of the model and it is calculated as 0.94022. AUNP is the normalised version of the area under the positive class. The higher the value, the better the model classifies the positive class. It is calculated as 0.9725. AUNU is the normalised version of the area under the negative class. The higher the value, the better the model classifies the negative class and is calculated as 0.9725. F1 Macro - The Macro F1 score is the average of the F1 scores of all classes. The F1 score is expressed as the harmonic mean of the precision and recall metrics and is calculated as 0.97797.  Micro F1 score is an F1 score calculated as the sum of TP, FP and FN values of all classes and is calculated as 0.98803. Hamming Loss - Hamming loss is the ratio of the total number of labels not correctly classified to the total number of labels and is calculated as 0.01197. Kappa is a measure of classification accuracy corrected for the possibility that the model randomly predicts the true classes. The closer the value is to 1, the better classification performance of the model and was found to be 0.95594. Matthews correlation is a balanced measure between correct and incorrect positive/negative classifications. The higher the value, the better classification performance of the model and it was obtained as 0.95608. A1 (Landis & Koch) indicates that the model classifies classes almost perfectly, according to the criterion proposed by Landis and Koch.")
        elif (selected_5=='Accuracy'):
            st.image('accuracy_test.png',caption="The most successful model ExtraTreesRegressor")
        elif (selected_5=='F1 Score'):
            st.image('f1score_test.png',caption="The most successful model ExtraTreesRegressor")
        elif (selected_5=='ROC-AUC'):
            st.image('roc_auc_test.png',caption="The most successful ExtraTreesRegressor")
        elif (selected_5=='SMILES Images'):
            st.image('smiles.png')
# Footer
st.markdown(
    
    """
    <br>
    <h6><a href="https://iuysal1905-streamlit-leukemia-dnhrmb.streamlit.app/" target="_blank">Lösemi İlaç-İlaç Etkileşim Ağ Grafiği</a></h6>
    <h6>Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.</h6>
    """, unsafe_allow_html=True
    )
