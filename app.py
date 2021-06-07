import streamlit as st
import pandas as pd
import numpy as np

st.title('Socring system for predicting positive finding after cranial CT in pediatric TBI')

from PIL import Image
img= Image.open("./FIGURE.jpg")
st.image(img, width=800)

st.header('Road_traffic_machanism')
st.info("Select mechanism( Non-Road traffic machanism =0, Road traffic machanism =2")
Road_traffic_machanism=st.slider("Road_traffic_machanism",0, 2, step=12)

st.header('Age_group')
st.success("Select age group( less than 2 years = 0 scores, 2 year or more =2)" )
Age_group=st.slider("Age_group",0, 2, step=2)

st.header('Motor_weakness')
st.success("Select Motor_weakness ( No =0, Yes =3) ")
Motor_weakness=st.slider("Motor weakness",0, 3, step=3)

st.header('Bleeding_per_ear/nose')
st.info("Select Bleeding per ear/nose ( No =0, Yes =6) ")
Bleeding_per_ear_nose=st.slider("Bleeding_per_ear/nose",0, 6, step=6)

st.header('GCS_score')
st.success("Select Glasgow Coma Scale (GCS) score (GCS 13-15 =0, GCS 9-12 =2, GCS 3-8 =4)")
GCS_score=st.slider("GCS_score",0, 4, step=2)

st.header('Pupillary_reflex')
st.info("Select Pupillary reflex (React BE= 0, Fixed one eye =1, Fied BE =4) ")
Pupillary_reflex=st.slider("Pupillary_reflex",0, 4, step=1)


Total_scores=Age_group+Road_traffic_machanism+Motor_weakness+Bleeding_per_ear_nose+GCS_score+Pupillary_reflex


if Total_scores < 3:
    img1 = Image.open("./Green.jpg")
    st.image(img1, width=200)
else:
    #Total_scores > 3:
        img2= Image.open("./Red.jpg")
        st.image(img2, width=200)

if Total_scores < 3:
    st.warning("GREEN ZONE")
    if st.checkbox("Click here to know more information about GREEN ZONE"):
        st.info("Observation and follow-up. If neurological deterioation development,cranial CT is recommended ")

else:
    #Total_scores > 3:
        st.warning("RED ZONE!!!")
        if st.checkbox("Click here to know more information about RED ZONE!!!"):
            st.info("Cranial CT is recommended")


if st.button("Total score"):
	result=("Total score = "+ str((Total_scores)))
	st.header(result)

