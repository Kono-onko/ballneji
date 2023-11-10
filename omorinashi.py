import pandas as pd
import matplotlib.pyplot as plt

nashi_data_df = pd.read_csv('csv/0922/0922_omorinashi_1.CSV', skiprows=2)
a2_data_df = pd.read_csv('csv/0922/0922_omorinashi_a2_1.CSV', skiprows=2)
d2_data_df = pd.read_csv('csv/0922/0922_omorinashi_d2_1.CSV', skiprows=2)
v2_data_df = pd.read_csv('csv/0922/0922_omorinashi_v2_1.CSV', skiprows=2)
wt2_data_df = pd.read_csv('csv/0922/0922_omorinashi_wt2_1.CSV', skiprows=2)
wt3_data_df = pd.read_csv('csv/0922/0922_omorinashi_wt3_1.CSV', skiprows=2)
# print(data_df)

nashi_data = nashi_data_df.rolling(100).var()
a2_data = a2_data_df.rolling(100).var()
d2_data = d2_data_df.rolling(100).var()
v2_data = v2_data_df.rolling(100).var()
wt2_data = wt2_data_df.rolling(100).var()
wt3_data = wt3_data_df.rolling(100).var()

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)

ax.plot(nashi_data.index + 0,nashi_data['torque'], label='nashi')
ax.plot(a2_data.index - 0,a2_data['torque'], label='accel2')
ax.plot(d2_data.index - 0,d2_data['torque'], label='distance2')
ax.plot(v2_data.index - 0,v2_data['torque'], label='speed2')
ax.plot(wt2_data.index + 0,wt2_data['torque'], label='wait_time2')
ax.plot(wt3_data.index - 0,wt3_data['torque'], label='wait_time3')
# ax.plot(data['torque'], label='idouheikinn')

plt.legend()
plt.show()
