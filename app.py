# -*- coding:utf-8 -*-
import streamlit as st
from eda_app import run_eda_app

def main():
    
    st.markdown("Hello World")
    menu = ["Home", "탐색적 자료분석", "머신러닝", "About"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "탐색적 자료분석":
        run_eda_app()
    elif choice == "머신러닝":
        pass
    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
