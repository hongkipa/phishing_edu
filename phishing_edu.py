import streamlit as st
import re
from datetime import datetime

def validate_resident_number(number):
    pattern = re.compile(r'^\d{6}-\d{7}$')
    return bool(pattern.match(number))

def save_submission(name, contact, resident_number, email):
    if 'submissions' not in st.session_state:
        st.session_state.submissions = []
    
    st.session_state.submissions.append({
        '이름': name,
        '연락처': contact,
        '주민등록번호': resident_number,
        'email': email,
        'submission_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def get_rank_suffix(rank):
    if rank % 10 == 1 and rank != 11:
        return "st"
    elif rank % 10 == 2 and rank != 12:
        return "nd"
    elif rank % 10 == 3 and rank != 13:
        return "rd"
    else:
        return "th"

def main():
    st.set_page_config(page_title="이벤트 참여하세요", page_icon="🔒")
    
    st.title("이벤트 참여")
    
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
                save_submission(name, contact, resident_number, email)
                st.warning("경고: 이것은 피싱 방지 훈련용 모의 페이지입니다. 실제 상황이었다면 귀하의 주민등록번호를 포함한 중요한 개인정보가 유출될 뻔했습니다. 절대로 이런 정보를 온라인 형식으로 제출하지 마세요.")
                st.success("귀하의 정보가 저장되었습니다. (훈련용)")

    # 제출된 정보 표시
    if 'submissions' in st.session_state and st.session_state.submissions:
        st.subheader("제출된 정보")
        for rank, submission in enumerate(reversed(st.session_state.submissions), 1):
            rank_display = f"{rank}{get_rank_suffix(rank)}"
            st.write(f"{rank_display} - 이름: {submission['name']}, 연락처: {submission['contact']}, 이메일: {submission['email']}, 제출 시간: {submission['submission_time']}")

if __name__ == "__main__":
    main()