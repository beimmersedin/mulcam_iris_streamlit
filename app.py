# -*- coding:utf-8 -*-

import streamlit as st 
import numpy as np
import pandas as pd 

from eda_app import run_eda_app
from ml_app import run_ml_app
# from graph_1 import run_graph_1

def main():
    
    st.markdown("Hello World")

    # menu = ["Home", "탐색적 자료 분석", "머신러닝", "About", "그래프_1"]
    menu = ["Home", "탐색적 자료 분석", "머신러닝", "About"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "탐색적 자료 분석":
        # st.subheader("탐색적 자료 분석")
        run_eda_app() ## 팀원1 담당
    elif choice == "머신러닝":
        # st.subheader("머신러닝") ## 팀원2 담당
        run_ml_app()
    elif choice == "About":
        st.subheader("About") ## 팀원3 담당
    # elif choice == "그래프_1":
    #     run_graph_1()
    else:
        pass


if __name__ == "__main__":
    main()