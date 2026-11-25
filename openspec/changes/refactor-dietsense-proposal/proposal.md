# Proposal: DietSense 專題提案重構與規格驅動架構轉換

## Why

全球肥胖與過重人口已超過 26 億人（其中肥胖人口達 9.4 億人），台灣成人過重與肥胖率更高達 47.9%，已成為需長期自我監測與介入的公共衛生挑戰。然而，現有商業飲食追蹤工具（如 MyFitnessPal、Cronometer）依賴繁瑣的手動檢索、食材秤重與複合料理拆解，造成高達 85% 的使用者在 30 天內放棄記錄；同時，自報飲食攝取誤差普遍達 18% 至 54%。另一方面，通用大型語言模型（LLM）雖具備對話能力，但直接詢問熱量時易產生數值幻覺、缺乏本土食物資料庫錨定，且可能給出極端節食等危險建議。

本提案旨在透過規格驅動開發（Spec-Driven Development, SDD）方法，將原提案重構為標準化、可驗證且具備安全護欄的 **DietSense 領域智慧代理人（Domain AI Agent）**。核心架構確立「LLM 負責意圖理解與任務協調，領域工具負責確定性數值運算，安全規則負責臨床邊界守門」之分工，解決傳統記錄工具的高認知負擔與純生成式 AI 的數值幻覺問題。

## What Changes

本變更（Change Proposal）依據 OpenSpec 規格驅動開發框架，將原本零散的提案與設計文件進行系統化重構：

- **規格驅動架構化**：將原本非正式的自然語言描述與文件，轉化為包含完整 `proposal.md`、`specs/`、`design.md` 與 `tasks.md` 的 OpenSpec 工作流資產。
- **核心定位與解藥清晰化**：明確落實「AI Agent + Domain Knowledge + Data Analytics + Real-World Application」四大維度，確立 DietSense 五大核心思維、三大專業權衡（Trade-offs）與十大深度技術細節。
- **模組邊界隔離與確定性計算**：
  - 將 LLM 的職責嚴格限制為意圖分類、實體抽取與澄清追問，不得直接生成隨機熱量數字。
  - 將營養檢索（USDA API、衛福部台灣食品資料庫、台式小吃向量庫）與代謝能量計算（Mifflin-St Jeor TDEE、巨量營養素比例）交由確定性領域模組處理。
- **導入不確定性量化與主動澄清迴圈（Clarification Loop）**：當使用者輸入模糊（如「一碗牛肉麵，湯喝一半」）且檢索信心低於 80% 時，主動追問關鍵特徵（大/小碗、清燉/紅燒），並以置信區間（如 520–640 kcal）取代偽精確單一數字。
- **建立臨床安全護欄（Safety Guardrails）**：嚴格設定每日最低熱量安全警戒線（< 1,200 kcal/天）與暴食-節食循環偵測，遇高風險情境立即降級並建議諮詢專業營養師。
- **學術誠信標準化**：嚴格區分「目標設計（Expected Outcomes）」與「實證結果（Verified Results）」，所有未完成實驗之評估指標均標示為預期目標。

## Capabilities

### New Capabilities

- `conversational-intake`: 負責接收日常繁體中文飲食自然語言描述，透過 Whisper 語音轉文字、語意正規化、意圖分類（記錄/查詢/分析/建議），並在關鍵資訊缺失時觸發多輪主動澄清對話（Clarification Loop）。
- `nutrition-grounding`: 多來源飲食事實錨定管線。整合 USDA FoodData Central、台灣衛福部食品成分資料庫與自建台式小吃料理向量資料庫（RAG），提供候選實體比對、信心加權評分與完整資料來源追溯。
- `metabolic-analytics`: 確定性營養與能量代謝分析引擎。實作 Mifflin-St Jeor 基礎代謝率（BMR）與總每日能量消耗（TDEE）運算、AMDR 巨量營養素分布分析，並依檢索信心動態計算不確定性信賴區間。
- `safety-guardrails`: 臨床健康與行為安全監控機制。即時攔截極端熱量赤字（< 1,200 kcal/天）、偵測潛在飲食失調（Eating Disorder）行為模式，提供免責聲明並強制引導至專業醫療資源。
- `personalized-recommendation`: 情境感知個人化回饋。根據個人生理特徵、生活習慣、歷史飲食紀錄與當日代謝缺口，提供符合台灣飲食情境之客製化微調建議與視覺化互動報告。

### Modified Capabilities

- （無既有 Capability 修改，本變更為初次導入完整的 SDD 系統規格庫）。

## Impact

- **架構影響**：於專案中建立 `openspec/specs/` 核心規格庫，包含 5 項獨立定義且可測試的系統規格，作為後續軟體工程實作與交接驗證的真實來源（Source of Truth）。
- **工程交付物**：
  - 產出標準化 `README.md`、`DESIGN.md` 與重構後的 `Proposal.md`。
  - 建立對應 Antigravity / Cursor 的 SDD 代理人自動化工作流程指令（`/opsx-explore`、`/opsx-propose`、`/opsx-apply`、`/opsx-archive`）。
- **評估基準影響**：定義 500 筆台式外食標註資料集結構、MyFitnessPal 手動輸入基準比較規約，以及 20 人 × 7 天的使用者體驗評估框架（SUS > 70、±20% 誤差內達標率 > 85%、記錄時間縮短 60%）。
- **依賴與安全性**：新增多來源資料庫 API 介面抽象層與安全守門器，所有個人飲食敏感數據與隱私日誌皆保留於本地隔離環境，避免健康隱私外洩。

