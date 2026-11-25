# Spec Delta

## Purpose

定義 ICEIB 論文第二節相關研究（Related Work）之規範，要求平衡整合人工智慧技術與臨床營養能量代謝領域知識，並收斂出明確的研究缺口（Research Gap）。

## ADDED Requirements

### Requirement: Balanced Dual-Domain Literature Review
相關研究章節 SHALL 嚴格維持約 50% 人工智慧技術與 50% 營養代謝領域知識之平衡論述，涵蓋 LLM Tool Use、RAG 向量檢索、Food NER、不確定性量化、BMR/TDEE 代謝公式、AMDR 比例與台灣每日飲食指南。

#### Scenario: Dual Perspective Coverage
- **WHEN** 檢視相關文獻各子章節長度與深度
- **THEN** 技術篇幅與營養學領域知識篇幅必須對稱，避免偏廢任何一方

### Requirement: Five-Article Summary Table
相關研究章節 SHALL 包含一張結構完整之文獻綜合摘要表（Table II），整理 2024 至 2026 年五篇代表性論文，欄位包含文獻編號、年份、研究問題、AI 方法、領域知識、資料集、主要發現與技術限制。

#### Scenario: Comprehensive Literature Matrix
- **WHEN** 查閱 Table II 比較表
- **THEN** 表格必須涵蓋語音/文字飲食記錄、影像熱量回歸、微調臨床 LLM、Tool-use Agent 與在地食物分類等代表性研究

### Requirement: Research Gap Convergence
文獻探討末段 SHALL 透過嚴謹之邏輯鏈（Existing Research -> Limitations -> Research Gap -> DietSense），論證當前學界尚無同時整合對話式互動、在地飲食資料庫錨定、不確定性置信區間與安全守門之端到端 Agent 系統。

#### Scenario: Scientific Gap Formulation
- **WHEN** 閱讀文獻總結段落
- **THEN** 必須明確界定 DietSense 填補之學術空白，凸顯本專案之獨特性
