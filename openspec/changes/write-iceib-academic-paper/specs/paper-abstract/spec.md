# Spec Delta

## Purpose

定義 ICEIB 會議論文之摘要（Abstract）與關鍵字（Index Terms）撰寫標準，確保嚴格符合 IEEE 雙欄格式、A-F 六段式故事結構與精確學術詞彙規範。

## ADDED Requirements

### Requirement: IEEE Conference Abstract Structure
論文摘要 SHALL 採單一段落結構呈現，字數介於 200 至 300 字之間，並完整覆蓋 A-F 六大要素：動機（Attention Getter）、現有瓶頸（But）、解藥代理人（Cure）、技術方法（Development）、評估規劃（Experiments）與預期成效（Findings）。

#### Scenario: Full Abstract Completeness
- **WHEN** 審查論文 Abstract 段落
- **THEN** 內文必須同時涵蓋 WHO 肥胖數據、自報 18% 至 54% 誤差挑戰、DietSense 代理人架構、多來源 RAG 錨定、500 筆測試集與預期達標率指標

### Requirement: Authoritative Index Terms Specification
論文 SHALL 於摘要下方提供正式的 Index Terms 區塊，收錄 6 至 8 個精準符合電子資訊與生醫工程領域之 IEEE 標準索引詞。

#### Scenario: Standard Index Terms Inclusion
- **WHEN** 檢查 Index Terms 列表
- **THEN** 必須依序包含 Conversational AI, domain-specific AI agents, dietary assessment, large language models, retrieval-augmented generation, uncertainty quantification, personalized weight management, safety-aware systems
