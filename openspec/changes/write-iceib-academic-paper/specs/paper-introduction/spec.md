# Spec Delta

## Purpose

定義 ICEIB 論文第一節緒論（Introduction）之論證架構，要求系統性回答專案核心價值，並以權威統計數據與對照表格確立研究必要性與創新貢獻。

## ADDED Requirements

### Requirement: Quantitative Problem Formulation
緒論第一段 SHALL 引用 WHO 2024 至 2025 年全球成人過重與肥胖數據（26 億人過重、9.4 億人肥胖），以及台灣衛生福利部 47.9% 過重率與年逾 500 億元醫療支出，量化飲食失調之公共衛生衝擊。

#### Scenario: Evidence-Backed Opening
- **WHEN** 閱讀緒論引言段落
- **THEN** 文本必須明確引述權威公衛文獻與官方統計數據作為問題重要性之客觀證據

### Requirement: Four Fundamental Obstacles Identification
緒論 SHALL 深入剖析傳統熱量記錄工具造成 85% 使用者於 30 天內放棄之四大障礙：手動查詢繁瑣、份量主觀模糊、複合料理拆解困難，以及缺乏亞洲與台灣在地料理資料覆蓋。

#### Scenario: User Friction Root Cause Analysis
- **WHEN** 檢視問題陳述段落
- **THEN** 必須逐點論述四大障礙如何擴大自報誤差（18% 至 54%）並導致長期依從性瓦解

### Requirement: Existing Tool Limitations Comparative Table
緒論 SHALL 提供專用對照表格（Table I），對比商業手動工具（MyFitnessPal）、電腦視覺照片辨識、研究型專用硬體系統與通用大型語言模型之技術限制。

#### Scenario: Competitive Baseline Analysis
- **WHEN** 查閱現有工具比較表
- **THEN** 必須指出拍照工具無法辨識隱藏油脂、硬體秤重無法日常隨身部署，以及通用 LLM 無法杜絕熱量數值幻覺

### Requirement: Core Innovations and Academic Contributions
緒論結尾 SHALL 條列 DietSense 之五大核心創新（自然語言輸入、主動代理人互動、情境感知、大數據驅動、安全護欄）與四大具體學術貢獻（可運作繁中代理人、500 筆台式料理基準集、多來源營養管線、多維度評估框架）。

#### Scenario: Clear Contributions Statement
- **WHEN** 審查論文研究貢獻
- **THEN** 必須清楚條列四項具備可交付性與可重現性之研究成果，且不包含主觀誇大形容詞

