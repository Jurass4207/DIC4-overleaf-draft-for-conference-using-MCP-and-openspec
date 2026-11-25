# Spec Delta

## Purpose

定義 ICEIB 論文第三節系統架構與設計（Proposed System Architecture and Methodology）之規格，要求包含八大模組設計、時序流程、帶行號演算法虛擬碼、代謝數學公式與臨床安全守門防護。

## ADDED Requirements

### Requirement: Eight-Module System Architecture Specification
系統設計章節 SHALL 詳盡闡述八大核心模組：① User Scenario、② Query Processing、③ Planner Agent、④ Data Retrieval、⑤ Analytics Engine、⑥ Domain Knowledge、⑦ Recommendation、⑧ Output Interaction，並提供系統架構圖說明。

#### Scenario: Structural Completeness
- **WHEN** 檢閱系統架構章節
- **THEN** 必須清晰界定各模組之輸入、輸出及模組間的資料契約，並強調「LLM 負責協調、領域工具負責計算」之核心解耦原則

### Requirement: Algorithm Pseudocode with Line Numbers
論文 SHALL 包含具行號之核心演算法虛擬碼（Algorithm 1: DietSense Pipeline），完整呈現意圖分流、多來源並行檢索、信心加權、澄清追問、確定性熱量換算與安全攔截。

#### Scenario: Algorithmic Reproducibility
- **WHEN** 審查 Algorithm 1 內容
- **THEN** 程式碼虛擬行必須明確標註行號（01 至 14 行以上），包含 await ask_user 澄清迴圈與 evaluate_safety_guardrails 安全守門函數

### Requirement: Mathematical Formulations and Uncertainty Model
論文 SHALL 以標準數學公式定義 Mifflin-St Jeor BMR 與 TDEE 計算式，並建立動態不確定性置信區間模型，依據檢索信心分數 C 計算熱量估算上下界。

#### Scenario: Formal Equation Presentation
- **WHEN** 檢查數學公式
- **THEN** 必須以 LaTeX 公式呈現男性與女性 BMR 算式、活動係數 PAL 乘積，以及邊界公式 Margin = E * (alpha + (1-C)*beta)

### Requirement: Clinical Safety Guardrails and Fallback Design
論文 SHALL 詳述系統面對低信心與高風險情境之處置邏輯，包含未知料理之基礎食材重構降級機制，以及每日熱量低於 1,200 kcal 之強制攔截與醫療免責導引。

#### Scenario: Safety Interception Mechanism
- **WHEN** 系統偵測到過度節食或特殊疾病患者時
- **THEN** 論文必須證明代理人架構具有硬性規則層阻斷生成危險減重建議，確保使用者生理安全

