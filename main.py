import streamlit as st
#from dotenv import load_dotenv
import openai
#import os
import random
import time

# 환경변수 로드 및 OpenAI API 키 설정
#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")

st.title('Life-Science Chat AI')

# 사용자 입력 받기
user_input = st.text_input('궁금한 내용을 물어보세요:', '')

# 랜덤 문구 선택
random_phrases = ["**많고 많은 사람 중에 그대 한 사람** - 2020년 대학수학능력평가 필적확인란", "**그대만큼 사랑스러운 사람을 본 일이 없다** - 2019년 대학수학능력평가 필적확인란"]
random_phrase = random.choice(random_phrases)

# OpenAI API를 사용하여 대화 응답 생성
if user_input:
    system_message = "넌 한국어를 사용하는 생명과학자야, 그리고 상대는 생명과학자들이니까, 추가설명 없이 그냥 답만 줘."
    
    # 스피너와 랜덤 문구를 함께 표시
    with st.spinner(f'답변을 준비중입니다...\n\n{random_phrase}'):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input}
            ],
            max_tokens=2000
        ).choices[0].message.content
        time.sleep(2)  # 스피너와 문구를 충분히 볼 수 있도록 일부러 지연시킴
    
    st.markdown(response, unsafe_allow_html=True)

# 기부 버튼 및 계좌 정보를 마지막에 배치
if st.button('새싹 과학자를 위한 기부', key='donate'):
    st.write('가상계좌 정보: XXXX-XXXX-XXXX')
    st.write('당신의 기부 덕분에 한국의 미래는 밝아졌습니다.')
