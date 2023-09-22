import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

from similarity_type import *
from similarity_search import *
from similarity_find_name import *

import numpy as np
import pandas as pd
import streamlit.components.v1 as html
import time



# 페이지 선택을 위한 버튼을 사이드바에 추가합니다.
with st.sidebar:
    choose = option_menu("나만의 위스키", ["컨텐츠","취향대로 위스키", "비슷한 위스키 찾기"],
                         icons=["emoji-kiss","bookmark-heart", "search-heart"],
                         menu_icon="menu-up", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "#FAFAFA"},
                             "icon": {"color": "black", "font-size": "25px"},
                             "nav-link": {"font-size": "16px", "color": "black", "text-align": "left", "margin": "0px",
                                          "--hover-color": "#eee"},
                             "nav-link-selected": {"background-color": "#EDF6F9"},
                         })
# "Welcome" 페이지
if choose == "컨텐츠":

    # 제목
    image = Image.open("main_img_1.jpg")
    st.image(image)
    
    
    # 이미지를 불러옵니다.
    image2 = Image.open("main_img_2.jpg")

    # 이미지를 좌우로 정렬하여 페이지의 너비에 맞게 표시합니다.
    st.image(image2)

    # 두 번째 이미지를 불러옵니다.
    image3 = Image.open("main_img_3.jpg")

    # 두 번째 이미지를 좌우로 정렬하여 페이지의 너비에 맞게 표시합니다.
    st.image(image3)

    # 간격 조정
    st.subheader("")

    # 세 번째 이미지를 불러옵니다.
    image4 = Image.open("main_img_4.jpg")

    # 세 번째 이미지를 좌우로 정렬하여 페이지의 너비에 맞게 표시합니다.
    st.image(image4)

# "Whiskey Recommend" 페이지
if choose == "취향대로 위스키":
  
    # 이미지를 불러옵니다.
    image5 = Image.open("main_img_5.jpg")

    # 이미지를 좌우로 정렬하여 페이지의 너비에 맞게 표시합니다.
    st.image(image5)

     # 간격 조정
    st.subheader("")
    
    types = {'위스키 타입을 선택해주세요': None,
            '싱글 몰트 위스키': '싱글몰트', 
            '블렌디드 위스키' : '블렌디드', 
            '블렌디드 몰트 위스키' : '블렌디드 몰트',
            '버번 & 라이 위스키' : '버번/라이'}
    
    selected_type = st.selectbox("**위스키 타입 선택**", types.keys())
    
    # 간격 조정
    st.subheader("")  
    
    # 사용자로부터 최소가격과 최대가격을 입력 받음
    min_price = st.text_input("**최소 가격 입력 (최대 8자)**", max_chars=8)
    max_price = st.text_input("**최대 가격 입력 (최대 8자)**", max_chars=8)

    # 입력값이 비어있지 않은 경우에만 처리
    if min_price and max_price:
        min_price = int(min_price)
        max_price = int(max_price)
    # 입력된 최소가격과 최대가격으로 필요한 처리 수행
        st.write(f"가격 범위는 {int(min_price)}원부터 {int(max_price)}원 까지 입니다")


    # 간격 조정
    st.subheader("")

    # 이미지를 불러옵니다.
    image6 = Image.open("main_img_6.jpg")

    # 이미지를 좌우로 정렬하여 페이지의 너비에 맞게 표시합니다.
    st.image(image6)
    
    image7 = Image.open("main_img_7.jpg")

    # 이미지를 좌우로 정렬하여 페이지의 너비에 맞게 표시합니다.
    st.image(image7)

     # 간격 조정
    st.subheader("")
    
    # 'aroma를 선택' 제목 추가
    st.write("**향 선택 (1 ~ 3 개)**")

    # 체크 박스를 가로로 8개 나열
    col1_aroma, col2_aroma, col3_aroma, col4_aroma = st.columns(4)
    user_cats_list = []
    # 각 열(column)에 4개씩 체크 박스 추가
    with col1_aroma:
        option1_aroma = st.checkbox('**나무**', key="aroma_option1")
        if option1_aroma:
            user_cats_list.append('aroma_나무향')
        option2_aroma = st.checkbox('**잔류액**', key="aroma_option2")
        if option2_aroma:
            user_cats_list.append('aroma_잔류액향')
            
    with col2_aroma:
        option3_aroma = st.checkbox('**와인**', key="aroma_option3")
        if option3_aroma:
            user_cats_list.append('aroma_와인향')
        option4_aroma = st.checkbox('**피트**', key="aroma_option4")
        if option4_aroma:
            user_cats_list.append('aroma_피트향')       

    with col3_aroma:
        option5_aroma = st.checkbox('**곡물**', key="aroma_option5")
        if option5_aroma:
            user_cats_list.append('aroma_곡물향')  
        option6_aroma = st.checkbox('**꽃향기**', key="aroma_option6")
        if option6_aroma:
            user_cats_list.append('aroma_꽃향기')  

    with col4_aroma:
        option7_aroma = st.checkbox('**과일**', key="aroma_option7")
        if option7_aroma:
            user_cats_list.append('aroma_과일향')  
        option8_aroma = st.checkbox('**유황**', key="aroma_option8")
        if option8_aroma:
            user_cats_list.append('aroma_유황')  

    # 'taste를 선택' 제목 추가
    st.write("**맛 선택 (1 ~ 3 개)**")

    # 체크 박스를 가로로 8개 나열
    col1_taste, col2_taste, col3_taste, col4_taste = st.columns(4)

    # 각 열(column)에 4개씩 체크 박스 추가
    with col1_taste:
        option1_taste = st.checkbox('**나무**', key="taste_option1")
        if option1_taste:
            user_cats_list.append('taste_나무향')  
        option2_taste = st.checkbox('**잔류액**', key="taste_option2")
        if option2_taste:
            user_cats_list.append('taste_잔류액향')  

    with col2_taste:
        option3_taste = st.checkbox('**와인**', key="taste_option3")
        if option3_taste:
            user_cats_list.append('taste_와인향')  
        option4_taste = st.checkbox('**피트**', key="taste_option4")
        if option4_taste:
            user_cats_list.append('taste_피트향')  

    with col3_taste:
        option5_taste = st.checkbox('**곡물**', key="taste_option5")
        if option5_taste:
            user_cats_list.append('taste_곡물향')  
        option6_taste = st.checkbox('**꽃향기**', key="taste_option6")
        if option6_taste:
            user_cats_list.append('taste_꽃향기')  

    with col4_taste:
        option7_taste = st.checkbox('**과일**', key="taste_option7")
        if option7_taste:
            user_cats_list.append('taste_과일향')  
        option8_taste = st.checkbox('**유황**', key="taste_option8")
        if option8_taste:
            user_cats_list.append('taste_유황')  

    # 'finish를 선택' 제목 추가
    st.write("**여운 선택 (1 ~ 3 개)**")

    # 체크 박스를 가로로 8개 나열
    col1_finish, col2_finish, col3_finish, col4_finish = st.columns(4)

    # 각 열(column)에 4개씩 체크 박스 추가
    with col1_finish:
        option1_finish = st.checkbox('**나무**', key="finish_option1")
        if option1_finish:
            user_cats_list.append('finish_유황')  
        option2_finish = st.checkbox('**잔류액**', key="finish_option2")
        if option2_finish:
            user_cats_list.append('finish_잔류액향')  

    with col2_finish:
        option3_finish = st.checkbox('**와인**', key="finish_option3")
        if option3_finish:
            user_cats_list.append('finish_와인향')  
        option4_finish = st.checkbox('**피트**', key="finish_option4")
        if option4_finish:
            user_cats_list.append('finish_피트향')  

    with col3_finish:
        option5_finish = st.checkbox('**곡물**', key="finish_option5")
        if option5_finish:
            user_cats_list.append('finish_곡물향')  
        option6_finish = st.checkbox('**꽃향기**', key="finish_option6")
        if option6_finish:
            user_cats_list.append('finish_꽃향기')  

    with col4_finish:
        option7_finish = st.checkbox('**과일**', key="finish_option7")
        if option7_finish:
            user_cats_list.append('finish_과일향')  
        option8_finish = st.checkbox('**유황**', key="finish_option8")
        if option8_finish:
            user_cats_list.append('finish_유황')  

    # 간격 조정
    st.subheader("")
    
    csv_file_path = r'./data/whisky_preprocessing.csv'

    # 유사도를 위한 데이터 전처리
    preprocessor = WhiskeySimilarityChecker(csv_file_path)
    preprocessor.preprocessing()

    user_name = 'User01' 
    show_list = ['nameKor','가격','타입','용량','도수','국가']
    
    Result = False
    
    if (types[selected_type] is not None) & (type(min_price) == int) & (type(max_price) == int) & (len(user_cats_list) > 0):
        Result = True
    else:
        Result = False

    # 출력개수 선택
    list_lengths = [
        5, 10, 15, 20, 25, 30
    ]
    
    list_length = st.selectbox("**출력 개수 선택**", list_lengths)
    
    # "선택 완료" 버튼을 누르면 스피너가 나타나도록 설정
    if st.button("**선택 완료**"):
        with st.spinner("**위스키 추천 중입니다...**"):
            # 시뮬레이션을 위한 대기 시간, 실제로는 데이터 처리 시간에 맞게 조절
            time.sleep(3)  
            
        if Result == True:
            st.success('**위스키 찾기가 완료되었습니다**', icon="✅")     
            user_types = [types[selected_type]]
            user_price = (min_price, max_price) # (min_price , max_price)
            similar_shows = preprocessor.find_similar_shows(user_name, user_types, user_price, user_cats_list, top_n=list_length)
            similar_shows.rename(columns = {'Whisky Name': '위스키 이름','type':'타입',
                                'price':'가격','capacity':'용량', 'country':'국가','alcohol':'도수'},inplace = True)
            
            st.write(similar_shows[show_list])

            
        elif Result == False:
            st.write('### :blue[값을 채워주세요!]')
            
if choose == "비슷한 위스키 찾기":
  
    # 이미지를 불러옵니다.
    image5 = Image.open("main_img_5.jpg")

    # 이미지를 좌우로 정렬하여 페이지의 너비에 맞게 표시합니다.
    st.image(image5)

     # 간격 조정
    st.subheader("")
    
    csv_file_path = r'./data/whisky_preprocessing.csv'
    
    input_whiskey = st.text_input('**취향인 위스키 이름을 검색해주세요 (영어)**: ') 
    findprocessor = WhiskeyFindProcessor(csv_file_path)
    sim_names = findprocessor.result_list(input_whiskey)
    
    time.sleep(3)
    whis_name = st.selectbox("**해당하는 위스키 이름 선택**", sim_names)
    
     
     # 간격 조정
    st.subheader("")
    
    types = {'위스키 타입을 선택해주세요': None,
            '싱글 몰트 위스키': '싱글몰트', 
            '블렌디드 위스키' : '블렌디드', 
            '블렌디드 몰트 위스키' : '블렌디드 몰트',
            '버번 & 라이 위스키' : '버번/라이'}
    
    selected_type = st.selectbox("**위스키 타입 선택**", types.keys())
    
    # 간격 조정
    st.subheader("")  
    
    # 사용자로부터 최소가격과 최대가격을 입력 받음
    min_price = st.text_input("**최소 가격 입력 (최대 8자)**", max_chars=8)
    max_price = st.text_input("**최대 가격 입력 (최대 8자)**", max_chars=8)

    # 입력값이 비어있지 않은 경우에만 처리
    if min_price and max_price:
        min_price = int(min_price)
        max_price = int(max_price)
    # 입력된 최소가격과 최대가격으로 필요한 처리 수행
        st.write(f"가격 범위는 {int(min_price)}원부터 {int(max_price)}원 까지 입니다")

    

    # 간격 조정
    st.subheader("")
    

    # 유사도를 위한 데이터 전처리
    preprocessor = WhiskeySimilaritySearcher(csv_file_path)
    preprocessor.preprocessing()

    show_list = ['nameKor','가격','타입','용량','도수','국가']
    
    Result = False
    
    if (types[selected_type] is not None) & (type(min_price) == int) & (type(max_price) == int):
        Result = True
    else:
        Result = False

    list_lengths = [
        5, 10, 15, 20, 25, 30
    ]
    
    list_length = st.selectbox("**출력 개수 선택**", list_lengths)
    
    
    # "선택 완료" 버튼을 누르면 스피너가 나타나도록 설정
    if st.button("**선택 완료**"):
        with st.spinner("**위스키 추천 중입니다...**"):
            # 시뮬레이션을 위한 대기 시간, 실제로는 데이터 처리 시간에 맞게 조절
            time.sleep(3)  
            
        if Result == True:
            st.success('**위스키 찾기가 완료되었습니다**', icon="✅")     
            user_types = [types[selected_type]]
            user_price = (min_price, max_price) # (min_price , max_price)
            similar_shows = preprocessor.find_similar_shows(whis_name, user_types, user_price, top_n=list_length)
            similar_shows.rename(columns = {'Whisky Name': '위스키 이름','type':'타입',
                                'price':'가격','capacity':'용량', 'country':'국가','alcohol':'도수'},inplace = True)
            
            st.write(similar_shows[show_list])
            
            
        elif Result == False:
            st.write('### :blue[값을 채워주세요!]')    
