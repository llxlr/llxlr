import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
plt.rc('text', usetex=True)  # 支持LaTeX

fig = plt.figure(figsize=(8, 3))  # 新建画布
ax = axisartist.Subplot(fig, 111)  # 使用axisartist.Subplot方法创建一个绘图区对象ax
fig.add_axes(ax)  # 将绘图区对象添加到画布中

ax.axis[:].set_visible(False)  # 隐藏原来的实线矩形

ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
ax.axis["y"] = ax.new_floating_axis(1, 0, axis_direction="bottom")  # 添加y轴

ax.axis["x"].set_ticklabel_direction("+")
ax.axis["y"].set_ticklabel_direction("-")

ax.axis["x"].set_axisline_style("->", size=1.0)  # 给x坐标轴加箭头
ax.axis["y"].set_axisline_style("->", size=1.0)  # 给y坐标轴加箭头

plt.xlim(0, 7)  # 设置横坐标范围
plt.ylim(0, 1.1)  # 设置纵坐标范围
ax.set_xticks([0, np.pi/2, np.pi, (3*np.pi)/2, 2*np.pi],
              [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])  # 设置x轴刻度
ax.set_yticks([0, 1], ['', r'$Q$'])  # 设置y轴刻度

x = np.linspace(0, 2*np.pi, 100)
y = x*np.tan(x)
plt.plot(x, y, color="blue", linestyle='-')

# a_x = np.arange(0,2*np.pi,0.01)
# a = np.cos(a_x)
# b = np.sin(a_x)

# plt.plot(a, b, color="red", linestyle='--')
plt.show()
