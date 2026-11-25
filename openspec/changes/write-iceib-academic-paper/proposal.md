# Proposal: ICEIB 國際學術會議論文撰寫規格與工作流程

## Why

本專案旨在將智慧飲食管理代理人 DietSense 之研究成果，依據 IEEE 國際研討會（IEEE International Conference on Electronic Information and Biomedical Engineering / Electronic Information and Business, ICEIB）之標準規範，系統性撰寫為符合學術發表水準的會議論文。
當前飲食追蹤工具存在高操作摩擦力（85% 用戶於 30 天內放棄）與自報熱量誤差（18% 至 54%）之痛點，而通用大型語言模型（LLM）又存在數值幻覺與缺乏本土飲食數據之缺陷。
透過規格驅動開發（OpenSpec SDD）方法，將學術論文之七大核心章節（摘要、緒論、相關文獻、系統設計、實驗評估、結論與參考文獻）轉化為標準化、可測試且可獨立驗證之規格合約，確保論文在架構嚴謹性、數據真實性與學術貢獻度上完全對齊 IEEE 會議規範。

## What Changes

本變更於 OpenSpec 體系內建立完整的學術論文寫作與驗證工作流：

- 建立 IEEE Conference 標準格式之章節規格庫，涵蓋：Abstract、Introduction、Related Work、Proposed Design、Experiments、Conclusion 與 References。
- 明確落實 A-F 六段式摘要結構，並銜接 IEEE Transactions on Systems / Conference 專業學術語義風格。
- 建立 1/2 AI 技術與 1/2 營養領域知識之文獻分析標準，包含 2024 至 2026 年五篇代表性文獻之結構化比較表（Article Summary Table）與研究缺口（Research Gap）。
- 定義八大模組架構、泳道流程圖、帶行號演算法虛擬碼（Algorithm 1）、Mifflin-St Jeor 代謝公式與不確定性置信區間數學模型。
- 定義 500 筆台式料理標註基準、MyFitnessPal 對照實驗與 20 人七天使用者研究（SUS 量表）之評估規範。
- 產出可直接上傳編譯之 Overleaf 完整 LaTeX 論文專案（包含 main.tex 與 references.bib）。
- 嚴格遵守學術誠信原則：所有未經實測之評估指標均標示為 Expected Outcomes，嚴禁虛構實驗數據；全文杜絕使用表情符號（emojis）。

## Capabilities

### New Capabilities

- `paper-abstract`: 規範論文摘要（Abstract）與關鍵字（Index Terms）之撰寫要求，包含 A-F 六段式邏輯（動機、挑戰、解藥、方法、評估、預期成果）、250 至 300 字限制與八大核心索引詞彙。
- `paper-introduction`: 規範緒論（Introduction）之論證結構，要求包含 WHO 與台灣衛福部公衛統計數據、手動飲食記錄四大障礙、既有工具對比表、DietSense 核心創新與四大具體學術貢獻。
- `paper-related-work`: 規範相關研究（Related Work）之文獻脈絡，平衡探討對話式代理人與能量代謝領域知識，納入五篇近年代表性文獻對比表並收斂出研究缺口鏈。
- `paper-proposed-design`: 規範系統設計與架構（Proposed Design）章節，定義八大模組職責、使用者與代理人交互泳道時序圖、帶行號虛擬碼演算法、Mifflin-St Jeor 公式、不確定性區間量化模型與臨床安全邊界。
- `paper-experiments`: 規範實驗設計與評估（Experimental Evaluation）章節，定義 500 筆台式外食標註數據集規格、MyFitnessPal 手動記錄對照基準、20 名受試者七天真實追蹤流程與量化指標（MAE, MAPE, 達標率, 耗時, SUS 分數）。
- `paper-conclusion`: 規範結論與未來展望（Conclusion and Future Work）章節，總結架構創新與學術價值，誠實揭示自報偏差等研究限制，並提出多模態感測與微量營養素追蹤發展方向。
- `paper-references`: 規範參考文獻（References）格式，全面採行 IEEE 標準引用規範，驗證文獻來源（DOI, 卷期, 頁碼）與公衛官方出版物之真實性。

### Modified Capabilities

- 無既有規格修改。

## Impact

- 產出專案根目錄之 Overleaf 專案目錄 `overleaf/`，內含符合 IEEEtran 樣式之 `main.tex`、BibTeX `references.bib` 與編譯說明文檔。
- 建立 OpenSpec 論文規格檔案庫，支援後續論文審稿意見修改與章節版本同步管理。
- 產出對齊資訊圖表之輔助研討文件，包含 A2Z 研究架構映射、Deep Research 三大核心問題與八大模組完整演算法規格。

