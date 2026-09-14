# 后记

一本书的中文版，从动念到成书，我们走了三年。

2023 年秋天，当这个仓库第一次被创建时，它不过是一个 README 加一份 LICENSE，像所有刚开张的开源项目一样朴素。彼时手里摊开的，是 M. J. Stevens 与 J. A. Covas 合著的《Extruder Principles and Operation》——1995 年的第二版，一本在塑料挤出领域被翻旧了的经典。国内讲挤出工艺的书不少，但像这样"以理论和经验为基础，帮助生产者让设备发挥最佳性能，并清醒认识其局限"的写法，并不多见。它不回避数学，却又坚持"数学方法仅限于阐明无法用语言表达的效果"；它面向车间里的工程师，也面向院校里高分子材料加工机械专业的学生。这样的书，值得有一本像样的中文版。

具体到这本中文版，三年可以压成了一条时间线。

## 三年时间线

- **2023 年 9 月** — 项目启动。第一件事是拆书：[MinerU](https://github.com/opendatalab/MinerU)（上海人工智能实验室开源的文档解析工具）把英文版 PDF 拆成结构化文本——公式转成 LaTeX、表格与图片按版式切分。对一本满是流体力学方程与工艺对照表的书，这一步省去了大量手抄。
- **2023 年下半年–2024 年** — 启动期。翻译依赖 [DeepL](https://www.deepl.com/translator) 网页版与谷歌翻译，彼时 DeepL 对国内用户并不友好，几乎拿不到接口，全书是无数个"Ctrl + C"与"Ctrl + V"一屏一屏堆砌出来的，还得不时提防字符编码捣乱。process、flow、viscosity、slit 等早期章节相继入库；之后 2024 年全年几乎只有 README 的零星维护。翻译的马拉松，跑一段停一段，是常态。
- **2025 年初** — 第 3、4、5 章密集提交。3.2.3、4.0、5.30、5.6……一个个章号从提交信息里跳过，像施工进度表上的对勾。
- **2026 年初** — 转机。DeepL 向国内客户开放了 API Key 并附赠免费额度，翻译终于从手工 Ctrl+C/Ctrl+V 变成了接口批量调用，速度陡增；第 6、7 章随之跟上。
- **2026 年 8 月** — 重构为编号章节结构，第 8 章图片的链接路径从反斜杠和绝对路径统一改为相对路径；8 月 28 日，提交信息里出现了"trans_end"——翻译主体，至此画上句号。
- **2026 年 9 月** — 收尾与校译。第 9–12 章、附录、索引相继补齐；公式渲染修正（`\mathbf` → `\mathrm`）、术语统一（"模具" → "模头"）、表格翻译、50 张配图进库。

但"画上句号"在翻译这件事上从来只是修辞。翻译主体完成之后，紧接着是更漫长、更琐碎的第二战场：校译。

"翻译易，校译难"，这六个字是三年里最深的体会。2026 年 9 月的两次提交格外能说明问题：一次是公式渲染的修正——`\mathbf` 换成 `\mathrm`，让数学符号在网页上站得更直；一次是把全书术语里的"模具"统一改为"模头"。这些修改单看都小，连起来却是几十上百处。还有 52 条交叉引用警告的逐条清零、附录 E 表格清单 47 条链接的逐一打通、20 个表格锚点的补建、50 张配图的进库、1680 行目录索引的整理……我们为这本书修的，远不止翻译。

技术栈同样经历了一番取舍，最终落在 Sphinx 7.1.2 + MyST（markdown-it-py 驱动的 Markdown 解析）+ ReadTheDocs 官方主题 sphinx-rtd-theme，辅以 sphinx_copybutton 与 sphinx_design。源码用 Markdown 与 reStructuredText 混写，数学公式由 MyST 解析，构建环境由 `.readthedocs.yaml` 声明（Ubuntu 22.04 + Python 3.10）。全书如今约一万六千行——12 章正文，外加附录 A（聚合物热与流动性能，单文件便超过两千行)、附录 B 与 C、附录 D/E、参考文献与目录索引，图片七百余张。从最初那个只装着 README 的仓库，到这份体量，恰好是三年。

部署上，这本书托管在 GitHub，以 GPL-3.0 协议开源，由 ReadTheDocs 自动构建发布——中文版在线随时可读，免费、无需登录、浏览器打开即是。英文原版 PDF 也一并分享，供对照查阅。开源的初衷很简单：它始于工具，也理应回到每一个需要它的人手里。

当然，必须诚实地说：机器翻译的底色、业余校译的局限，决定了这版中文仍有许多术语不当之处。读者若是发现错漏，欢迎在仓库提交 Issue 或 Pull Request。这正是我们选择 GPL-3.0 的原因——一本书的生命，不在封笔那一刻，而在它被阅读、被挑错、被改进的漫长过程里。

三年，五十二次提交，一部经典的中文版。它还很年轻，也还有很长的路要走。

## 相关链接

**本书与源码**

- 中文版在线阅读（ReadTheDocs）：<https://extruder-principles-and-operation.readthedocs.io/zh-cn/latest/>
- 源代码仓库（GitHub）：<https://github.com/lybhb8/Extruder-Principles-and-Operation>
- 开源协议：<https://github.com/lybhb8/Extruder-Principles-and-Operation/blob/main/LICENSE>（GPL-3.0）
- 英文原版（1995 第二版）下载：<https://www.aliyundrive.com/s/UkTJ9axrtRQ>

**PDF 解析**

- MinerU（文档解析工具）：<https://github.com/opendatalab/MinerU>

**机器翻译**

- DeepL（翻译 API 与网页版）：<https://www.deepl.com/translator>
- DeepL API 文档：<https://www.deepl.com/pro-api>
- Google 翻译：<https://translate.google.com/>

**文档构建与主题**

- Sphinx：<https://www.sphinx-doc.org/>
- MyST（myst-parser，Markdown 解析）：<https://myst-parser.readthedocs.io/>
- markdown-it-py：<https://markdown-it-py.readthedocs.io/>
- sphinx-rtd-theme（ReadTheDocs 主题）：<https://sphinx-rtd-theme.readthedocs.io/>
- sphinx_copybutton：<https://sphinx-copybutton.readthedocs.io/>
- sphinx_design：<https://sphinx-design.readthedocs.io/>

**部署平台**

- ReadTheDocs：<https://readthedocs.org/>
- .readthedocs 配置文件说明：<https://docs.readthedocs.io/en/stable/config-file/v2.html>