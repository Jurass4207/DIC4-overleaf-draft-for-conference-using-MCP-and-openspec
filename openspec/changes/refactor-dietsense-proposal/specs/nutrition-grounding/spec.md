# Spec Delta

## Purpose

建立整合美國 USDA、台灣衛福部食品成分資料庫與自建台式料理向量庫的多來源事實錨定管線，消除生成式 AI 幻覺，並提供具備來源可追溯性的營養候選排序。

## ADDED Requirements

### Requirement: Multi-Source Nutrition Database Retrieval
系統 SHALL 依據抽取之食物實體名稱，依序檢索台灣衛生福利部食品成分資料庫（TFDA）、USDA FoodData Central 與自建台式料理向量資料庫（RAG），確保台灣在地夜市與複合菜餚的高涵蓋率。

#### Scenario: Taiwanese Local Food Query
- **WHEN** 使用者輸入台灣小吃實體「蚵仔煎」或「珍珠奶茶」
- **THEN** 系統優先自台灣食品成分資料庫與台式料理向量庫檢索匹配項目並回傳候選營養係數

#### Scenario: Western Food Ingredient Query
- **WHEN** 使用者輸入「燕麥片」或「希臘優格」
- **THEN** 系統自 USDA FoodData Central 檢索高精度每 100g 營養素數據

### Requirement: Candidate Ranking and Confidence Scoring
系統 SHALL 根據語意相似度、份量描述吻合度與在地飲食先驗機率，計算各候選項目之綜合信心分數（0.0 至 1.0），並選出最符合當前情境之營養基準項目。

#### Scenario: High Confidence Direct Match
- **WHEN** 候選項目在台灣食品成分庫中具完全同名且份量單位匹配
- **THEN** 系統計算信心分數高於 0.85，將其選定為基準數據並附帶資料來源標籤

#### Scenario: Low Confidence Fallback
- **WHEN** 食物為無精確資料之自製混合菜餚且最高候選信心低於 0.60
- **THEN** 系統將菜餚拆解為基礎食材代理項目（Proxy Ingredients）進行組合估算，並標註資料來源為「食材重構近似值」

