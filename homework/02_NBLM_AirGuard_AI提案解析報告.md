# AirGuard AI 專案提案系統性解析報告
### 依據《期末專題提案作業規範》與《A2Z outline example.pdf》26 字母架構進行深度評析

---

## 一、 依據《期末專題提案作業規範》核心維度檢視符合度

### 1. 核心定位符合度（AI Agent + 領域知識 + 數據分析 + 真實世界應用）
- **超越單一 Model 與單純 Chatbot**：專題規範明確要求不能只訓練單一 AI 模型或製作純問答 Chatbot，必須是具備專業推理、取得資料與決策能力的 Domain AI Agent。
- **AirGuard AI 的定位與實踐**：
  - **AI Agent**：以 LLM（GPT-4o / Claude 3.5 Sonnet）作為 Planner 核心，透過 LangChain 整合實體識別（NER）、澄清追問迴圈（Clarification Loop）與白名單工具調用（Function Calling）。
  - **Domain Knowledge（領域知識）**：引入大氣擴散邊界層理論、環境部 AQI 分段線性計算法、多污染物主導機制、光化臭氧日夜特性、國健署運動即時防護指引（PM2.5 達 50.5 μg/m³ 門檻），以及醫療安全拒答守門機制。
  - **Data Analytics（數據分析）**：整合環境部 AQX_P_488 歷時資料庫（清洗後 606,137 筆）與 AQX_P_432 即時串流；建立滾動時序回歸預測模型（SARIMAX/GBDT），並以持續性模型（Persistence）作為客觀基線對比。
  - **Real-World Application（真實世界應用）**：鎖定全台數百萬戶外慢跑與耐力運動族群，解決運動時每分鐘換氣通氣量暴增 6–10 倍時暴露於突發空污的真實公共衛生健康痛點。

### 2. Abstract（摘要）與 Introduction（緒論）結構對照
- **Abstract 六段式（A–F）對照**：
  - **A. Attention Getter**：引用 WHO 2025/2026 最新空污健康報告、運動時換氣通氣量暴增 6–10 倍，深層肺泡 PM2.5 沉積量激增 4–10 倍引題。
  - **B. But (挑戰)**：現有系統被動呈現歷史讀值、缺乏 1–6 小時短期趨勢；缺乏個人化排程推理機制；通用 LLM 易產生數值幻覺與越權捏造醫療處方。
  - **C. Cure (解藥)**：提出 AirGuard AI 工具導向 Domain AI Agent。
  - **D. Development (方法)**：整合 FastAPI、LangChain 白名單工具、SARIMAX/GBDT 時序預測與官方活動防護規則庫。
  - **E. Experiments (評估)**：規劃 2024–2026 臺中測站滾動回測、60 題在地問答基準集，以及 30 個涵蓋異常/越界的 Agent 情境測試。
  - **F. Findings (預期產出)**：嚴格遵循「未實驗者僅列 Expected Outcomes，不虛構數據」，明訂預期在 MAE/RMSE 與基線相比的改善率（15%–25%），以及 100% 來源揭露與安全拒答率。
- **Introduction 論證精神**：明確回答「Why is this project worth doing?」，結構完整包含 A (引題) $\to$ B (背景) $\to$ C (真正問題) $\to$ D (既有不足) $\to$ E (創新架構) $\to$ F (四大預期貢獻)。

### 3. Related Work 與 Deep Research 三大核心問題對照
- **AI 技術與領域知識平衡（1/2 AI + 1/2 Domain）**：
  - **AI 面**：涵蓋時序統計迴歸（SARIMAX/GBDT）、多代理協同架構（Neuro-Air）、序列異常偵測與白名單 Function Calling。
  - **Domain 面**：涵蓋大氣微氣候空間代表性、微型感測器吸濕性光學散射偏差（RH 修正）、台灣盆地逆溫層效應與官方 AQI 暴露安全標準。
- **Article Summary Table**：完整提供 8 篇跨 2020–2026 年（優先納入 2025/2026 最新文獻）的結構化文獻矩陣，清晰收斂出 Research Gap。
- **Deep Research 三大核心問題對照**：
  - **Q1. 5 個核心思維模式**：深入論述「AQI 多污染物摘要」、「測站代表微環境非個人劑量」、「資料來源與品質分級」、「時間尺度精確對齊」與「時空相關性不等於因果/醫療邊界」。
  - **Q2. 3 個重要專業爭論**：
    1. 低成本物聯網感測器 (AirBox) vs. 參考級官方測站。
    2. 簡單統計/物理基準模型 vs. 複雜機器學習/深度學習時序預測。
    3. 自由端到端 LLM 推理 vs. 確定性白名單工具呼叫。
  - **Q3. 10 個深度理解問題**：涵蓋 Why, What-if, Trade-off, Failure Case, Evidence, Comparison, Design Decision 與 Real-world Scenario 等高階推理層次。

### 4. Proposed Scheme（系統架構與技術表示）
- **八大模組架構（完整對應規範 ①～⑧）**：
  - ① User Scenario：慢跑與戶外活動排程輸入。
  - ② Query/Input Processing：地點實體抽取、時段正規化、意圖分類。
  - ③ Planner & Reasoning Agent：LLM 任務拆解、多輪記憶管理、澄清迴圈（Clarification Loop）。
  - ④ Data Acquisition/Retrieval：AQX_P_488 歷時資料庫與 AQX_P_432 API 即時串流。
  - ⑤ Analytics Engine：數值確定性聚合、趨勢斜率、持續性基準與 SARIMAX/GBDT 滾動預測。
  - ⑥ Domain Knowledge Integration：環境部 AQI 分級門檻、國健署防護建議規則庫。
  - ⑦ Decision/Recommendation：排程建議、室內替代方案、醫療越權攔截。
  - ⑧ Output & Interaction：結構化 Markdown 回應、測站浮水印標籤、不確定性區間提示。
- **Flowchart 與 Pseudocode**：
  - Flowchart：提供包含意圖分流、品質檢驗、澄清迴圈、安全守門與資料降級之完整泳道流程圖。
  - Pseudocode：提供具體步驟與行號的演算法（Algorithm 1: AirGuard Domain AI Agent 與 Algorithm 2: Evidence Guard），明確處理非同步澄清、時序回歸與安全攔截機制。

---

## 二、 依據《A2Z SOP Outline》26 字母結構深度解析

| 字母 | A2Z SOP 定義 | AirGuard AI 專案具體落實與內容映射 |
|:---:|---|---|
| **A** | **Attention Getter** | 引用 WHO 2025/2026 空污致死報告；運動通氣量激增 6–10 倍，深層肺泡 PM2.5 沉積量放大 4–10 倍之真實公衛痛點。 |
| **B** | **But** | 官方測站僅被動呈現過去讀值，無 1–6 小時趨勢；一般 LLM 數值幻覺嚴重且缺乏醫療法規邊界約束。 |
| **C** | **Cure** | 提出整合環境部開放資料、時序滾動預測與官方活動指引的「AirGuard AI 工具導向代理人」。 |
| **D** | **Development** | 採用 FastAPI 後端、LangChain 白名單 Function Calling、確定性時序模型與版本化環境部防護規則庫。 |
| **E** | **Experiments** | 規劃 2024–2026 臺中測站滾動回測、60 題在地空品問答集，以及 30 個涵蓋異常/越界之對抗測試案例。 |
| **F** | **Findings** | 嚴守學術誠實（不捏造數據），預期達成預測 MAE 相對改善 15–25%、100% 來源揭露率與 100% 醫療越權攔截。 |
| **G** | **General** | 戶外運動與大眾健康管理市場龐大，台灣環境部建置了覆蓋 88 個標準測站之高品質逐時公開監測網。 |
| **H** | **However** | 原始監測資料存在重複列與鍵值衝突；大氣擴散具非線性，且民眾難以將監測讀值直接轉化為個人化排程。 |
| **I** | **In literature** | 文獻從傳統氣象插值、物理擴散模型、機器學習預測（GBDT），發展至跨區多代理決策系統（Neuro-Air）。 |
| **J** | **Judgement** | 傳統物理模型運算昂貴；單純 ML 缺乏對話互動；通用 LLM 無法保證數字正確；多代理系統架構過度繁複。 |
| **K** | **Keypoint** | 堅持「語言生成與數值運算分離」；白名單工具保證無幻覺；官方指引規則化確保安全可稽核。 |
| **L** | **List organization** | 依序規劃摘要、緒論、文獻探討、Deep Research、八大模組架構、演算法偽程式碼與雙軌評估實驗。 |
| **M** | **Methods** | 分類為：(1) 時序統計與 ML 迴歸；(2) 微型感測器空間校正；(3) 異常偵測；(4) LLM Agent 決策支援。 |
| **N** | **New proposed** | 「台灣逐時官方資料 + 滾動時序預測 + 官方活動防護規則庫 + Evidence Guard 溯源審核」整合架構。 |
| **O** | **Organize** | 納入 8 篇 2020–2026 跨領域文獻，收斂出兼具在地資料特性與個人化決策的 Research Gap。 |
| **PA** | **Aim** | 打造降低跑者空污暴露風險、具備 1–6 小時短期趨勢且 100% 可溯源之空氣品質運動排程決策代理人。 |
| **PB** | **Based on** | 依託台灣環境部 AQX_P_488/432 開放資料庫、衛福部/國健署戶外防護指引與大氣邊界層擴散理論。 |
| **PC** | **Cure / Cause** | 透過確定性代碼運算徹底杜絕 LLM 算術黑盒；透過多輪澄清機制（Clarification Loop）消除時空歧義。 |
| **PD** | **Design** | 典範轉移：從「使用者自行查詢篩選數十個監測欄位」轉向「AI Agent 依意圖自主調度工具並給出安全指引」。 |
| **PE** | **Paper Element** | 嚴格拆解為八大子模組：UI、Query NLP、Planner、Data API、Analytics Engine、Domain Rules、Decision、Output。 |
| **PF** | **Formulation** | 定義預測指標 MAE, RMSE、環境部 AQI 分段線性公式與持續性基線。 |
| **PG** | **Graph** | 提供完整的系統架構圖與包含判斷、異常降級和多輪追問的 Mermaid 決策流程圖。 |
| **PH** | **How** | 透過 Pydantic 結構化參數解析、滾動時序回歸、防護規則門檻硬編碼及輸出 Markdown 來源標註達成。 |
| **PI** | **Implementation** | 撰寫具備標準步驟的 Algorithm 1: AirGuard Domain AI Agent 演算法虛擬碼。 |
| **PJ** | **Jump to an example** | 實測範例：「我明天早上 6 點想在台中西屯慢跑 10 公里，安全嗎？」的端到端解析、預測與防護建議產出。 |
| **PK** | **Key points contribution** | 交付開源清洗管線、FastAPI+LangChain 代理人原型、60+30 雙軌評估集及客觀多維驗證框架。 |
| **PL** | **Later simulation** | 規劃 2024–2026 歷史資料滾動時間窗回測，比對 Persistence、Seasonal Naïve 與 SARIMAX 效能。 |
| **PM** | **Math proof / Logic** | 驗證預測模型上下限物理守恆邊界（濃度不可為負），以及副指標最大值與總體 AQI 的數學邏輯一致性。 |
| **Q** | **Quality & Quantity** | MAE, RMSE, R², 數值精確匹配率 (>95%), 來源對應正確率 (100%), 醫療越權拒答率 (100%)。 |
| **R** | **Related method** | 對比三種條件：(1) LLM-only 直答；(2) 純確定性分析工具輸出；(3) AirGuard AI 完整代理人。 |
| **S** | **Simulation Setup** | 建置台中測站（西屯、忠明）資料測試環境、FastAPI Mock 伺服器與標準化 Prompt 評估沙盒。 |
| **T** | **Tuning parameters** | SARIMAX 階數 (p,d,q)(P,D,Q)s、意圖分類信心度門檻（預設 0.85）、時序滾動回測窗口長度。 |
| **U** | **Useful results** | 產生包含時段空品趨勢圖、PM2.5 預測區間、防護建議等級（正常/減量/室內）與資料來源說明的整合決策。 |
| **V** | **Verify** | 驗證預測誤差相較基線顯著改善，且在 30 個對抗性越界情境下 100% 成功攔截並安全降級。 |
| **W** | **What proposed** | 總結為解決戶外運動空污暴露健康痛點、根除 LLM 幻覺並具備法律安全邊界的 Domain AI Agent。 |
| **X** | **eXcel** | 專精於「台灣在地測站即時與短程預報」與「戶外運動生活排程決策」之深度結合。 |
| **Y** | **Yields** | 完整 GitHub Repo、標準 README.md、通過 OpenSpec 驗證之規格文件、Demo 影片與簡報。 |
| **Z** | **Zen** | 坦承單一測站無法等同個人劑量，未來可進一步融合穿戴式心率手環、微型感測器與即時生理通氣量估算。 |

---

## 三、 綜合評審亮點與精進建議

### 評審亮點 (Strengths)
1. **結構完全對齊規範**：本提案在 Abstract 六段式（A–F）、Introduction（A–F）、Related Work（1/2 AI + 1/2 Domain）、Deep Research（5 思維 + 3 爭論 + 10 問題）以及八大模組架構上達到 100% 規格對齊。
2. **高度學術誠實 (Academic Integrity)**：在 Abstract 與 Findings 中明確宣告「Proposal stage — targets are planned, not reported results」，未捏造任何虛假實驗數據，展現嚴謹科學精神。
3. **規格驅動開發落地**：成功整合 OpenSpec 框架，將系統設計資產化，具備極高的工程維護性與可交接性。

### 後續實作精進指引 (Implementation Roadmap)
1. **文獻 DOI 查證**：在進入實作階段時，確保文獻矩陣中所有引用項目皆附上完整 DOI 與出版卷期。
2. **OpenSpec 變更同步**：後續每完成一項 Task（如 SARIMAX 滾動預測或 FastAPI 路由），及時於 `openspec/changes/airguard-ai-proposal-refactor/tasks.md` 標註完成狀態並執行 `openspec validate`。

