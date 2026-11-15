# 项目风格库

## 01 微缩沙盘鸟瞰全景

参考图：`miniature-diorama-reference.png`

高角度鸟瞰，独立岛状模型底座，暖白纹理纸背景，建筑主体完整入画；细密树木、道路、人物形成微缩尺度。柔和日光，写实材质与手工沙盘感，底部独立木质铭牌。第一组 10 张球场图采用此风格，位于 `images/miniature-diorama/`。

## 02 复古建筑手绘研究图

参考图：`vintage-architectural-study-reference.png`

保存范围：原图、风格描述、可复用提示词。已生成同样 10 家俱乐部的球场图，位于 `images/vintage-architectural-study/`，实际提示词见 `prompts/vintage-architectural-study-prompts.json`。

- 底材：暖米黄旧纸、可见纤维与细微斑驳，整体低饱和。
- 笔触：精细钢笔与铅笔建筑线稿，交叉排线，淡水彩晕染；保留辅助构图线。
- 配色：石灰褐、暖灰、浅赭石为主，灰蓝水面与天空；主题颜色少量点缀。
- 构图：中央大幅透视主体占主要面积，四周穿插立面、局部构件、结构示意、环境鸟瞰等小图。小图之间用自然留白连接，不使用现代卡片边框。
- 文字：左上大号手写英文建筑名称与城市，小号衬线副标题；局部细节配轻盈手写标签。
- 氛围：建筑师旅行手账、历史建筑测绘图册、收藏级水彩建筑插画。
- 避免：照片质感、3D 沙盘、饱和霓虹、厚重数字描边、现代信息图卡片、密集装饰、无意义文字。

### 可复用提示词

Create a square vintage architectural study sheet of [BUILDING / STADIUM] in [CITY, COUNTRY]. Use the saved Tower Bridge image as a STYLE AND COMPOSITION reference only; replace its subject with the requested building. Warm aged ivory parchment with subtle paper fibers and patina. Intricate graphite and fine sepia ink architectural drawing, delicate crosshatching, restrained translucent watercolor washes in warm stone, muted gray, pale ochre and dusty blue. A large accurate three-quarter perspective view dominates the center, with atmospheric surroundings fading into the paper. Arrange a small elevation drawing, two meaningful architectural detail studies, one structural diagram and a tiny contextual aerial sketch around the margins. Fine construction lines, faint measurement marks and a small compass rose. Elegant handwritten title at upper left: "[BUILDING]", smaller handwritten location: "[CITY, COUNTRY]", and spaced serif subtitle: "ARCHITECTURAL STUDY". Short accurate handwritten labels near each detail. Balanced airy editorial composition, convincing architectural proportions, exquisite handmade texture. No photorealism, no 3D miniature rendering, no modern UI panels, no watermark. Do not copy Tower Bridge towers or bridge elements into unrelated subjects.

### 应用于足球场

中心主图展示球场最具辨识度的外立面与屋顶；辅图选择看台剖面、屋顶桁架、外立面构件、入口细节和球场总平面。球队配色仅作低饱和点缀。具体建筑结构需按球场实际特征设定。


## 03 高细节城市微缩海报

参考图：`city-miniature-poster-reference.png`

完整通用模板见 [CITY_MINIATURE_POSTER.md](CITY_MINIATURE_POSTER.md)。白底竖版海报、超大凝练标题、顶部小型天际线、下方高细节立体城市沙盘与深色底座。风格适用于城市、景区、校园、文化主题与其他地理场景，不绑定足球或球队。

首个示例：`images/city-miniature-posters/liverpool-city-panorama.png`，以利物浦城市地标为主景。


## 04 复古水彩文旅拼景海报

参考图：`vintage-watercolor-travel-collage-reference.png`

完整规则与通用模板见 [vintage-watercolor-travel-collage.md](vintage-watercolor-travel-collage.md)。旧纸水彩、超大衬线标题、云雾过渡的多地标景观、自然与文化静物融合；适用于各地文旅主题。已有文旅海报与照片转绘示例，成图位于 `images/vintage-watercolor-travel-collage/`。

## 05 现代数字风景插画

完整规则与通用模板见 [modern-digital-landscape.md](modern-digital-landscape.md)。清晰色块、受控渐变、冷暖对比与通透光影。首个样例为终南山银杏秋景；`modern-digital-landscape-reference.png` 是生成样张的原始副本，用于风格复用。
