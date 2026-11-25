# Spec Delta

## Purpose

建立臨床級安全邊界與行為防護機制，防範過度節食、極端熱量限制與飲食失調模式，並為特殊生理族群提供免責聲明與專業醫療轉介。

## ADDED Requirements

### Requirement: Minimum Caloric Intake Interception
系統 SHALL 監控使用者設定之每日目標熱量與實際全日攝取總額，當目標或實際攝取連續低於每日 1,200 kcal（成人臨床安全底線）時，系統 MUST 觸發危險警戒攔截機制，拒絕生成進一步限制熱量之建議。

#### Scenario: Extreme Calorie Restriction Intercept
- **WHEN** 使用者要求「請幫我規劃每天只吃 800 大卡的快速瘦身菜單」
- **THEN** 系統立即攔截該請求，拒絕產出低於 1,200 kcal 的菜單，並提示過低熱量將導致肌肉流失與代謝損傷

### Requirement: Eating Disorder Pattern Detection
系統 SHALL 分析使用者過去 7 天的飲食日誌時序資料，偵測是否存在暴食後極端節食（Binge-Restrict Cycle）或極端補償心理行為模式。

#### Scenario: Binge Restrict Pattern Detected
- **WHEN** 系統偵測到使用者在單日暴飲暴食超過 TDEE 150% 後，隔日完全禁食或僅攝取小於 500 kcal
- **THEN** 系統標註 `WARNING` 狀態，發出關懷警示，溫和引導使用者恢復平穩飲食節奏

### Requirement: Medical Disclaimer and Vulnerable Population Routing
系統 SHALL 在所有建議輸出中附帶非醫療診斷免責聲明；當使用者個人資料標註為孕婦、授乳婦女、腎臟病或糖尿病患者時，系統 MUST 限制處方型營養建議並建議轉介專業營養師與臨床醫師。

#### Scenario: Pregnant User Guardrail
- **WHEN** 個人基本資料標註懷孕週數或患有慢性腎臟病
- **THEN** 系統停止常規減重熱量赤字計算，改為顯示衛福部孕期營養建議基準，並強制附帶諮詢婦產科與營養師之轉介提示

