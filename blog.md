# 部落格

部落格是同一套構成放慢的版本：平面退到文章卡片的圖版裡，內文讓給閱讀。

## 版面

- 頁面最大寬度 `page-max`，邊距手機 `space-4`、桌面 `space-8`。
- 文章內文欄寬 `measure-article`，置中。16 px 內文約 40 個全形字一行。
- 文章列表用 `PostCard` 排格線：960 px 以上三欄、640 px 以上兩欄、以下一欄，間距 `space-8`。
- 頁首：左邊「ChR」文字（`heading` 樣式、`display` 字族），右邊導覽用 `label` 樣式。頁首下方一條 `line` 細線。
- 頁尾：底色 `ink`，文字 `canvas`。深色主題下會反轉成淺底深字，不需要另外處理。

## 文章排版

| 元素 | 樣式 | 規則 |
| --- | --- | --- |
| 眉標 | `label` | 分類與集數，`persona-ink` |
| 標題 h1 | `display` | 最多三行；手機縮到 32 px |
| 日期、閱讀時間 | `data` | `2026.10.25 · 閱讀 6 分鐘`，`ink-muted` |
| 內文 | `body` | 段落間距 `space-6` |
| h2 | `heading` | 上方留 `space-12` |
| h3 | `title` | 上方留 `space-8` |
| 圖說 | `small` | `ink-muted`，圖片下方 `space-2` |
| 程式碼 | `mono` 字族 14 px | 底色 `canvas-raised`，直角，可橫向捲動 |

- 連結：`persona-ink`，1px 底線、底線距文字 3 px；hover 時底線加粗到 2 px。
- 引言：上方放一個 6 × 6 的 `persona` 方塊，引文用 `title` 樣式。不要用左側色條。
- 圖片：滿欄寬、直角、不加邊框和投影。
- 分隔線：一根 48 × 4 px 的 `ink` 長條，沿 `tilt-axis` 傾斜。這是內文裡唯一允許的傾斜元素。

## 主題

- 跟隨系統的淺色／深色設定：淺色是 **Canvas**，深色是 **Graphite**。
- 若提供手動切換，在 `<html>` 設定 `data-theme="light"` 或 `data-theme="dark"`。
- 文章中的圖片不隨主題改變；若圖片是白底，深色主題下加一層 `canvas-raised` 的外框留白。

## 沒有封面圖的文章

`PostCard` 不給 `image` 時，會用平面構成當圖版，從 `motif` 選一種：`square`（黑方塊 + 勃艮第長條）、`circle`（灰圓盤 + 勃艮第方塊）、`cross`（十字）。同一個分類固定用同一種，讓讀者能從圖版認出分類。
