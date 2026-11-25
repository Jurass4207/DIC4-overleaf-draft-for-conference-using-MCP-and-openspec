# AirGuard AI: 資訊圖表 A4 橫式高密度 NUMBERING 架構規格書
### 適用於 A4 橫向 (Landscape 297mm × 210mm) 海報、簡報雙跨頁與高密度資訊圖表排版

```
+-------------------------------------------------------------------------------------------------------------------------+
| AIRGUARD AI: PRECISION AIR-QUALITY & OUTDOOR WORKOUT ADVISORY DOMAIN AGENT                                              |
| Spec-Driven Architecture Grounded in Taiwan MOENV Real-Time & Historical Datasets                                       |
+------------------------------------------+------------------------------------------+-----------------------------------+
| [COLUMN 1: MOTIVATION & DOMAIN TRIAD]    | [COLUMN 2: ARCHITECTURE & ALGORITHMS]    | [COLUMN 3: EVALUATION & SAFETY]   |
| 1.0 Executive Identity                   | 4.0 8-Module System Architecture         | 6.0 Experimental Methodology      |
| 2.0 Epidemiological Evidence & Pain      | 4.1 Input & NLP Extraction               | 6.1 2024-2026 Rolling Backtest    |
| 3.0 Deep Research Triad                  | 4.2 Planner & Whitelist Tools            | 6.2 60-Question Ground Truth QA   |
|   3.1 5 Core Domain Mindsets             | 4.3 Versioned Rule Engine                | 6.3 30-Case Adversarial Safety    |
|   3.2 3 Major Expert Controversies       | 5.0 Data Engineering & Pseudocode        | 7.0 Quantitative Expected Targets |
|   3.3 10 Critical Engineering Decisions  |   5.1 Key Conflict Isolation             | 8.0 OpenSpec Spec-Driven Handover |
+------------------------------------------+------------------------------------------+-----------------------------------+
```

---

## 1.0 PROJECT IDENTITY & CORE PARADIGM
- **1.1 Formal Title**: AirGuard AI: Taiwan Air Quality Evidence Agent for Traceable Local Workout Advisory.
- **1.2 Core Paradigm**: Tool-augmented Domain AI Agent (AI Agent + Domain Knowledge + Data Analytics + Public Health).
- **1.3 Mission Statement**: 消除戶外跑者在突發空污下的健康暴露盲區，提供 1–6 小時具備 100% 來源可溯源性的運動生活排程決策。

---

## 2.0 EPIDEMIOLOGICAL MOTIVATION & DATA EVIDENCE
- **2.1 Exposure Augmentation**: 
  - `2.1.1` 安靜狀態呼吸通氣量：$V_E = 6\sim 8\,\text{L/min}$（以鼻腔過濾為主）。
  - `2.1.2` 戶外慢跑與訓練通氣量：$V_E = 60\sim 100\,\text{L/min}$（口呼吸主導，換氣量劇增 6–10 倍）。
  - `2.1.3` 深層肺泡沉積率：微粒沉積量較靜止狀態放大 **4 至 10 倍**，顯著提升心肌缺血與氣喘急性誘發率。
- **2.2 Official Action Thresholds (Taiwan MOENV)**:
  - `2.2.1` PM2.5 小時濃度 $\ge 50.5\,\mu\text{g/m}^3$（紅色警示，啟動即時防護動員，停止戶外劇烈運動）。
  - `2.2.2` 臭氧（O3）小時濃度 $\ge 0.086\,\text{ppm}$（強氧化劑刺激呼吸道黏膜，午後光化突波防範）。
- **2.3 Existing Industry Limitations**:
  - `2.3.1` 官方網頁/天氣 App：僅被動呈現 1 小時前歷史數據，缺乏未來 1–6 小時短期趨勢與個人化排程指引。
  - `2.3.2` 純通用 LLM 直答：數值幻覺率高、偽造測站紀錄、越權捏造未經核准之臨床醫療處方。

---

## 3.0 DEEP RESEARCH TRIAD (5 CORES + 3 CONTROVERSIES + 10 DETAILS)
- **3.1 Five Core Domain Mindsets (5 大思維)**:
  - `3.1.1` [Multi-Pollutant] AQI 為多污染物最大副指標運算，展示時必須同時揭露主導污染物與計算時間窗。
  - `3.1.2` [Micro-Environment] 測站讀值代表區域宏觀背景，非跑者微環境個人呼吸吸入劑量。
  - `3.1.3` [Source Hierarchy] 嚴格區分官方參考級測站（真值）與未校正 IoT 感測器（僅作空間輔助）。
  - `3.1.4` [Temporal Alignment] 小時值、8 小時滑動平均與 24 小時日均值具備相異毒理意義，禁止跨尺度混淆。
  - `3.1.5` [Clinical Boundary] 時空共變性不等於污染源因果，嚴禁越權提供個人醫療診斷與用藥處方。
- **3.2 Three Major Expert Controversies (3 大爭論)**:
  - `3.2.1` [IoT vs Official Station] 空間密度 vs 吸濕光散射漂移（共識：官方測站為 Ground Truth，IoT 需共置校正）。
  - `3.2.2` [Simple Baseline vs Deep ML] 泛化可解釋性 vs 非線性突波（共識：以 Persistence/SARIMAX 為核心基線）。
  - `3.2.3` [Free LLM vs Whitelist Tool] 生成靈活性 vs 數值可稽核性（共識：語言與計算徹底分離）。
- **3.3 Ten Critical Engineering Decisions (10 大細節)**:
  - `3.3.1` 空間代表性判定（結合風速風向與地形）；`3.3.2` 主導污染物暫缺處理；`3.3.3` 跨日趨勢資料覆蓋率檢查（<75% 降級）；`3.3.4` 副指標一致性公式重算；`3.3.5` 傳輸論證門檻；`3.3.6` 原始資料去重主鍵 `(SiteId, Timestamp)`；`3.3.7` 持續性基線啟用時機（$t+1$ 平穩期）；`3.3.8` 醫療詢問零容忍攔截；`3.3.9` 微型感測器先驗對齊要件；`3.3.10` 數值精確匹配驗證協議。

---

## 4.0 SYSTEM ARCHITECTURE & 8-MODULE PIPELINE
- **4.1 ① User Scenario**: 跑者自然語言輸入（地點、預計跑步時長、過敏病史）。
- **4.2 ② Query/NLP Parser**: Pydantic 實體抽取，解析測站編號、時間窗與運動強度。
- **4.3 ③ Planner & Reasoning Agent**: LangChain 意圖路由，觸發澄清機制（Clarification Loop）。
- **4.4 ④ Data Acquisition API**: 串接 AQX_P_488 歷時資料庫（清洗後 606,137 筆）與 AQX_P_432 即時串流。
- **4.5 ⑤ Forecasting Analytics Engine**: 滾動輸出 1h/3h/6h 預測濃度、95% 置信區間與基線對比。
- **4.6 ⑥ Domain Knowledge Engine**: 硬編碼 MOENV/HPA 活動安全矩陣（安全/減量/室內）。
- **4.7 ⑦ Decision & Safety Guard**: 跨表核對主張數值與原始觀測，攔截醫療處方與因果歸因。
- **4.8 ⑧ Output & Interaction**: 結構化 Markdown、浮水印溯源標籤與不確定性宣告。

---

## 5.0 DATA FLOW & ALGORITHMIC PSEUDOCODE
- **5.1 Dataset Audit (MOENV AQX_P_488)**:
  - `5.1.1` 原始下載列數：970,296 列 (2026-01-01 至 2026-10-29)。
  - `5.1.2` 清洗去重：合併中英文重複列，恢復 4 筆座標唯一測站，隔離 13 組數值衝突鍵。
  - `5.1.3` 高品質觀測列：淨產出 **606,137 筆** 唯一測站觀測紀錄。
- **5.2 Core Algorithmic Steps (Algorithm 1: AirGuard Agent)**:
  - `Line 01-04`：實體解析與歧義追問（Clarification Loop）。
  - `Line 05-07`：醫療諮詢即時攔截與拒答（Zero Medical Advice）。
  - `Line 08-13`：MOENV 歷史與即時觀測檢索，完成品質覆蓋檢驗。
  - `Line 14-19`：滾動執行 SARIMAX 預測與持續性（Persistence）基線計算。
  - `Line 20-22`：比對官方運動防護門檻，Evidence Guard 核驗數值來源。
  - `Line 23-24`：輸出具備測站時間浮水印的結構化運動排程建議。

---

## 6.0 EXPERIMENTAL METHODOLOGY & BENCHMARKING
- **6.1 2024–2026 Rolling Backtesting**:
  - `6.1.1` 測站選取：臺中西屯站（交通密集盆地）、忠明站（市區背景）。
  - `6.1.2` 評估指標：$MAE = \frac{1}{n}\sum |y - \hat{y}|$、$RMSE = \sqrt{\frac{1}{n}\sum (y - \hat{y})^2}$、$R^2$、方向準確率（$DA$）。
- **6.2 60-Question Domain QA Benchmark**:
  - `6.2.1` 45 題可回答任務：短期趨勢 (15)、多站比較 (15)、AQI/主導污染物解讀 (15)。
  - `6.2.2` 15 題邊界任務：資料缺漏、感測器衝突、超範圍提問。
- **6.3 30-Case Adversarial Safety Suite**:
  - `6.3.1` 10 題臨床醫療與藥物處方誘導。
  - `6.3.2` 8 題非客觀污染源因果歸因指控。
  - `6.3.3` 7 題數值竄改與 Prompt Injection 測試。
  - `6.3.4` 5 題 API 逾時與回傳中斷壓力測試。
- **6.4 Tri-Condition Experimental Setup**:
  - `Condition 1`：LLM-only 直答（衡量幻覺率與越權率）。
  - `Condition 2`：純確定性工具程式輸出（衡量表達僵化度）。
  - `Condition 3`：AirGuard AI 工具型代理人（衡量端到端綜合效能）。

---

## 7.0 EXPECTED OUTCOMES & ACADEMIC INTEGRITY
- **7.1 Integrity Principle**: 提案階段不虛構任何實驗數據（Targets are planned, not reported results）。
- **7.2 Quantitative Planned Targets**:
  - `7.2.1` 1–3 小時預測 MAE 相對改善率：$\ge 15\% \sim 25\%$（對比持續性基線）。
  - `7.2.2` 數值精確匹配率（Exact Numeric Match）：$\ge 95\%$。
  - `7.2.3` 來源對應率（Provenance Fidelity）：$100\%$。
  - `7.2.4` 醫療越權拒答率（Safety Refusal Rate）：$100\%$。
  - `7.2.5` 異常資料安全降級率（Graceful Degradation）：$100\%$。

---

## 8.0 FINAL HANDOVER PACKAGE REQUIREMENTS
- **8.1 OpenSpec Compliance**: 透過 `openspec validate --strict` 達成 100% 規格驅動資產合規。
- **8.2 Deliverable Package Inventory**:
  - `8.2.1` 完整專題企劃書（Proposal Document）。
  - `8.2.2` 規格文件（`DESIGN.md` 與 `openspec/` 變更規格）。
  - `8.2.3` 開源資料處理腳本（`scripts/clean_aqi_data.py`）。
  - `8.2.4` 雙軌評估基準測試集（60+30 題）。
  - `8.2.5` 專題簡報 PPT 與 Demo 影片。

