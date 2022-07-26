import streamlit as st

import requests

# st.set_page_config(layout='wide')

# Title Text

st.markdown("# Spaceship Titanic")
st.markdown("### What could go wrong?!")

# Sidebar

st.sidebar.write('by Lorcan Rae')
st.sidebar.write('My other projects on [github](https://github.com/lorcanrae)!')
st.sidebar.write('See my experiences on [Linkedin](https://linkedin.com/in/lorcanrae)')

# Blurb

st.markdown('''In the year 2912 the intersteller passenger liner _Spaceship Titanic_ \
    has set out on its maiden voyage transporting almost 13,000 passengers from our solarsystem \
    to three newly habitable exoplanets nearby.''')

st.markdown('''On route to the first destination, the unwary _Spaceship Titanic_ has collided with \
    a spacetime anomaly hidden within a dust cloud. Like it's namesake from 1000 years \
    ealier, it has met a similar fate.''')

# Input Parameters

st.markdown('### See if you would have survived!')
st.markdown('##### Input Parameters:')

homeplanet_options = ['Earth', 'Europo', 'Mars']
HomePlanet = st.selectbox('What is your HomeWorld?', homeplanet_options)

cryosleep_selector = st.selectbox('Are you going into Cryosleep?',
                                ['Yes', 'No'])
CryoSleep = True if cryosleep_selector == 'Yes' else False

cabin_deck_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T']
Cabin_Deck = st.selectbox('What deck are you staying on?',
                        cabin_deck_options)

Cabin_Level = st.number_input('What level have you been assigned to? (1 - 1894)',
                            min_value=1, max_value=1894, step=1)

cabin_side_selector = st.selectbox(
    'Are you travelling on Port or Starboard sode of the ship',
    ['Port', 'Starboard']
    )
Cabin_Side = 'S' if cabin_side_selector == 'Starboard' else 'P'

Destination=st.selectbox('What planet are you travelling to?',
                        ['TRAPPIST-1e', 'PSO J318.5-22', '55 Cancri e'])

vip_selector = st.selectbox('Are you a VIP', ['No', 'Yes'])
VIP=False if vip_selector == "No" else True

Age=st.number_input('What is your age?', min_value=0, max_value=100, value=27)

RoomService = st.number_input('How much will you spend on room service?'
                            , min_value=0., value=0.)
FoodCourt = st.number_input('How much will you spend on food and beverage?'
                            , min_value=0., value=0.)
ShoppingMall = st.number_input('How much will you spend on shopping?'
                            , min_value=0., value=0.)
Spa = st.number_input('How much will you spend on spa services?'
                            , min_value=0., value=0.)
VRDeck = st.number_input('How much will you spend on VR Entertainment?'
                            , min_value=0., value=0.)

# API and params

url = 'https://spaceship-titanic-api-zby5e6zv3q-ew.a.run.app/predict'

params = dict(
    HomePlanet=HomePlanet,
    CryoSleep=CryoSleep,
    Cabin_Deck=Cabin_Deck,
    Cabin_Level=Cabin_Level,
    Cabin_Side=Cabin_Side,
    Destination=Destination,
    Age=Age,
    VIP=VIP,
    RoomService=RoomService,
    FoodCourt=FoodCourt,
    ShoppingMall=ShoppingMall,
    Spa=Spa,
    VRDeck=VRDeck,
)

predict = st.button('Click here to see if you would survive the collision with the spacetime anomaly!')

if predict:
    response = requests.get(url, params=params)
    prediction = response.json()['Transported']
    if prediction:
        out_text = 'You where transported to an alternate dimension! Maybe for the better?'
        st.error(out_text)
    else:
        out_text = 'You where survived the collision with the anomaly! Did you really win though?'
        st.success(out_text)
