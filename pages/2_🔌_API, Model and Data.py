import streamlit as st
import os

# Config

st.set_page_config(layout='wide')

# Title

st.markdown("# API, Model and Data 🔌")

# Sidebar

st.sidebar.write('Created by Lorcan Rae')
st.sidebar.write('[Front End repo](https://github.com/lorcanrae/spaceship-titanic-web)\
    \n[Package, Model and EDA repo](https://github.com/lorcanrae/spaceship-titanic)\
    \nView my other projects on [github](https://github.com/lorcanrae)!')

st.sidebar.write('See my experiences on [Linkedin](https://linkedin.com/in/lorcanrae)!')

st.sidebar.write('Created and deployed with:')

sbcol1, sbcol2, sbcol3 = st.sidebar.columns([1, 1, 1])

with sbcol1:
    st.image('https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg', width=60)
    st.image('https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg', width=60)

with sbcol2:
    st.image('https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg', width=60)
    st.image('https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg', width=70)

with sbcol3:
    st.image('https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg', width=60)
    st.image('https://streamlit.io/images/brand/streamlit-mark-color.png', width=65)

# Content

api_url = 'https://spaceship-titanic-api-zby5e6zv3q-ew.a.run.app'

st.markdown('### API:')
st.markdown("""This API was created by containerising a python package with Docker, pushing
            the package to GCP Container Registry, and exposing the API using
            GCP Cloud Run. FastAPI and Uvicorn where used to build the api.
            \nThe API base endpoint can be found [here]({api_url}). Prediction can be accessed at the /predict endpoint.""")
st.markdown(f"""Generally, people who are older and spend more on Room Service, Food, Shopping, Spa and VR are not transported (10,000+ per category).""")

st.markdown('### Modelling:')
st.markdown("""An ensemble voting classifier composed of a Suport Vector Classifier with a RBF kernel,
KNN Classifier, and Gradient Boosted Random Forest was used. The model was positioned at the end of a
pipeline that transformed, imputed, encoded, and scaled the data. Hyperparameters
where optimized using a gridsearch.
The model has an accuracy of 80.0009% on the test data set.""")
st.markdown('This model was trained in the cloud using GCP AI Platform - for my own practice.')

st.markdown('### Data:')
st.markdown("""The data used for the model is from the Spaceship Titanic dataset available on kaggle.
Refer to kaggles [Spaceship Titanic competition](https://www.kaggle.com/competitions/spaceship-titanic) for specifics.
I have performed an Exploratory Data Analysis of this data set, including Univariate and Bivariate anayslse,
available on my [github](https://github.com/lorcanrae/spaceship-titanic/tree/master/notebooks) or my
[kaggle profile](https://www.kaggle.com/code/lorcansamuel/spaceship-titanic-eda-ensemble-using-pipes/notebook).
            """)
