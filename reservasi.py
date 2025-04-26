import streamlit as st

# Setup
st.set_page_config(page_title="GO AWARDS 2025", layout="wide")

TOTAL_KURSI = 500
if 'kursi' not in st.session_state:
    st.session_state.kursi = ["kosong"] * TOTAL_KURSI
if 'sudah_pilih' not in st.session_state:
    st.session_state.sudah_pilih = False

st.markdown("<h1 style='text-align: center;'>🎉 GO AWARDS 2025 - Reservasi Kursi 🎉</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input kode pembayaran
kode = st.text_input("Masukkan kode pembayaran (contoh: LUNAS)")

if kode == "LUNAS":
    st.success("Kode pembayaran valid! Silakan pilih kursi.")
    
    if not st.session_state.sudah_pilih:
        pilihan = st.selectbox("Pilih nomor kursi yang masih kosong:", 
                               [i+1 for i, k in enumerate(st.session_state.kursi) if k == "kosong"])

        if st.button("Reservasi Kursi"):
            st.session_state.kursi[pilihan-1] = "terisi"
            st.session_state.sudah_pilih = True
            st.success(f"Kursi nomor {pilihan} berhasil dipesan!")
    else:
        st.info("Anda sudah memilih kursi. Terima kasih.")
else:
    if kode != "":
        st.error("Kode pembayaran salah. Hubungi panitia jika ada masalah.")
st.subheader("Daftar Kursi Kosong:")
st.write(kursi_kosong)