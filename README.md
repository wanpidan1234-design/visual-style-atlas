# Visual Style Atlas

通用图像风格库：保存参考图、可复用风格规则、实际生成提示词与成图示例。主题可以是城市、建筑、景区、校园、体育或其他场景；足球场只是第一批示例。

Reusable visual styles, references, prompts, and generated examples across subjects.

当前收录 **4 种风格、24 张成图、5 张参考图（含 1 张主体照片）**，成图均由内置 `image_gen` 生成。

## 风格目录

| 风格 | 视觉特征 | 示例 | 提示词 |
| --- | --- | --- | --- |
| [微缩沙盘鸟瞰全景](styles/STYLE_GUIDE.md) | 暖白纸背景、独立模型底座、细密景观、木质铭牌 | 10 张球场图 | [完整提示词](prompts/stadium-prompts.json) |
| [复古建筑手绘研究图](styles/STYLE_GUIDE.md) | 旧纸、钢笔线稿、淡水彩、建筑细节分图 | 10 张球场图 | [完整提示词](prompts/vintage-architectural-study-prompts.json) |
| [高细节城市微缩海报](styles/CITY_MINIATURE_POSTER.md) | 白底大标题、立体城市沙盘、精密街区和地标 | 利物浦城市全景 | [完整提示词](prompts/liverpool-city-poster.json) |
| [复古水彩文旅拼景海报](styles/vintage-watercolor-travel-collage.md) | 旧纸、大衬线标题、云雾连接的多地标山水与文化静物 | 美国、云南与樱花山林 | [可复用模板](prompts/vintage-watercolor-travel-collage-template.json) |

## 复古水彩文旅海报

| 美国 | 云南 |
| --- | --- |
| <a href="images/vintage-watercolor-travel-collage/united-states-travel-poster.png"><img src="images/vintage-watercolor-travel-collage/united-states-travel-poster.png" width="360" alt="美国复古水彩文旅海报"></a> | <a href="images/vintage-watercolor-travel-collage/yunnan-travel-poster.png"><img src="images/vintage-watercolor-travel-collage/yunnan-travel-poster.png" width="360" alt="云南复古水彩文旅海报"></a> |

实际提示词：[美国复古水彩文旅海报](prompts/vintage-watercolor-travel-collage/united-states-travel-poster.json) · [云南复古水彩文旅海报](prompts/vintage-watercolor-travel-collage/yunnan-travel-poster.json)

## 樱花山林：照片转绘

将用户提供的红顶建筑与樱花山林照片转绘为风格 4，保留主体和构图；未标注未经确认的地点。

<a href="images/vintage-watercolor-travel-collage/sakura-forest-watercolor-poster.png"><img src="images/vintage-watercolor-travel-collage/sakura-forest-watercolor-poster.png" width="480" alt="樱花山林水彩海报"></a>

[主体原始照片](styles/references/vintage-watercolor-travel-collage-12e6470cebe31a76.png) · [实际提示词与参考角色](prompts/vintage-watercolor-travel-collage/sakura-forest-watercolor-poster.json)

## 利物浦城市全景

以城市地标为主景：皇家利物大厦、阿尔伯特码头、利物浦博物馆、两座大教堂、圣乔治大厅与默西河。

<a href="images/city-miniature-posters/liverpool-city-panorama.png"><img src="images/city-miniature-posters/liverpool-city-panorama.png" width="650" alt="利物浦城市微缩海报"></a>

## 球场案例：两种风格对照

点击图片查看原图。

| 俱乐部 | 微缩沙盘 | 复古建筑手绘 |
| --- | --- | --- |
| Real Madrid | <a href="images/miniature-diorama/01-real-madrid-bernabeu.png"><img src="images/miniature-diorama/01-real-madrid-bernabeu.png" width="260" alt="Real Madrid 微缩沙盘"></a> | <a href="images/vintage-architectural-study/01-real-madrid-bernabeu.png"><img src="images/vintage-architectural-study/01-real-madrid-bernabeu.png" width="260" alt="Real Madrid 复古建筑手绘"></a> |
| FC Barcelona | <a href="images/miniature-diorama/02-barcelona-camp-nou.png"><img src="images/miniature-diorama/02-barcelona-camp-nou.png" width="260" alt="FC Barcelona 微缩沙盘"></a> | <a href="images/vintage-architectural-study/02-barcelona-camp-nou.png"><img src="images/vintage-architectural-study/02-barcelona-camp-nou.png" width="260" alt="FC Barcelona 复古建筑手绘"></a> |
| Manchester United | <a href="images/miniature-diorama/03-manchester-united-old-trafford.png"><img src="images/miniature-diorama/03-manchester-united-old-trafford.png" width="260" alt="Manchester United 微缩沙盘"></a> | <a href="images/vintage-architectural-study/03-manchester-united-old-trafford.png"><img src="images/vintage-architectural-study/03-manchester-united-old-trafford.png" width="260" alt="Manchester United 复古建筑手绘"></a> |
| Liverpool FC | <a href="images/miniature-diorama/04-liverpool-anfield.png"><img src="images/miniature-diorama/04-liverpool-anfield.png" width="260" alt="Liverpool FC 微缩沙盘"></a> | <a href="images/vintage-architectural-study/04-liverpool-anfield.png"><img src="images/vintage-architectural-study/04-liverpool-anfield.png" width="260" alt="Liverpool FC 复古建筑手绘"></a> |
| Arsenal FC | <a href="images/miniature-diorama/05-arsenal-emirates.png"><img src="images/miniature-diorama/05-arsenal-emirates.png" width="260" alt="Arsenal FC 微缩沙盘"></a> | <a href="images/vintage-architectural-study/05-arsenal-emirates.png"><img src="images/vintage-architectural-study/05-arsenal-emirates.png" width="260" alt="Arsenal FC 复古建筑手绘"></a> |
| Chelsea FC | <a href="images/miniature-diorama/06-chelsea-stamford-bridge.png"><img src="images/miniature-diorama/06-chelsea-stamford-bridge.png" width="260" alt="Chelsea FC 微缩沙盘"></a> | <a href="images/vintage-architectural-study/06-chelsea-stamford-bridge.png"><img src="images/vintage-architectural-study/06-chelsea-stamford-bridge.png" width="260" alt="Chelsea FC 复古建筑手绘"></a> |
| FC Bayern Munich | <a href="images/miniature-diorama/07-bayern-allianz-arena.png"><img src="images/miniature-diorama/07-bayern-allianz-arena.png" width="260" alt="FC Bayern Munich 微缩沙盘"></a> | <a href="images/vintage-architectural-study/07-bayern-allianz-arena.png"><img src="images/vintage-architectural-study/07-bayern-allianz-arena.png" width="260" alt="FC Bayern Munich 复古建筑手绘"></a> |
| Juventus FC | <a href="images/miniature-diorama/08-juventus-allianz-stadium.png"><img src="images/miniature-diorama/08-juventus-allianz-stadium.png" width="260" alt="Juventus FC 微缩沙盘"></a> | <a href="images/vintage-architectural-study/08-juventus-allianz-stadium.png"><img src="images/vintage-architectural-study/08-juventus-allianz-stadium.png" width="260" alt="Juventus FC 复古建筑手绘"></a> |
| AC Milan | <a href="images/miniature-diorama/09-ac-milan-san-siro.png"><img src="images/miniature-diorama/09-ac-milan-san-siro.png" width="260" alt="AC Milan 微缩沙盘"></a> | <a href="images/vintage-architectural-study/09-ac-milan-san-siro.png"><img src="images/vintage-architectural-study/09-ac-milan-san-siro.png" width="260" alt="AC Milan 复古建筑手绘"></a> |
| Inter Milan | <a href="images/miniature-diorama/10-inter-san-siro.png"><img src="images/miniature-diorama/10-inter-san-siro.png" width="260" alt="Inter Milan 微缩沙盘"></a> | <a href="images/vintage-architectural-study/10-inter-san-siro.png"><img src="images/vintage-architectural-study/10-inter-san-siro.png" width="260" alt="Inter Milan 复古建筑手绘"></a> |

## 复用方式

1. 在 `styles/` 中选取参考图和风格说明。
2. 替换提示词里的主题、地标、地区、配色与标题文字。
3. 按主题和风格分别保存成图，并记录实际使用的提示词。
4. 更新 `catalog.json` 中的索引。

## 可复用 Skill

项目包含可安装的 [visual-style-atlas skill](skills/visual-style-atlas/SKILL.md)，提供上面四种风格选项，覆盖主题替换、参考图使用、批量生成、视觉检查和完整归档。

新风格自动入库：提供新参考用于生成或保存时，自动保存原图、提炼通用模板，更新风格目录与 skill 选项，并同步本机安装副本。风格持续追加，主题变化沿用已有风格；所有成图和实际提示词均保存在项目中。

把 `skills/visual-style-atlas` 文件夹复制到个人 Codex skills 目录后，可这样调用：

```text
用 $visual-style-atlas 的风格 3，生成一张杭州城市微缩海报，保存到项目。
用 $visual-style-atlas 的复古建筑手绘风格，为这三座建筑各生成一张。
```

`scripts/register_image.py` 归档脚本需要 Python 和 Pillow；它只复制与校验图片，记录提示词和更新索引，不调用生成 API。本项目按 [AGENTS.md](AGENTS.md) 在代码及 skill 修改完成并检查通过后自动提交、直接推送，默认不创建 PR；其他项目遵循各自的规则和用户授权。

## 文件组织

```text
images/
  miniature-diorama/
  vintage-architectural-study/
  city-miniature-posters/
styles/
prompts/
skills/visual-style-atlas/
catalog.json
image-verification.json
```

`image-verification.json` 记录全部 24 张成图的尺寸及 SHA-256。图片已检查可读取，复制过程已校验完整性；压缩包保存在本地，仓库直接保存原图以便预览与下载。

诺坎普采用经典改建前外观；米兰双雄为同一球场的不同球队氛围版本。图像和细节分图属于艺术化表现，地理距离可为构图压缩，不作为精确地图或建筑工程图。
