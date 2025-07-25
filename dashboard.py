import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import os
import base64
from streamlit_option_menu import option_menu

# Konfigurasi tampilan
st.set_page_config(page_title="Dashboard Penjualan Zara", layout="wide")


def show_logo_in_sidebar(image_path, width=250):
    if not os.path.exists(image_path):
        st.sidebar.error(f"Logo file not found: {image_path}")
        return
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
        st.sidebar.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/svg+xml;base64,{encoded_string}" width="{width}" />
            </div>
            """,
            unsafe_allow_html=True
        )

show_logo_in_sidebar("Zara_Logo.svg")


# Load Data
df = pd.read_csv("zara_cleaned.csv")


# -------------------------------#
#           Sidebar              #
# -------------------------------#

# Fungsi untuk mengatur latar belakang gradien sidebar
def set_backgorund():
    st.markdown(
        """
        <style>
        /* Sidebar background solid color */
        section[data-testid="stSidebar"] {
            background-color: #fef7f1;
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
set_backgorund()


# Navigasi halaman di sidebar
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)  # Jarak ke bawah agar lebih elegan

    page = option_menu(
        menu_title="Menu Halaman",
        options=["Tentang Zara", "Analisis Data Penjualan"],
        icons=["info-circle", "bar-chart-line"],
        default_index=0,
        menu_icon="folder",
        styles={
            "container": {
                "padding": "24px 8px",
                "background-color": "#faece6",  # Warna sidebar keseluruhan
                "border-radius": "12px",
            },
            "menu-title":{ 
                "font-size": "20px",
                "color": "#5c3c3c"
            },
            "icon": {
                "color": "#c44569",
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "17px",
                "color": "#444444",
                "margin": "6px 0px",
                "border-radius": "8px",
                "padding": "10px 15px",
                "transition": "all 0.3s ease-in-out",
                "--hover-color": "#fdeee9"
            },
            "nav-link-selected": {
                "background-color": "#fddede",
                "font-weight": "600",
                "color": "#000000",
                "border-radius": "8px",
            }

        }
    )

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
        Data yang digunakan untuk membuat analisis penjualan Zara ini diambil dari platform open source 
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



# ------------------------------------------------------------------------- PAGE 2: ANALISIS DATA PENJUALAN ------------------------------------------------------------------------- 
elif page == "Analisis Data Penjualan":
    st.title("Analisis Penjualan Produk Zara")
#-------------------------------------------------------------- FILTER
    # FILTERS - hanya muncul di halaman Analisis
    st.sidebar.header("🔎 Filter Data")
    section_options = ["Semua"] + sorted(df["section"].unique())
    section_choice = st.sidebar.selectbox("Pilih Section", section_options)

    promo_choice = st.sidebar.selectbox("Status Promo", ["Semua", "Yes", "No"])

    # Terapkan filter Section
    if section_choice != "Semua":
        df = df[df["section"] == section_choice]

    # Terapkan filter Promo
    if promo_choice != "Semua":
        df = df[df["Promotion"] == promo_choice]


    # --- Styling tambahan untuk membuat tampilannya rapi ---
    st.markdown("""
    <style>
    /* Container filter section */
    .filter-box {
        background-color: #fdf1ec;  /* Blush-pink lembut */
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        margin-bottom: 20px;
    }

    /* Judul dan label */
    .filter-box h3, .filter-box label {
        color: #3d2b2b;
        font-weight: 600;
    }

    /* Custom selectbox */
    .stSelectbox > div {
        background-color: #fff9f7;
        border: 1px solid #eac9c1;
        border-radius: 8px;
        padding: 8px 10px;
        box-shadow: 0 1px 5px rgba(0,0,0,0.02);
    }

    .stSelectbox label {
        font-size: 14px;
        margin-bottom: 4px;
        display: block;
    }

    /* Jarak antar elemen */
    .stSelectbox {
        margin-bottom: 16px;
    }
    </style>
""", unsafe_allow_html=True)

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
        sns.barplot(y=top_produk.index, x=top_produk.values, palette="Set3", ax=ax_top)
        ax_top.set_xlabel("Jumlah Terjual")
        ax_top.set_ylabel("Nama Produk")
        st.pyplot(fig_top)

    # Visualisasi Produk Terburuk
    with col2:
        st.markdown("#### 🔻 Produk Paling Sedikit Terjual")
        fig_bottom, ax_bottom = plt.subplots(figsize=(8, 6))
        sns.barplot(y=bottom_produk.index, x=bottom_produk.values, palette="Set3", ax=ax_bottom)
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
    fig2, ax2 = plt.subplots(figsize=(10,5))
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

    #---------------------------------------------------------------------------- Distribusi Volume Penjualan
    # Subjudul utama
    st.subheader('Distribusi Total Penjualan Produk Zara')

    # Buat tab
    tab1, tab2= st.tabs(["Kategori Produk (terms)", "Kategori Konsumen (section)"])

    # Tab 1: Berdasarkan 'terms'
    with tab1:
        # Group by total sales per terms
        terms_sales = df.groupby("terms")["Sales Volume"].sum().reset_index().sort_values(by="Sales Volume", ascending=False)

        # Streamlit layout
        st.subheader("📊 Total Penjualan berdasarkan Kategori Produk (terms)")

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 5))
        colors = sns.color_palette("Set2", n_colors=len(terms_sales))

        # Horizontal bar chart
        sns.barplot(
            data=terms_sales,
            x="Sales Volume",
            y="terms",
            palette=colors,
            ax=ax
        )

        # Custom legend
        legend_labels = [
            Patch(facecolor=colors[i], label=f'{terms_sales["terms"].iloc[i]}: {terms_sales["Sales Volume"].iloc[i]:,.0f}')
            for i in range(len(terms_sales))
        ]
        ax.legend(handles=legend_labels, title="Sales Volume", loc="lower right", frameon=True)

        # Labels dan title
        ax.set_title("Total Penjualan berdasarkan Kategori Produk (terms)")
        ax.set_xlabel("Jumlah Produk Terjual")
        ax.set_ylabel("Kategori Produk (terms)")

        st.pyplot(fig)

        st.markdown(
            """
            <div style="background-color:#fff3cd; padding:10px; border-left:6px solid #ffa500; border-radius:5px;">
            📌 <b>Insight:</b> Kategori teratas yang memiliki volume penjualan tertinggi bisa menjadi indikasi bahwa produk tersebut sangat diminati oleh pelanggan. 
            Hal ini bisa menjadi fokus utama untuk strategi promosi atau pengembangan produk baru.
            </div>
            """,
            unsafe_allow_html=True
        )

    # Tab 2: Berdasarkan 'section' (Kategori Konsumen)
    with tab2:
        # Group berdasarkan section (Kategori Konsumen)
        section_sales = df.groupby("section")["Sales Volume"].sum().reset_index().sort_values(by="Sales Volume", ascending=False)

        st.markdown("### 🧍‍♀️🧍 Total Penjualan berdasarkan Kategori Konsumen(Section)")

        # Plot
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        colors = sns.color_palette("Set2", n_colors=len(section_sales))

        sns.barplot(
            data=section_sales,
            x="Sales Volume",
            y="section",
            palette=colors,
            ax=ax2
        )

        # Tambahkan legenda manual
        legend_labels = [
            Patch(facecolor=colors[i], label=f'{section_sales["section"].iloc[i]}: {section_sales["Sales Volume"].iloc[i]:,.0f}')
            for i in range(len(section_sales))
        ]
        ax2.legend(handles=legend_labels, title="Sales Volume", loc="lower right", frameon=True)

        # Label sumbu dan judul
        ax2.set_xlabel("Jumlah Produk Terjual")
        ax2.set_ylabel("Kategori Konsumen (Gender)")
        ax2.set_title("Total Penjualan berdasarkan Kategori Konsumen (Section)")

        st.pyplot(fig2)

        st.markdown(
            """
            <div style="background-color:#fff3cd; padding:10px; border-left:6px solid #ffa500; border-radius:5px;">
            📌 <b>Insight:</b> Berdasarkan grafik total penjualan berdasarkan gender (section), terlihat bahwa produk untuk pria (MAN) memiliki jumlah penjualan yang jauh lebih tinggi dibandingkan produk untuk wanita (WOMAN). 
            Penjualan produk pria mencapai sekitar 394.361 unit, sedangkan produk wanita hanya sekitar 63.374 unit. Oleh karena itu, perlu dilakukan evaluasi dan pengembangan strategi penjualan khusus untuk produk wanita, 
            agar dapat meningkatkan daya tarik dan mendorong peningkatan angka penjualan pada kategori tersebut.
            </div>
            """,
            unsafe_allow_html=True
        )

    # -------------------------------------------------------------------- function penjualan berdasarkan section
    # Buat 2 tab: Pria & Wanita
    st.subheader('Distribusi Kategori Produk(terms) Berdasarkan Kategori Konsumen(section)')
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
    
    st.markdown(
            """
            <div style="background-color:#fff3cd; padding:10px; border-left:6px solid #ffa500; border-radius:5px;">
            📌 <b>Insight:</b> Konsumen pria cenderung lebih banyak membeli produk yang lebih bervariasi, sementara konsumen wanita cenderung hanya membeli satu varian produk saja 
            </div>
            """,
            unsafe_allow_html=True
        )
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
        fig6, ax6 = plt.subplots(figsize=(10, 5))
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

    # ---------- Tab 1: hubungan strategi promosi dan posisi
    with tab1:
        st.subheader("Efektivitas Promosi di Tiap Posisi Produk")

        promo_pos = df.groupby(["Product Position", "Promotion"])["Sales Volume"].mean().reset_index()

        fig8, ax8 = plt.subplots(figsize=(10, 5))
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

    # ---------- Tab 2: hubungan strategi promosi dan section
    with tab2:
        st.subheader("Efektivitas Promosi per Section")

        heat_data = df.pivot_table(index="section", columns="Promotion", values="Sales Volume", aggfunc="mean")
        fig5, ax5 = plt.subplots(figsize=(8, 4))
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