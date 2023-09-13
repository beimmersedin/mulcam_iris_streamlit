# -*- coding:utf-8 -*-

import streamlit as st
import joblib
import os
import numpy as np

def run_ml_app():
    st.subheader("머신러닝 페이지")

    # layout
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("수치 입력해주세요!")
        sepal_length = st.select_slider("Sepal Length", options = np.arange(1, 11))
        sepal_width = st.select_slider("Sepal Widgth", options = np.arange(1, 11))
        petal_length = st.select_slider("Petal Length", options = np.arange(1, 11))
        petal_width = st.select_slider("Petal Widgth", options = np.arange(1, 11))

        sample_list = [sepal_length, sepal_width, petal_length, petal_width]
        st.write(sample_list)

