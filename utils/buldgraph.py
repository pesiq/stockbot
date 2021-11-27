from matplotlib import pyplot as plt


def plot(time_axis, values_SMA_7, values_SMA_25):
    plt.figure(1, figsize=[19, 8])
    plt.plot(time_axis, values_SMA_7, label="SMA 7")
    plt.plot(time_axis, values_SMA_25, label="SMA 25")
    # plt.plot(time_axis, values_SMA_99, label="SMA 99")
    # plt.plot(gd.time_axis, gd.values_kline_open, '--', label="Open")
    # plt.plot(gd.time_axis, gd.values_kline_close, '-.', label="Close")
    plt.legend()
    plt.tight_layout()
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.show()


if __name__ == '__main__':
    from loc import graphdata as gd

    plot(gd.time_axis, gd.values_SMA_7, gd.values_SMA_25)
