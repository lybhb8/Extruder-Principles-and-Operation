# 附录D 熔体输送段的稳定性

在6.5节中，总产量已通过方程(6.50)用转速N和压力P表示：

$$
Q _ {\mathrm{Tot}} = A N - \frac {B P}{\eta}\tag{6.50}
$$

其中A和B是取决于螺杆与口模尺寸的常数(方程(6.51)和(6.52))。就本章目的而言，为方便起见定义：

$$
\begin{array}{r l} B ^ {\prime} & = B Z \\ & = \frac {b h ^ {3}}{1 2} \end{array}\tag{D.1}
$$

方程(6.50)变为：

$$
Q _ {\mathrm{Tot}} = A N - \frac {B ^ {\prime} P}{\eta Z}\tag{D.2}
$$

且方程(6.58)变为：

$$
Q _ {\mathrm{Tot}} \left(1 + \frac {B ^ {\prime}}{K Z}\right) = A N\tag{D.3}
$$

或：

$$
Q = \frac {A N K Z}{K Z + B ^ {\prime}}\tag{D.4}
$$

如果由于外部原因(如"凝胶点"向后移动)使熔体长度增加到 $Z + dz$ ，且口模常数K不变，则产量将变为 $Q + dq$ ，压力将变为 $P + dp$ 。此时：

$$
Q + \mathrm{d} q = \frac {A N K (Z + \mathrm{d} z)}{K (Z + \mathrm{d} z) + B ^ {\prime}}\tag{D.5}
$$

瞬时来看，熔融速率仍保持为Q，产量的变化代表一个附加体积 $bh \, dz$ 。因此，稳定操作要求对于给定的熔体长度变化，产量变化应最小化；这由 $dq/Q \, dt$ 表示。

将方程(D.4)代入(D.5)，得：

$$
\frac {\mathrm{d} q}{Q} = \frac {K Z + B ^ {\prime}}{K Z} \cdot \frac {K (Z + \mathrm{d} z)}{K (Z + \mathrm{d} z) + B ^ {\prime}} - 1\tag{D.6}
$$

于是：

$$
\begin{array}{r l} \frac {1}{Q} \frac {\mathrm{d} q}{\mathrm{d} t} & = \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {K Z + B ^ {\prime}}{K Z} \cdot \frac {K (Z + \mathrm{d} z)}{K (Z + \mathrm{d} z) + B ^ {\prime}}\right) \\ & = \frac {K Z + B ^ {\prime}}{K Z} \cdot \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {K (Z + \mathrm{d} z)}{K (Z + \mathrm{d} z) + B ^ {\prime}}\right) \\ & = \frac {K Z + B ^ {\prime}}{K Z} \cdot \frac {\mathrm{d}}{\mathrm{d} t} \left(1 - \frac {B ^ {\prime}}{K (Z + \mathrm{d} z) + B ^ {\prime}}\right) \\ & = \frac {K Z + B ^ {\prime}}{K Z} \left(\frac {B ^ {\prime} K}{(K (Z + \mathrm{d} z) + B ^ {\prime}) ^ {2}}\right) \frac {\mathrm{d} (\mathrm{d} z)}{\mathrm{d} t} \end{array}\tag{D.7}
$$

当dz/Z较小时：

$$
\begin{array}{r l} \frac {1}{Q} \cdot \frac {\mathrm{d} q}{\mathrm{d} t} & \simeq \frac {B ^ {\prime}}{Z (K Z + B ^ {\prime})} \cdot \frac {\mathrm{d} (\mathrm{d} z)}{\mathrm{d} t} \\ & = \frac {1}{Z \left(\frac {K Z}{B ^ {\prime}} + 1\right)} \cdot \frac {\mathrm{d} (\mathrm{d} z)}{\mathrm{d} t} \end{array}\tag{D.8}
$$

代入 $B'$ 后：

$$
\frac {1}{Q} \cdot \frac {\mathrm{d} q}{\mathrm{d} t} \simeq \frac {1}{Z \left(\frac {1 2 K Z}{b h ^ {3}} + 1\right)} \cdot \frac {\mathrm{d} (\mathrm{d} z)}{\mathrm{d} t}\tag{D.9}
$$

由方程(D.9)可见，如果槽深h减小，则dq/dt减小；同样，如果槽长Z增大，dq/dt也减小；这两种措施都会使熔体输送段在受到扰动(例如熔融速率与泵送速率之间的不平衡)时，产生幅值更小的产量和压力振荡(功率输入的振荡亦然)。

# 附录E 表格清单

2.1 挤出成形中使用的热塑性塑料 5  
2.2 加工要求的比较 25  
3.1 流动方程汇总 38  
4.1 热性能：换算系数与典型值 55  
5.1 阻尼常数 $n$ 的取值 71  
5.2 操作变量和几何变量对口模内流动条件的影响 122  
5.3 吹膜、流延膜、管材和异型材挤出口模相关问题的故障排除 124  
6.1 各种锥度 $h_1/h_2$ 螺杆的壁面剪切速率(由方程(6.69)求得)与无量纲产量的关系，以拖曳流动中螺杆末端剪切速率 $W/h_2$ 的比值表示 171  
7.1 加料试验所用的材料 177  
7.2 用于计算的螺杆几何参数 199  
8.1 熔体输送段中的热流 238  
8.2 螺棱间隙中的剪切加热与温升，表面阻力可忽略不计 250  
8.3 作为尺寸函数的产量和功率输入(恒定 $Q/Wbh$ )，由方程(8.11)、(8.12)和(8.24)-(8.27)求得 252  
8.4 机械功率随背压的变化(kW/转) 260  
8.5 能量平衡随背压的变化 264  
8.6 能量平衡随熔体温度和螺杆转速的变化 267  
9.1 螺杆类型示例(直径90 mm、单头螺纹、螺距等于直径(螺旋角 $17.6^{\circ}$ )) 294  
9.2 操作策略：需要提高产量 296  
9.3 操作策略：需要提高压力 297

9.4 操作策略：需要提高熔体温度 298  
9.5 操作策略：需要降低熔体温度 301  
9.6 操作策略：需要降低机械功率输入 304  
9.7 操作策略：需要减小熔体温度波动 307  
9.8 操作策略：需要改善熔融 311  
9.9 操作策略：需要改进混合 313  
10.1 螺杆在轴线平面和中间平面处的间隙面积 341  
10.2 单螺杆与双螺杆挤出机的比较 349  
11.1 各具体加工过程建议采用的条件 374  
11.2 单螺杆挤出机的放大：以 $Q / Wbh$ 为常数时各种放大策略效果汇总 378  
12.1 简单故障排查 385  
12.2 操作人员安全 390  
A.1 固态热性能(室温) 406  
B.1 台阶式螺杆中的压力梯度 421  
C.1 静态热损失 434  
C.2 热损失试验中的表面温度( $^\circ\text{C}$ ) 434  
C.3 表面传热系数：从料筒到聚合物 442  
C.4 若干阻力比 $m = k/hx$ 下螺棱中的径向导热 444  
C.5 牛顿流体在螺杆槽中的剪切加热 $\left( \times \frac{\eta W^2}{h^2} \, \text{W m}^{-3} \right)$ 452  
C.6 单位面积的累积剪切加热 $\left( \times \frac{\eta W^2}{h} \, \text{W m}^{-2} \right)$ 452  
C.7 横向速度与流量 454  
C.8 用于估算传热的径向微元 455  
C.9 转速1 rps、温度 $150^\circ\text{C}$ 下螺杆槽内径向传热的估算 456  
C.10 循环流动使槽内温差的减小 457  
C.11 转速1 rps、温度 $150^\circ\text{C}$ 下由方程(8.7)与C.4节所得槽内功率的比较 458  
C.12 螺棱间隙中的剪切加热 461  
C.13 螺棱通过时料筒内的径向温度分布 462  
C.14 料筒内"静停"期间的温度分布 465
