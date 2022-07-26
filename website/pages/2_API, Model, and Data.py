import streamlit as st

# Title

st.markdown("# API, Model, and Data")

# Sidebar

st.sidebar.write('by Lorcan Rae')
st.sidebar.write('My other projects on [github](https://github.com/lorcanrae)!')
st.sidebar.write('See my experiences on [Linkedin](https://linkedin.com/in/lorcanrae)')

# Content

st.markdown('### API:')
st.markdown("""This front end queries an API exposed using GCP products, Docker, and FastAPI. \
This API was created by containerising the package with Docker, pushing \
the package to GCP Container Registry, and exposing the API using \
GCP Cloud Run.""")
st.markdown('''The API can be found [here](https://spaceship-titanic-api-zby5e6zv3q-ew.a.run.app/predict)''')

st.markdown('### Modelling:')
st.markdown('''An ensemble voting classifier composed of a Suport Vector Classifier with a Linear kernel, \
KNN Classifier, and Gradient Boosted Random Forest was used. These models formed part of a \
pipeline that transformed, imputed, encoded, and scaled the data. Hyperparameters \
where optimized using a gridsearch.
The model has a test score of 80.0009 %.''')

st.markdown('### Data:')
st.markdown('''The data used for the model is from the Spaceship Titanic dataset available on kaggle. \
Refer to kaggles [Spaceship Titanic competition](https://www.kaggle.com/competitions/spaceship-titanic) for specifics. \
I have performed an Exploratory Data Analysis of this data set, available on my GH or \
[here](https://www.kaggle.com/code/lorcansamuel/spaceship-titanic-eda-ensemble-using-pipes/notebook).
            ''')
