import streamlit as st

def render_discord_page():
    # 페이지 제목 및 설명
    st.write("# 투자고수가 되고싶나요?")
    st.subheader("그렇다면 잘 찾아오셨습니다! 여기는 시스템 트레이딩을 연구하고 공유하는 터틀 트레이딩 커뮤니티 입니다!🎉")
    st.write("""
    이 커뮤니티는 다양한 트레이딩 전략, 수익 인증, 기술적/기본적 분석 등을 자유롭게 공유하는 공간입니다.
    다양한 관점을 배우고, 더 나은 투자 결정을 내릴 수 있는 환경을 제공합니다.
    투기가 아닌 진정한 투자와 자산관리에 대해 관심있는분들을 모집합니다!
    """)

    # Discord 초대 버튼
    st.markdown(
        """
        ### 지금 가입하세요!
        Discord 커뮤니티에 가입하려면 아래 버튼을 클릭하세요.
        """
    )

    st.markdown(
        """
        <a href="https://discord.gg/873btJH9Kc" target="_blank">
            <button style="background-color: #7289da; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer;">
                디스코드 커뮤니티 가입하기 🚀
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    # 가입 가이드
    st.markdown("---")
    st.header("가입 가이드")
    st.write("""
    1. 위 버튼을 클릭하여 Discord로 이동합니다.
    2. Discord 계정이 없다면 회원가입을 진행합니다.
    3. 커뮤니티 규칙을 읽고 '동의'를 클릭하세요.
    4. 다양한 채널에 참여하여 질문하고, 의견을 공유하세요!
    """)

    # FAQ 섹션
    st.markdown("---")
    st.header("자주 묻는 질문 (FAQ)")
    
    with st.expander("Discord 계정을 만들려면 어떻게 해야 하나요?"):
        st.write("""
        Discord 앱 또는 웹사이트에서 회원가입 버튼을 클릭한 후 이메일과 비밀번호를 설정하세요.
        사용자명을 입력하고 계정을 인증하면 준비 완료입니다!
        """)

    with st.expander("어떤 채널이 있나요?"):
        st.write("""
        - **📈 전략 공유**: 다양한 트레이딩 전략을 공유합니다.
        - **💰 수익 인증**: 투자 성과를 공유하고 서로를 응원합니다.
        - **🛠️ 기술적 분석**: 차트와 지표에 대한 심층 토론.
        - **📖 기본적 분석**: 경제 데이터와 기업 정보 분석.
        """)

    with st.expander("디스코드 커뮤니티는 무료인가요?"):
        st.write("""
        네! 커뮤니티 가입과 참여는 100% 무료입니다.
        """)

    with st.expander("가입했는데 질문이 있어요."):
        st.write("""
        디스코드의 **도움 요청** 채널에 질문을 남겨주세요. 관리자와 다른 멤버들이 도움을 드릴 것입니다.
        """)

    # 추가 정보 섹션
    st.markdown("---")
    st.header("추가 정보")
    st.write("""
    Discord 커뮤니티는 여러분의 투자 여정을 돕기 위해 만들어졌습니다.
    참여를 통해 서로 배움의 기회를 나누고, 더 나은 투자자가 되어보세요!
    """)

if __name__ == "__main__":
    render_discord_page()
