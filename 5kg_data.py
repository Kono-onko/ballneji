import pandas as pd
import matplotlib.pyplot as plt

#nashi_data_df = pd.read_csv('csv/1020/1020_omorinashi_1.CSV', skiprows=2)
# ari_data_df = pd.read_csv('csv/1020/1020_omori5kg_1.CSV', skiprows=2)
# a2_data_df = pd.read_csv('csv/1020/1020_5kg_a2_1.CSV', skiprows=2)
# d2_data_df = pd.read_csv('csv/1020/1020_5kg_d2_1.CSV', skiprows=2)
# v2_data_df = pd.read_csv('csv/1020/1020_5kg_v2_1.CSV', skiprows=2)
# wt2_data_df = pd.read_csv('csv/1020/1020_5kg_wt2_1.CSV', skiprows=2)
# wt3_data_df = pd.read_csv('csv/1020/1020_5kg_wt3_1.CSV', skiprows=2)
# print(data_df)

# 距離をd2にした時の比較用
# ari_data_df = pd.read_csv('csv/1020/1020_omori5kg_1.CSV', skiprows=2)
# a2_d1_data_df = pd.read_csv('csv/1020/1020_5kg_a2_d1_1.CSV', skiprows=2)
# a2_d2_data_df = pd.read_csv('csv/1020/1020_5kg_a2_d2_1.CSV', skiprows=2)
# v2_d1_data_df = pd.read_csv('csv/1020/1020_5kg_v2_d1_1.CSV', skiprows=2)
# v2_d2_data_df = pd.read_csv('csv/1020/1020_5kg_v2_d2_1.CSV', skiprows=2)
# v3_d1_data_df = pd.read_csv('csv/1020/1020_5kg_v3_d1_1.CSV', skiprows=2)
# v3_d2_data_df = pd.read_csv('csv/1020/1020_5kg_v3_d2_1.CSV', skiprows=2)
# v4_d1_data_df = pd.read_csv('csv/1020/1020_5kg_v4_d1_1.CSV', skiprows=2)
# v4_d2_data_df = pd.read_csv('csv/1020/1020_5kg_v4_d2_1.CSV', skiprows=2)
# wt2_d1_data_df = pd.read_csv('csv/1020/1020_5kg_wt2_d1_1.CSV', skiprows=2)
# wt2_d2_data_df = pd.read_csv('csv/1020/1020_5kg_wt2_d2_1.CSV', skiprows=2)
# wt3_d1_data_df = pd.read_csv('csv/1020/1020_5kg_wt3_d1_1.CSV', skiprows=2)
# wt3_d2_data_df = pd.read_csv('csv/1020/1020_5kg_wt3_d2_1.CSV', skiprows=2)

#時間を変更した時の比較用
# ari_data_df = pd.read_csv('csv/1020/1020_omori5kg_10min_1.CSV', skiprows=2)
# a2_d1_data_df = pd.read_csv('csv/1020/1020_5kg_a2_d1_10min_1.CSV', skiprows=2)
# a2_d2_data_df = pd.read_csv('csv/1020/1020_5kg_a2_d2_10min_1.CSV', skiprows=2)
# v2_d1_data_df = pd.read_csv('csv/1020/1020_5kg_v2_d1_10min_1.CSV', skiprows=2)
# v2_d2_data_df = pd.read_csv('csv/1020/1020_5kg_v2_d2_10min_1.CSV', skiprows=2)
# v3_d1_data_df = pd.read_csv('csv/1020/1020_5kg_v3_d1_10min_1.CSV', skiprows=2)
# v3_d2_data_df = pd.read_csv('csv/1020/1020_5kg_v3_d2_10min_1.CSV', skiprows=2)
# v4_d1_data_df = pd.read_csv('csv/1020/1020_5kg_v4_d1_10min_1.CSV', skiprows=2)
# v4_d2_data_df = pd.read_csv('csv/1020/1020_5kg_v4_d2_10min_1.CSV', skiprows=2)
# wt2_d1_data_df = pd.read_csv('csv/1020/1020_5kg_wt2_d1_10min_1.CSV', skiprows=2)
# wt2_d2_data_df = pd.read_csv('csv/1020/1020_5kg_wt2_d2_10min_1.CSV', skiprows=2)
# wt3_d1_data_df = pd.read_csv('csv/1020/1020_5kg_wt3_d1_10min_1.CSV', skiprows=2)
# wt3_d2_data_df = pd.read_csv('csv/1020/1020_5kg_wt3_d2_10min_1.CSV', skiprows=2)

#d3,d4等距離を短く往復させた場合（揺動）の比較
# ari_data_df = pd.read_csv('csv/1020/1020_omori5kg_10min_1.CSV', skiprows=2)
# d2_data_df = pd.read_csv('csv/1020/1020_5kg_d2_10min_1.CSV', skiprows=2)
# d3_data_df = pd.read_csv('csv/1020/1020_5kg_d3_10min_1.CSV', skiprows=2)
# d4_data_df = pd.read_csv('csv/1020/1020_5kg_d4_10min_1.CSV', skiprows=2)
# d5_data_df = pd.read_csv('csv/1020/1020_5kg_d5_10min_1.CSV', skiprows=2)

#position hikaku
ari_data_df = pd.read_csv('csv/1020/1020_5kg_d1_10min_1.CSV', skiprows=2)
position1_data_df = pd.read_csv('csv/1020/1020_5kg_d1_position1_10min_1.CSV', skiprows=2)
position2_data_df = pd.read_csv('csv/1020/1020_5kg_d1_position2_10min_1.CSV', skiprows=2)

#nashi_data = nashi_data_df.rolling(100).var()
# ari_data = ari_data_df.rolling(56).var()
# a2_data = a2_data_df.rolling(56).var()
# d2_data = d2_data_df.rolling(56).var()
# v2_data = v2_data_df.rolling(56).var()
# wt2_data = wt2_data_df.rolling(56).var()
# wt3_data = wt3_data_df.rolling(56).var()

# 距離をd2にした時の比較用
# ari_data = ari_data_df.rolling(56).var()
# a2_d1_data = a2_d1_data_df.rolling(56).var()
# a2_d2_data = a2_d2_data_df.rolling(56).var()
# v2_d1_data = v2_d1_data_df.rolling(56).var()
# v2_d2_data = v2_d2_data_df.rolling(56).var()
# v3_d1_data = v3_d1_data_df.rolling(56).var()
# v3_d2_data = v3_d2_data_df.rolling(56).var()
# v4_d1_data = v4_d1_data_df.rolling(56).var()
# v4_d2_data = v4_d2_data_df.rolling(56).var()
# wt2_d1_data = wt2_d1_data_df.rolling(56).var()
# wt2_d2_data = wt2_d2_data_df.rolling(56).var()
# wt3_d1_data = wt3_d1_data_df.rolling(56).var()
# wt3_d2_data = wt3_d2_data_df.rolling(56).var()

#d3,d4等距離を短く往復させた場合（揺動）の比較
# ari_data = ari_data_df.rolling(56).var()
# d2_data = d2_data_df.rolling(56).var()
# d3_data = d3_data_df.rolling(56).var()
# d4_data = d4_data_df.rolling(56).var()
# d5_data = d5_data_df.rolling(56).var()

ari_data = ari_data_df.rolling(56).var()
position1_data = position1_data_df.rolling(100).var()
position2_data = position2_data_df.rolling(100).var()

fig = plt.figure(figsize=(10,5))

#torque
ax = fig.add_subplot(2,1,1)

# ax.plot(ari_data_df['torque'], label='ari')
# ax.plot(position1_data.index - 40, position1_data['torque'], label='1')
# ax.plot(position2_data.index - 100, position2_data['torque'], label='2')
#ax.plot(nashi_data.index - 0,nashi_data['torque'], label='nashi')

#normal data
# ax.plot(ari_data.index - 0,ari_data['torque'], label='ari')

#accel
# ax.plot(a2_d1_data.index + 0,a2_d1_data['torque'], label='accel2_d1')
# ax.plot(a2_d2_data.index + 0,a2_d2_data['torque'], label='accel2_d2')

#distance
# ax.plot(d2_data.index - 0,d2_data['torque'], label='distance2')
# ax.plot(d3_data.index - 0,d3_data['torque'], label='distance3')
# ax.plot(d4_data.index - 0,d4_data['torque'], label='distance4')
# ax.plot(d5_data.index - 0,d5_data['torque'], label='distance5')

#speed
# ax.plot(v2_d1_data.index - 0,v2_d1_data['torque'], label='speed2_d1')
# ax.plot(v2_d2_data.index - 0,v2_d2_data['torque'], label='speed2_d2')
# ax.plot(v3_d1_data.index - 0,v3_d1_data['torque'], label='speed3_d1')
# ax.plot(v3_d2_data.index - 0,v3_d2_data['torque'], label='speed3_d2')
# ax.plot(v4_d1_data.index - 0,v4_d1_data['torque'], label='speed4_d1')
# ax.plot(v4_d2_data.index - 0,v4_d2_data['torque'], label='speed4_d2')

#wait_time
# ax.plot(wt2_d1_data.index + 0,wt2_d1_data['torque'], label='wait_time_d1')
# ax.plot(wt2_d2_data.index + 0,wt2_d2_data['torque'], label='wait_time2_d2')
# ax.plot(wt3_d1_data.index + 0,wt3_d1_data['torque'], label='wait_time3_d1')
# ax.plot(wt3_d2_data.index + 0,wt3_d2_data['torque'], label='wait_time3_d2')

#position change
ax.plot(ari_data_df.index - 0,ari_data_df['torque'], label='ari')
ax.plot(position1_data_df.index - 280, position1_data_df['torque'], label='1')
ax.plot(position2_data_df.index - 30, position2_data_df['torque'], label='2')

#speed
ax = fig.add_subplot(2,1,2)

#normal data
# ax.plot(ari_data_df.index - 0,ari_data_df['speed'], label='ari')

#accel
# ax.plot(a2_d1_data_df['speed'], label='accel2_d1')
# ax.plot(a2_d2_data_df['speed'], label='accel2_d2')

#distance
# ax.plot(d2_data_df.index - 0,d2_data_df['speed'], label='distance2')
# ax.plot(d3_data_df.index - 0,d3_data_df['speed'], label='distance3')
# ax.plot(d4_data_df.index - 0,d4_data_df['speed'], label='distance4')
# ax.plot(d5_data_df.index - 0,d5_data_df['speed'], label='distance5')

#speed
# ax.plot(v2_d1_data_df.index - 0,v2_d1_data_df['speed'], label='speed2_d1')
# ax.plot(v2_d2_data_df.index - 0,v2_d2_data_df['speed'], label='speed2_d2')
# ax.plot(v3_d1_data_df.index - 0,v3_d1_data_df['speed'], label='speed3_d1')
# ax.plot(v3_d2_data_df.index - 0,v3_d2_data_df['speed'], label='speed3_d2')
# ax.plot(v4_d1_data_df.index - 0,v4_d1_data_df['speed'], label='speed4_d1')
# ax.plot(v4_d2_data_df.index - 0,v4_d2_data_df['speed'], label='speed4_d2')

#wait_time
# ax.plot(wt2_d1_data_df.index + 0,wt2_d1_data_df['speed'], label='wait_time_d1')
# ax.plot(wt2_d2_data_df.index + 0,wt2_d2_data_df['speed'], label='wait_time2_d2')
# ax.plot(wt3_d1_data_df.index + 0.0,wt3_d1_data_df['speed'], label='wait_time3_d1')
# ax.plot(wt3_d2_data_df.index + 0.0,wt3_d2_data_df['speed'], label='wait_time3_d2')

#position change
ax.plot(ari_data_df.index - 0,ari_data_df['speed'], label='ari')
ax.plot(position1_data_df.index - 0, position1_data_df['speed'], label='1')
ax.plot(position2_data_df.index - 0, position2_data_df['speed'], label='2')


plt.legend()
plt.show()