# Spec Delta

## Purpose

結合個人代謝目標、歷史飲食趨勢、用餐生活情境與大數據模式，產出具備可解釋性、在地可行性與視覺化呈現的個人化飲食調整建議。

## ADDED Requirements

### Requirement: Energy Balance and Nutrient Gap Analysis
系統 SHALL 於每次飲食記錄後，即時計算全日累計熱量相對於目標 TDEE 的赤字/盈餘差距，並對照 AMDR 巨量營養素推薦比例（碳水化合物 45-65%、蛋白質 10-35%、脂肪 20-35%）產出缺口評估報告。

#### Scenario: Real-time Deficit Tracking
- **WHEN** 使用者已記錄早餐與午餐累計 1,300 kcal，其目標 TDEE 為 2,000 kcal
- **THEN** 系統計算出剩餘額度為 700 kcal，並提示晚餐之蛋白質與膳食纖維建議攝取配額

### Requirement: Context-Aware Food Substitution Suggestion
系統 SHALL 依據當前用餐情境（外食便利商店、夜市、手搖飲、家庭便當），提出等飽足感但熱量密度較低之在地食材替換方案。

#### Scenario: Night Market Substitution
- **WHEN** 使用者在夜市情境中詢問「晚餐想吃炸雞排，但熱量已快超標，該怎麼選？」
- **THEN** 系統主動建議「可改選鹹酥雞攤的烤雞串或鹽水雞（去皮、多選花椰菜與木耳），既能滿足肉食口感又可減少約 350 kcal 油脂負擔」

### Requirement: Multi-Modal Interactive Reporting
系統 SHALL 以 Markdown 結構化文字、巨量營養素比例圖表標記與信賴區間可視化圖形呈現日誌摘要，引導使用者持續進行多輪對話互動。

#### Scenario: Daily Summary Presentation
- **WHEN** 使用者觸發每日總結（get_analysis 或意圖 analyze）
- **THEN** 系統輸出包含總熱量區間、碳水/蛋白/脂肪佔比圓餅圖結構、安全提醒與下一餐建議之綜合報告

