# Design: ICEIB 國際會議論文之系統設計與排版規格

## Context

本技術設計文件旨在規範 DietSense 於 IEEE ICEIB 國際學術會議論文中之形式化表達、排版規格與數學架構。
參考 `proposal.md` 所確立之目標，論文需符合 IEEE 標準雙欄（Two-Column）格式，嚴格遵守 IEEEtran 類別檔要求，並將系統之八大核心模組、Mifflin-St Jeor 能量代謝公式、動態不確定性信賴區間模型、多來源檢索管線與臨床安全守門規則，以符合一流國際研討會標準之英文學術論文形式呈現。

## Goals / Non-Goals

**Goals:**
- 提供具備高編譯相容性之 Overleaf 完整 LaTeX 專案（main.tex 與 references.bib），可於 Overleaf 雲端環境一次編譯成功（Zero Warnings / Zero Errors）。
- 設計完整之章節脈絡，完整對應 ICEIB 會議標準：I. Introduction、II. Related Work、III. Proposed Architecture & Methodology、IV. Experimental Design & Evaluation、V. Conclusion & Future Work。
- 繪製並排版高品質向量演算法框（Algorithm 1）與對照表格（Table I 現有工具限制、Table II 相關研究綜合表）。
- 建立符合 IEEE 規範之數學符號表示法，精準表達能量守恆、代謝率換算與不確定性邊界量化。

**Non-Goals:**
- 不在論文正文中使用非學術性語彙、網路用語或任何表情符號（emojis）。
- 提案階段論文不捏造未經實證之實驗數值，所有數值均明確標註為預期成果（Expected Outcomes）或評估目標。
- 不引入非標準或過於冷門之 LaTeX 巨集套件，確保於 Overleaf TeX Live 2024 環境中具備極佳相容性。

## Paper Architecture & Structural Flow

論文整體結構嚴格遵循 IEEE Conference 格式，章節分配如下：

1. **Title & Meta Info**: 
   - 標題：DietSense: A Data-Grounded and Safety-Aware Conversational AI Agent for Personalized Dietary Assessment and Weight Management
   - 作者單位：國立中興大學電機工程學系 / 物聯網與人工智慧實驗室。
2. **Abstract & Index Terms**: 
   - 250 至 300 字單一段落摘要，貫串 A-F 邏輯；8 個標準 IEEE Index Terms。
3. **Section I: Introduction**: 
   - 引言與動機（WHO 與台灣衛福部公衛統計數據）。
   - 傳統飲食追蹤之四大核心障礙與自報誤差。
   - 現有工具技術限制分析（Table I 比較表）。
   - DietSense 五大核心創新與四大主要學術貢獻。
4. **Section II: Related Work**: 
   - 人工智慧對話代理人與工具調用（Tool Use）。
   - 營養學領域知識與能量代謝平衡模型。
   - 2024 至 2026 年近年文獻綜合表（Table II）。
   - 現有研究限制與本專案研究缺口（Research Gap）。
5. **Section III: Proposed Architecture and Methodology**: 
   - 八大核心模組架構（User, NLP, Planner, Retrieval, Analytics, Domain, Decision, Interaction）。
   - 互動時序與 Clarification Loop 泳道圖描述。
   - 核心演算法虛擬碼（Algorithm 1: DietSense Pipeline，具完整行號）。
   - 數學形式化定義（Mifflin-St Jeor TDEE、不確定性區間模型）。
   - 臨床安全守門與降級防護機制（< 1,200 kcal/天攔截、飲食失調警示）。
6. **Section IV: Experimental Evaluation and Methodology**: 
   - 500 筆台式外食與小吃標註資料集建構方法。
   - 與商業基準 MyFitnessPal 手動記錄之 A/B 對照組設計。
   - 20 名受試者 7 天真實追蹤實驗流程。
   - 評估指標設定（MAE, MAPE, ±10%/±20% 達標率 > 85%, 時間縮短 60%, SUS > 70）。
7. **Section V: Conclusion and Future Work**: 
   - 核心技術結論與實務價值回顧。
   - 研究局限性反思（回憶偏差、單純文字輸入邊界）。
   - 未來多模態影像融合與 CGM 物聯網感測演進規劃。
8. **References**: 
   - 完整 BibTeX 格式引用，包含 DOI 與卷期頁碼。

## Mathematical & Algorithmic Formulation Standards

### 1. Mifflin-St Jeor 能量代謝模型

男性基礎代謝率（BMR）：
$$
\text{BMR}_{\text{male}} = 10 \cdot W + 6.25 \cdot H - 5 \cdot A + 5
$$
女性基礎代謝率（BMR）：
$$
\text{BMR}_{\text{female}} = 10 \cdot W + 6.25 \cdot H - 5 \cdot A - 161
$$
每日總能量消耗（TDEE）：
$$
\text{TDEE} = \text{BMR} \times \text{PAL}
$$
其中 $W$ 為體重（kg），$H$ 為身高（cm），$A$ 為年齡（years），$\text{PAL}$ 為身體活動係數。

### 2. 不確定性置信區間傳遞模型

單項食物點估計值：
$$
E = \frac{\text{Portion}(\text{g}) \times \text{kcal}_{100\text{g}}}{100}
$$
動態置信半寬（Margin of Error）：
$$
\Delta E = E \times \left( \alpha + (1 - C) \times \beta \right)
$$
置信區間表示式：
$$
\mathcal{I}_E = \left[ E - \Delta E, \; E + \Delta E \right]
$$
其中 $C \in [0, 1]$ 為多來源檢索綜合匹配信心度，基準變異度 $\alpha = 0.08$，動態放大因子 $\beta = 0.35$。

## Overleaf & LaTeX Formatting Design Decisions

- **樣式類別（Document Class）**：採用標準 `\documentclass[conference]{IEEEtran}`，確保欄寬、邊距與字體大小完全合規。
- **演算法宏包**：採用 `algorithm2e` 或 `algorithmicx` + `algpseudocode` 實作標準學術虛擬碼，設定 `[linesnumbered,ruled,vlined]` 支援清晰行號與區塊豎線。
- **表格設計**：採用 `booktabs` 樣式（`\toprule`, `\midrule`, `\bottomrule`），避免垂直隔線，維持 IEEE 頂級出版物外觀。
- **引用系統**：使用 `cite` 宏包與獨立 `references.bib` 檔案，透過 BibTeX 引擎生成標準 `[1]`, `[2]` 數值引用。

## Risks / Trade-offs

- **[Risk 1: LaTeX 套件衝突導致 Overleaf 編譯失敗]** -> **Mitigation**: 精選 IEEEtran 官方相容套件清單（`amsmath`, `amssymb`, `cite`, `graphicx`, `booktabs`, `algorithm`, `algorithmic`），避免載入已知會覆寫 IEEEtran 內部標題定義之第三方宏包。
- **[Risk 2: 雙欄排版之長公式或寬表格溢出邊界]** -> **Mitigation**: 對於跨欄大表格採用 `table*` 環境，複雜多步公式採用 `aligned` 拆行，確保排版無 Overfull \hbox 警告。
- **[Risk 3: 非正式口吻影響審稿觀感]** -> **Mitigation**: 全文採用標準學術被動語態與形式化定義，嚴禁出現第一人稱情緒性詞彙與表情符號。

## Verification & Compilation Workflow

1. **LaTeX 本地語法檢驗**：檢查所有環境閉合（`\begin` / `\end`）與 BibTeX 鍵值對齊。
2. **OpenSpec 規格驗證**：執行 `openspec validate write-iceib-academic-paper --strict`，確保 Delta 規範 100% 合規。
3. **交付物歸檔**：將 Overleaf 所需檔案集中於 `overleaf/` 目錄，提供清晰之一鍵匯入教學指引。

