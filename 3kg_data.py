import pandas as pd
import matplotlib.pyplot as plt

# position1_data_df = pd.read_csv('csv/0922/0922_position1_3kg_1.CSV', skiprows=2)
# position2_data_df = pd.read_csv('csv/0922/0922_position2_3kg_1.CSV', skiprows=2)
# position3_data_df = pd.read_csv('csv/0922/0922_position3_3kg_1.CSV', skiprows=2)
# position4_data_df = pd.read_csv('csv/0922/0922_position4_3kg_1.CSV', skiprows=2)
#　　nashi_data_df = pd.read_csv('csv/0922/0922_omorinashi_1.CSV', skiprows=2)
# ari_data_df = pd.read_csv('csv/0922/0922_omori3kg_1.CSV', skiprows=2)
# a2_data_df = pd.read_csv('csv/0922/0922_3kg_a2_1.CSV', skiprows=2)
# d2_data_df = pd.read_csv('csv/0922/0922_3kg_d2_1.CSV', skiprows=2)
# v2_data_df = pd.read_csv('csv/0922/0922_3kg_v2_1.CSV', skiprows=2)
# wt2_data_df = pd.read_csv('csv/0922/0922_3kg_wt2_1.CSV', skiprows=2)
# wt3_data_df = pd.read_csv('csv/0922/0922_3kg_wt3_1.CSV', skiprows=2)
# print(data_df)

# 距離をd2にした時の比較用
ari_data_df = pd.read_csv('csv/1011/1011_omori3kg_1.CSV', skiprows=2)
a2_d1_data_df = pd.read_csv('csv/1011/1011_3kg_a2_d1_1.CSV', skiprows=2)
a2_d2_data_df = pd.read_csv('csv/1011/1011_3kg_a2_d2_1.CSV', skiprows=2)
v2_d1_data_df = pd.read_csv('csv/1011/1011_3kg_v2_d1_1.CSV', skiprows=2)
v2_d2_data_df = pd.read_csv('csv/1011/1011_3kg_v2_d2_1.CSV', skiprows=2)
v3_d1_data_df = pd.read_csv('csv/1011/1011_3kg_v3_d1_1.CSV', skiprows=2)
v3_d2_data_df = pd.read_csv('csv/1011/1011_3kg_v3_d2_1.CSV', skiprows=2)
v4_d1_data_df = pd.read_csv('csv/1011/1011_3kg_v4_d1_1.CSV', skiprows=2)
v4_d2_data_df = pd.read_csv('csv/1011/1011_3kg_v4_d2_1.CSV', skiprows=2)
wt2_d1_data_df = pd.read_csv('csv/1011/1011_3kg_wt2_d1_1.CSV', skiprows=2)
wt2_d2_data_df = pd.read_csv('csv/1011/1011_3kg_wt2_d2_1.CSV', skiprows=2)
wt3_d1_data_df = pd.read_csv('csv/1011/1011_3kg_wt3_d1_1.CSV', skiprows=2)
wt3_d2_data_df = pd.read_csv('csv/1011/1011_3kg_wt3_d2_1.CSV', skiprows=2)

# position1_data = position1_data_df.rolling(56).aggregate()
# position2_data = position2_data_df.rolling(56).aggregate()
# position3_data = position3_data_df.rolling(56).aggregate()
# position4_data = position4_data_df.rolling(56).aggregate()
#nashi_data = nashi_data_df.rolling(56).aggregate()
# ari_data = ari_data_df.rolling(56).aggregate()
# a2_data = a2_data_df.rolling(56).aggregate()
# d2_data = d2_data_df.rolling(56).aggregate()
# v2_data = v2_data_df.rolling(56).aggregate()
# wt2_data = wt2_data_df.rolling(56).aggregate()
# wt3_data = wt3_data_df.rolling(56).aggregate()

# 距離をd2にした時の比較用
ari_data = ari_data_df.rolling(56).mean()
a2_d1_data = a2_d1_data_df.rolling(56).mean()
a2_d2_data = a2_d2_data_df.rolling(56).mean()
v2_d1_data = v2_d1_data_df.rolling(56).mean()
v2_d2_data = v2_d2_data_df.rolling(56).mean()
v3_d1_data = v3_d1_data_df.rolling(56).mean()
v3_d2_data = v3_d2_data_df.rolling(56).mean()
v4_d1_data = v4_d1_data_df.rolling(56).mean()
v4_d2_data = v4_d2_data_df.rolling(56).mean()
wt2_d1_data = wt2_d1_data_df.rolling(56).mean()
wt2_d2_data = wt2_d2_data_df.rolling(56).mean()
wt3_d1_data = wt3_d1_data_df.rolling(56).mean()
wt3_d2_data = wt3_d2_data_df.rolling(56).mean()

fig = plt.figure(figsize=(10,5))

#torque
ax = fig.add_subplot(2,1,1)

# ax.plot(omorinasi_data_df.index + 220, omorinasi_data_df['torque'], label='nashi')
# ax.plot(ari_data_df['torque'], label='ari')
# ax.plot(position1_data.index - 260, position1_data['torque'], label='1')
# ax.plot(position2_data.index - 220, position2_data['torque'], label='2')
# ax.plot(position3_data.index - 380, position3_data['torque'], label='3')
# ax.plot(position4_data.index - 90, position4_data['torque'], label='4')
#ax.plot(nashi_data.index + 0,nashi_data['torque'], label='nashi')
#ax.plot(ari_data.index - 0,ari_data['torque'], label='ari')

#accel
# ax.plot(a2_d1_data['torque'], label='accel2_d1')
# ax.plot(a2_d2_data['torque'], label='accel2_d2')

#distance
# ax.plot(d2_data.index - 0,d2_data['torque'], label='distance2')

#speed
# ax.plot(v2_d1_data.index - 0,v2_d1_data['torque'], label='speed2_d1')
# ax.plot(v2_d2_data.index - 0,v2_d2_data['torque'], label='speed2_d2')
ax.plot(v3_d1_data.index - 0,v3_d1_data['torque'], label='speed3_d1')
ax.plot(v3_d2_data.index - 0,v3_d2_data['torque'], label='speed3_d2')
# ax.plot(v4_d1_data.index - 0,v4_d1_data['torque'], label='speed4_d1')
# ax.plot(v4_d2_data.index - 0,v4_d2_data['torque'], label='speed4_d2')

#wait_time
# ax.plot(wt2_d1_data.index + 0,wt2_d1_data['torque'], label='wait_time_d1')
# ax.plot(wt2_d2_data.index + 0,wt2_d2_data['torque'], label='wait_time2_d2')
# ax.plot(wt3_d1_data.index + 0.0,wt3_d1_data['torque'], label='wait_time3_d1')
# ax.plot(wt3_d2_data.index + 0.0,wt3_d2_data['torque'], label='wait_time3_d2')

#speed
ax = fig.add_subplot(2,1,2)

#accel
# ax.plot(a2_d1_data_df['speed'], label='accel2_d1')
# ax.plot(a2_d2_data_df['speed'], label='accel2_d2')

#distance
# ax.plot(d2_data_df.index - 0,d2_data_df['speed'], label='distance2')

#speed
# ax.plot(v2_d1_data_df.index - 0,v2_d1_data_df['speed'], label='speed2_d1')
# ax.plot(v2_d2_data_df.index - 0,v2_d2_data_df['speed'], label='speed2_d2')
ax.plot(v3_d1_data_df.index - 0,v3_d1_data_df['speed'], label='speed3_d1')
ax.plot(v3_d2_data_df.index - 0,v3_d2_data_df['speed'], label='speed3_d2')
# ax.plot(v4_d1_data_df.index - 0,v4_d1_data_df['speed'], label='speed4_d1')
# ax.plot(v4_d2_data_df.index - 0,v4_d2_data_df['speed'], label='speed4_d2')

#wait_time
# ax.plot(wt2_d1_data_df.index + 0,wt2_d1_data_df['speed'], label='wait_time_d1')
# ax.plot(wt2_d2_data_df.index + 0,wt2_d2_data_df['speed'], label='wait_time2_d2')
# ax.plot(wt3_d1_data_df.index + 0.0,wt3_d1_data_df['speed'], label='wait_time3_d1')
# ax.plot(wt3_d2_data_df.index + 0.0,wt3_d2_data_df['speed'], label='wait_time3_d2')


plt.legend()
plt.show()
