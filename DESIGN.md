# DietSense: 領域智慧代理人系統架構與設計文件 (Living System Design)

本文件依據期末專題交接規範，詳細闡明 DietSense 之問題定義、需求分析、八大模組架構、資料流程、演算法偽碼、數學公式、安全防護與驗證方式。即使後續由新開發者接手，亦能依循此文件完全理解並繼續推進實作。

## 1. 核心問題與架構定位 (Problem & Positioning)

### 1.1 痛點與挑戰
- 傳統熱量記錄工具需要大量手動搜尋與秤重，操作負擔沉重，導致 85% 使用者在 30 天內放棄。
- 自報飲食份量誤差高達 18% 至 54%，深碗、羹湯與隱藏烹調油進一步擴大熱量不確定性。
- 通用 LLM 直接生成卡路里數值時 MAPE 高達 35.8%，存在嚴重數值幻覺與缺乏本土食材資料庫問題。

### 1.2 四大核心定位 (AI Agent + Domain + Analytics + Real-World)
- **AI Agent**: 採用 LLM Planner 作為大腦核心，管理對話歷史與槽位抽取，並在資訊不足時主動發起追問（Clarification Loop）。
- **Domain Knowledge**: 引入熱力學能量代謝模型、Mifflin-St Jeor TDEE 公式、AMDR 巨量營養素比例、衛福部每日飲食指南，以及安全下限（< 1,200 kcal/天）硬性防護。
- **Data Analytics**: 整合 TFDA 台灣資料庫、USDA FoodData Central 與自建台式小吃向量庫，計算動態信賴區間而非單一偽精確數字。
- **Real-World Application**: 鎖定台灣在地外食文化（夜市小吃、便當、複合湯麵、手搖飲），解決真實公衛減重痛點。

## 2. 八大系統模組與時序資料流 (System Architecture & Data Flow)

系統模組嚴格拆解如下：
1. **① User Scenario**: 接收日常繁中語音或文字（「午餐吃了一碗加蛋牛肉麵，湯喝一半」）。
2. **② Query Processing**: Whisper 語音轉文字、繁簡正規化、四元意圖分類（`log_food`, `query_nutrition`, `analyze`, `recommend`）。
3. **③ Planner Agent**: 維護對話上下文，調度外部檢索工具，當檢索信心 < 80% 時產出澄清問題。
4. **④ Data Acquisition**: 並行查詢 TFDA、USDA API 與在地 RAG 向量庫。
5. **⑤ Analytics Engine**: 依確定性公式計算熱量、蛋白質、脂肪、碳水，並依信心度計算信賴區間。
6. **⑥ Domain Knowledge**: 驗證 AMDR 巨量營養素比例，檢查全日攝取是否觸碰臨床安全底線。
7. **⑦ Decision/Recommendation**: 計算個人化代謝缺口，推薦在地低卡原型替代食材。
8. **⑧ Output/Interaction**: 輸出結構化 Markdown 卡片、圓餅圖數據與下一輪對話引導。

### 互動時序邏輯 (Swimlane Workflow)
```
使用者輸入 -> 意圖解析 -> 實體抽取 (NER) -> 多來源資料庫檢索 -> 信心度評估
[若 信心度 < 80%] -> 觸發 Clarification Loop -> 追問關鍵細節 -> 重新錨定
[若 信心度 >= 80%] -> 確定性熱量換算 -> 不確定性區間量化 -> 寫入每日日誌 -> 臨床安全檢查
[若 總熱量 < 1200 kcal] -> 攔截生成 -> 發布安全警告與醫療轉介
[若 狀態正常] -> 產出結構化圖表與在地替換建議 -> 結束交互
```

## 3. 核心演算法與數學公式 (Algorithm & Formulations)

### 3.1 核心演算法 (Algorithm 1: DietSense Pipeline)
```python
# 帶行號之系統主程序
01: def diet_agent_pipeline(Q: str, P: UserProfile, D: DailyLog) -> tuple[Response, DailyLog]:
02:     Q_norm = normalize_natural_language(Q)
03:     intent = classify_intent(Q_norm)
04:     if intent == "log_food":
05:         entities = extract_food_entities(Q_norm)
06:         for item in entities:
07:             candidates = query_all_databases(item.name)
08:             best_match, confidence = rank_candidates(candidates, item.context)
09:             if confidence < 0.80:
10:                 clarification_q = generate_clarification_prompt(item, candidates)
11:                 user_answer = await ask_user_interactive(clarification_q)
12:                 item = update_entity_with_clarification(item, user_answer)
13:                 best_match, confidence = rank_candidates(query_all_databases(item.name), item.context)
14:             grams = estimate_portion_grams(item.portion, best_match.standard_unit)
15:             kcal_point = (grams * best_match.kcal_per_100g) / 100.0
16:             kcal_low, kcal_high = compute_uncertainty_interval(kcal_point, confidence)
17:             D.add_entry(food=best_match, portion_g=grams, kcal_point=kcal_point, bounds=(kcal_low, kcal_high))
18:     elif intent == "analyze":
19:         daily_total = sum(entry.kcal_point for entry in D.entries)
20:         bmr = compute_mifflin_bmr(P.weight_kg, P.height_cm, P.age, P.gender)
21:         tdee = bmr * P.activity_multiplier
22:         deficit = daily_total - tdee
23:     safety_status = evaluate_safety_guardrails(D, P)
24:     if safety_status == "DANGER":
25:         return format_response(alert="Extreme Caloric Restriction Intercepted"), D
26:     return format_response(daily_log=D, analytics=(daily_total, tdee, deficit)), D
```

### 3.2 能量代謝與不確定性數學形式
- **Mifflin-St Jeor 基礎代謝率**:
  $$\text{BMR}_{\text{male}} = 10W + 6.25H - 5A + 5$$
  $$\text{BMR}_{\text{female}} = 10W + 6.25H - 5A - 161$$
  $$\text{TDEE} = \text{BMR} \times \text{PAL}$$
- **動態不確定性信賴區間**:
  $$E = \frac{\text{Portion(g)} \times \text{kcal}_{100\text{g}}}{100}$$
  $$\Delta E = E \times \left( \alpha + (1 - C) \times \beta \right), \quad \alpha = 0.08, \; \beta = 0.35$$
  $$\mathcal{I}_E = \left[ E - \Delta E, \; E + \Delta E \right]$$

## 4. 系統安全、隱私與降級設計 (Safety & Privacy)

1. **臨床安全守門**:
   - 每日目標或累積攝取低於 1,200 kcal/天時強制阻斷極端節食建議；
   - 偵測暴食後極端節食之補償心理循環（Binge-Restrict Pattern），啟動心理關懷與註冊營養師諮詢轉介。
2. **未知食材優雅降級 (Fallback Decomposition)**:
   - 遇未建檔之私房菜或特殊混合料理，將其拆解為「基礎澱粉 + 主蛋白質肉類 + 蔬菜 + 烹調油」代理食材加總估算，並明確標記為近似重構值。
3. **個資安全與本地隔離**:
   - 使用者之身高、體重、年齡與個人飲食歷史存放於本地隔離加密資料庫，不隨意上傳至第三方未授權雲端。

## 5. 評估與驗證方式 (How to Verify)

1. **500 筆台式料理基準集驗證**: 評估 MAE, MAPE，目標為 $\pm 20\%$ 誤差內達標率高於 85%。
2. **A/B 交叉對照實驗 (vs. MyFitnessPal)**: 20 名受試者 7 天追蹤，驗證單餐記錄耗時縮短 60%。
3. **系統可用性評估**: 試驗結束後填寫標準 10 題 SUS 量表，目標評分 SUS > 70 分。
4. **OpenSpec 規範檢驗**: 執行 `openspec validate write-iceib-academic-paper --strict` 確認工程合規。
