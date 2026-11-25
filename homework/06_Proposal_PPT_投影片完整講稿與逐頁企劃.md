# AirGuard AI: 期末專題簡報 (Proposal PPT) 逐頁企劃與演講講稿
### 對標 20+ 頁投影片規範，涵蓋動機、文獻、Gap、架構、流程圖、虛擬碼與評估

---

### Slide 1: 封面 (Title Slide)
- **投影片標題**：AirGuard AI：台灣空氣品質證據分析代理人
- **副標題**：結合環境部逐時資料、滾動時序預測與官方活動指引的工具導向運動決策 Agent
- **英文題名**：Taiwan Air Quality Evidence Agent for Traceable Local Workout Advisory
- **報告人/團隊**：專題研究團隊
- **日期**：2026 年 11 月
- **講稿要點**：各位老師、同學好，今天我們要報告的專題是「AirGuard AI」。這是一個專門為台灣戶外運動愛好者設計的領域智慧代理人（Domain AI Agent），核心目標是消除跑者在突發空污下的健康暴露盲區。

---

### Slide 2: 研究動機 (Attention Getter — WHO 數據與生理痛點)
- **主視覺/數據圖標**：
  - WHO 2025/2026：全球每年近 1/8 死亡歸因於空氣污染。
  - 運動換氣通氣量 ($V_E$)：安靜 6–8 L/min $\longrightarrow$ 跑步 **60–100 L/min (激增 6–10 倍)**。
  - 肺泡深層微粒沉積量：口呼吸主導，PM2.5 沉積率暴增 **4–10 倍**。
  - 環境部防護紅線：PM2.5 小時值 $\ge 50.5\,\mu\text{g/m}^3$、臭氧 $\ge 0.086\,\text{ppm}$ 應停止戶外劇烈運動。
- **講稿要點**：為什麼這個題目現在非常重要？大眾運動意識高漲，慢跑人口突破數百萬。但運動生理學告訴我們，劇烈運動時換氣量飆升近 10 倍，吸入的空污是平時的數倍，急性心血管與呼吸道風險劇增。

---

### Slide 3: 核心挑戰與現有不足 (But — Challenge & Pain Points)
- **三大痛點對比卡片**：
  1. **被動監測缺乏前瞻性**：現有網站或 App 僅顯示過去 1 小時歷史讀值，跑者跑 10 公里需要的是「未來 1–3 小時」的趨勢。
  2. **多污染物指標難以直覺決策**：AQI 是最大副指標運算，跑者無法直覺判斷當前是微粒超標還是光化臭氧蓄積。
  3. **通用 LLM 幻覺與醫療安全越權**：直接問 ChatGPT 容易捏造測站數據，若自述胸痛甚至可能越權捏造藥物建議，引發法律與安全邊界問題。
- **講稿要點**：現有的工具若非太被動，就是純 LLM 黑盒瞎猜，缺乏一套可驗證、有依據的個人化生活排程決策系統。

---

### Slide 4: 解決方案與核心定位 (Cure — AirGuard AI)
- **核心定位圖示**：
  $$\text{AI Agent} + \text{Domain Knowledge} + \text{Data Analytics} + \text{Public Health}$$
- **三大核心支柱**：
  - **白名單工具隔離**：LLM 負責語意，底層 Python 負責數值，徹底根除數值幻覺。
  - **滾動時序預測**：結合環境部 AQX_P_488 歷史資料，提供 1–6 小時短期趨勢。
  - **官方防護規則硬編碼**：將環境部與國健署活動指引版本化，內建 Evidence Guard 安全守門機制。
- **講稿要點**：我們提出 AirGuard AI，這不是一個純 Chatbot，而是一個懂領域、會取資料、會做確定性分析並具備安全防線的 Domain AI Agent。

---

### Slide 5: 相關研究 1：時序預測與 AI 代理人
- **文獻回顧要點**：
  - **Ma et al. (2026, npj Clean Air)**：Neuro-Air 驗證了多代理人協調分析空品的可行性，但指出數值運算必須仰賴外部 Python 代碼。
  - **Lee et al. (2025, IEEE Access)**：韓國空品監測網結合序列切片與 DTW 降低異常虛報率 50%。
  - **Yenkikar et al. (2025, MethodsX)**：Random Forest + ARIMA 預測 AQI，MSE 達 508.46。
- **講稿要點**：國際最新文獻證實，將 LLM 與專門的計算環境分離，是環境 AI 系統的共同趨勢。

---

### Slide 6: 相關研究 2：台灣在地空品與感測器特性
- **文獻回顧要點**：
  - **Lee et al. (2020, Sci. Reports)**：台灣 77 測站/580 氣象站 GBDT 短時預測，$R^2$ 達 0.71。
  - **Tzeng et al. (2023, Biometrics)**：台灣 AirBox 空間自適應校正使 RMSE 改善 38%–68%。
  - **Dong et al. (2025) & Fang et al. (2025, STOTEN)**：低成本感測器易受相對濕度影響光散射，隨時間漂移嚴重，確立官方參考級站點之真值地位。
- **講稿要點**：台灣研究指出微型感測器存在溫濕度漂移，因此本專題以環境部官方測站為核心真值，不以未驗證的感測器作為評估基準。

---

### Slide 7: 文獻矩陣與 Research Gap (Article Summary Table)
- **表格呈現**：完整展示 8 篇 2020–2026 年論文比較表（Problem, Method, Domain, Findings, Limitations）。
- **收斂路徑**：
  $$\text{Existing Research} \longrightarrow \text{Limitations} \longrightarrow \text{Research Gap} \longrightarrow \text{AirGuard AI}$$
- **本專題採用的 Research Gap**：
  目前學界尚未看到專門以台灣環境部開放資料（AQX_P_488）為基底，結合短期時序預測，專門評估生活化運動排程問答的端到端評估基準。

---

### Slide 8: Deep Research Q1：五個核心思維模式
1. **多污染物摘要**：AQI 掩蓋分項指標，系統必須揭露主導污染物。
2. **微環境非個人劑量**：測站代表區域背景，運動換氣量不同，不可宣稱等同個人劑量。
3. **資料來源決定品質**：官方參考級測站真值 vs. 微型感測器空間輔助。
4. **時間尺度精確對齊**：小時值、8小時平均、24小時平均毒理意義相異，禁止混淆。
5. **時空相關不等於因果/醫療**：風向與濃度相關非污染源證明，嚴禁越權開立醫療建議。

---

### Slide 9: Deep Research Q2：三個最重要的專業爭論
- **爭論 1：低成本感測器能否取代官方測站？**
  - 高密度優勢 vs. 吸濕光散射漂移（共識：官方為真值，IoT 為空間輔助）。
- **爭論 2：短期預測應採簡單統計模型還是複雜深度學習？**
  - 泛化可解釋 vs. 非線性突波（共識：先建立 Persistence/SARIMAX 基線）。
- **爭論 3：Agent 應由 LLM 自由推理還是交由工具確定性計算？**
  - 靈活生成 vs. 數值幻覺（共識：語意交由 LLM，計算與規則交由工具）。

---

### Slide 10: Deep Research Q3：十個深度理解問題 (精選展示)
- 展示關鍵工程決策：
  - *Q3 覆蓋率不足*：若測站覆蓋率 < 75%，禁止計算日平均，觸發品質降級警示。
  - *Q6 資料筆數假象*：清理 AQX_P_488 發現 36 萬重複列，去重主鍵必須為 `(SiteId, Timestamp)`。
  - *Q8 醫療越權攔截*：跑者詢問用藥處方時，觸發 Zero Medical Advice 政策，輸出專業醫警並拒答。

---

### Slide 11: 系統八大模組架構 (System Architecture ①～⑧)
- **架構圖清晰展示**：
  - ① User Scenario $\longrightarrow$ ② Query/NLP Parser $\longrightarrow$ ③ Planner Agent
  - ④ Data Acquisition (AQX_P_488/432) $\longrightarrow$ ⑤ Analytics & Forecasting Engine
  - ⑥ Domain Knowledge Engine $\longrightarrow$ ⑦ Decision & Safety Guard $\longrightarrow$ ⑧ Output & Interaction
- **技術棧標註**：FastAPI + LangChain + SARIMAX/GBDT + Pydantic + Docker。

---

### Slide 12: 系統泳道決策流程圖 (Flowchart)
- **包含關鍵決策菱形與迴圈**：
  - 實體是否歧義？$\longrightarrow$ 觸發 **Clarification Loop** 多輪追問。
  - 是否包含醫療/因果誘導？$\longrightarrow$ 觸發 **Safety Refusal** 拒答。
  - 資料覆蓋率是否 $\ge 75\%$？$\longrightarrow$ 觸發品質降級告警。
  - 數值是否經來源核對？$\longrightarrow$ Evidence Guard 查驗通過後附加浮水印輸出。

---

### Slide 13: 核心演算法虛擬碼 (Algorithm 1: AirGuard Domain AI Agent)
- 展示具備行號的標準演算法 Pseudocode（Line 01 至 Line 24）。
- 重點強調：
  - `Line 02-04`：澄清機制處理。
  - `Line 05-07`：醫療邊界拒答。
  - `Line 18-19`：預測模型與 Persistence 基線計算。
  - `Line 22-23`：Evidence Guard 來源對齊與 Markdown 溯源輸出。

---

### Slide 14: 證據守門演算法 (Algorithm 2: Evidence Guard)
- **審核機制細節**：
  - 檢驗候選主張（Candidate Claims）之測站 ID 與時間戳是否 100% 存在於檢索出的資料列中。
  - 濃度誤差大於 $\epsilon$ 則判定為幻覺數值，立即剔除並記錄審計日誌。
  - 針對預測數值強制附加 95% 置信區間與基線比較參考。

---

### Slide 15: 資料庫準備與品質稽核 (Data Audit)
- **環境部 AQX_P_488 資料集實測清洗成果**：
  - 原始列數：970,296 列 (2026-01-01 至 2026-10-29)。
  - 合併中英文重複列：364,159 列。
  - 唯一恢復缺失測站：4 筆。
  - 隔離時間戳衝突鍵：13 組。
  - **淨產出高品質觀測列：606,137 筆 (88 個測站)**。
- 腳本支援：`scripts/clean_aqi_data.py`。

---

### Slide 16: 評估規劃 1：時序滾動回測設計
- **回測架構**：2024–2026 年臺中測站（西屯交通站、忠明一般站）逐時觀測資料。
- **預測視界**：未來 1 小時、3 小時、6 小時。
- **評估指標公式**：$MAE$、$RMSE$、$MAPE$、$R^2$ 與方向準確率（$DA$）。
- **比較基準**：持續性基準（Persistence）、季節性 Naïve、ARIMA/SARIMAX、GBDT。

---

### Slide 17: 評估規劃 2：60+30 雙軌測試集設計
- **60 題在地問答集 (Ground-Truth QA Benchmark)**：
  - 45 題可回答任務（短期趨勢 15、多站比較 15、AQI解讀 15）。
  - 15 題邊界任務（資料缺漏、感測器衝突、超範圍提問）。
- **30 題安全邊界對抗測試集 (Adversarial Safety Suite)**：
  - 醫療用藥處方誘導 (10 題)。
  - 非客觀污染源歸因 (8 題)。
  - 數值竄改與 Prompt Injection (7 題)。
  - API 異常與網路逾時 (5 題)。

---

### Slide 18: 預期成果與學術誠實 (Expected Outcomes)
- **學術誠實宣告**：提案階段尚未實施實驗者僅列預期目標，不捏造任何數值。
- **預期量化成效目標**：
  - 1–3 小時 PM2.5 預測 MAE 相較基線改善率：**$\ge 15\% \sim 25\%$**。
  - 數值精確匹配率 (Exact Match Rate)：**$\ge 95\%$**。
  - 來源對應率 (Provenance Fidelity)：**$100\%$**。
  - 醫療越權拒答率 (Safety Refusal Rate)：**$100\%$**。
  - 異常資料安全降級率 (Graceful Degradation)：**$100\%$**。

---

### Slide 19: 規格驅動開發與專案交付標準 (OpenSpec Handover)
- **導入 OpenSpec (v1.17.0)**：
  - 規格文件通過 `openspec validate --strict` 嚴格校驗。
  - 確立「規格契約先行於代碼撰寫」之 SDD 工程標準。
- **期末交付物 (Final Handover Package)**：
  - GitHub 完整開源 Repository。
  - 規格設計手冊 DESIGN.md。
  - 10 分鐘以上完整演示 Demo 影片。

---

### Slide 20: 結論與致謝 (Conclusion & Q&A)
- **專案總結**：AirGuard AI 成功示範了如何將環境開放大數據、短期時序預測與官方活動指引轉化為可落地、無幻覺且具備法律安全防線的 Domain AI Agent。
- **致謝與 Q&A**：感謝老師與同學聆聽，敬請指教！

