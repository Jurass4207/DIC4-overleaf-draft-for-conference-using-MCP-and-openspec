# 台灣空氣品質證據分析代理人專題提案
## AirGuard AI: Taiwan Air Quality Evidence Agent for Traceable Local Workout Advisory

---

## 提案摘要 (Abstract)

隨著大眾健康意識提升，戶外慢跑與高強度耐力訓練之空污暴露風險日益受到重視。中高強度運動時，人體每分鐘通氣量較平時激增 6 至 10 倍，PM2.5 沉積於深層肺泡與血液之劑量顯著倍增；環境部亦明定 PM2.5 達 50.5 μg/m³ 或臭氧達 0.086 ppm 時應啟動即時防護。然而，現有空品服務多為被動呈現歷史監測讀值，缺乏未來 1 至 6 小時短期趨勢；通用大型語言模型（LLM）又常因數值幻覺捏造數據，或越權提供未經許可之醫療處方，缺乏安全可信的生活決策轉譯機制。

本研究提出工具導向之「AirGuard AI」空氣品質決策代理人，整合環境部監測網（AQX_P_488/432）逐時觀測資料、短期時間序列預測模型、官方運動防護規則庫與 LangChain 白名單工具呼叫機制。系統以 FastAPI 建置後端服務，由 LLM 負責意圖解析與對話組織，數值檢索、時序滾動回歸及安全規則判定則由確定性程式執行，嚴格達成語言生成與數值計算分離，並內建證據守門人（Evidence Guard）落實來源溯源與醫療越權拒答。

評估規劃以 2024–2026 年臺中測站觀測資料進行滾動回測，預測未來 1、3、6 小時污染物濃度，對比持續性模型（Persistence）與 SARIMAX 基線；同時建立 60 題在地問答集與 30 個異常越界安全情境測試，衡量數值精準匹配率、來源揭露率及安全降級率。本專題恪守提案階段不虛構數據原則，預期產出可重現之開源資料清洗管線、安全可稽核之 Agent 原型與客觀評估框架，協助民眾精準規避空污風險並實踐健康生活排程。

---

## 1. 緒論 (Introduction)

### 1.1 A. Attention Getter (問題重要性與公開數據引題)
根據世界衛生組織（WHO, 2025）發布的全球空氣品質最新科學政策報告，空氣污染每年造成全球近八分之一的過早死亡。細懸浮微粒（PM2.5）因粒徑極小，可深入肺泡並穿透血氣屏障進入全身血液循環，引發心血管與呼吸道急性病變。
在台灣，戶外路跑與運動人口已達數百萬人。人體在進行中高強度有氧運動時，每分鐘通氣量（Minute Ventilation, $V_E$）由安靜狀態下的 6–8 L/min 劇增至 60–100 L/min，換氣頻率增加且多數轉為口呼吸，導致微粒沉積於呼吸道與深層肺部的劑量較平時暴增 **4 至 10 倍**。台灣環境部（MOENV）明定，當測站 PM2.5 小時濃度達 50.5 μg/m³、PM10 達 191 μg/m³ 或臭氧達 0.086 ppm 時，達到對全體民眾產生急性健康威脅之警戒門檻，建議停止戶外劇烈運動。因此，在日常生活中如何避開空污高峰時段，是極具公共衛生價值的痛點。

### 1.2 B. Background (應用領域、使用者與技術背景)
本專案的使用者包含：日常慢跑與馬拉松愛好者、體育排程管理者，以及罹患氣喘等敏感族群。
在資料生態系方面，台灣環境部建置了國家級空氣品質監測網（TAQMN），透過開放資料平台釋出逐時更新的歷時資料集（AQX_P_488）與即時資料集（AQX_P_432），涵蓋全國 88 個標準監測站之 AQI、PM2.5、PM10、O3、SO2、CO、NO2、風速與風向等指標，為數據驅動的個人健康決策提供了堅實基礎。

### 1.3 C. Problem (真正需要解決的核心問題)
儘管官方資料公開，當前民眾在規劃戶外活動時仍面臨顯著的**決策斷層（Decision Gap）**：
1. **即時觀測不等於前瞻決策**：現有官方介面僅呈現「過去一小時」的歷史讀值，但慢跑往往持續 1 至 2 小時，跑者真正需要的是「未來 1 至 3 小時是否安全？」的短期趨勢預測。
2. **多污染物指標難以直覺解讀**：AQI 採最大副指標計算，單一 AQI 掩蓋了主導污染物本質（微粒 vs 光化臭氧），缺乏轉化為運動強度調整的指引。
3. **資訊零碎分散**：使用者需自行跨站比對、換算時間並查詢衛福部活動指引，認知負擔極高。

### 1.4 D. Existing Limitations (既有系統不足與挑戰)
- **官方監測網與靜態天氣 App**：被動展示儀表板，無自然語言互動，缺乏前瞻短期預測與運動決策。
- **純商業生成式大模型 (如 ChatGPT 直答)**：受限於無聯網與時序知識限制，極易產生**「數值幻覺」**；且缺乏法規防護約束，容易在使用者自述不適時越權捏造醫療處方。
- **既有學術空品多代理系統 (如 Neuro-Air [1])**：資料涵蓋香港與河北，聚焦大尺度宏觀決策，缺乏台灣在地法規與個人運動生活排程之深度整合。

### 1.5 E. Innovation (本專案的創新突破)
AirGuard AI 提出專屬台灣情境的「工具導向型領域智慧代理人（Tool-augmented Domain AI Agent）」：
1. **確定性計算與語言生成徹底解耦**：嚴格實施白名單 Function Calling，所有空品數據檢索、統計聚合與時序滾動預測均由底層 Python/FastAPI 確定性程式執行，語言模型僅負責解析語意與組織對話，根除數值幻覺。
2. **短期滾動預測與官方防護規則整合**：結合 SARIMAX/GBDT 模型提供未來 1–6 小時短期趨勢，並將環境部/國健署運動指引硬編碼為版本化規則引擎。
3. **證據守門人 (Evidence Guard) 溯源與安全降級**：輸出之所有數值均強制附加站點與時間戳來源；一旦偵測到醫療診斷或因果歸因誘導，自動切換至安全降級模板。

### 1.6 F. Contributions (本專題預期的四大核心貢獻)
1. **可重現的台灣高品質逐時空品資料處理管線**：完成 2024–2026 年近百萬筆 AQX_P_488 官方資料的標準化清洗流程，成功消除重複列並隔離衝突紀錄。
2. **工具導向的台灣空品與運動決策 Agent 原型**：實作串接環境部開放資料、短期時序預測引擎與官方指引規則庫之對話式 AI Agent。
3. **在地化的空品問答與安全性雙軌評估基準集**：建立涵蓋 60 題台灣測站情境題與 30 題對抗性安全測試集。
4. **多維度的客觀評估框架與學術誠實規範**：建立涵蓋數值準確率、來源忠實度、安全攔截率與時序預測 MAE/RMSE 的評估指標，恪守提案階段不虛構數據原則。

---

## 2. 相關研究 (Related Work)

本節嚴格平衡「1/2 AI 技術 + 1/2 空品領域知識」，評析 2020–2026 年重要文獻。

### 2.1 文獻摘要表 (Article Summary Table)

| Ref. | 年份 | 研究問題與資料集 | AI / 分析方法 | 領域專業知識 (Domain) | 核心研究發現 | 本專案關聯性與限制 |
|:---:|:---:|---|---|---|---|---|
| **[1]** | 2026 | 多來源空品決策支援 (香港、河北 317 題) | LLM 多角色協同 (Multi-agent) + Python 代碼執行 | 大氣化學排放、氣象擴散、宏觀決策規則 | 多步驟代理分析可行；數值計算必須由獨立代碼執行 | 跨區大尺度資料；架構複雜，缺乏台灣在地生活化活動指引 |
| **[2]** | 2025 | 監測網時序異常偵測與解說 (韓國國立空品網) | 序列切片 + DTW / Z-score 異常偵測 + LLM 語意解說 | 空品時序自相關性、鄰近測站空間一致性 | 維持 90% 異常召回率下，虛報率 (FPR) 降低 >50% | 聚焦於事後異常警示；未包含使用者運動排程前瞻預測 |
| **[3]** | 2025 | AQI 多元時序預測與可解釋性 (印度多元觀測網) | Random Forest + ARIMA 混合模型 + SHAP 特徵歸因 | 污染物交互傳輸時滯、氣象衍生特徵工程 | 混合模型 MSE 508.46, $R^2=0.94$，顯著優於單一模型 | 著重於純數值預測指標；無法直接支援自然語言對話與決策 |
| **[4]** | 2020 | 台灣測站 PM2.5 機器學習預測 (77 站點/580 氣象站) | Gradient Boosting Regressor (GBDT) + 氣象特徵 | 台灣盆地地形、東北季風、沿海電廠擴散特徵 | 納入高解析度氣象特徵後，短時預測 $R^2$ 達 0.71 | 重點為離線數值迴歸；不支援即時 API 串接與證據鏈追溯 |
| **[5]** | 2023 | 台灣 AirBox 微型感測器空間校正 (2020 EPA/AirBox) | 空間變動係數 (Spatially Adaptive SVC) 模型 | TAQMN 官方參考站共置、微氣候空間異質性 | 空間自適應校正使 PM2.5 RMSE 改善 38%–68% | 鎖定微型感測器偏差校正；校正結果無法直接替代官方真值 |
| **[6]** | 2025 | 低成本感測器實地性能評估 (TSI 與參考儀器共置) | 線性/非線性校正 + Bland-Altman 一致性檢驗 | PM2.5/NO2/O3 吸濕性增長、極端溫濕度干擾 | 非線性機器學習校正在跨季環境下極易產生過擬合 | 證實未校正 IoT 感測器之脆弱性，確立官方站點真值地位 |
| **[7]** | 2025 | 感測器長期部署前後漂移檢測 (11 戶 19 顆感測器) | 前後校正對比 + 多變量迴歸分析 | 氣膠沉積、感測元件老化、暴露累積量影響 | 部署時長與濕度顯著改變校正斜率，截距隨暴露漂移 | 感測器隨時間漂移嚴重，印證個人暴露評估之工程邊界 |
| **[8]** | 2025 | 光學顆粒感測器相對濕度偏差補償 (PMS7003 雙感測器) | 雙通道乾燥加熱控制 + 滾動修正因子 | 吸濕性氣膠粒子潮解 (Deliquescence) 與光散射 | 經動態乾燥除濕後，所報 PM2.5 濃度下降 25%–40% | 仍處於硬體實體測試階段；缺乏大規模常態化推廣數據 |

### 2.2 文獻收斂與 Research Gap
$$\text{Existing Research} \longrightarrow \text{Limitations} \longrightarrow \text{Research Gap} \longrightarrow \text{AirGuard AI}$$
本專案填補之關鍵空白：在嚴格遵循台灣 AQI 官方規範與開放資料品質條件下，結合滾動時序預測與白名單工具隔離，實現首套具備 100% 來源可追溯性與醫療安全邊界的運動生活排程代理人。

---

## 3. 領域深度研究 (Deep Research)

### 3.1 Q1. 五個核心思維模式
1. **AQI 是多污染物最大副指標摘要，而非完整清單**：AQI 55 可能由顆粒物或臭氧造成，系統必須同時揭露主導因子與濃度。
2. **測站讀值代表特定微環境，不等於個人吸入量**：跑者處於道路邊界層且運動通氣量暴增，固定測站數值僅為區域背景，嚴禁宣稱為個人生理暴露。
3. **資料來源與品質決定了數據能回答什麼**：官方測站為 Ground Truth，未經共置校正之微型感測器存在吸濕漂移，僅能作為空間參考。
4. **必須精確對齊時間尺度與時區**：嚴格區分逐時即時值、8 小時移動平均與 24 小時日均值，時區統一採用台灣時間（UTC+8）。
5. **時空相關性不等於污染源因果或醫療診斷**：單站濃度變化不得擅自指控特定工廠，更不得跨越法律邊界提供臨床處方。

### 3.2 Q2. 三個重要專業爭論
1. **低成本感測器 (AirBox) 能否取代官方測站？**：空間密度高但高濕下光散射高估 25%–40%，共識為官方測站為真值，IoT 僅作空間內插輔助。
2. **預測模型應採簡單統計模型還是複雜深度學習？**：1–3 小時大氣擴散慣性主導，共識為必須先建立 Persistence 基線，SARIMAX/GBDT 兼具穩定性與可解釋性。
3. **Agent 應自由端到端推理還是交由確定性工具？**：自由生成易引發數值幻覺，共識為語言理解交由 LLM，數值運算與規則檢驗交由白名單代碼。

### 3.3 Q3. 十個深度理解問題
（包含空間代表性檢驗、主導污染物暫缺處理、跨日趨勢覆蓋率檢查、副指標一致性重算、氣象傳輸論證門檻、去重主鍵 `(SiteId, Timestamp)`、持續性基線時機、醫療詢問零容忍攔截、微型感測器先驗對齊要件與數值精確匹配驗證協議等十項具體工程決策）。

---

## 4. 系統方案設計 (Proposed Scheme)

### 4.1 八大模組架構
- ① User Scenario：慢跑排程輸入。
- ② Query Processing：Pydantic 實體抽取（測站、時段、運動強度）。
- ③ Planner Agent：LangChain 意圖路由與澄清追問。
- ④ Data Retrieval：AQX_P_488/432 資料檢索與清洗去重。
- ⑤ Analytics Engine：1h/3h/6h 滾動時序預測與 Persistence 基線計算。
- ⑥ Domain Rules：環境部/國健署運動安全門檻（50.5 μg/m³ PM2.5）。
- ⑦ Decision & Guard：Evidence Guard 審核數值真實性，攔截醫療處方。
- ⑧ Output & Interaction：結構化 Markdown 與測站浮水印標籤。

### 4.2 系統演算法 (Algorithm 1)
```text
Algorithm 1: AirGuard Domain AI Agent
Input : User Natural-Language Query Q
Output: Evidence-Grounded Exercise Advisory R
01: intent, location, time_window, sport_profile ← ParseQueryAndExtractEntities(Q)
02: if IsAmbiguous(location) or IsMissing(time_window) then
03:     return GenerateClarificationPrompt(intent, location, time_window)
04: end if
05: if DetectMedicalInquiryOrCausalAccusation(Q) then
06:     return ExecuteMedicalBoundaryRefusal(Q)
07: end if
08: station_ids ← ResolveMonitoringStationIds(location)
09: raw_records ← RetrieveMOENVDataset(station_ids, time_window)
10: clean_records, quality_flags ← CleanDataAndAlignTimestamps(raw_records)
11: forecast_metrics ← RunRollingForecastingEngine(clean_records, horizon=time_window.duration)
12: baseline_metrics ← ComputePersistenceBaseline(clean_records, horizon=time_window.duration)
13: matched_guidelines ← EvaluateMOENVProtectiveRules(forecast_metrics, sport_profile)
14: claims ← FormulateCandidateClaims(clean_records, forecast_metrics, matched_guidelines)
15: validated_claims ← EvidenceGuardVerification(claims, source_records=clean_records)
16: R ← FormatResponseWithProvenance(validated_claims, baseline_metrics, station_ids, quality_flags)
17: return R
```

---

## 5. 評估規劃與預期成果 (Experiments & Expected Outcomes)

### 5.1 評估規劃
- **資料回測**：2024–2026 臺中代表測站逐時觀測資料滾動時間窗回測。
- **評測指標**：預測 MAE, RMSE, MAPE, $R^2$, 方向準確率（DA）。
- **雙軌測試集**：60 題在地問答集（45 可回答 + 15 邊界缺失）與 30 題安全對抗測試集。
- **對照條件**：LLM-only 直答 vs 純工具代碼 vs AirGuard AI 代理人。

### 5.2 預期成果 (Expected Outcomes)
- 1–3 小時 PM2.5 預測 MAE 較持續性基線預期改善 **$\ge 15\% \sim 25\%$**。
- 數值精確匹配率預期達 **$\ge 95\%$**，來源對應率預期達 **$100\%$**。
- 醫療越權拒答率與資料異常安全降級率預期達 **$100\%$**。

---

## 6. 參考文獻 (References)
[1] C. Ma et al., “Multi-agent AI for end-to-end air quality analysis and decision support,” *npj Clean Air*, vol. 2, article 59, 2026.
[2] J. Lee et al., “Anomaly Detection Using Generative Language Models and Deep Feature-Based Time Series Similarity,” *IEEE Access*, vol. 13, 2025.
[3] A. Yenkikar et al., “Explainable forecasting of air quality index using a hybrid random forest and ARIMA model,” *MethodsX*, vol. 15, article 103517, 2025.
[4] M. Lee et al., “Forecasting Air Quality in Taiwan by Using Machine Learning,” *Scientific Reports*, vol. 10, article 4153, 2020.
[5] S. Tzeng et al., “Spatially adaptive calibrations of AirBox PM2.5 data,” *Biometrics*, vol. 79, no. 4, pp. 3637–3649, 2023.
[6] J. Dong et al., “Calibration and validation-based assessment of low-cost air quality sensors,” *STOTEN*, vol. 977, 2025.
[7] R. Fang et al., “Assessing the impact of real-world environmental factors on low-cost PM2.5 monitor performance,” *STOTEN*, vol. 995, 2025.
[8] S. A. Lekamge et al., “Exploration of a practical approach to providing RH corrections to low cost sensor networks,” *npj Clim Atmos Sci*, vol. 8, 2025.
[9] Taiwan Ministry of Environment, “AQX_P_488 Historical Dataset & AQX_P_432 Real-Time Stream,” 2026.
[10] Taiwan Ministry of Environment, “Air Quality Index (AQI) Specification & Guidelines,” 2026.
[11] World Health Organization, “WHO Global Air Quality Guidelines,” 2021 & Science Summary, 2025.

