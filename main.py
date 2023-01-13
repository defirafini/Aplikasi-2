import streamlit as st

page_bg_img = '''
<style>
[data-testid='stAppViewContainer'] {
background-color: #f2e4fa;
opacity: 0.7;
background-image: radial-gradient(#5c2f78 0.5px, #f2e4fa 0.5px);
background-size: 10px 10px;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Achemtools🧪')
st.markdown('''
Barang ada di tangan kapanpun kamu butuhkan!''')

title = st.text_input('Alamat E-mail'),('Alamat E-mail Kamu')

title = st.text_input('Nama'),('Nama Kamu')

kelas= st.selectbox(
    'Kelas',
    ('1A', '1B', '1C', '1D', '1E', '1F', '1G', '2A', '2B', '2C', '2D', '2E', '2F', '2G', '3A', '3B', '3C', '3D', '3E', '3F', '3G'))

tempat= st.selectbox(
    'Tempat Pengambilan',
    ('Gedung B', 'Gedung C', 'Gedung F', 'Gedung G'))

waktu= st.number_input('Waktu Pengambilan Pukul')

st.header('Produk')

st.subheader('1. Tabung Reaksi')

tab1, tab2, tab3 = st.tabs(['Tabung Reaksi Biasa', 'Tabung Reaksi Ulir', 'Tabung Reaksi Besar'])

with tab1:
    st.subheader('Tabung Reaksi')
    st.write('Tabung reaksi dengan merk Iwaki lebih menahan panas dibandingkan dengan merk lain.')
    st.write('Rp.15.000')

with tab2:
    st.subheader('Tabung Reaksi Ulir')
    st.write('Tabung reaksi Ulir dengan merk iwaki dengan menggunakan tutup yang aman.')
    st.write('Rp.30.000')

with tab3:
    st.subheader('Tabung Reaksi Besar')
    st.write('Tabung reaksi besar dengan merk iwaki dengan menggunakan tutup yang aman.')
    st.write('Rp.65.000')

st.subheader('2. Pipet')

tab1, tab2, tab3 = st.tabs(['Pipet Tetes', 'Pipet Volume', 'Pipet Mohr'])

with tab1:
    st.subheader('Pipet Tetes')
    st.write('Pipet tetes dengan kaca berkualitas dan panjang 17cm.')
    st.write('Rp.3.000')


with tab2:
    st.subheader('Pipet Volume')
    st.write('Pipet volume dengan kaca berkualitas tahan terhadap panas dan bahan kimia.')
    st.write('Rp.35.000')


with tab3:
    st.subheader('Pipet Mohr')
    st.write('Pipet mohr dengan pengukuran yang lebih akurat dapat menahan panas dan bahan kimia.')
    st.write('Rp.45.000')

st.subheader('3. Cawan')

tab1, tab2, tab3 = st.tabs(['Cawan petri', 'Cawan Porselein', 'Cawan Cursible'])

with tab1:
    st.subheader('Cawan Petri')
    st.write('Cawan Petri dengan sodalime glass memiliki ukuran 90x15mm.')
    st.write('Rp.25.000')

with tab2:
    st.subheader('Cawan Porselein')
    st.write('Cawan porselein dengan merk Iwaki lebih menahan panas dibandingkan dengan merk lain.')
    st.write('Rp.15.000')

with tab3:
    st.subheader('Cawan Cursible')
    st.write('Cawan Cursible dengan tutup terbuat dari porselein tahan panas dan memiliki kapasitas 50mL.')
    st.write('Rp.20.000')  

st.subheader('4. Bulb')

tab1, tab2, tab3 = st.tabs(['Rubber Bulb', 'Tensi Bulb', 'Bulb Pipet Tetes'])

with tab1:
    st.subheader('Rubber Bulb')
    st.write('Bulb dengan kualitas karet yang baik untuk dipasangkan pada pipet volume dan pipet mohr.')
    st.write('Rp.40.000')
    
with tab2:
    st.subheader('Tensi Bulb')
    st.write('Bulb dengan kualitas karet yang baik dan digunakan secara manual.')
    st.write('Rp.20.000')

with tab3:
    st.subheader('Bulb Pipet Tetes')
    st.write('Bulb pipet tetes dengan kualitas karet yang baik dan variasi warna yang cantik.')
    genre=st.radio(
        'Warna bulb yang diinginkan:',
        ('Merah', 'Kuning', 'Biru'))
    st.write('Rp.2.000')

st.subheader('5. Gelas Ukur')
st.write('Gelas ukur terbuat dari kaca pyrex borocylicate dan menahan panas dengan baik.')
ukuran = st.selectbox(
    'Ukuran dan Harga Gelas Ukur',
    ('10mL-Rp.30.000','25mL-Rp.35.000','50mL-Rp.40.000','100mL-Rp.50.000','250mL-Rp.90.000'))
    
st.subheader('6. Gelas Piala')
st.write('Gelas piala terbuat dari kaca pyrex borocylicate dan menahan panas dengan baik dibandingkan dengan merk lain.')
ukuran = st.selectbox(
    'Ukuran dan Harga Gelas Piala',
    ('50mL-Rp.22.000','100mL-Rp.25.000','250mL-Rp.30.000','500mL-Rp.40.000'))

st.subheader('7. Batang Pengaduk')
st.write('Batang pengaduk dengan bahan kaca berkualitas, diameter 6mm dan panjang 60cm.')
st.write('Rp.6.000')

st.subheader('8. Alu dan Mortar')
st.write('Alu dan Mortar terbuat dari porselein tebal ukuran 16cm untuk menghaluskan sampel.')
st.write('Rp.60.000')

st.subheader('9. Corong')
st.write('Corong terbuat dari bahan borocylicate berkualitas memiliki kapasitas 50mL.')
st.write('Rp.25.000')

st.subheader('10. Erlenmeyer')
st.write('Erlenmeyer')
ukuran = st.selectbox(
    'Ukuran dan Harga Erlenmeyer',
    ('50mL-Rp.30.000','100mL-Rp.35.000','125mL-Rp.37.000','250mL-Rp.40.000','300mL-Rp.45.000','500mL-Rp.62.000'))

st.header('Cek Pesanan')

st.write("Tanggal Pengambilan Pesananmu")
st.date_input('Pilih tanggal')

metodepembayaran = st.selectbox(
    'Metode Pembayaran',
    ('Transfer Bank','E-Wallet','Bayar di tempat'))

opsipengiriman = st.selectbox(
    'Opsi Pengiriman',
    ('JNT','Sicepat','Wahana','Ambil di tempat'))

st.write('Total Pesanan')

title = st.text_input('Barang dan Jumlah Pesanan'),('Nama Barang')

if st.button('Select'):
    st.write('Pesanan Kamu Akan di Proses')