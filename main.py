import streamlit as st

# 앱 기본 설정
st.set_page_config(page_title="MBTI 직업 추천기 🎯", page_icon="🧠", layout="centered")

# 앱 제목
st.title("🌟 MBTI 유형으로 알아보는 잘 어울리는 직업은?! 🌟")
st.caption("나의 성격유형과 찰떡궁합인 직업은 무엇일까요? 🎯 MBTI로 지금 바로 확인해보세요!")

# MBTI 목록
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 직업 추천 및 이모지
mbti_jobs = {
    "INTJ": ("전략가형 🧠", ["데이터 과학자 📊", "AI 개발자 🤖", "정책 분석가 🏛️"]),
    "INTP": ("논리적 사색가 🔬", ["연구원 🧪", "시스템 엔지니어 💻", "이론 물리학자 🌌"]),
    "ENTJ": ("지도자형 👑", ["CEO 🏢", "경영 컨설턴트 📈", "기획 관리자 📋"]),
    "ENTP": ("발명가형 ⚡", ["스타트업 창업자 🚀", "광고 기획자 🎨", "마케터 📢"]),
    "INFJ": ("옹호자형 💫", ["심리상담사 🧘", "사회운동가 ✊", "작가 ✍️"]),
    "INFP": ("중재자형 🎨", ["작가 📚", "애니메이터 🎬", "사회복지사 🤝"]),
    "ENFJ": ("선도자형 ✨", ["교육자 📚", "강연가 🎤", "커뮤니케이션 전문가 📞"]),
    "ENFP": ("활동가형 🌈", ["브랜드 매니저 🧴", "연예인 🎤", "크리에이터 📸"]),
    "ISTJ": ("세상의 관리자 🗂️", ["공무원 🏛️", "회계사 🧾", "데이터 관리자 💽"]),
    "ISFJ": ("수호자형 🛡️", ["간호사 🏥", "초등교사 👩‍🏫", "행정직원 🗃️"]),
    "ESTJ": ("경영자형 💼", ["운영 관리자 📦", "군 장교 🎖️", "현장 감독관 👷"]),
    "ESFJ": ("돌봄 제공자 🤗", ["간호사 💉", "인사담당자 🧑‍💼", "케이터링 매니저 🧁"]),
    "ISTP": ("장인형 🔧", ["기계공 🔩", "응급 구조사 🚑", "보안 전문가 🕶️"]),
    "ISFP": ("예술가형 🎨", ["사진작가 📷", "플로리스트 💐", "패션 디자이너 👗"]),
    "ESTP": ("사업가형 📢", ["세일즈맨 💼", "응급 구조사 🚨", "투자 전문가 💰"]),
    "ESFP": ("연예인형 🎭", ["배우 🎬", "이벤트 플래너 🎉", "SNS 인플루언서 📱"])
}

# 사용자 입력
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택해주세요!", mbti_list)

# 버튼 클릭 시 추천 결과 출력
if st.button("🔍 직업 추천받기!"):
    st.balloons()  # 풍선 효과 🎈
    st.subheader(f"🧬 {selected_mbti} 유형 - {mbti_jobs[selected_mbti][0]}")

    st.markdown("### ✨ 어울리는 직업 추천 리스트:")
    for job in mbti_jobs[selected_mbti][1]:
        st.markdown(f"- {job}")

    st.success("🎯 당신에게 찰떡인 직업들입니다! 도전해볼까요? 🚀")

    # 특별한 눈 효과는 외향형에게만
    if selected_mbti[0] == "E":
        st.snow()
        st.info("❄️ 와우! 외향적인 당신에게 눈처럼 반짝이는 커리어가 기다리고 있어요!")

# 푸터
st.markdown("---")
st.markdown("🚀 만든이: 송쌤의 AI 연구소 | Powered by Streamlit 💻")
