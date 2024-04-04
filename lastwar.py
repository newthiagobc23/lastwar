import streamlit as st
import numpy as np

level_exp = [0,100,200,300,400, #1-5
            500,600,700,800,900, #6-10
            1000,1100,1200,1300,1400, #11-15
            1500,1600,1700,1800,1900, #16-20
            2000,2100,2300,2700, #21-25
            3200,3900,4600,5500,6600, #26-30
            8000,9500,12000,14000,17000,20000, #31-35
            24000,29000,35000,41000,49000, #36-40
            59000,71000,85000,110000,130000, #41-45
            150000,180000,220000,310000,  #46-50
            370000,440000,530000,630000,760000, #51-55
            910000,1100000,1400000,1600000,1900000, #56-60
            2100000,2300000,2500000,2800000,3100000, #61-65
            3400000,3700000,4100000,4500000,4900000, #66-70
            5400000,5900000,6500000,7200000,7900000, #71-75
            8700000,9500000,11000000,12000000,13000000, #76-80
            13000000,14000000,14000000,15000000,16000000, #81-85
            17000000,18000000,19000000,20000000,21000000, #86-90
            22000000,23000000,24000000,25000000,26000000, #91-95
            27000000,28000000,30000000,31000000,33000000, #96-100
            35000000,37000000,39000000,41000000,33000000, #101-105
            45000000,47000000,49000000,51000000,53000000, #106-110
            55000000,57000000,59000000,61000000,63000000, #111-115
            65000000,67000000,69000000,71000000,73000000, #116-120
            75000000,77000000,79000000,81000000,83000000, #121-125
            85000000,87000000,89000000,91000000,93000000, #126-130
            95000000,97000000,100000000,105000000,110000000, #131-135
            115000000,120000000,125000000,130000000,135000000, #136-140
            140000000,145000000,150000000,155000000,160000000, #141-145
            165000000,170000000,175000000,180000000,185000000 #146-150
            ]

def numformat(num):
    fn = 0
    if num > 999999999:
        if not num % 1000000000:
            fn = f'{num // 1000000000}G'
        else:
            fn = f'{round(num / 1000000000, 1)}G'

    elif num > 999999:
        if not num % 1000000:
            fn = f'{num // 1000000}M'
        else:
            fn = f'{round(num / 1000000, 1)}M'

    elif num > 999:
        if not num % 1000:
            fn = f'{num // 1000}K'
        else:
            fn = f'{round(num / 1000, 1)}K'

    if fn == 0: 
        return ''
    else: 
        return f'{fn}' 


###############################################TABS###################################################
######################################################################################################
tab1, tab2, tab3, tab4 = st.tabs(["Hero Exp", "Speed-Up", "Stamina", "Loot Load"])

###############################################TABS###################################################
######################################################################################################

with tab1:
    st.header('Hero Level Calculator')

    col1, col2 = st.columns(2)

    with col1:
        current_level = st.selectbox(
            'Current Hero Level',
            np.arange(1,151))
    with col2:
        target_level = st.selectbox(
        'Target Hero Level',
        np.arange(1,151))

    st.write('Going from level ', int(current_level), ' to level ', target_level)

    req_exp = sum(level_exp[current_level-1:target_level])

    if numformat(req_exp) != '':
        st.write('Required Experience: ', numformat(req_exp), '({:0,})'.format(req_exp))
    else:
        st.write('Required Experience: ', '{:0,}'.format(req_exp))


    st.markdown('## VS Hero Day Points Calculator')
    vs_event = st.selectbox(
        'VS reward per 660xp points:',
        [1,2])

    if req_exp/660 >= 1000000:
        st.write('VS Points: ', numformat(int(req_exp/660)*vs_event), '({:0,})'.format(int(req_exp/660)*vs_event) )
    else:
        st.write('VS Points: ', '{:0,}'.format(int(req_exp/660)*vs_event) )
###############################################TABS###################################################
######################################################################################################

with tab2:
    st.header('Speed-up Calculator')


    om = st.number_input('Number of 1 Minute Speedups:', value=0, format='%d')
    fm = st.number_input('Number of 5 Minutes Speedups:', value=0, format='%d')
    oh = st.number_input('Number of 1 Hour Speedups:', value=0, format='%d')
    th = st.number_input('Number of 3 Hours Speedups:', value=0, format='%d')
    eh = st.number_input('Number of 8 Hours Speedups:', value=0, format='%d')

    fm_min = fm * 5
    oh_min = oh * 60
    th_min = th * 180
    eh_min = eh * 480

    total_minutes = om + fm_min + oh_min + th_min + eh_min

    total_hours = total_minutes/60
    total_days = total_hours/24


    remainder_hours = total_hours - int(total_days)*24
    remainder_minutes = total_minutes - (int(remainder_hours)*60) - (int(total_days)*24*60)

    if total_days >= 1:
        st.write('Total time:', '{:0,}'.format(int(total_days)), ' days, ', '{:0,}'.format(int(remainder_hours)), ' hours, and ', '{:0,}'.format(int(remainder_minutes)), ' minutes', '({:0,}'.format(total_minutes), ' minutes)')
    elif remainder_hours >= 1:
        st.write('Total time:', '{:0,}'.format(int(remainder_hours)), ' hours, and ', '{:0,}'.format(int(remainder_minutes)), ' minutes', '({:0,}'.format(total_minutes), ' minutes)')
    else:
        st.write('Total time:', '{:0,}'.format(total_minutes), ' minutes')

    st.markdown('## VS Points Calculator')
    speedup_points = st.number_input('Points per 1min speed-up:', value=0, format='%d')

    st.write('VS Points: ', numformat(speedup_points * total_minutes), '({:0,})'.format(speedup_points * total_minutes) )

###############################################TABS###################################################
######################################################################################################

with tab3:
    st.header('Full Stamina Time')

    c_stamina = st.number_input('Your current stamina:', value=0, format='%d')
    if c_stamina < 120:
        m_stamina = 120 - c_stamina
        stamina_time = m_stamina * 5

        if stamina_time >= 60:
            stamina_hours = stamina_time/60
            stamina_minutes = stamina_time - (int(stamina_hours) * 60)
            st.write('Time remaining for full stamina:', '{:0,}'.format(int(stamina_hours)), ' Hours and ', '{:0,}'.format(stamina_minutes), 'Minutes ({:0,} minutes)'.format(stamina_time))
        else:
            st.write('Time remaining for full stamina:', stamina_time, 'Minutes')
    else:
        st.write('Already at full stamina')

######################################################################################################
######################################################################################################

with tab4:
    st.header('Attack Loot Estimate')

    max_load = st.number_input('Your unit load in Millions:', value=0.)

    load_red = st.selectbox('Load Reduction:', ['none', '15%', '5%'])

    load = max_load
    if load_red == '15%':
        load = load * 0.15
    if load_red == '5%':
        load = load * 0.05

    iron = st.number_input("Target's IRON in millions:", value=0.)
    coin = st.number_input("Target's COIN in millions:", value=0.)
    bread = st.number_input("Target's FOOD in millions:", value=0.)

    total_resources = iron + coin + bread
    iron_p = 0
    coin_p = 0
    bread_p = 0

    if total_resources > 0:
        iron_p = iron / total_resources
        coin_p = coin / total_resources
        bread_p = bread / total_resources

    iron_loot = iron_p * load
    if iron_loot > iron:
        iron_loot = iron

    coin_loot = coin_p * load
    if coin_loot > coin:
        coin_loot = coin
    
    bread_loot = bread_p * load
    if bread_loot > bread:
        bread_loot = bread

    def convert(num):
        if num < 1:
            return '{:.2f}K'.format(num * 1000)
        else:
            return '{:.2f}M'.format(num)


    if iron_loot != 0 or coin_loot != 0 or bread_loot != 0:
        st.divider()
        
        st.write('IRON loot: ', convert(iron_loot))
        st.write('COIN loot: ', convert(coin_loot))
        st.write('BREAD loot: ', convert(bread_loot))



footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by thiagobc23 | #54 WRG <a style='display: block; text-align: center;' href="https://ko-fi.com/thiagobc23" target="_blank">Enjoyed your visit? Show your support with a tip!</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)