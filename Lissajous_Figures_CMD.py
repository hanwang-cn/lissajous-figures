import matplotlib.pyplot as plt
import numpy as np 
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
def make(a1, num1,a2, num2, chr):
    dur = 2
    fig_mpl, ax = plt.subplots(1, figsize=(5,5), facecolor='white')
    aa = np.linspace(-4 * (np.pi), 4 * (np.pi), 240000) 
    xx = a1 * (np.sin(2 * (np.pi) * num1 * aa))
    yy = lambda d: a2 * (np.sin(2 * (np.pi) * num2 * aa + d))
    ax.set_title("Lissajous Figures")
    ax.set_ylim(-a2,a2)
    ax.set_xlim(-a1,a1)
    line, = ax.plot(xx, yy(0), lw=3)
    def make_frame_mpl(t):
        line.set_ydata(yy(2 * np.pi * t / dur))  # 更新曲面
        return mplfig_to_npimage(fig_mpl) # 图形的RGB图像
    animation = mpy.VideoClip(make_frame_mpl, duration=dur)
    return animation.write_gif(chr, fps=120)
