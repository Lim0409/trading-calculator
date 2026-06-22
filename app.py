import streamlit as st

st.set_page_config(page_title="交易胜率计算器", page_icon="📈")
st.title("📈 交易胜率与盈亏计算器")

wins = st.number_input("盈利次数", min_value=0, value=0)
losses = st.number_input("亏损次数", min_value=0, value=0)
avg_win = st.number_input("平均盈利金额", min_value=0.0, value=100.0)
avg_loss = st.number_input("平均亏损金额", min_value=0.0, value=50.0)

if st.button("开始计算"):
    total = wins + losses
    if total > 0:
        win_rate = (wins / total) * 100
        rr_ratio = avg_win / avg_loss if avg_loss > 0 else 0
        expectancy = ((wins/total) * avg_win) - ((losses/total) * avg_loss)
        
        st.write("---")
        st.metric(label="胜率", value=f"{win_rate:.2f}%")
        st.metric(label="盈亏比", value=f"{rr_ratio:.2f} : 1")
        st.metric(label="每笔期望收益", value=f"{expectancy:.2f}")
    else:
        st.warning("请输入交易次数")
