# Spec Delta

## Purpose

定義 ICEIB 論文第四節實驗評估（Experimental Design and Evaluation）之規劃標準，規範台式料理標註資料集、對照組基準、使用者研究方案與預期指標之呈現方式。

## ADDED Requirements

### Requirement: Benchmark Dataset and Ground Truth Formulation
實驗章節 SHALL 詳細說明 500 筆台灣在地料理與外食自然語言描述資料集之建構標準，涵蓋夜市小吃、便當、湯麵、複合菜餚、手搖飲料與家庭料理，並結合 TFDA 與 USDA 營養成分標註黃金標準（Ground Truth）。

#### Scenario: Dataset Diversity and Categorization
- **WHEN** 審查資料集說明
- **THEN** 必須條列料理分類佔比與熱量標準答案之標註來源，驗證測試樣本能代表真實生活飲食情境

### Requirement: Comparative Baseline and Experimental Setup
實驗設計 SHALL 明確建立與商業基準 MyFitnessPal 手動記錄之 A/B 對照實驗架構，並設計 20 名受試者連續 7 天之真實飲食記錄研究流程。

#### Scenario: User Study Protocol
- **WHEN** 閱讀受試者實驗步驟
- **THEN** 必須說明受試者分組、每日三餐輸入模式、記錄耗時記錄方式，以及防範霍桑效應（Hawthorne Effect）之措施

### Requirement: Multi-Dimensional Evaluation Metrics
論文 SHALL 統整多維度評估量化指標，包含熱量絕對誤差（MAE）、平均絕對百分比誤差（MAPE）、±10% 與 ±20% 達標率（目標 > 85%）、記錄耗時縮短率（目標 60%）與系統可用性量表（SUS > 70）。

#### Scenario: Academic Integrity in Metrics Reporting
- **WHEN** 閱讀實驗數據與目標設定
- **THEN** 論文必須嚴格標明提案階段所有指標數值為預期目標（Expected Outcomes），恪守學術倫理，不得假造實測數據
