# 附录D 熔体输送段的稳定性

在6.5节中，总产量已通过方程(6.50)用转速N和压力P表示：

$$
Q _ {\mathrm{Tot}} = A N - \frac {B P}{\eta}\tag{6.50}
$$

其中A和B是取决于螺杆与口模尺寸的常数(方程(6.51)和(6.52))。就本章目的而言，为方便起见定义：

$$
B ^ {\prime} = B Z \quad = \frac {b h ^ {3}}{1 2}\tag{D.1}
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
\frac {1}{Q} \frac {\mathrm{d} q}{\mathrm{d} t} = \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {K Z + B ^ {\prime}}{K Z} \cdot \frac {K (Z + \mathrm{d} z)}{K (Z + \mathrm{d} z) + B ^ {\prime}}\right) = \frac {K Z + B ^ {\prime}}{K Z} \cdot \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {K (Z + \mathrm{d} z)}{K (Z + \mathrm{d} z) + B ^ {\prime}}\right) = \frac {K Z + B ^ {\prime}}{K Z} \cdot \frac {\mathrm{d}}{\mathrm{d} t} \left(1 - \frac {B ^ {\prime}}{K (Z + \mathrm{d} z) + B ^ {\prime}}\right) = \frac {K Z + B ^ {\prime}}{K Z} \left(\frac {B ^ {\prime} K}{(K (Z + \mathrm{d} z) + B ^ {\prime}) ^ {2}}\right) \frac {\mathrm{d} (\mathrm{d} z)}{\mathrm{d} t}\tag{D.7}
$$

当dz/Z较小时：

$$
\frac {1}{Q} \cdot \frac {\mathrm{d} q}{\mathrm{d} t} \simeq \frac {B ^ {\prime}}{Z (K Z + B ^ {\prime})} \cdot \frac {\mathrm{d} (\mathrm{d} z)}{\mathrm{d} t} = \frac {1}{Z \left(\frac {K Z}{B ^ {\prime}} + 1\right)} \cdot \frac {\mathrm{d} (\mathrm{d} z)}{\mathrm{d} t}\tag{D.8}
$$

代入 $B'$ 后：

$$
\frac {1}{Q} \cdot \frac {\mathrm{d} q}{\mathrm{d} t} \simeq \frac {1}{Z \left(\frac {1 2 K Z}{b h ^ {3}} + 1\right)} \cdot \frac {\mathrm{d} (\mathrm{d} z)}{\mathrm{d} t}\tag{D.9}
$$

由方程(D.9)可见，如果槽深h减小，则dq/dt减小；同样，如果槽长Z增大，dq/dt也减小；这两种措施都会使熔体输送段在受到扰动(例如熔融速率与泵送速率之间的不平衡)时，产生幅值更小的产量和压力振荡(功率输入的振荡亦然)。

# 附录E 表格清单

{ref}`2.1 挤出成形中使用的热塑性塑料 <table-2-1>` 5  
{ref}`2.2 加工要求的比较 <table-2-2>` 25  
{ref}`3.1 流动方程汇总 <table-3-1>` 38  
{ref}`4.1 热性能：换算系数与典型值 <table-4-1>` 55  
{ref}`5.1 阻尼常数 $n$ 的取值 <table-5-1>` 71  
{ref}`5.2 操作变量和几何变量对口模内流动条件的影响 <table-5-2>` 122  
{ref}`5.3 吹膜、流延膜、管材和异型材挤出口模相关问题的故障排除 <table-5-3>` 124  
{ref}`6.1 各种锥度 $h_1/h_2$ 螺杆的壁面剪切速率(由方程(6.69)求得)与无量纲产量的关系，以拖曳流动中螺杆末端剪切速率 $W/h_2$ 的比值表示 <table-6-1>` 171  
{ref}`7.1 加料试验所用的材料 <table-7-1>` 177  
{ref}`7.2 用于计算的螺杆几何参数 <table-7-2>` 199  
{ref}`8.1 熔体输送段中的热流 <table-8-1>` 238  
{ref}`8.2 螺棱间隙中的剪切加热与温升，表面阻力可忽略不计 <table-8-2>` 250  
{ref}`8.3 作为尺寸函数的产量和功率输入(恒定 $Q/Wbh$ )，由方程(8.11)、(8.12)和(8.24)-(8.27)求得 <table-8-3>` 252  
{ref}`8.4 机械功率随背压的变化(kW/转) <table-8-4>` 260  
{ref}`8.5 能量平衡随背压的变化 <table-8-5>` 264  
{ref}`8.6 能量平衡随熔体温度和螺杆转速的变化 <table-8-6>` 267  
{ref}`9.1 螺杆类型示例(直径90 mm、单头螺纹、螺距等于直径(螺旋角 $17.6^{\circ}$ )) <table-9-1>` 294  
{ref}`9.2 操作策略：需要提高产量 <table-9-2>` 296  
{ref}`9.3 操作策略：需要提高压力 <table-9-3>` 297  

{ref}`9.4 操作策略：需要提高熔体温度 <table-9-4>` 298  
{ref}`9.5 操作策略：需要降低熔体温度 <table-9-5>` 301  
{ref}`9.6 操作策略：需要降低机械功率输入 <table-9-6>` 304  
{ref}`9.7 操作策略：需要减小熔体温度波动 <table-9-7>` 307  
{ref}`9.8 操作策略：需要改善熔融 <table-9-8>` 311  
{ref}`9.9 操作策略：需要改进混合 <table-9-9>` 313  
{ref}`10.1 螺杆在轴线平面和中间平面处的间隙面积 <table-10-1>` 341  
{ref}`10.2 单螺杆与双螺杆挤出机的比较 <table-10-2>` 349  
{ref}`11.1 各具体加工过程建议采用的条件 <table-11-1>` 374  
{ref}`11.2 单螺杆挤出机的放大：以 $Q / Wbh$ 为常数时各种放大策略效果汇总 <table-11-2>` 378  
{ref}`12.1 简单故障排查 <table-12-1>` 385  
{ref}`12.2 操作人员安全 <table-12-2>` 390  
{ref}`A.1 固态热性能(室温) <table-a-1>` 406  
{ref}`B.1 台阶式螺杆中的压力梯度 <table-b-1>` 421  
{ref}`C.1 静态热损失 <table-c-1>` 434  
{ref}`C.2 热损失试验中的表面温度( $^\circ\text{C}$ ) <table-c-2>` 434  
{ref}`C.3 表面传热系数：从料筒到聚合物 <table-c-3>` 442  
{ref}`C.4 若干阻力比 $m = k/hx$ 下螺棱中的径向导热 <table-c-4>` 444  
{ref}`C.5 牛顿流体在螺杆槽中的剪切加热 $\left( \times \frac{\eta W^2}{h^2} \, \text{W m}^{-3} \right)$ <table-c-5>` 452  
{ref}`C.6 单位面积的累积剪切加热 $\left( \times \frac{\eta W^2}{h} \, \text{W m}^{-2} \right)$ <table-c-6>` 452  
{ref}`C.7 横向速度与流量 <table-c-7>` 454  
{ref}`C.8 用于估算传热的径向微元 <table-c-8>` 455  
{ref}`C.9 转速1 rps、温度 $150^\circ\text{C}$ 下螺杆槽内径向传热的估算 <table-c-9>` 456  
{ref}`C.10 循环流动使槽内温差的减小 <table-c-10>` 457  
{ref}`C.11 转速1 rps、温度 $150^\circ\text{C}$ 下由方程(8.7)与C.4节所得槽内功率的比较 <table-c-11>` 458  
{ref}`C.12 螺棱间隙中的剪切加热 <table-c-12>` 461  
{ref}`C.13 螺棱通过时料筒内的径向温度分布 <table-c-13>` 462  
{ref}`C.14 料筒内"静停"期间的温度分布 <table-c-14>` 465  
