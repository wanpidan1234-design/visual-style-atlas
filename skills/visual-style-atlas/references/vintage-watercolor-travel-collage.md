# 复古水彩文旅拼景海报

风格 ID：`vintage-watercolor-travel-collage`；选项编号：4。

## 视觉规则

- **画幅与底材**：优先 4:5 竖版，暖米白旧纸，细纤维与轻微斑驳，柔和留白。
- **媒介**：细密写实水彩与轻钢笔勾线，纸面渗色和矿物色层次；保持插画感。
- **标题层级**：顶部当地文字小标题、超大优雅衬线主标题、字距较宽的小号副标题。主标题可用古铜褐色；文字内容按用户主题替换。
- **构图**：将多处自然景观、建筑和文化符号合成一幅连续梦境；前中后景尺度有变化，以山雾、水面、植物与淡彩过渡连接，不用矩形分格。
- **叙事路线**：中央山水、道路或水系引导视线；两侧安排主要地标，前景放少量可触摸的文化静物，让密集细节仍有主次。
- **配色**：灰蓝、矿物绿、暖赭、米白为主，桃粉或朱红少量点缀，整体低饱和而富层次。
- **注记与装饰**：少量手写地名、细线角花，可选底部短句；印章和书法仅在文化语境适合时使用。
- **题材范围**：国家、地区、城市、旅行路线、自然与文化主题；示例中的中国、熊猫、长城、茶具和食物均为可替换内容。

## 与已有选项的区别

选项 2 用单体建筑主视图配立面、剖面等研究小图；本风格用云雾和景观连续衔接多处地点与文化静物，突出旅行意境。选项 3 使用白底大标题和立体模型底座；本风格采用平面水彩纸面。

## 可替换参数

`DESTINATION`、`REGION`、`LOCAL_TITLE`、`MAIN_TITLE`、`SUBTITLE`、`NATURAL_LANDSCAPES`、`LANDMARKS`、`WILDLIFE_AND_PLANTS`、`CULTURAL_OBJECTS_AND_FOOD`、`SHORT_LABELS`、`FOOTER`。

通常选取 3–6 个核心地标，文化静物与动物不必全部出现。无适合内容的可选参数直接省略，不编造地方文化或把参考图中的中国元素硬套到其他地区。需要中文标题时明确给出文字；无需文字时删去标题段。

## 可复用提示词

```text
Create one refined vertical 4:5 vintage watercolor travel-collage poster celebrating [DESTINATION], [REGION]. Use the supplied reference image only for its medium, typography hierarchy, atmospheric composition and paper texture; replace its geographic and cultural subject matter with the requested destination.

Warm ivory aged paper with subtle visible fibers, fine realistic ink and watercolor illustration, muted mineral greens, dusty blue-gray, warm ochre and soft peach accents. At the top, a small culturally appropriate local-language heading "[LOCAL_TITLE]", a monumental elegant serif display title "[MAIN_TITLE]" in muted antique brown, and a widely spaced small serif subtitle "[SUBTITLE]". Keep text legible with generous breathing room.

Build a single seamless dreamlike landscape collage: [NATURAL_LANDSCAPES] flow through foreground, middle distance and hazy background, interwoven with recognizable [LANDMARKS] at carefully varied scales. Use mist, water, hills, foliage or soft watercolor edges to join different places without boxed panels. Create an inviting central visual route through the scene. Place culturally and geographically appropriate [WILDLIFE_AND_PLANTS] as optional supporting accents, and a small foreground arrangement of [CULTURAL_OBJECTS_AND_FOOD] with exquisite material detail. Keep the composition rich but hierarchical, with quiet pale areas around the title and major subjects.

Use a few delicate handwritten place labels only where requested: [SHORT_LABELS]. Optional hairline corner ornaments and an understated culturally appropriate mark; omit either if not relevant. Optional bottom caption: "[FOOTER]". The layout should feel like a collectible illustrated travel poster and poetic cultural atlas. It is an artistic synthesis, not an accurate map. No modern infographic cards, no technical elevations or sectional diagrams, no 3D miniature display plinth, no glossy photographic rendering, no copied China-specific motifs unless China is the chosen subject, no meaningless script and no watermark.
```

## 当前状态

已收录原始参考图、通用提示词模板、文旅海报和照片转绘示例；具体作品以项目 `catalog.json` 为准。项目成图位于 `images/vintage-watercolor-travel-collage/`，逐张实际提示词位于 `prompts/vintage-watercolor-travel-collage/`。

参考图：`../assets/vintage-watercolor-travel-collage-reference.png`
