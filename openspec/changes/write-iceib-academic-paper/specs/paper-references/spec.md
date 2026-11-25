# Spec Delta

## Purpose

定義 ICEIB 論文參考文獻（References）之格式與內容規範，確保所有文獻引用符合 IEEE 期刊與會議標準格式，且出版資訊完備具備可查證性。

## ADDED Requirements

### Requirement: Strict IEEE Citation Formatting
所有參考文獻 SHALL 嚴格採用 IEEE 標準引用樣式（依文中引用順序以中括號 [1], [2] 編號），欄位必須完整包含作者全名或縮寫、論文篇名、出版刊物全稱、卷期號、頁碼、出版年份與正式 DOI。

#### Scenario: Complete BibTeX Fields
- **WHEN** 檢查 references.bib 與文中引用
- **THEN** 每一筆文獻必須欄位齊全，無缺漏作者或期刊名稱，且格式符合 IEEEtran.bst 剖析標準

### Requirement: Contemporary and Authoritative Sourcing
參考文獻 SHALL 包含世界衛生組織（WHO 2024/2025）、台灣衛生福利部官方公衛調查報告，以及近年（2024 至 2026 年）發表於臨床營養、計算機科學與人機互動頂尖期刊之實證文獻。

#### Scenario: Literature Quality Verification
- **WHEN** 審查文獻年代與權威性
- **THEN** 至少須涵蓋 Teixeira (2025), Hall (2012), Zeevi (2015), Cheng (2024), Poslusna (2009), Ludwig (2018), Helander (2014) 等經典與最新研究

