# Spec Delta

## Purpose

提供以繁體中文日常對話為主的飲食語意解析與互動介面，支援語音轉文字、實體抽取與多輪主動澄清機制，大幅降低使用者飲食記錄之操作負擔。

## ADDED Requirements

### Requirement: Natural Language Input Normalization
系統 SHALL 接收使用者以自然語言輸入之語音或文字飲食描述，並完成繁簡轉換、全半形標準化與意圖分類（紀錄 log_food、查詢 query_nutrition、分析 analyze、建議 recommend）。

#### Scenario: Text Input Processing
- **WHEN** 使用者輸入文字「午餐吃了一碗加蛋牛肉麵，湯喝一半」
- **THEN** 系統將文字正規化並正確識別意圖為 `log_food`，提取餐別為午餐

#### Scenario: Audio Input Transcoding
- **WHEN** 使用者上傳台語或中文語音錄音
- **THEN** 系統透過 Whisper 模型轉換為繁體中文文字並交由意圖分類器處理

### Requirement: Food Named Entity Recognition
系統 SHALL 從正規化文字中精確抽取食物名稱（Food Name）、份量描述（Portion Description）、烹調方式（Cooking Method）與用餐時間（Meal Time）。

#### Scenario: Complex Food Entity Extraction
- **WHEN** 使用者描述「大碗炸排骨便當加一份燙青菜」
- **THEN** 系統抽取出兩個食物實體：排骨便當（份量：大碗，主菜：炸排骨）與燙青菜（份量：一份）

### Requirement: Proactive Clarification Loop
當實體抽取之份量、烹調方式或特定品牌模糊且導致檢索信心低於 80% 時，系統 SHALL 主動發起精準追問以釐清關鍵細節，且單次追問以一至二個封閉式或選項問題為限。

#### Scenario: Ambiguous Portion Clarification
- **WHEN** 使用者僅輸入「剛剛吃了一碗泡麵」
- **THEN** 系統主動追問「請問是哪一款泡麵？份量是一般碗裝還是特大碗？是否有額外加蛋或青菜？」

#### Scenario: Sufficient Information Skip Clarification
- **WHEN** 使用者輸入「統一肉燥麵一包，加一顆水煮蛋，湯沒喝」
- **THEN** 系統判定實體與烹調條件明確，檢索信心度高於 80%，跳過追問直接進入營養計算

