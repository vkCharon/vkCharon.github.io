---
title: 平面誌的靜態出版流程
description: 從一份 README 到可訂閱的刊物，保留同一個 Pages 地址與原生建置流程。
date: 2026-11-20
serial: "01"
stack: [Jekyll, Liquid, Markdown, GitHub Pages]
repository_link: https://github.com/vkCharon/vkCharon.github.io/tree/main/_layouts
---
## 問題

個人網站要能長期維護，發一篇文章就不該需要手動更新首頁、索引、訂閱檔和網站地圖。原站已經使用分支出版，因此先問：能不能不增加一套部署流程？

## 做法

文章只存一份 Markdown。清單與 RSS 讀取同一個文章集合，專案則是獨立集合，不會混進文章的時間順序。兩種內頁共用閱讀版面；編輯可以在每個檔案的檔頭決定標題、摘要與分類。

## 取捨

沒有後台資料庫，也沒有需要保存的部署金鑰。代價是每次新增或修訂都要等靜態建置完成。對這份以文章為主、更新頻率不高的刊物，這比即時更新更容易維護。

從[訂閱檔]({{ '/feed.xml' | relative_url }})和[文章索引]({{ '/posts/' | relative_url }})可以看到同一批內容如何送到不同的閱讀入口。
