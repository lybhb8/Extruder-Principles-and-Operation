=======
1 介绍
=======


1.1 范围和局限性
`````````````````
 
本书旨在总结塑料和橡胶螺杆挤出工艺的原理、实际性能及其理论解释，以及利用这种性能的操作程序。
与设计不同，后者在现有文献中没有很好地涉及。

本书旨在为有效的实际操作做出原创性贡献，因此并不试图全面回顾文献，而只是参考那些有助于理解操作的著作。

工作范围包括螺杆挤出机作为主机、与模头的组合、作为整个制造过程的一部分（包括混料和排气等辅助功能）的原理和操作。
它包括对挤出机个别工艺的特殊要求，如包线、管状薄膜吹塑和吹塑成型，但不包括这些工艺的其他方面。
为了在一本篇幅合理的书中充分涵盖目标，某些事项被排除在外，读者可参阅书后的参考文献以获取更多信息。
特别是螺杆挤出机的机械结构和特殊用途的改装，部分受第 2 章所述工艺要求的制约，但也受标准化、制造方法和机械可靠性的制约。Fisher (1976) 第 6 章和 Schenkel (1966) 第 6 章对机械结构进行了阐述。Fisher 和 Schenkel 以及《塑料与橡胶周刊\*》等定期刊物也介绍了挤出机的商业模型和非常规类型。由于本书主要涉及操作，它并不打算成为一本为特定性能精确设计机器、螺杆或模头尺寸的手册。包括 Fenner（1970 年）在内的多位作者已对此进行了阐述。


\*Plastics and Rubber Weekly, Maclaren and Sons Ltd, London .


1.2 方法
```````````````

首先概述了一些实用的挤出工艺，以及它们对挤出机和模头的要求。然后介绍了相关的质量和热流一般方程，并阐述了它们在挤出问题中的应用。解释了适合挤出的塑料和橡胶材料特性的重要性，特别是聚合物熔体的流动和热特性。然后为挤出机的设计和操作建立了流动方程。针对单螺杆挤出机的质量流量和能量消耗，提出了简化的挤出理论，并以代数和图表形式展示了尺寸和操作变量对产量、能量平衡、熔体温度和产品均匀性的影响。利用这些影响提出操作策略，以优化挤出机的性能。然后简要介绍了双螺杆挤出机的一般原理和操作。随后讨论挤出机的操作和控制，以消除整个系统的故障。特别是研究了将挤出工艺从实验室开发升级到大规模生产的问题。尽管简化理论是近似的，但其预测在很大程度上得到了实践的证实。与更精确的方法相比，简化理论更适用于更精确的方法，因为解的代数形式允许随时识别和理解不同变量对挤出机和模头性能的影响；而更精确的方法通常涉及数字计算，往往会掩盖这一点。
作为稳态运行分析的补充，还根据实际经验给出了启动、停机、拆卸和清洁的建议。

塑料和橡胶挤出的整个商业流程包括将聚合物原料（通常为粉末或颗粒状）转化为可销售的成品或半成品。这包括与许多其他材料和工艺相同的管理和工厂组织事项。它还包括聚合物处理和储存、产品规格和质量控制、工厂布局、安装和维护、产品加工、组装、包装和分销，
所有这些都是许多塑料加工过程中的一般问题，与挤出的实际操作只是间接相关。本册的目的是提供挤出工艺的具体要求及其解释，这些要求和解释构成了整个工艺及其外围方面的技术背景。作为对稳态运行分析的补充，本册还根据实际经验给出了有关启动、停机、拆除和清洁的建议。
塑料和橡胶挤出的整个商业流程包括将原料聚合物（通常为粉末或颗粒状）转化为可销售的成品或半成品。这包括与许多其他材料和工艺相同的管理和工厂组织事项。它还包括聚合物处理和储存、产品规格和质量控制、工厂布局、安装和维护、产品加工、组装、包装和分销，所有这些都是许多塑料加工过程中的一般问题，
与挤出的实际操作只是间接相关。本册的目的是提供挤出的具体要求及其解释，这构成了整个工艺及其外围方面的技术背景。

最简单地说，挤出是将液态（通常为熔融状态）聚合物在压力作用下通过模头挤出，形成连续的断面或轮廓。然后可对其进行定型、拉伸、波纹等处理，以改变和控制断面的形状和尺寸，有时还可改变其性能（机械性能、光学性能等）。
就热塑性塑料而言，产品或挤出物必须经过冷却才能保持形状，而橡胶则要经过化学交联（固化）才能获得弹性、耐化学腐蚀性和耐热性等特性。在某些工艺中，例如吹塑、注塑和在线真空成型，挤出物在冷却或固化前可能会被塑造成不连续或间断的形状。其他辅助工序，如印刷、分切和在线测试，可在卷绕或切割成可处理的长度之前进行。
模头后的这些操作（统称为后成型）的细节与材料和产品的具体情况密切相关，其中很多都是各公司的机密，因此篇幅有限，无法在此进行详尽研究。不过 ， 然而，挤出机对产品的 "质量"、尺寸和表面光洁度同样重要；了解牵引率与挤出机产量之比的影响对经济生产至关重要。模头后变化的影响通常是可见的，甚至是不言而喻的，但人们无法看到挤出机内部发生了什么，
本书旨在提供有助于解释螺杆和模头性能的基本机制，以及它们与后成型操作之间的相互作用。本书还介绍了操作策略（第 9 章和第 10 章）和控制策略（第 11 章），以及螺杆选择、启动、清洁和故障查找方面的一些实践经验（第 11 章和第 12 章）。

对于开发工程师来说，一个重要的课题是如何根据小型实验室工艺预测大规模生产设备的性能，因为重型移动机械的性质决定了其改装或更换成本高昂，而且由于特殊材料和制造工艺，改装会导致长时间和高成本的生产延误。参考文献按字母顺序排列在书末。数学公式按出现顺序编号，每章和附录分别编号。全文均使用国际单位(SI)，含有有绝对单位制(CGS)或 英尺.磅.秒 `(FPS) <https://handwiki.org/wiki/Foot%E2%80%93pound%E2%80%93second_system>`_。除非另有说明，数字常量都是无量纲的，因此在任何一致的单位系统中都是相同的。
