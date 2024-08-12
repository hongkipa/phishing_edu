import streamlit as st
import re
from datetime import datetime

def validate_resident_number(number):
    pattern = re.compile(r'^\d{6}-\d{7}$')
    return bool(pattern.match(number))

def get_rank_suffix(rank):
    if rank % 10 == 1 and rank != 11:
        return "st"
    elif rank % 10 == 2 and rank != 12:
        return "nd"
    elif rank % 10 == 3 and rank != 13:
        return "rd"
    else:
        return "th"

st.set_page_config(page_title="신한신용정보 이벤트 참여", page_icon="🔒")

# 두 개의 컬럼 생성
col1, col2 = st.columns([3, 1])  # 3:1 비율로 너비 설정

# 첫 번째 컬럼에 제목 추가
with col1:
    st.title("신한신용정보 이벤트 참여")

# 두 번째 컬럼에 이미지 추가
with col2:
    st.image("shinhanci.png", width=100)  # 이미지 파일명과 크기를 적절히 조정하세요

st.write("신한신용정보 이벤트 참여 페이지 입니다.")

with st.form("info_form"):
    name = st.text_input("이름")
    contact = st.text_input("연락처")
    resident_number = st.text_input("주민등록번호 (예: 123456-1234567)")
    password = st.text_input("비밀번호", type="password")
    email = st.text_input("이메일 주소")
    
    submitted = st.form_submit_button("제출하기")
    
    if submitted:
        if not validate_resident_number(resident_number):
            st.error("올바른 형식의 주민등록번호를 입력해주세요.")
        else:
            if 'submissions' not in st.session_state:
                st.session_state.submissions = []
            
            st.session_state.submissions.append({
                'name': name,
                'contact': contact,
                'resident_number': resident_number,
                'email': email,
                'submission_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.warning("경고: 이것은 피싱 방지 훈련용 모의 페이지입니다. 실제 상황이었다면 귀하의 주민등록번호를 포함한 중요한 개인정보가 유출될 뻔했습니다. 절대로 이런 정보를 온라인 형식으로 제출하지 마세요.")
            st.success("귀하의 정보가 저장되었습니다. (훈련용)")

# 제출된 정보 표시
if 'submissions' in st.session_state and st.session_state.submissions:
    st.subheader("제출된 정보")
    for rank, submission in enumerate(reversed(st.session_state.submissions), 1):
        rank_display = f"{rank}{get_rank_suffix(rank)}"
        st.write(f"{rank_display} - 이름: {submission['name']}, 연락처: {submission['contact']}, 이메일: {submission['email']}, 제출 시간: {submission['submission_time']}")