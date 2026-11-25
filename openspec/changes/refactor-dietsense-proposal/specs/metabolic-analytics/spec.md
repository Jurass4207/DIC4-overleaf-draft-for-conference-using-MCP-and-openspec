# Spec Delta

## Purpose

提供確定性之能量代謝與巨量營養素計算引擎，整合 Mifflin-St Jeor 公式、TDEE 計算與不確定性信賴區間量化，以誠實的數值範圍取代偽精確單一數字。

## ADDED Requirements

### Requirement: Deterministic Calorie and Macronutrient Computation
系統 SHALL 透過確定性數學公式計算單餐與全日熱量總和與巨量營養素（碳水化合物、蛋白質、脂肪、膳食纖維），計算公式為每項食物份量（克）乘以此食物每 100 克之各項營養密度後除以 100，嚴禁 LLM 自由猜測隨機數字。

#### Scenario: Normal Nutrient Calculation
- **WHEN** 獲得基準食物每 100g 含 180 kcal 及份量 250g
- **THEN** 系統計算出精確熱量為 450 kcal，並分別計算蛋白質、脂肪與碳水化合物之絕對克數

### Requirement: BMR and TDEE Estimation
系統 SHALL 依據使用者之性別、年齡、身高、體重與活動量係數，採用 Mifflin-St Jeor 公式計算基礎代謝率（BMR）與總每日能量消耗（TDEE）。

#### Scenario: Male TDEE Calculation
- **WHEN** 使用者為 30 歲男性，體重 75 kg、身高 175 cm，中度活動量（係數 1.55）
- **THEN** 系統計算 BMR = 10*(75) + 6.25*(175) - 5*(30) + 5 = 1,698.75 kcal，TDEE = 1,698.75 * 1.55 = 2,633 kcal

#### Scenario: Female TDEE Calculation
- **WHEN** 使用者為 28 歲女性，體重 55 kg、身高 160 cm，輕度活動量（係數 1.375）
- **THEN** 系統計算 BMR = 10*(55) + 6.25*(160) - 5*(28) - 161 = 1,249 kcal，TDEE = 1,249 * 1.375 = 1,717 kcal

### Requirement: Uncertainty Interval Quantification
系統 SHALL 依據檢索信心分數與份量描述模糊程度，計算熱量與巨量營養素之信賴區間（Confidence Interval），以估算下限與上限範圍形式呈顯。

#### Scenario: High Uncertainty Broad Interval
- **WHEN** 使用者輸入描述模糊（如「夜市滷味一份」）且信心分數為 0.65
- **THEN** 系統輸出熱量置信區間為 [420 kcal, 630 kcal]，誤差裕度擴展至 ±20% 以上，並提示主要不確定性來源為醬汁與食材組成

