import streamlit as st
import pandas    as pd

st.set_page_config(
    layout='wide',
    page_title='Spotify Songs'
)

df = pd.read_csv('C:\\Users\\Ariane\\Desktop\\Spotify\\Spotify.csv')
df.set_index('Track', inplace=True) 

artist_photos = {
    'Bon Jovi': 'https://images2.alphacoders.com/217/217180.jpg',
    'Iron Maiden': 'https://cdn.nsite.com.br/imgcache/494/1400x/uploads/494/iron%20maiden.png.webp',
    'Gorillaz': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTWusx8Swyr9JGTgmqpRGlO5CosjjYJvj4s1GhL-g3hQNlOpvA1',
    'AC/DC': 'https://veja.abril.com.br/wp-content/uploads/2020/11/10025-01E-JC-white_group_4559.jpg?quality=90&strip=info&w=1280&h=720&crop=1',
    'Metallica': 'https://facts.net/wp-content/uploads/2023/07/20-facts-about-metallica-1689075581.jpg',
    'Alok': 'https://thebackstage-deezer.com/wp-content/uploads/2023/11/alok-heading-1240x600.jpg',
    'Lady Gaga': 'https://classic.exame.com/wp-content/uploads/2019/02/2019-02-25t085345z_1540329751_hp1ef2p0opki1_rtrmadp_3_awards-oscars-vanityfair.jpg?ims=750x/filters:quality(75):format(webp)',
    'Cyndi Lauper': 'https://www.rbsdirect.com.br/imagesrc/25322874.jpg?w=800&h=535',
    'Ariana Grande': 'https://fmeldorado.com.br/wp-content/uploads/2024/01/ariana-grande-060523-4-329c2a0fc59b44d09608503641788567-300x200.jpg',
}
    
artists = df['Artist'].value_counts().index
artist = st.sidebar.selectbox('**ARTISTA**', artists)
df_filtered = df[df['Artist'] == artist]

albuns= df_filtered['Album'].value_counts().index
album = st.selectbox('**ALBUM**', albuns)

df_filtered2 = df[df['Album'] == album]

col1, col2 = st.columns(2) 
col1.bar_chart(df_filtered2['Stream'])
col2.line_chart(df_filtered2['Danceability'])
    
st.write(artist)

if artist in artist_photos:
    st.image(artist_photos[artist], caption=artist, use_column_width=True)
else:
    st.write("Foto não disponível")
    
    