import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
pd.set_option("display.max_rows", None, "display.max_columns", None)
# def count_one(n):
#       n = str(bin(n))
#       one_count = 0
#       for i in n:
#          if i == "1":
#             one_count+=1
#       return one_count


def count_n_bit(row):
    result = 0
    if (row["exp_v_dec"]&0b00000001) != (row["flip_v_dec"]&0b00000001):
        result = 0
    elif (row["exp_v_dec"]&0b00000010) != (row["flip_v_dec"]&0b00000010):
        result = 1
    elif (row["exp_v_dec"]&0b00000100) != (row["flip_v_dec"]&0b00000100):
        result = 2
    elif (row["exp_v_dec"]&0b00001000) != (row["flip_v_dec"]&0b00001000):
        result = 3
    elif (row["exp_v_dec"]&0b00010000) != (row["flip_v_dec"]&0b00010000):
        result = 4
    elif (row["exp_v_dec"]&0b00100000) != (row["flip_v_dec"]&0b00100000):
        result = 5
    elif (row["exp_v_dec"]&0b01000000) != (row["flip_v_dec"]&0b01000000):
        result = 6
    else:
        result = 7
    return result


def count_m_bit(row):
    result = 0
    if (row["exp_v_dec"]&0b10000000) != (row["flip_v_dec"]&0b10000000):
        result = 7
    elif (row["exp_v_dec"]&0b01000000) != (row["flip_v_dec"]&0b01000000):
        result = 6
    elif (row["exp_v_dec"]&0b00100000) != (row["flip_v_dec"]&0b00100000):
        result = 5
    elif (row["exp_v_dec"]&0b00010000) != (row["flip_v_dec"]&0b00010000):
        result = 4
    elif (row["exp_v_dec"]&0b00001000) != (row["flip_v_dec"]&0b00001000):
        result = 3
    elif (row["exp_v_dec"]&0b00000100) != (row["flip_v_dec"]&0b00000100):
        result = 2
    elif (row["exp_v_dec"]&0b00000010) != (row["flip_v_dec"]&0b00000010):
        result = 1
    else:
        result = 0
    return result


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python histogram.py inputFile")
        exit(1)

    df_result = pd.DataFrame({'brc', 'byte[7]', },)
    df = pd.read_csv(sys.argv[1])
#    df = pd.read_csv(sys.argv[1], dtype={'sec':'str','hammering':'str'})
    df['exp_v_bin'] = df.expected_value.apply(
        lambda v: str(format(int(v, 16), '08b')))
    df['flip_v_bin'] = df.flipped_value.apply(
        lambda v: str(format(int(v, 16), '08b')))
    df['flip_bit'] = df.exp_v_bin.str.count("0") - df.flip_v_bin.str.count("0")
    df['flip_bit_abs'] = df.flip_bit.abs()
    df['1b_flip_cnt'] = df.flip_bit_abs.cumsum()
    df['2b_flip_cnt'] = (df["flip_bit_abs"] > 1).cumsum()
    df['CE cell'] = (~df.address.duplicated()).cumsum()
    df['2b_add_dist'] = df.address.astype(
        str)+"-"+df["flip_bit_abs"].astype(str)
    df['UCE row(byte)'] = ((~df["2b_add_dist"].duplicated())
                           & (df["flip_bit_abs"] > 1)).cumsum()
    df['brc'] = df.bank.astype(str) + "-" + \
        df.row.astype(str) + "-" + df.col.astype(str)
    df['brch'] = df.bank.astype(str) + "-" + df.row.astype(str) + \
        "-" + df.col.astype(str)+"-" + \
        df.hammering.astype(str)
    df['2b_add_cnt_each'] = ((df["brch"].duplicated())).cumsum()

    df.loc[(df["brch"].duplicated() == 1),
           'row_match_diff_byte'] = df.brc.astype(str)
    df.loc[~((df["brch"].duplicated() == 1)), 'row_match_diff_byte'] = "0"
    df["UCE_Diff"] = ((~df["row_match_diff_byte"].duplicated())
                      & (df["row_match_diff_byte"] != "0")).cumsum()

    df.loc[(df["brch"].duplicated() == 1) | ((~df["2b_add_dist"].duplicated()) & (
        df["flip_bit_abs"] > 1)), 'row_match'] = df.brc.astype(str)
    df.loc[~((df["brch"].duplicated() == 1) | (
        (~df["2b_add_dist"].duplicated()) & (df["flip_bit_abs"] > 1))), 'row_match'] = "0"
    df["UCE row(ECC word)"] = ((~df["row_match"].duplicated())
                               & (df["row_match"] != "0")).cumsum()

 #   df['brc_byte_v'] = df.bank.astype(str) +"-"+ df.row.astype(str) +"-"+ df.col.astype(str) +"-"+ df.byteoffset.astype(str) + "-"+df.flip_v_bin.astype(str)
 #   df['brc_bit'] = df.bank.astype(str) + df.row.astype(str) + df.col.astype(str) + df.flip_bit_abs.astype(str)
 #   df['2b_add_cnt_first'] = ((~df["2b_add_dist"].duplicated())&(df["flip_bit_abs"] >1)&(~df["brc"].duplicated())).cumsum()
 #   df['2b_add_cnt_each'] = ((df["brc"].duplicated())&(~df["brc_byte_v"].duplicated())).cumsum()
 #   df['UCE_add_cum'] = df["2b_add_cnt_each"]

    df['hour'] = pd.to_numeric(df['hour'], downcast='float')
    df['min'] = pd.to_numeric(df['min'], downcast='float')
    df['sec'] = pd.to_numeric(df['sec'], downcast='float')
#    df['hour'] = pd.to_numeric(df['hour'])
#    df['min'] = pd.to_numeric(df['min'])
#    df['sec'] = pd.to_numeric(df['sec'])
#     df['min(h)'] = df['min'].div(60)
#     df['sec(h)'] = df['sec'].div(3600)
    df['exp_v_dec'] = df.expected_value.apply(lambda v: int(v, 16))
    df['flip_v_dec'] = df.flipped_value.apply(lambda v: int(v, 16))

    df['time_h'] = df['hour'] + df['min'].div(60) + df['sec'].div(3600)


#    df['brc_time'] = df.bank.astype(str) + df.row.astype(str) + df.col.astype(str) + df.time_h.astype(str)
#    df['UCE_ECC_WORD'] = (df['brc_time'].duplicated()&df['brc'].duplicated()).cumsum()
#    df['UCE_error'] = df['UCE_ECC_WORD']+df['UCE_byte']

#    df['brc_comp'] = df.brc.astype(str)+"-"+df["UC_ECC_WORD"].astype(str)
#    df['2b_add_cnt_ind'] = ((df.brc_comp.duplicated())).cumsum()
# Define a custom function that uses an if statement to select a value

    df['n_bit'] = df.apply(count_n_bit, axis=1)
    df['m_bit'] = df.apply(count_m_bit, axis=1)

    df['brc_byte_nbit'] = df.bank.astype(str) + "-" + df.row.astype(str) + "-" + df.col.astype(
        str) + "-" + df.byteoffset.astype(str) + "-" + df.n_bit.astype(str)
    df['brc_byte_mbit'] = df.bank.astype(str) + "-" + df.row.astype(str) + "-" + df.col.astype(
        str) + "-" + df.byteoffset.astype(str) + "-" + df.m_bit.astype(str)

    df.loc[~(df["brc"].duplicated()), 'UE_GEN'] = "0"
    df.loc[(~(df["brc"].duplicated()))&(df["flip_bit_abs"]>1), 'UE_GEN'] = "1"
    df.loc[(df["brc"].duplicated()) & (~df["brc_byte_nbit"].duplicated()), 'UE_GEN'] = "1"
    df.loc[(df["brc"].duplicated()) & (~df["brc_byte_mbit"].duplicated()), 'UE_GEN'] = "1"
    df.loc[(df["brc"].duplicated()) & (df["brc_byte_nbit"].duplicated()) &(df["flip_bit_abs"]<2) , 'UE_GEN'] = "0"
    df.loc[(df["brc"].duplicated()) & (df["brc_byte_mbit"].duplicated()) &(df["flip_bit_abs"]<2), 'UE_GEN'] = "0"

    df['CNT_UE_GEN'] = (df["UE_GEN"] == "1").cumsum()

#    df['CE cell'] = (~df.address.duplicated()).cumsum()

    # df2.time_h=df['time_h']
    # df2.CNT_UE_GEN=df['CNT_UE_GEN']

    # s = df.time_h.to_csv(), df.CNT_UE_GEN.to_csv()
    s = df[["time_h", "CNT_UE_GEN"]].tail(1).to_csv(index=False)
        
    print(s)

#    # df.plot(x='', y='fdg', marker='.')
#    fig, (ax1, ax2) = plt.subplots(1,2)
#    df.plot(kind = 'line', x = 'time_h', y = '1b_flip_cnt', ax=ax1)
#    df.plot(kind = 'line', x = 'time_h', y = '1b_add_cnt', ax=ax1)
#
#    df.plot(kind = 'line', x = 'time_h', y = '2b_flip_cnt', ax=ax2)
#    df.plot(kind = 'line', x = 'time_h', y = '2b_add_cnt', ax=ax2)
#    # print(df.dtypes)

    # df.plot(x='', y='fdg', marker='.')
#     fig, (ax1, ax2) = plt.subplots(1, 2)
# #    df.plot(kind = 'line', x = 'hammering', y = '1b_flip_cnt', ax=ax1)
# # df.plot(kind = 'line', x = 'hammering', y = 'CE cell', ax=ax1)
#     df.plot(kind='line', x='time_h', y='CE cell', ax=ax1)
# #    df.plot(kind = 'line', x = 'hammering', y = '2b_flip_cnt', ax=ax2)
# # df.plot(kind = 'line', x = 'hammering', y = 'UCE row(byte)', ax=ax2)
# # df.plot(kind = 'line', x = 'hammering', y = 'UCE row(ECC word)', ax=ax2)
#     df.plot(kind='line', x='time_h', y='CNT_UE_GEN', ax=ax2)
#     df.plot(kind='line', x='time_h', y='UCE row(ECC word)', ax=ax2)
# #    df.plot(kind = 'line', x = 'hammering', y = 'UCE_Diff', ax=ax2)
# #    xlabels =['{:,2f}'.format(x) +'K']
# #    df.set_xticklabels(xlabels)
# #    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x)
#     ax1.yaxis.set_major_formatter(ticker.FuncFormatter(
#         lambda y, pos: '{:,.0f}'.format(y/1000)+'K'))
#     ax1.set_ylabel("# of Cells")
# #    ax2.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x)
#     ax2.yaxis.set_major_formatter(
#         ticker.FuncFormatter(lambda y, pos: '{:,.0f}'.format(y)))
#     ax2.set_ylabel("# of Rows")
# #    df.plot(kind = 'line', x = 'hammering', y = 'UCE_error', ax=ax2)
# #    df.plot(kind = 'line', x = 'hammering', y = 'UCE_add_cum', ax=ax2)
#     # print(df.dtypes)

#     # x,y1_1,y1_2,y2_1,y2_2 = [],[],[],[],[]

#     # x.append(df.time(h))
#     # y1_1.append(df.1b_flip_cnt)
#     # y1_2.append(df.1b_add_cnt)
#     # y2_1.append(df.2b_flip_cnt)
#     # y2_2.append(df.2b_add_cnt)

#     # print(f'Number of point {len(x)}')

#     # #n, bins, patches = ax.hist(x, num_bins, density=False)
#     # fig.suptitle('Number of flipped bits and address')

#     # ax1.plot(x, y1_1)
#     # ax2.plot(x, y2_1)

#     # ax.set_xlabel("Hammering time [hour]")
#     # ax.set_ylabel("# of addresss")

#     plt.show()
