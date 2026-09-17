import streamlit as st
import pandas as pd

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính Lãi Tiết Kiệm",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰 Công Cụ Tính Lãi Tiết Kiệm")
st.write(
    "So sánh tiền lãi thu được giữa **Lãi đơn** và **Lãi kép**."
)

# =========================
# NHẬP DỮ LIỆU
# =========================
col1, col2 = st.columns(2)

with col1:
    so_tien_gui = st.number_input(
        "Số tiền gửi (VNĐ):",
        min_value=1000,
        value=100_000_000,
        step=1_000_000,
        format="%d"
    )

    lai_suat_nam = st.number_input(
        "Lãi suất (%/năm):",
        min_value=0.1,
        max_value=20.0,
        value=6.0,
        step=0.1,
        format="%.1f"
    )

with col2:
    so_thang_gui = st.number_input(
        "Số tháng gửi:",
        min_value=1,
        max_value=360,
        value=12,
        step=1
    )

    tan_suat_nhap_lai = st.selectbox(
        "Tần suất nhập lãi (cho lãi kép):",
        options=[
            "Hàng tháng",
            "Hàng quý",
            "Hàng năm"
        ]
    )

# =========================
# QUY ĐỔI TẦN SUẤT NHẬP LÃI
# =========================
map_tan_suat = {
    "Hàng tháng": 12,
    "Hàng quý": 4,
    "Hàng năm": 1
}

n = map_tan_suat[tan_suat_nhap_lai]

# =========================
# QUY ĐỔI THỜI GIAN SANG NĂM
# =========================
t_nam = so_thang_gui / 12

# =========================
# TÍNH LÃI ĐƠN
# Công thức:
# I = P × r × t
# =========================
r = lai_suat_nam / 100

lai_don = so_tien_gui * r * t_nam
tong_tien_lai_don = so_tien_gui + lai_don

# =========================
# TÍNH LÃI KÉP
# Công thức:
# A = P × (1 + r/n)^(
