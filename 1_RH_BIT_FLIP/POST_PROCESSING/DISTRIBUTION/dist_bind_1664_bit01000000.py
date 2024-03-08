# 3D Heatmap in Python using matplotlib

# to make plot interactive
#%matplotlib

import sys
import csv
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import plotly.express as px
import plotly.graph_objects as pgo
from plotly import data

from pylab import *
from mpl_toolkits import mplot3d


# def count_one(n):
#       n = str(bin(n))
#       one_count = 0
#       for i in n:
#          if i == "1":
#             one_count+=1
#       return one_count


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python histogram.py inputFile")
        exit(1)


    df = pd.read_csv(sys.argv[1])
    df['exp_v_bin'] = df.expected_value.apply(lambda v: str(format(int(v, 16), '08b')))
    df['flip_v_bin'] = df.flipped_value.apply(lambda v: str(format(int(v, 16), '08b')))
    df['flip_bit'] = df.exp_v_bin.str.count("0") - df.flip_v_bin.str.count("0")
    df['flip_bit_abs'] = df.flip_bit.abs()
    df['1b_flip_cnt'] =df.flip_bit_abs.cumsum()
    df['2b_flip_cnt'] = (df["flip_bit_abs"] >1).cumsum()
    df['1b_add_cnt'] = (~df.address.duplicated()).cumsum()
    df['2b_add_cnt'] = ((~df.address.duplicated())&(df["flip_bit_abs"] >1)).cumsum()
    # df['hour'] = pd.to_numeric(df['hour'], downcast='float64')
    # df['min'] = pd.to_numeric(df['min'], downcast='float64')
    # df['sec'] = pd.to_numeric(df['sec'], downcast='float64')
    # df['min(h)'] = df['min'].div(60)
    # df['sec(h)'] = df['sec'].div(3600)
    df['time_h'] = df['hour'] +  df['min'].div(60) +  df['sec'].div(3600)

    print(df)

    x_b0 = df.row[(df.bank==0)]
    y_b0 = df.col[(df.bank==0)]

    x_b0_byte = df.row[(df.bank==0) & (df.byteoffset==1)]
    y_b0_byte = df.col[(df.bank==0) & (df.byteoffset==1)]

    x_b0_bit = df.row[(df.bank==0) & (df.flip_v_bin=="00001000") ]
    y_b0_bit = df.col[(df.bank==0) & (df.flip_v_bin=="00001000") ]
#    x_b0_bit = df.row[((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 0)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 1)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 2)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 3)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 4)) |  ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 5)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 6)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 7)) ]
#    y_b0_bit = df.col[((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 0)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 1)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 2)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 3)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 4)) |  ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 5)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 6)) | ((df.bank==0) & (df.flip_v_bin=="00100000") & (df.byteoffset== 7)) ]



    x_b0_byte1_bit0 = df.row[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00000001") ]
    y_b0_byte1_bit0 = df.col[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00000001") ]

    x_b0_byte1_bit1 = df.row[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00000010") ]
    y_b0_byte1_bit1 = df.col[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00000010") ]

    x_b0_byte1_bit2 = df.row[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00000100") ]
    y_b0_byte1_bit2 = df.col[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00000100") ]

    x_b0_byte1_bit3 = df.row[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00001000") ]
    y_b0_byte1_bit3 = df.col[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00001000") ]

    x_b0_byte1_bit4 = df.row[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00010000") ]
    y_b0_byte1_bit4 = df.col[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00010000") ]

    x_b0_byte1_bit5 = df.row[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00100000") ]
    y_b0_byte1_bit5 = df.col[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="00100000") ]

    x_b0_byte1_bit6 = df.row[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="01000000") ]
    y_b0_byte1_bit6 = df.col[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="01000000") ]

    x_b0_byte1_bit7 = df.row[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="10000000") ]
    y_b0_byte1_bit7 = df.col[(df.bank==0) & (df.byteoffset==1) & (df.flip_v_bin=="10000000") ]



    x_b2_byte3_bit0 = df.row[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00000001") ]
    y_b2_byte3_bit0 = df.col[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00000001") ]

    x_b2_byte3_bit1 = df.row[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00000010") ]
    y_b2_byte3_bit1 = df.col[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00000010") ]

    x_b2_byte3_bit2 = df.row[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00000100") ]
    y_b2_byte3_bit2 = df.col[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00000100") ]

    x_b2_byte3_bit3 = df.row[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00001000") ]
    y_b2_byte3_bit3 = df.col[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00001000") ]

    x_b2_byte3_bit4 = df.row[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00010000") ]
    y_b2_byte3_bit4 = df.col[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00010000") ]

    x_b2_byte3_bit5 = df.row[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00100000") ]
    y_b2_byte3_bit5 = df.col[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="00100000") ]

    x_b2_byte3_bit6 = df.row[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="01000000") ]
    y_b2_byte3_bit6 = df.col[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="01000000") ]

    x_b2_byte3_bit7 = df.row[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="10000000") ]
    y_b2_byte3_bit7 = df.col[(df.bank==2) & (df.byteoffset==3) & (df.flip_v_bin=="10000000") ]





#     heatmap, xedges, yedges = np.histogram2d(y_b0, x_b0, bins=128,64)
#     extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
#     plt.clf()
#     plt.imshow(heatmap.T, extent=extent, origin='lower')
#     plt.show()

    # 2D histogram
    fig0 = pgo.Figure(pgo.Histogram2d(x=y_b0_bit,y=x_b0_bit, colorbar=dict(title="<b># of errors</b>"), #ticktext=[0,20,40,60,80,100],
        autobinx=False,
        xbins=dict(start=0, end=1023, size=16),
        autobiny=False,
        ybins=dict(start=0, end=4095, size=64),
        texttemplate= "%{z}"
        ))
    fig0.update_layout(xaxis_title="<b>Column (bin16)</b>", yaxis_title="<b>Row (bin64)</b>", font=dict(color="Black"))
    fig0.update_layout(yaxis = dict(tickmode='array', tickvals=[1023,2047,3071,4095], ticktext=[1023,2047,3071,4095]))
    fig0.update_layout(xaxis = dict(tickmode='array', tickvals=[255,511,767,1023], ticktext=[255,511,767,1023]))

#    fig0.add_trace(pgo.Histogram2d(x=[0, 4095],y=[0,1023]))
#    colorbar= dict(title="count", yanchor="top", y=1)

#    fig0.update_coloraxes(colorbar_title_text="Count")

#    layout.coloraxis.colorbar.title='count'

#    fig0.update_layout(coloraxis_colorbar=colorbar)

    #fig0.show()
    fig0.write_image("dist.png")
#
#
#    fig1 = pgo.Figure(pgo.Histogram2d(x=x_b0_byte,y=y_b0_byte,
#        autobinx=False,
#        xbins=dict(start=0, end=4095, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=1023, size=1),
#        texttemplate= "%{z}"))
#    fig1.show()
#
##    fig2 = pgo.Figure(pgo.Histogram2d(x=x_b0_bit,y=y_b0_bit,
#        autobinx=False,
#        xbins=dict(start=0, end=4095, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=1023, size=1),
#        texttemplate= "%{z}"))
#    fig2.show()
#

#        x_min = 0
#        x_max = 4095
#        y_min = 0
#        y_max = 1023
#
#        x_bins = np.linspace(x_min, x_max, 1)
#        y_bins = np.linspace(y_min, y_max, 1)
#
#        fig, ax = plt.subplots(figsize=10,7))
#        plt.hist2d(x_b0, y_b0, bins =[xbins, ybins], cmap = plt.cm.nipy_spectral)
#        plt.title("Histogram test")
#        plt.colobar()
##
#        ax.set_xlabel('X-axis')
#        ax.set_ylabel('Y-axis')
#
#        plt.tight_layout()
#        plot.show()








# Bank0 Byte offset 1

#    fig_010 = pgo.Figure(pgo.Histogram2d(x=y_b0_byte1_bit0,y=x_b0_byte1_bit0,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_010.show()

#    fig_011 = pgo.Figure(pgo.Histogram2d(x=y_b0_byte1_bit1,y=x_b0_byte1_bit1,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_011.show()
#
#    fig_012 = pgo.Figure(pgo.Histogram2d(x=x_b0_byte1_bit2,y=y_b0_byte1_bit2,
#        autobinx=False,
#        ybins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        xbins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_012.show()

#    fig_013 = pgo.Figure(pgo.Histogram2d(x=y_b0_byte1_bit3,y=x_b0_byte1_bit3,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_013.show()

#    fig_014 = pgo.Figure(pgo.Histogram2d(x=y_b0_byte1_bit4,y=x_b0_byte1_bit4,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_014.show()

#    fig_015 = pgo.Figure(pgo.Histogram2d(x=y_b0_byte1_bit5,y=x_b0_byte1_bit5,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_015.show()
#
#    fig_016 = pgo.Figure(pgo.Histogram2d(x=y_b0_byte1_bit6,y=x_b0_byte1_bit6,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_016.show()
#
#    fig_017 = pgo.Figure(pgo.Histogram2d(x=y_b0_byte1_bit7,y=x_b0_byte1_bit7,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_017.show()
#
#
# Bank2 Byte offset 3

#    fig_230 = pgo.Figure(pgo.Histogram2d(x=y_b2_byte3_bit0,y=x_b2_byte3_bit0,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_230.show()
#
#    fig_231 = pgo.Figure(pgo.Histogram2d(x=y_b2_byte3_bit1,y=x_b2_byte3_bit1,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_231.show()
#
#    fig_232 = pgo.Figure(pgo.Histogram2d(x=y_b2_byte3_bit2,y=x_b2_byte3_bit2,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_232.show()
#
#    fig_233 = pgo.Figure(pgo.Histogram2d(x=y_b2_byte3_bit3,y=x_b2_byte3_bit3,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_233.show()
#
#    fig_234 = pgo.Figure(pgo.Histogram2d(x=y_b2_byte3_bit4,y=x_b2_byte3_bit4,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_234.show()
#
#    fig_235 = pgo.Figure(pgo.Histogram2d(x=y_b2_byte3_bit5,y=x_b2_byte3_bit5,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_235.show()
#
#    fig_236 = pgo.Figure(pgo.Histogram2d(x=y_b2_byte3_bit6,y=x_b2_byte3_bit6,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_236.show()
#
#    fig_237 = pgo.Figure(pgo.Histogram2d(x=y_b2_byte3_bit7,y=x_b2_byte3_bit7,
#        autobinx=False,
#        xbins=dict(start=0, end=1023, size=1),
#        autobiny=False,
#        ybins=dict(start=0, end=4095, size=1),
#        texttemplate= "%{z}"))
#    fig_237.show()
#


    #3D histogram


    # fig = plt.figure(figsize = (10, 7))
    # ax = plt.axes(projection ="3d")

    # # Creating plot
    # ax.scatter3D(y_b0, x_b0, z_b0, color = "green")
    # plt.title("simple 3D scatter plot")

    # # show plot
    # plt.show()

    # df.plot(x='', y='fdg', marker='.')
    # fig, (ax1, ax2) = plt.subplots(1,2)
    # df.plot(kind = 'line', x = 'time_h', y = '1b_flip_cnt', ax=ax1)
    # df.plot(kind = 'line', x = 'time_h', y = '1b_add_cnt', ax=ax1)

    # df.plot(kind = 'line', x = 'time_h', y = '2b_flip_cnt', ax=ax2)
    # df.plot(kind = 'line', x = 'time_h', y = '2b_add_cnt', ax=ax2)

    # #n, bins, patches = ax.hist(x, num_bins, density=False)
    # fig.suptitle('Number of flipped bits and address')

    # ax1.plot(x, y1_1)
    # ax2.plot(x, y2_1)

    # ax.set_xlabel("Hammering time [hour]")
    # ax.set_ylabel("# of addresss")

    # plt.show()


