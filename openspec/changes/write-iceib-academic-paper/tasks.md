# Tasks: ICEIB 國際學術會議論文撰寫與交付清單

## 1. OpenSpec 規格與設計架構確認

- [x] 1.1 建立 `write-iceib-academic-paper` 變更提案並完成 `proposal.md`
- [x] 1.2 完成七大核心章節規格檔案（`paper-abstract`, `paper-introduction`, `paper-related-work`, `paper-proposed-design`, `paper-experiments`, `paper-conclusion`, `paper-references`）
- [x] 1.3 完成論文排版與系統形式化設計文件 `design.md`

## 2. Overleaf IEEE Conference LaTeX 專案產出

- [x] 2.1 建立 `overleaf/` 目錄並撰寫完整的 IEEE 雙欄會議論文主文檔 `overleaf/main.tex`
- [x] 2.2 撰寫完備且具備真實 DOI/出版資訊之 BibTeX 文獻庫 `overleaf/references.bib`
- [x] 2.3 撰寫 Overleaf 專案匯入、本地編譯與套件相容性指南 `overleaf/README.md`

## 3. 論文內文七大章節完整英文化實作

- [x] 3.1 實作 Abstract 與 Index Terms，體現 A-F 六段式邏輯與 8 個專業索引詞彙
- [x] 3.2 實作 Section I Introduction，整合 WHO/衛福部公衛統計、四大認知障礙、Table I 工具限制對比表、核心創新與貢獻
- [x] 3.3 實作 Section II Related Work，平衡 AI 技術與營養領域知識，置入 Table II 近年 5 篇文獻對比表與 Research Gap
- [x] 3.4 實作 Section III Proposed Architecture and Methodology，詳述八大模組、泳道圖、帶行號 Algorithm 1 虛擬碼、Mifflin-St Jeor 公式與不確定性量化模型
- [x] 3.5 實作 Section IV Experimental Design and Evaluation，定義 500 筆台式料理標註集、MyFitnessPal 對照實驗、20 人 7 天受試者研究與量化指標（MAE, MAPE, 達標率 > 85%, 縮短 60%, SUS > 70）
- [x] 3.6 實作 Section V Conclusion and Future Work，總結貢獻、誠實指出文字輸入局限，並提出多模態與物聯網 CGM 整合路線
- [x] 3.7 實作 References 章節，確保所有文中引用 [1]-[16] 均精確對應 `references.bib`

## 4. 產出對應資訊圖表之輔助學術參考文件

- [x] 4.1 產出 `01_A2Z_DietSense_26字母完整研究架構.md`（完整映射 A 到 Z 研究脈絡）
- [x] 4.2 產出 `02_Deep_Research_三大核心問題分析.md`（5 核心思維、3 專業爭論、10 深度問題）
- [x] 4.3 產出 `03_DietSense_八大模組架構與演算法規格.md`（八大模組、流程圖、帶行號虛擬碼與數學公式）
- [x] 4.4 產出 `04_DietSense_完整學術專題提案企劃書.md`（完整繁體中文專題提案報告）
- [x] 4.5 產出 `05_DietSense_實驗評估與使用者研究規劃.md`（500 筆資料集規格、A/B 測試與 SUS 量表）

## 5. 格式檢驗與嚴格規格驗證

- [x] 5.1 執行 `openspec validate write-iceib-academic-paper --strict` 確認所有 OpenSpec 規範無警告與錯誤
- [x] 5.2 全域檢查所有產生之 Markdown 與 LaTeX 檔案，確認未包含任何表情符號（emojis）

## Workflow follow-up

- 驗證完成後，透過 `/opsx-apply` 或 `openspec archive` 將論文變更正式封存並合併入主規格庫。
