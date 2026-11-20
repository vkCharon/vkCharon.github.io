---
title: 不連伺服器的文章篩選器
description: 用原生表單篩選已經下載的文章卡片，保留可分享的查詢與鍵盤操作。
date: 2026-11-20
serial: "02"
stack: [JavaScript, HTML, URLSearchParams]
repository_link: https://github.com/vkCharon/vkCharon.github.io/blob/journal/assets/site.js
---
## 使用情境

在手機上看到一個感興趣的標籤，點下去就想讀，不想再等一個搜尋服務回應。初期文章不多，可以把索引當成文件，而不是應用程式。

## 介面決定

用原生選單選分類和標籤，不另外造一套鍵盤操作規則。搜尋框比對標題、摘要與標籤；三個條件同時生效。網址保留參數，頁面讀取時還原表單，讓從文章標籤進來的人直接看到對應結果。

## 規模界線

現在的篩選成本隨文章數量線性增加，也不支援全文排名。當索引下載量明顯成長時，可以改為建置時產生全文索引，並在讀者啟動搜尋後才載入；文章本身的固定地址不必改變。

[試讀帶有 JavaScript 標籤的索引]({{ '/posts/' | relative_url }}?tag=JavaScript)。
