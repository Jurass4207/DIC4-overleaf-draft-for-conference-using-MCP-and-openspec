# DietSense: A Data-Grounded and Safety-Aware Conversational AI Agent for Personalized Dietary Assessment and Weight Management

本專案為國立中興大學物聯網數據分析與應用（DIC3）期末專題提案之規格驅動開發（OpenSpec）重構專案，整合日常繁體中文自然語言對話、台灣在地飲食大數據錨定、Mifflin-St Jeor 確定性能量代謝計算、動態不確定性信賴區間量化與臨床安全守門防護機制。

本儲存庫收錄符合國際學術會議（IEEE ICEIB）規範之 Overleaf 完整論文草稿、OpenSpec 規格驅動開發資產，以及對應資訊圖表之完整學術提案文件。

## 核心交付項目

### 1. Overleaf IEEE Conference 完整論文草稿
位於 `overleaf/` 目錄，專為 IEEE 雙欄會議論文排版設計：
- [overleaf/main.tex](overleaf/main.tex)：完整論文 LaTeX 原始碼，涵蓋 Title, Abstract, Index Terms, Section I (Introduction), Section II (Related Work), Section III (Proposed Architecture & Methodology), Section IV (Experimental Evaluation), Section V (Conclusion & Future Work), Acknowledgment 與 References。
- [overleaf/references.bib](overleaf/references.bib)：完備之 BibTeX 格式文獻庫，收錄 15+ 篇權威文獻，包含完整 DOI、卷期、頁碼與出版機構。
- [overleaf/README.md](overleaf/README.md)：Overleaf 一鍵上傳指南與本地 TeX Live / latexmk 編譯說明。

### 2. OpenSpec 規格驅動開發體系
基於 OpenSpec 1.17.0 之標準 SDD 工作流，收錄於 `openspec/`：
- [openspec/config.yaml](openspec/config.yaml)：專案整體規格配置與繁體中文規則約束。
- [openspec/changes/write-iceib-academic-paper/](openspec/changes/write-iceib-academic-paper/)：ICEIB 會議論文專用變更提案，包含：
  - `proposal.md`：論文寫作目標與章節契約。
  - `specs/`：七大核心章節規格庫（`paper-abstract`, `paper-introduction`, `paper-related-work`, `paper-proposed-design`, `paper-experiments`, `paper-conclusion`, `paper-references`）。
  - `design.md`：論文形式化數學模型與排版架構。
  - `tasks.md`：小顆粒度之可追蹤任務清單。
- [openspec/changes/refactor-dietsense-proposal/](openspec/changes/refactor-dietsense-proposal/)：系統層級重構變更提案，涵蓋五大核心能力（`conversational-intake`, `nutrition-grounding`, `metabolic-analytics`, `safety-guardrails`, `personalized-recommendation`）。

### 3. 對齊資訊圖表之輔助學術參考文件
依據《DietSense 專題提案系統性解析資訊圖表》之七大區塊完整展開：
- [01_A2Z_DietSense_26字母完整研究架構.md](01_A2Z_DietSense_26字母完整研究架構.md)：完整映射 A 到 Z 26 個字母之研究脈絡與具體實踐。
- [02_Deep_Research_三大核心問題分析.md](02_Deep_Research_三大核心問題分析.md)：五大專家核心思維、三大專業爭論（權衡分析）與十大深度理解問題。
- [03_DietSense_八大模組架構與演算法規格.md](03_DietSense_八大模組架構與演算法規格.md)：八大模組定義、流程圖、帶行號核心演算法虛擬碼（Algorithm 1）與代謝數學公式。
- [04_DietSense_完整學術專題提案企劃書.md](04_DietSense_完整學術專題提案企劃書.md)：完整繁體中文專題提案報告，包含五篇近年文獻比較表（Table II）。
- [05_DietSense_實驗評估與使用者研究規劃.md](05_DietSense_實驗評估與使用者研究規劃.md)：500 筆台灣在地料理標註集、MyFitnessPal A/B 實驗協議與 SUS 10 題問卷量表。

## 系統核心特色與架構定位

DietSense 落實「AI Agent + Domain Knowledge + Data Analytics + Real-World Application」四大維度：
1. **職責徹底解耦**: 「LLM 負責語意理解與任務協調，領域工具負責確定性數值運算，安全規則庫負責臨床邊界防護」，杜絕傳統通用 LLM 生成熱量之數值幻覺。
2. **多來源數據事實錨定**: 整合美國農業部 USDA FoodData Central、台灣衛生福利部食品營養成分資料庫（TFDA），以及自建之台式外食與夜市料理向量資料庫（RAG）。
3. **主動澄清迴圈 (Clarification Loop)**: 當實體抽取之份量或烹調模糊且檢索置信度低於 80% 時，主動發起針對性單一追問。
4. **動態不確定性信賴區間**: 以包含農產品天然變異與語意模糊之置信區間（如 [580, 710] kcal）取代誤導性之單一偽精確數字。
5. **臨床安全硬性護欄**: 底層硬性規則攔截每日總攝取低於 1,200 kcal 之極端節食請求，並對暴食-節食循環發出警示與專業轉介。

## 如何驗證與執行 OpenSpec 規格檢查

本專案已完成 OpenSpec CLI 安裝與配置，可透過以下指令進行嚴格規格校驗：

```bash
# 驗證 ICEIB 論文寫作規格
openspec validate write-iceib-academic-paper --strict

# 驗證 DietSense 提案重構規格
openspec validate refactor-dietsense-proposal --strict

# 查看當前變更進度
openspec status --change write-iceib-academic-paper
```

## 學術誠信與免責聲明

本專案現處於提案與架構驗證階段。文中所有評估指標（如 ±20% 誤差內達標率 > 85%、記錄時間縮短 60%、SUS > 70）均為規劃之預期成效（Expected Outcomes），未進行未經實測之數據捏造。本系統提供之飲食分析僅供個人化體重健康管理參考，不具備法律醫療診斷處方效力。全文無使用任何表情符號（emojis）。
