# AirGuard AI: 系統設計與架構規格書 (DESIGN.md)

## 1. 系統背景與設計目標
本文件為 AirGuard AI 在 Proposal 與實作階段的活體工程設計手冊（Living Design Document）。
系統旨在解決跑者與運動族群面臨之突發空污暴露風險，將語言理解與數值計算解耦，建立工具導向之 Domain AI Agent。

## 2. 範圍定義 (Scope)
- **提案原型範圍 (In-Scope)**：
  - 環境部 AQX_P_488 歷史逐時 CSV 檔案之標準化清理與離線分析。
  - 臺中代表性測站（西屯、忠明）1、3、6 小時滾動時序回歸預測。
  - 基於環境部與國健署官方指引的運動安全排程建議（PM2.5 50.5 μg/m³ 警戒）。
  - 確定性分析工具與白名單 Function Calling 整合。
  - 60 題在地問答集與 30 題安全邊界對抗測試。
- **後續擴充範圍 (Out-of-Scope for MVP)**：
  - 個人呼吸生理傳感器之即時硬體串接。
  - 未經共置校正之微型感測器（AirBox）強制融合。
  - 大尺度大氣化學網格傳輸模擬（CTM / CMAQ）。

## 3. 資料清點與稽核狀態 (Data Inventory & Audit)
- **主資料源**：環境部 AQX_P_488 歷時資料集（2026-01-01 至 2026-10-29）。
- **原始總列數**：970,296 列，涵蓋全國 88 個監測站。
- **清理後淨資料**：**606,137 筆** 唯一觀測紀錄。
  - 消除 364,159 筆因中英文或系統重複回傳之 localized duplicate rows。
  - 依據經緯度與行政區唯一恢復 4 筆缺失之 `SiteId`。
  - 嚴格隔離 13 組同一測站時間戳但數值衝突的記錄（存於 `aqi_2026_conflicts.csv`）。

## 4. 八大模組與架構拓撲
```mermaid
flowchart LR
    U[① User Scenario] --> P[② Query NLP]
    P --> PL[③ Planner Agent]
    PL --> D[(④ MOENV Dataset)]
    D --> Q[⑤ Quality & Alignment]
    Q --> A[⑤ Forecasting Engine]
    A --> R[⑥ Domain Rules]
    R --> G[⑦ Evidence Guard]
    G --> O[⑧ Provenanced Output]
```

## 5. 核心決策與權衡取捨 (Decisions & Trade-offs)
1. **白名單工具 vs. 自由生成**：LLM 僅負責語意抽取與回答組織，數值全部由 Python 確定性工具產生，消除幻覺。
2. **滾動統計時序 vs. 複雜黑盒深度模型**：短期 1–3 小時大氣擴散慣性強烈，以 Persistence 與 SARIMAX 為核心基線，避免小樣本過擬合。
3. **官方測站真值 vs. 微型感測器**：以參考級測站為真值基準，IoT 資料僅在具備共置校正與濕度補償時作為可選空間參考。

## 6. 安全政策與醫療免責 (Safety Policies)
- **Zero Medical Advice**：若使用者詢問氣喘用藥或疾病因果，Evidence Guard 強制觸發安全拒答，引導尋求專業醫師診治。
- **Zero Causal Accusation**：若使用者誘導演算法指控特定工廠排污，系統主動宣告大氣擴散局限性，拒絕非科學歸因。

## 7. OpenSpec 規格驅動開發對齊
本設計手冊已完全對齊 `openspec/changes/airguard-ai-proposal-refactor/` 規格契約，遵循規格驅動開發（SDD）之生命週期管理。

