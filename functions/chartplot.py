import numpy as np
import matplotlib.pyplot as plt


def draw_bar_chart(datax, datay):
    """Takes two list of the data and draw bar chart"""
    net_salaries = datay
    y_pos = np.arange(len(net_salaries))
    gross_salaries = datax

    plt.bar(y_pos, gross_salaries, align='center', alpha=0.5)
    plt.xticks(y_pos, net_salaries)
    plt.ylabel('Wynagrodzenie brutto')
    plt.xlabel('Wynagrodzenie netto')
    plt.title('Wynagrodzenie brutto/netto')

    plt.show()
