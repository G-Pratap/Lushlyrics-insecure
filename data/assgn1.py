import pandas as pd

dt = pd.read_csv(r"C:\Users\gaorav.pratap\Downloads\Huawei_lte_pms_cell60min_all.csv")
# print(dt)
# cell1 = dt.loc[dt['name']=='L-401216-33']
filt = dt['name']=='L-401216-33'
cell1 = dt[filt]
# print(cell1)
# cell1.to_csv('cell-reading.csv', index=False)
df={'date':[], 'dl_ue_throughput_num':[], 'dl_ue_throughput_den':[], 'cell_name':[]}
df = pd.DataFrame(df)
cnt=4
dl_ue_throughput_num=0
dl_ue_throughput_den=0
i=0
for data1 in cell1['dl_ue_throughput_num']:
    dl_ue_throughput_num += data1
    dl_ue_throughput_den += dt['dl_ue_throughput_den'].loc[dt['dl_ue_throughput_num']==data1].iat[0]
    cnt-=1
    # print(dl_ue_throughput_num)
    if cnt==0:
        # print(dl_ue_throughput_num)
        df.loc[i] = [dt['start_time'].loc[dt['dl_ue_throughput_num']==data1].iat[0], dl_ue_throughput_num, dl_ue_throughput_den, 'L-401216-33']
        # df['dl_ue_throughput_num'][0].append(dl_ue_throughput_num)
        # df['date'][0].append(dt['start_time'].loc[dt['dl_ue_throughput_num']==data].iat[0])
        # filt = dt['dl_ue_throughput_num']==data
        # df['date'] = dt.loc[filt, 'start_time']
        dl_ue_throughput_num=0
        dl_ue_throughput_den=0
        cnt=4
        i+=1
# print(df)
df.to_csv('cell_reading.csv', index=False)
    
# print(df['date'])

# for data in cell1['dl_ue_throughput_den']:
#     cnt=4
#     dl_ue_throughput_den=0
#     while cnt>0:
#         dl_ue_throughput_den += data
#         cnt-=1
#         print(dl_ue_throughput_den)
