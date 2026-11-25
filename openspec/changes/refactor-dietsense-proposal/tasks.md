# Tasks: DietSense 專案提案重構與規格驅動開發任務清單

## 1. 規格驅動開發環境與 OpenSpec 架構初始化

- [x] 1.1 安裝 Node.js 22+ 與 OpenSpec CLI (`@fission-ai/openspec`) 並驗證版本
- [x] 1.2 執行 `openspec init --tools antigravity --language zh-TW` 初始化本專案規格環境，驗證產出之 `.agents/` 工作流指令與 `openspec/config.yaml`
- [x] 1.3 建立變更提案 `refactor-dietsense-proposal` 並完成 `proposal.md`、五大核心能力 Delta Specs 與系統級 `design.md`

## 2. 專案核心思維與深度研究重構 (A–F, 5 Cores, 3 Trade-offs, 10 Details)

- [ ] 2.1 撰寫並校準 A–F 六段式摘要（Attention Getter、But、Cure、Development、Experiments、Findings），納入 IEEE Transactions on Systems 風格摘要與 300 字精簡版本
- [ ] 2.2 重構 Deep Research Q1：五大專家核心思維模式（能量平衡、巨量營養素組成、份量不確定性、個體差異、行為情境意識），闡明其科學證據與系統模組映射
- [ ] 2.3 重構 Deep Research Q2：三大專業爭論與權衡（卡路里品質 vs 數量、AI 份量估算精確度 vs 硬體、個人化營養 vs 通用指引），明確收斂共識與 DietSense 解決策略
- [ ] 2.4 重構 Deep Research Q3：十大深度理解問題（Why、What-if、Trade-off、Failure Case、Evidence、Comparison、Design Decision、Real-world Scenario、Math Proof、Safety Guardrail）

## 3. 緒論 (Introduction) 系統化重構

- [ ] 3.1 撰寫 Introduction A. Attention Getter：引用 WHO 2024–2025 全球過重與肥胖數據（26 億/9.4 億）及台灣國健署 47.9% 過重率與年逾 500 億醫療支出
- [ ] 3.2 撰寫 Introduction B. Background 與 C. Problem：分析飲食自報 18%–54% 誤差與 85% 放棄率之四大根本障礙（檢索負擔、份量模糊、複合拆解、在地食物缺乏）
- [ ] 3.3 建立 Introduction D. Existing Limitations 對照表：嚴謹比較 MyFitnessPal、AI 照片辨識、研究型硬體系統與通用 LLM 之瓶頸
- [ ] 3.4 條列 Introduction E. Innovation（自然語言輸入、主動代理人互動、情境感知、大數據驅動、安全護欄）與 F. Contributions 四大核心學術產出

## 4. 相關研究 (Related Work) 體系重構

- [ ] 4.1 撰寫 1/2 AI Technology（LLM Function Calling Agent、RAG 向量檢索、Food NER、不確定性量化）文獻梳理
- [ ] 4.2 撰寫 1/2 Domain Knowledge（能量代謝 BMR/TDEE、AMDR 巨量營養素比例、手掌容器估算法、衛福部每日飲食指南）核心論述
- [ ] 4.3 建立 2024–2026 近年 5 篇代表性文獻之 Article Summary Table（橫跨 Ref, Year, Problem, AI Method, Domain Knowledge, Dataset, Findings, Limitation）
- [ ] 4.4 歸納研究缺口鏈（Existing Research → Limitations → Research Gap → Our Project）

## 5. 系統設計、虛擬碼與 OpenSpec 工作流轉化

- [ ] 5.1 繪製八大模組系統架構圖（①～⑧ 完整串接）與泳道流程圖（包含 Clarification Loop 與安全守門判斷）
- [ ] 5.2 撰寫帶行號之虛擬碼（Algorithm 1: DietSense Pipeline），實作 Mifflin-St Jeor 公式、不確定性信賴區間與安全攔截機制
- [ ] 5.3 撰寫完整頂層 `DESIGN.md`，使後續開發者能獨立理解、執行與驗證架構
- [ ] 5.4 執行 `openspec validate` 驗證所有 OpenSpec 變更與規格之格式合規性

## 6. 整合交付與 GitHub 專案庫建立

- [ ] 6.1 整合撰寫全面重構後的正式提案檔案 `Proposal.md`
- [ ] 6.2 撰寫專案根目錄 `README.md`，說明專案定位、OpenSpec 規格驅動開發流程、系統架構、安裝方式與測試驗證指南
- [ ] 6.3 建立本地 Git 版本控制倉庫，提交所有重構後文件，並整理遠端推送與繳交連結指引

## Workflow follow-up

- 執行 `openspec validate --strict` 確認所有 delta specs 與任務格式無誤。
- 當變更通過專題團隊審查後，執行 `/opsx-apply` 或 `openspec archive` 將變更合併至主規格庫。

