import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Konfigurasi tampilan
st.set_page_config(page_title="Dashboard Penjualan Zara", layout="wide")

import base64

# Fungsi encode gambar jadi base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Fungsi untuk menampilkan logo di sidebar
def show_logo_in_sidebar(image_path, width=200):
    image_base64 = get_base64_of_bin_file(image_path)
    st.sidebar.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_base64}" width="{width}">
        </div>
        """,
        unsafe_allow_html=True
    )

# Tampilkan logo di sidebar
show_logo_in_sidebar("Logo_Gunadarma.jpg")

# Load Data
df = pd.read_csv("zara_cleaned.csv")


# -------------------------------#
#        Sidebar & Filter       #
# -------------------------------#

# Fungsi untuk mengatur latar belakang gradien sidebar
def set_gradient_beige():
    st.markdown(
        """
        <style>
        /* Background sidebar gradien beige ke putih */
        section[data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #f5eae0, #ffffff);
        }

        /* Warna teks sidebar */
        section[data-testid="stSidebar"] * {
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Panggil fungsi styling sidebar
set_gradient_beige()


# Navigasi halaman di sidebar
page = st.sidebar.selectbox("📂 Navigasi Halaman", ["Tentang Zara", "Analisis Data Penjualan"])

# Sidebar Header
st.sidebar.header("🔎 Filter Data")
# Filter berdasarkan Section
section_options = ["Semua"] + sorted(df["section"].unique())
section_choice = st.sidebar.selectbox("Pilih Section", section_options)

# Filter berdasarkan Status Promo
promo_choice = st.sidebar.selectbox("Status Promo", ["Semua", "Yes", "No"])

# Terapkan filter Section
if section_choice != "Semua":
    df = df[df["section"] == section_choice]

# Terapkan filter Promo
if promo_choice != "Semua":
    df = df[df["Promotion"] == promo_choice]


# ------------------------------------------------------------------------- PAGE 1: TENTANG ZARA ------------------------------------------------------------------------- 
if page == "Tentang Zara":
# Judul halaman
    st.title("Tentang Zara")
    
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("Zara_Logo.svg")

    st.markdown(
        """
        <div style="text-align: justify;">
        Zara adalah merek fashion global yang dikenal dengan konsep fast fashion, yaitu memproduksi dan memasarkan pakaian sesuai tren yang sedang digemari pasar. 
        Didirikan oleh Amancio Ortega pada tahun 1975 di La Coruna, Spanyol, Zara hadir sebagai jawaban atas keterbatasan pilihan fashion bagi konsumen pada masa itu. 
        Kesuksesannya di pasar lokal mendorong ekspansi ke berbagai negara seperti Amerika Serikat, Prancis, dan Meksiko. Hingga kini, Zara telah memiliki lebih dari 2.200 gerai yang tersebar di 96 negara. 
        Di Indonesia, Zara mulai beroperasi pada 18 Agustus 2005 di bawah naungan PT Mitra Adiperkasa Tbk (MAP), perusahaan ritel besar dengan ribuan gerai di seluruh nusantara.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")
    st.write("""
        Berikut adalah beberapa produk populer dari Zara:
        1. **Zara Woman**  
        Zara Woman menawarkan berbagai produk fashion untuk wanita, mulai dari pakaian atasan seperti trench coat, parka, kaus, dan kemeja, hingga bawahan seperti rok dan celana. 
        Koleksi ini juga dilengkapi dengan berbagai aksesori, termasuk sabuk, syal, tas tangan, dan sepatu.
        2. **Zara Men**  
        Zara Men menyediakan beragam busana untuk pria, baik untuk tampilan formal seperti jas dan kemeja, maupun gaya kasual seperti kaus dan celana. 
        Selain itu, tersedia juga berbagai aksesori seperti sepatu, tas, dan perlengkapan lainnya.
        """)

    st.subheader("Data Understanding")
    st.dataframe(df)
    
    st.markdown(
        """
        <div style="text-align: justify;">
        Data yang digunakan untuk membuat analisis penjualan Zara US diambil dari platform open source 
        <a href="https://www.kaggle.com/datasets/xontoloyo/data-penjualan-zara" target="_blank">Kaggle</a> 
        dan dipublikasikan oleh pengguna bernama <i>samnambewan</i>. Dataset ini terdiri dari 251 baris dan 16 kolom, dengan 13 kolom bertipe data object, 2 kolom bertipe int64, dan 1 kolom bertipe float64. 
        Setiap kolom dalam dataset ini memiliki arti dan peran masing-masing dalam analisis.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write("")
    st.markdown("""
        <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        </style>

        <table>
        <thead>
        <tr>
            <th>Variabel</th>
            <th>Tipe Data</th>
            <th>Keterangan</th>
        </tr>
        </thead>
        <tbody>
        <tr><td>Product ID</td><td>int64</td><td>Identitas unik untuk membedakan setiap produk.</td></tr>
        <tr><td>Product Position</td><td>object</td><td>Letak produk dalam katalog atau toko, seperti Aisle, Front of Store, End-Cap.</td></tr>
        <tr><td>Promotion</td><td>object</td><td>Status apakah produk sedang dalam promosi atau tidak.</td></tr>
        <tr><td>Product Category</td><td>object</td><td>Kategori produk seperti pakaian, aksesori, atau sepatu.</td></tr>
        <tr><td>Seasonal</td><td>object</td><td>Menunjukkan apakah produk termasuk koleksi musiman.</td></tr>
        <tr><td>Sales Volume</td><td>int64</td><td>Jumlah produk yang berhasil terjual.</td></tr>
        <tr><td>Brand</td><td>object</td><td>Merek dari produk tersebut.</td></tr>
        <tr><td>URL</td><td>object</td><td>Tautan produk (jika dijual secara online).</td></tr>
        <tr><td>SKU</td><td>object</td><td>Kode unik untuk identifikasi produk dalam inventaris.</td></tr>
        <tr><td>Name</td><td>object</td><td>Nama dari produk.</td></tr>
        <tr><td>Description</td><td>object</td><td>Deskripsi singkat tentang produk.</td></tr>
        <tr><td>Price</td><td>float64</td><td>Harga produk.</td></tr>
        <tr><td>Currency</td><td>object</td><td>Mata uang dari harga produk.</td></tr>
        <tr><td>Scraped_at</td><td>object</td><td>Waktu data diambil (misalnya melalui web scraping).</td></tr>
        <tr><td>Terms</td><td>object</td><td>Jenis produk yang dijual (jaket, sweater, t-shirt, jeans, shoes).</td></tr>
        <tr><td>Section</td><td>object</td><td>Kategori toko tempat produk dijual (wanita, pria).</td></tr>
        </tbody>
        </table>
        """, 
        unsafe_allow_html=True)



# ------------------------------------------------------------------------- PAGE 1: TENTANG ZARA ------------------------------------------------------------------------- 
elif page == "Analisis Data Penjualan":
    # Judul halaman
    st.title("Analisis Penjualan Produk Zara US")
# -------------------------------------------------------------------- Function revenue n sales
    # Fungsi hitung total revenue
    def total_revenue(df):
        return (df['price'] * df['Sales Volume']).sum()

    # Fungsi hitung total sales
    def total_sales(df):
        return df['Sales Volume'].sum()

    # Hitung hasilnya dari dataframe yang sudah difilter
    total_sales_value = total_sales(df)
    total_revenue_value = total_revenue(df)

    # Tampilkan metrik di layout 2 kolom
    st.markdown("## 📊 Ringkasan Data")
    col1, col2 = st.columns(2)
    col1.metric("Total Sales", f"{int(total_sales_value):,}")
    col2.metric("Total Revenue", f"USD {total_revenue_value:,.2f}")

    # -------------------------------------------------------------------- Tampilkan data
    # Tampilkan data awal
    st.subheader("Data Sample")
    st.dataframe(df)

    # -------------------------------------------------------------------- Function best n worst product
    # Grafik 1: Produk terlaris
    st.subheader("🎯 Produk dengan Penjualan Tertinggi & Terendah")

    # Hitung total penjualan per produk
    produk_terjual = df.groupby("name")["Sales Volume"].sum()

    # Top 10 Produk Terlaris
    top_produk = produk_terjual.sort_values(ascending=False).head(10)

    # Bottom 10 Produk dengan Penjualan Terendah (non-zero)
    bottom_produk = produk_terjual[produk_terjual > 0].sort_values(ascending=True).head(10)

    # Layout dua kolom
    col1, col2 = st.columns(2)

    # Visualisasi Produk Terlaris
    with col1:
        st.markdown("#### 🔝 Produk Terlaris")
        fig_top, ax_top = plt.subplots(figsize=(8, 6))
        sns.barplot(y=top_produk.index, x=top_produk.values, palette="Blues_r", ax=ax_top)
        ax_top.set_xlabel("Jumlah Terjual")
        ax_top.set_ylabel("Nama Produk")
        st.pyplot(fig_top)

    # Visualisasi Produk Terburuk
    with col2:
        st.markdown("#### 🔻 Produk Paling Sedikit Terjual")
        fig_bottom, ax_bottom = plt.subplots(figsize=(8, 6))
        sns.barplot(y=bottom_produk.index, x=bottom_produk.values, palette="Reds_r", ax=ax_bottom)
        ax_bottom.set_xlabel("Jumlah Terjual")
        ax_bottom.set_ylabel("Nama Produk")
        st.pyplot(fig_bottom)

    # Kesimpulan
    with st.expander("Insight"):
        st.write("""
        Produk dengan volume penjualan tertinggi, mencerminkan banyaknya minat pasar terhadap kategori produk tertentu. 
        Sebaliknya, beberapa produk dengan volume penjualan rendah dapat menjadi indikator perlunya evaluasi desain, strategi penempatan, atau efektivitas promosi pada produk tersebut.
        """)

    # -------------------------------------------------------------------- Function distribusi harga
    # Grafik 2: Distribusi Harga
    st.subheader("Distribusi Harga Produk")
    fig2, ax2 = plt.subplots(figsize=(16, 8))
    sns.histplot(df["price"], bins=30, kde=True, color="orange", ax=ax2)
    ax2.set_xlabel("Harga (USD)")
    st.pyplot(fig2)
    st.markdown(
        """
        <div style="background-color:#fff3cd; padding:10px; border-left:6px solid #ffa500; border-radius:5px;">
        📌 <b>Insight:</b> Sebagian besar produk Zara berada pada kisaran <b>harga rendah hingga menengah</b>. 
        Hal ini menunjukkan bahwa Zara menawarkan produk yang <b>terjangkau dan menarik bagi banyak konsumen</b>, 
        meskipun terdapat sedikit produk dengan harga tinggi.
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------------------------- function harga vs penjualan
    # # Grafik 3: Harga vs Penjualan
    # st.subheader("Harga vs Penjualan")
    # fig3, ax3 = plt.subplots(figsize=(16, 8))
    # sns.scatterplot(data=df, x="price", y="Sales Volume", hue="section", ax=ax3)
    # ax3.set_xlabel("Harga")
    # ax3.set_ylabel("Jumlah Terjual")
    # st.pyplot(fig3)

    # -------------------------------------------------------------------- function penjualan berdasarkan section
    # Buat 2 tab: Pria & Wanita
    st.subheader('Penjualan Berdasarkan Section')
    tab1, tab2 = st.tabs(["Men", "Women"])

    # ---------- Tab 1: Produk Pria
    with tab1:
        men_terms = df[df['section'] == 'MAN']['terms'].value_counts().reset_index()
        men_terms.columns = ['terms', 'count']
        
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        sns.barplot(data=men_terms, x='terms', y='count', palette='Blues_d', ax=ax1)
        ax1.set_title("Distribusi Terms - Produk Pria")
        ax1.set_ylabel("Jumlah Produk")
        ax1.set_xlabel("Terms")
        ax1.tick_params(axis='x', rotation=45)
        st.pyplot(fig1)

    # ---------- Tab 2: Produk Wanita
    with tab2:
        women_terms = df[df['section'] == 'WOMAN']['terms'].value_counts().reset_index()
        women_terms.columns = ['terms', 'count']
        
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        sns.barplot(data=women_terms, x='terms', y='count', palette='Purples', ax=ax2)
        ax2.set_title("Distribusi Terms - Produk Wanita")
        ax2.set_ylabel("Jumlah Produk")
        ax2.set_xlabel("Terms")
        ax2.tick_params(axis='x', rotation=45)
        st.pyplot(fig2)


    # -------------------------------------------------------------------- function pengaruh strategi 
    st.subheader("Pengaruh Strategi Terhadap Penjualan")
    tab1, tab2 = st.tabs(["Promosi", "Posisi"])

    # ---------- Tab 1: strategi promosi
    with tab1:
        # Hitung total penjualan berdasarkan status promosi
        promo_sales = df.groupby("Promotion")["Sales Volume"].sum().reset_index()

        # Buat layout dua kolom dengan ukuran yang lebih seimbang
        col1, col2 = st.columns([2, 3])  # pie chart sedikit lebih lebar

        with col1:
            fig5, ax5 = plt.subplots(figsize=(4, 4))  # Ukuran lebih kompak
            colors = ['#FF9999', '#66B3FF']
            wedges, texts, autotexts = ax5.pie(
                promo_sales["Sales Volume"],
                labels=promo_sales["Promotion"],
                autopct='%1.1f%%',
                startangle=140,
                colors=colors,
                textprops={'fontsize': 11}
            )
            ax5.axis('equal')
            st.pyplot(fig5)

        with col2:
            # Paragraf penjelasan
            st.markdown(
                """
                <div style='display: flex; flex-direction: column; justify-content: center; height: 100%; padding: 20px 10px; font-size: 16px;'>
                    <p>Produk yang mendapatkan promosi ternyata tidak menghasilkan penjualan yang lebih tinggi dibandingkan produk tanpa promosi.</p>
                    <p>Oleh karena itu, diperlukan evaluasi terhadap strategi dan pelaksanaan promosi yang telah dilakukan.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Tabel ringkasan jumlah penjualan per kategori promosi
            st.markdown("**Jumlah Penjualan per Kategori Promosi:**")
            st.table(promo_sales.rename(columns={"Promotion": "Status Promosi", "Sales Volume": "Jumlah Terjual"}))



    # ---------- Tab 2: strategi posisi
    with tab2:
        position_sales = df.groupby("Product Position")["Sales Volume"].mean().sort_values(ascending=False).reset_index()
        fig6, ax6 = plt.subplots(figsize=(12, 6))
        sns.barplot(data=position_sales, x="Product Position", y="Sales Volume", palette="Spectral", ax=ax6)
        # Tambahkan label nilai rata-rata
        for i, row in position_sales.iterrows():
            ax6.text(i, row["Sales Volume"] + 0.5, f'{row["Sales Volume"]:.2f}', ha='center', fontweight='bold')
        # Label dan judul sumbu
        ax6.set_xlabel("Posisi Produk di Halaman")
        ax6.set_ylabel("Rata-rata Jumlah Produk Terjual")
        ax6.set_title("Rata-rata Penjualan Berdasarkan Posisi Produk")
        st.pyplot(fig6)

        st.markdown(
            """
            <div style="background-color:#fff3cd; padding:10px; border-left:6px solid #ffa500; border-radius:5px;">
            📌 <b>Insight:</b> Produk yang ditempatkan di bagian depan toko (Front Of Store) memiliki rata-rata penjualan tertinggi dibandingkan posisi lainnya, yakni sekitar 1.873 unit. 
                    Posisi lorong tengah (Aisle) menyusul dengan rata-rata 1.829 unit, sementara posisi ujung rak (End-Cap) mencatat penjualan terendah sebesar 1.778 unit. 
                    Hal ini menunjukkan bahwa penempatan produk di bagian depan toko lebih efektif dalam menarik perhatian konsumen dan mendorong penjualan.
            </div>
            """,
            unsafe_allow_html=True
        )

    # -------------------------------------------------------------------- function pengaruh strategi 
    st.subheader("Pengaruh Efektivitas Promosi")
    tab1, tab2= st.tabs(["Posisi", "Section"])

    # ---------- Tab 3: hubungan strategi promosi dan posisi
    with tab1:
        st.subheader("Efektivitas Promosi di Tiap Posisi Produk")

        promo_pos = df.groupby(["Product Position", "Promotion"])["Sales Volume"].mean().reset_index()

        fig8, ax8 = plt.subplots(figsize=(12, 6))
        sns.barplot(data=promo_pos, x="Product Position", y="Sales Volume", hue="Promotion", ax=ax8, palette="pastel")
        ax8.set_title("Rata-rata Penjualan Produk Promosi vs Non-promosi di Tiap Posisi")
        ax8.set_ylabel("Rata-rata Terjual")
        ax8.set_xlabel("Posisi Produk")
        st.pyplot(fig8)

        st.markdown(
            """
            <div style="background-color:#fff3cd; padding:10px; border-left:6px solid #ffa500; border-radius:5px;">
            📌 <b>Insight:</b> Produk tanpa promosi (No) cenderung memiliki rata-rata penjualan yang lebih tinggi dibandingkan produk dengan promosi (Yes) di hampir semua posisi (Aisle, End-Cap, dan Front of Store).
            Hal ini mengindikasikan bahwa strategi penempatan produk lebih berpengaruh terhadap penjualan dibandingkan pemberian promosi. Produk yang ditempatkan dengan strategi yang tepat (seperti di Front of Store) tetap bisa menarik minat beli yang tinggi walaupun tidak dipromosikan.
            Evaluasi terhadap efektivitas promosi perlu dilakukan, karena terlihat bahwa promosi belum memberikan dampak signifikan pada peningkatan rata-rata penjualan, bahkan bisa jadi justru tidak efisien.
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------- Tab 4: hubungan strategi promosi dan section
    with tab2:
        st.subheader("Efektivitas Promosi per Section")

        heat_data = df.pivot_table(index="section", columns="Promotion", values="Sales Volume", aggfunc="mean")
        fig5, ax5 = plt.subplots(figsize=(16, 8))
        sns.heatmap(heat_data, annot=True, fmt=".1f", cmap="PuBu", ax=ax5)
        ax5.set_title("Rata-rata Penjualan Produk Promosi per Section")
        st.pyplot(fig5)

        st.markdown(
            """
            <div style="background-color:#fff3cd; padding:10px; border-left:6px solid #ffa500; border-radius:5px;">
            📌 <b>Insight:</b> Promosi terbukti efektif meningkatkan penjualan pada produk wanita, dengan rata-rata penjualan naik signifikan saat ada promosi. 
            Sebaliknya, produk pria justru mengalami sedikit penurunan penjualan saat dipromosikan. 
            Hal ini menunjukkan bahwa promosi lebih berdampak positif pada produk wanita, sementara strategi promosi untuk produk pria perlu dievaluasi agar lebih tepat sasaran.
            </div>
            """,
            unsafe_allow_html=True
        )



    st.markdown("---")
    st.caption("Dibuat dengan menggunakan Streamlit oleh [Elisa Wulansari]")