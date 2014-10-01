# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 10:30:44 2014
"""
from matplotlib import patches, pyplot as plt
from math import sin, cos, pi
from matplotlib.font_manager import FontProperties
def star(coord, size, rotate):
    pts = [(size * sin(i * 4 * pi / 5 + rotate) + coord[0], \
        size * cos(i * 4 * pi / 5 + rotate) + coord[1]) \
        for i in range(5)]
    return patches.Polygon(pts, fc='yellow', ec='yellow',alpha = .6)
def drawcanvas(ax):
    flagpatch = patches.Rectangle([0, -2], 3, 2, fc='red', ec='#dd1c77', alpha = .9)
    ax.add_patch(flagpatch)
    star1patch = star((0.5, -0.5), 0.3, 0.0)
    ax.add_patch(star1patch)
    ax.add_patch(star((1.0, -0.2), 0.07, 0.3))
    ax.add_patch(star((1.2, -0.4), 0.07, 0.9))
    ax.add_patch(star((1.2, -0.7), 0.07, 0.0))
    ax.add_patch(star((1.0, -0.9), 0.07, 0.3))
def addtext(ax, text = None, xloc = 1, yloc = -1.5, color = '#dd1c77', style =
'italic', weight = 'light', rotation = 10):
    font0 = FontProperties()
    font0.set_style(style)
    font0.set_weight(weight)
    if text == None:
        text = 'Happy 65 anniversary my beloved China  =^^=\n\
            Continue to give priority to development,\n\
            adhere to reform and innovation and \n\
            stay committed to the path of peaceful development\n\
                                                                       Love,R'
    ax.text(xloc, yloc, text , color = color, fontproperties=font0, rotation=rotation)
def turnoffaxis(ax, off = True):
    if off:
        ax.set_axis_off()
    else:
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
def savecanvas(path = 'national_flag.png', dpi = 400, box = 'tight', pad = 0, transparent = True):
    plt.axis('scaled')
    plt.savefig(path, dpi = dpi, bbox_inches = box, pad_inches = pad, transparent = transparent)

if __name__ == '__main__':
    plt.xkcd()
    fig = plt.figure(figsize = (12,10), dpi = 400)
    ax = fig.add_subplot(111)

    drawcanvas(ax)
    addtext(ax)
    turnoffaxis(ax, False)
    savecanvas()
