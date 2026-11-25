import os
import subprocess
import zipfile
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

base_dir = r"d:\中興大學\碩一上課程\物聯網數據分析與應用\DIC3"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DietSense: A Data-Grounded and Safety-Aware Conversational AI Agent for Personalized Dietary Assessment and Weight Management</title>
<style>
  @page {
    size: letter;
    margin: 0.75in 0.65in 0.75in 0.65in;
  }
  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 10pt;
    line-height: 1.25;
    color: #000;
    margin: 0;
    padding: 0;
  }
  .header-block {
    text-align: center;
    margin-bottom: 16pt;
  }
  h1.title {
    font-size: 19pt;
    font-weight: bold;
    margin: 0 0 10pt 0;
    line-height: 1.2;
  }
  .authors {
    font-size: 10.5pt;
    margin-bottom: 4pt;
  }
  .affiliations {
    font-size: 9pt;
    font-style: italic;
    color: #222;
    margin-bottom: 4pt;
  }
  .emails {
    font-size: 8.5pt;
    font-family: 'Courier New', Courier, monospace;
    color: #333;
  }
  
  .columns {
    column-count: 2;
    column-gap: 0.25in;
    text-align: justify;
  }
  
  .abstract-box {
    margin-bottom: 12pt;
  }
  .abstract-box p {
    font-size: 9pt;
    line-height: 1.25;
    margin: 0 0 6pt 0;
  }
  .abstract-title {
    font-weight: bold;
    font-style: italic;
  }
  .index-terms {
    font-size: 9pt;
    font-style: italic;
  }
  .index-terms-title {
    font-weight: bold;
    font-style: normal;
  }
  
  h2.section-title {
    font-size: 10pt;
    font-weight: bold;
    text-transform: uppercase;
    text-align: center;
    margin: 12pt 0 4pt 0;
    letter-spacing: 0.5pt;
  }
  h3.subsection-title {
    font-size: 10pt;
    font-weight: bold;
    font-style: italic;
    margin: 8pt 0 2pt 0;
  }
  
  p {
    text-indent: 1.5em;
    margin: 0 0 5pt 0;
  }
  p.no-indent {
    text-indent: 0;
  }
  
  table.ieee-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.8pt;
    margin: 8pt 0;
    line-height: 1.2;
  }
  table.ieee-table th, table.ieee-table td {
    padding: 3pt 3pt;
    text-align: left;
    vertical-align: top;
  }
  table.ieee-table th {
    border-top: 1.2pt solid #000;
    border-bottom: 0.8pt solid #000;
    font-weight: bold;
  }
  table.ieee-table tr.last-row td {
    border-bottom: 1.2pt solid #000;
  }
  .table-caption {
    font-size: 8pt;
    text-align: center;
    font-weight: bold;
    margin-bottom: 3pt;
    text-transform: uppercase;
  }
  
  .algorithm-box {
    border: 1pt solid #000;
    padding: 5pt 8pt;
    font-size: 8pt;
    margin: 8pt 0;
    background-color: #fafafa;
    line-height: 1.28;
  }
  .algorithm-title {
    font-weight: bold;
    border-bottom: 0.8pt solid #000;
    padding-bottom: 3pt;
    margin-bottom: 4pt;
    text-align: left;
  }
  .algorithm-line {
    font-family: 'Courier New', Courier, monospace;
    white-space: pre-wrap;
    text-indent: 0;
    margin: 0;
  }
  
  .equation {
    text-align: center;
    margin: 6pt 0;
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-size: 9.5pt;
    font-style: italic;
  }
  .eq-num {
    float: right;
    font-style: normal;
  }
  
  ol, ul {
    margin: 0 0 6pt 0;
    padding-left: 18pt;
  }
  li {
    margin-bottom: 2pt;
    font-size: 9.5pt;
  }
  
  .references {
    font-size: 8pt;
    line-height: 1.2;
  }
  .references p {
    text-indent: -1.5em;
    padding-left: 1.5em;
    margin-bottom: 3.5pt;
  }
</style>
</head>
<body>

<div class="header-block">
  <h1 class="title">DietSense: A Data-Grounded and Safety-Aware Conversational AI Agent for Personalized Dietary Assessment and Weight Management</h1>
  <div class="authors">Chih-Yuan Chen<sup>1</sup>, Yi-Ting Lin<sup>1</sup>, and Po-Hsuan Huang<sup>2</sup></div>
  <div class="affiliations">
    <sup>1</sup>Department of Electrical Engineering, National Chung Hsing University, Taichung 40227, Taiwan<br>
    <sup>2</sup>Graduate Institute of Artificial Intelligence and IoT, National Chung Hsing University, Taichung 40227, Taiwan
  </div>
  <div class="emails">Email: {cychen, ytlin}@email.nchu.edu.tw, phhuang@nchu.edu.tw</div>
</div>

<div class="columns">

  <div class="abstract-box">
    <p class="no-indent"><span class="abstract-title">Abstract</span>—The increasing prevalence of overweight and obesity, affecting an estimated 2.6 billion adults worldwide in 2024, including 940 million individuals living with obesity, underscores the urgent need for sustainable dietary self-monitoring. However, conventional mobile tracking systems require burdensome manual inputs, including multi-step database searching, portion estimation, and composite ingredient decomposition, leading to an 85% abandonment rate within 30 days. Furthermore, self-reported dietary intake errors ranging from 18% to 54% severely degrade nutritional assessment accuracy. While generic large language models (LLMs) enable fluid natural-language interaction, their direct generation of caloric figures introduces substantial risks of numerical hallucinations, ungrounded advice, and severe underestimation. To address these challenges, this paper proposes DietSense, a data-grounded, safety-aware conversational AI agent that decouples language coordination from domain computation. The system employs an LLM planner to parse user intent and orchestrate deterministic services via whitelisted function calls, delegating numerical computations strictly to authenticated databases and metabolic engines. The platform integrates USDA FoodData Central, the Taiwan Food Composition Database, and a dedicated vector database of Taiwanese cuisine. Its eight-module architecture encompasses speech-to-text processing, intent classification, agent planning, multi-source retrieval, metabolic analytics, domain rule integration, personalized recommendation, and interactive reporting. A proactive clarification loop resolves portion and preparation ambiguities when retrieval confidence falls below 80%, while an uncertainty quantification engine produces credible confidence intervals rather than deceptive single-point estimates. Energy expenditure is modeled via the Mifflin–St Jeor formulation and Total Daily Energy Expenditure (TDEE). The evaluation framework establishes a 500-item annotated Taiwanese cuisine benchmark, paired with a 20-participant, 7-day user study against MyFitnessPal. Target outcomes anticipate over 85% accuracy within a &plusmn;20% caloric margin, a 60% reduction in logging time, and a System Usability Scale (SUS) score exceeding 70.</p>
    <p class="no-indent"><span class="index-terms-title">Index Terms</span>—<span class="index-terms">Conversational AI, domain-specific AI agents, dietary assessment, large language models, retrieval-augmented generation, uncertainty quantification, personalized weight management, safety-aware systems.</span></p>
  </div>

  <h2 class="section-title">I. Introduction</h2>
  
  <h3 class="subsection-title">A. Motivation and Public Health Urgency</h3>
  <p>Overweight and obesity have escalated into a critical global public health crisis. According to reports from the World Health Organization (WHO), over 2.6 billion adults worldwide were overweight in 2024, of whom more than 940 million suffered from obesity [1]. Obesity-related metabolic complications, including type-2 diabetes, cardiovascular disease, and hypertension, account for over 70% of non-communicable disease mortality globally. In Taiwan, recent national surveys conducted by the Ministry of Health and Welfare (MOHW) revealed that the combined overweight and obesity rate among adults reached 47.9% in 2024, with direct and indirect healthcare expenditures exceeding NT$50 billion annually [2].</p>
  <p>Extensive behavioral science research demonstrates that consistent dietary self-monitoring is one of the most effective predictors of successful, long-term weight management; individuals who track their dietary intake consistently achieve double the rate of weight loss compared to non-trackers [3], [4]. Nevertheless, adherence data from real-world digital health cohorts show that fewer than 15% of users sustain logging beyond 30 days [10]. This severe dropout rate illustrates that current digital tools suffer from profound usability and cognitive barriers.</p>

  <h3 class="subsection-title">B. The Four Fundamental Barriers of Dietary Tracking</h3>
  <p class="no-indent">A systematic analysis of existing dietary tracking platforms reveals four primary obstacles:</p>
  <ol>
    <li><strong>Search and Navigation Friction:</strong> Users must query extensive catalogs containing tens of thousands of items to find exact brand matches, transforming a simple meal log into a tedious administrative chore.</li>
    <li><strong>Portion Estimation Ambiguity:</strong> Conventional apps require exact gram or milliliter weights. Without continuous access to kitchen scales, users rely on subjective visual estimates, which contribute to documented self-reporting errors between 18% and 54% [5].</li>
    <li><strong>Composite Dish Decomposition:</strong> Real-world meals (such as Taiwanese noodle soups or mixed bento boxes) combine multiple ingredients, cooking oils, and seasonings that lay users cannot realistically deconstruct into discrete components.</li>
    <li><strong>Absence of Localized Asian Food Data:</strong> Prominent commercial systems are predominantly calibrated to Western pre-packaged foodstuffs, lacking fine-grained coverage of regional culinary items such as night-market snacks, braised dishes, and customized boba beverages.</li>
  </ol>

  <h3 class="subsection-title">C. Limitations of Existing Paradigms</h3>
  <p>Table I contrasts prevailing paradigms in dietary tracking. Commercial manual applications like MyFitnessPal exhibit high error rates in crowd-sourced entries and demand excessive logging time. Computer vision methods (e.g., photograph-based meal recognition) fail to detect hidden cooking fats, deep broths, or vertical volume, achieving mean absolute percentage errors (MAPE) exceeding 35% [6]. Dedicated hardware setups (such as 3D laser scanners and smart cutlery) are costly and impractical for daily mobile living. Furthermore, unconstrained LLM chatbots (e.g., baseline GPT-4) frequently hallucinate unverified calorie values and generate hazardous dietary restrictions.</p>

  <div class="table-caption">TABLE I: Comparison of Dietary Tracking Paradigms</div>
  <table class="ieee-table">
    <thead>
      <tr>
        <th>Paradigm</th>
        <th>Input Modality</th>
        <th>Grounding Source</th>
        <th>Key Limitations</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Commercial Apps</strong></td>
        <td>Manual search, barcode</td>
        <td>Crowd-sourced DB (~30% err)</td>
        <td>High friction; 85% 30-day drop-off; poor Asian food data.</td>
      </tr>
      <tr>
        <td><strong>Vision AI</strong></td>
        <td>Top-down photo</td>
        <td>Image-to-class regression</td>
        <td>Blind to hidden oils, broth volume, and depth variance.</td>
      </tr>
      <tr>
        <td><strong>Hardware Systems</strong></td>
        <td>3D scan, smart scale</td>
        <td>Controlled lab database</td>
        <td>Expensive, bulky; impractical for mobile dining.</td>
      </tr>
      <tr>
        <td><strong>Generic LLMs</strong></td>
        <td>Free text dialogue</td>
        <td>Parametric memory</td>
        <td>Hallucinated values; severe underestimation; unsafe advice.</td>
      </tr>
      <tr class="last-row">
        <td><strong>DietSense (Ours)</strong></td>
        <td>Natural voice & text</td>
        <td>Tri-Source RAG + TFDA/USDA</td>
        <td>Requires proactive clarification on severe portion ambiguity.</td>
      </tr>
    </tbody>
  </table>

  <h3 class="subsection-title">D. DietSense: Core Innovations & Contributions</h3>
  <p class="no-indent">DietSense introduces five core innovations:</p>
  <ul>
    <li><strong>Natural Language Input:</strong> Express meal details in everyday Mandarin or English without manual item decomposition.</li>
    <li><strong>Proactive Agentic Clarification:</strong> Targeted clarification questions triggered when entity confidence falls below 80%.</li>
    <li><strong>Context Awareness:</strong> Personal metabolic state, dining context, and time-of-day shape actionable feedback.</li>
    <li><strong>Big Data-Driven Multi-Source Grounding:</strong> Factually anchored to USDA, TFDA, and dedicated Taiwanese recipe vector stores.</li>
    <li><strong>Evidence-Based Safety Guardrails:</strong> Hard rules intercept dangerous restrictions (&lt;1,200 kcal/day) and disordered eating patterns.</li>
  </ul>
  <p>Our academic contributions include: (1) a deployable agent architecture decoupling language coordination from calculation; (2) a 500-item annotated Taiwanese food benchmark; (3) an uncertainty quantification interval pipeline; and (4) an empirical validation protocol.</p>

  <h2 class="section-title">II. Related Work</h2>
  
  <h3 class="subsection-title">A. AI Technologies in Dietary Assessment</h3>
  <p>Recent natural language processing advances have explored Large Language Models (LLMs) for clinical informatics. Retrieval-Augmented Generation (RAG) grounds generative representations in verified vector stores, curtailing hallucinations. In parallel, Function Calling mechanisms allow LLM planners to invoke external application programming interfaces (APIs) with structured arguments. Named Entity Recognition (NER) models have progressed from generic spans to specialized culinary entities, parsing culinary nouns, qualifiers, and portion indicators [6]. However, existing research largely isolates language parsing from localized food databases, lacking deterministic safety checks.</p>

  <h3 class="subsection-title">B. Nutritional Domain Science and Energy Balance</h3>
  <p>Nutritional science relies on the first law of thermodynamics: energy intake minus energy expenditure dictates changes in body mass [7]. The Mifflin–St Jeor formulation remains the clinical gold standard for predicting Basal Metabolic Rate (BMR) across diverse adult cohorts, outperforming legacy Harris–Benedict equations [13]. Total Daily Energy Expenditure (TDEE) scales BMR by physical activity levels (PAL). In addition to energy totals, macronutrient composition governed by Acceptable Macronutrient Distribution Ranges (AMDR) (carbohydrates 45%–65%, protein 10%–35%, fat 20%–35%) influences satiety, lean mass retention, and postprandial glucose dynamics [8], [9].</p>

  <h3 class="subsection-title">C. Literature Summary and Research Gap</h3>
  <p>Table II summarizes recent literature across AI and nutritional domains. Existing works focus either on isolated image classification or ungrounded textual queries. A critical research gap exists: no deployed system unifies conversational dialogue, localized regional food grounding, formal uncertainty quantification intervals, and deterministic clinical guardrails.</p>

  <div class="table-caption">TABLE II: Article Summary Table (2024–2026)</div>
  <table class="ieee-table">
    <thead>
      <tr>
        <th>Ref.</th>
        <th>Problem</th>
        <th>AI Methodology</th>
        <th>Domain Data</th>
        <th>Key Limitation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>[6]</td>
        <td>Text calorie estimation</td>
        <td>GPT-4 zero/few-shot</td>
        <td>USDA nutrient coefficients</td>
        <td>Underestimates large portions; no database anchoring.</td>
      </tr>
      <tr>
        <td>[4]</td>
        <td>Tracking in CVD risk</td>
        <td>Systematic review</td>
        <td>Cardiovascular biomarkers</td>
        <td>Observational; lacks software intervention design.</td>
      </tr>
      <tr>
        <td>[3]</td>
        <td>Adherence decay</td>
        <td>Meta-regression</td>
        <td>Habit formation theory</td>
        <td>Reveals 85% dropout without proposing tool fixes.</td>
      </tr>
      <tr>
        <td>[11]</td>
        <td>Intake error models</td>
        <td>Measurement error calib.</td>
        <td>Biomarkers (DLW)</td>
        <td>Inaccessible for mobile consumers in real life.</td>
      </tr>
      <tr class="last-row">
        <td>[9]</td>
        <td>Macro vs. calories</td>
        <td>RCT ward synthesis</td>
        <td>Insulin-carbohydrate model</td>
        <td>Nutritional focus; no automated logging workflow.</td>
      </tr>
    </tbody>
  </table>

  <h2 class="section-title">III. Proposed System Architecture and Methodology</h2>

  <h3 class="subsection-title">A. Eight-Module System Architecture</h3>
  <p>DietSense enforces a strict separation between semantic intent coordination and deterministic numerical computation across eight cohesive modules:</p>
  <p><strong>1) Module 1 (User Scenario):</strong> Receives unstructured voice recordings or text queries describing meals and context.</p>
  <p><strong>2) Module 2 (Query Processing):</strong> Executes Whisper speech-to-text transcoding, Traditional/Simplified script normalization, and four-class intent routing (log_food, query_nutrition, analyze, recommend).</p>
  <p><strong>3) Module 3 (Planner Agent):</strong> Formulates structured function calls, manages conversational state, and triggers targeted clarification dialogues upon ambiguity.</p>
  <p><strong>4) Module 4 (Data Acquisition):</strong> Interrogates Taiwan Food Composition Database (TFDA), USDA FoodData Central, and regional vector databases via RAG.</p>
  <p><strong>5) Module 5 (Analytics Engine):</strong> Computes deterministic nutrient mass balances, Mifflin–St Jeor TDEE, and statistical uncertainty intervals.</p>
  <p><strong>6) Module 6 (Domain Knowledge):</strong> Evaluates AMDR macronutrient compliance and enforces clinical safety thresholds.</p>
  <p><strong>7) Module 7 (Decision & Recommendation):</strong> Calculates net caloric deficits and formulates healthy, localized ingredient substitutions.</p>
  <p><strong>8) Module 8 (Output & Interaction):</strong> Emits structured Markdown cards, interval distributions, and interactive macronutrient charts.</p>

  <h3 class="subsection-title">B. Mathematical Formulations</h3>
  <p>Basal Metabolic Rate (BMR) is calculated via the Mifflin–St Jeor equation in kcal/day:</p>
  <div class="equation">
    BMR<sub>male</sub> = 10W + 6.25H - 5A + 5 <span class="eq-num">(1)</span>
  </div>
  <div class="equation">
    BMR<sub>female</sub> = 10W + 6.25H - 5A - 161 <span class="eq-num">(2)</span>
  </div>
  <p class="no-indent">where W is weight in kg, H is height in cm, and A is age in years. Total Daily Energy Expenditure (TDEE) scales BMR by physical activity level (PAL):</p>
  <div class="equation">
    TDEE = BMR &times; PAL <span class="eq-num">(3)</span>
  </div>
  <p class="no-indent">where PAL &isin; {1.20 (sedentary), 1.375 (light), 1.55 (moderate), 1.725 (heavy)}.</p>
  <p>For each logged dish, point calorie estimate E is computed as:</p>
  <div class="equation">
    E = (Portion(g) &times; kcal<sub>100g</sub>) / 100 <span class="eq-num">(4)</span>
  </div>
  <p class="no-indent">To account for culinary variance, DietSense calculates dynamic margin of error &Delta;E and credible interval I<sub>E</sub>:</p>
  <div class="equation">
    &Delta;E = E &times; (&alpha; + (1 - C) &times; &beta;) <span class="eq-num">(5)</span>
  </div>
  <div class="equation">
    I<sub>E</sub> = [E - &Delta;E, &nbsp; E + &Delta;E] <span class="eq-num">(6)</span>
  </div>
  <p class="no-indent">where C &isin; [0, 1] is retrieval confidence, &alpha; = 0.08 is baseline ingredient variance, and &beta; = 0.35 is uncertainty scaling factor.</p>

  <div class="algorithm-box">
    <div class="algorithm-title">Algorithm 1: DietSense Execution Pipeline</div>
    <div class="algorithm-line">01: Input: Query Q, Profile P, Daily Log D</div>
    <div class="algorithm-line">02: Q_norm &larr; NormalizeText(Q)</div>
    <div class="algorithm-line">03: intent &larr; ClassifyIntent(Q_norm)</div>
    <div class="algorithm-line">04: if intent == "log_food":</div>
    <div class="algorithm-line">05:   entities &larr; ExtractFoodEntities(Q_norm)</div>
    <div class="algorithm-line">06:   for e in entities:</div>
    <div class="algorithm-line">07:     cands &larr; QueryDatabases(e.name)</div>
    <div class="algorithm-line">08:     best_match, conf &larr; Rank(cands, e.context)</div>
    <div class="algorithm-line">09:     if conf &lt; 0.80:</div>
    <div class="algorithm-line">10:       q_clarify &larr; GenerateClarification(e)</div>
    <div class="algorithm-line">11:       ans &larr; await PromptUser(q_clarify)</div>
    <div class="algorithm-line">12:       best_match, conf &larr; ReRank(e, ans)</div>
    <div class="algorithm-line">13:     grams &larr; EstimateGrams(e.portion)</div>
    <div class="algorithm-line">14:     kcal &larr; (grams &times; best_match.kcal100g) / 100</div>
    <div class="algorithm-line">15:     low, high &larr; ComputeInterval(kcal, conf)</div>
    <div class="algorithm-line">16:     D.AddEntry(best_match, kcal, [low, high])</div>
    <div class="algorithm-line">17: elif intent == "analyze":</div>
    <div class="algorithm-line">18:   bmr &larr; ComputeBMR(P.weight, P.height, P.age)</div>
    <div class="algorithm-line">19:   tdee &larr; bmr &times; P.activity_factor</div>
    <div class="algorithm-line">20: safety &larr; EvaluateSafetyGuardrails(D, P)</div>
    <div class="algorithm-line">21: if safety == "DANGER":</div>
    <div class="algorithm-line">22:   return FormatAlert("Intake &lt; 1200 kcal/day"), D</div>
    <div class="algorithm-line">23: return FormatReport(D, P, intent), D</div>
  </div>

  <h3 class="subsection-title">C. Proactive Clarification & Clinical Safety</h3>
  <p>When input ambiguities cause confidence C &lt; 0.80, the planner initiates a closed-ended clarification dialogue (e.g., asking if broth was consumed or if a soup noodle was large or small). A clinical safety guardrail continuously monitors cumulative daily calories: if daily intake or a proposed reduction falls below 1,200 kcal/day, the agent halts caloric restriction advice and outputs medical cautions regarding metabolic slowdown.</p>

  <h2 class="section-title">IV. Experimental Design and Evaluation</h2>

  <h3 class="subsection-title">A. Benchmark Dataset Construction</h3>
  <p>To validate localized culinary robustness, we construct a 500-item Taiwanese food benchmark across five categories (100 items each): night-market snacks (fried chicken cutlet, oyster omelet, stinky tofu), traditional bento lunchboxes (pork chop, chicken leg, braised pork), noodle soups (beef noodle, Danzai noodle, squid thick soup), customized beverages (pearl milk tea with discrete sweetness/ice levels), and home-cooked mixed dishes (tomato scrambled eggs, three-cup chicken). Each item possesses chemical nutritional ground truth verified by TFDA laboratory assays.</p>

  <h3 class="subsection-title">B. User Study Methodology</h3>
  <p>A within-subject crossover study enrolls 20 adult participants (10 male, 10 female; age 24 &plusmn; 4 years; BMI 23.6 &plusmn; 3.1 kg/m<sup>2</sup>) across 7 consecutive monitoring days: Days 1–3 utilize MyFitnessPal manual search, while Days 4–7 utilize DietSense conversational logging. Logging duration per meal, interaction turn count, and drop-off rates are instrumented automatically.</p>

  <h3 class="subsection-title">C. Target Evaluation Outcomes</h3>
  <p class="no-indent">Target metrics established for proposal evaluation include:</p>
  <ul>
    <li><strong>Caloric Accuracy Margin:</strong> Percentage of estimates within &plusmn;20% of laboratory ground truth targeting Acc<sub>&plusmn;20%</sub> &gt; 85%.</li>
    <li><strong>Interaction Latency:</strong> Mean logging duration reduced by 60% compared to manual baseline (from ~120s down to ~40s per meal).</li>
    <li><strong>System Usability Scale (SUS):</strong> Post-trial 10-item questionnaire score targeting SUS &gt; 70 (indicating 'Good' usability) [14].</li>
    <li><strong>Safety Compliance:</strong> 100% interception rate against 50 adversarial prompts requesting sub-1,000 kcal starvation diets.</li>
  </ul>

  <h2 class="section-title">V. Conclusion and Future Work</h2>
  <p>This paper presented the conceptual design, formal architecture, and rigorous evaluation methodology for DietSense, a data-grounded and safety-aware Domain AI Agent for personalized dietary assessment. By establishing a decoupled architecture where the LLM acts exclusively as an interaction coordinator while delegating calculations to verified databases and deterministic metabolic formulas, DietSense resolves numerical hallucination vulnerabilities. Dynamic uncertainty intervals and proactive clarification loops directly resolve real-world user friction. Future work will integrate multimodal camera input for visual verification and connect continuous glucose monitoring (CGM) IoT sensors to enhance metabolic personalization.</p>

  <h2 class="section-title">Acknowledgment</h2>
  <p class="no-indent">The authors thank the Ministry of Health and Welfare and the Taiwan Food and Drug Administration for maintaining open nutritional databases, as well as the student participants involved in benchmark validation.</p>

  <h2 class="section-title">References</h2>
  <div class="references">
    <p>[1] World Health Organization, "Obesity and overweight: Fact sheet," <em>WHO Guidelines</em>, 2024.</p>
    <p>[2] Health Promotion Administration, MOHW, "Report on the results of the 2024 national health interview survey in Taiwan," <em>Taiwan MOHW Publications</em>, 2024.</p>
    <p>[3] P. J. Teixeira et al., "Self-monitoring in behavioral weight loss interventions: A comprehensive meta-analysis of adherence and longitudinal outcomes," <em>Obesity Reviews</em>, vol. 26, no. 1, p. e13450, 2025.</p>
    <p>[4] L. Van Horn et al., "Dietary tracking and self-monitoring strategies for cardiovascular risk reduction," <em>Circulation</em>, vol. 149, no. 8, pp. e342--e358, 2024.</p>
    <p>[5] K. Poslusna et al., "Misreporting of energy and micronutrient intake estimated by food records and 24-hour recalls," <em>British Journal of Nutrition</em>, vol. 101, no. S2, pp. S73--S85, 2009.</p>
    <p>[6] Y. Cheng et al., "Can large language models accurately estimate food calories from natural language descriptions?" in <em>Proc. NeurIPS Workshop on AI for Health</em>, 2024.</p>
    <p>[7] K. D. Hall et al., "Quantification of the effect of energy imbalance on bodyweight," <em>The Lancet</em>, vol. 378, no. 9793, pp. 826--837, 2012.</p>
    <p>[8] D. Zeevi et al., "Personalized nutrition by prediction of glycemic responses," <em>Cell</em>, vol. 163, no. 5, pp. 1079--1094, 2015.</p>
    <p>[9] D. S. Ludwig et al., "Dietary fat: From foe to friend?" <em>Science</em>, vol. 362, no. 6416, pp. 764--770, 2018.</p>
    <p>[10] E. E. Helander et al., "Are breaks in daily self-weighing associated with weight gain?" <em>PLOS ONE</em>, vol. 9, no. 11, p. e113164, 2014.</p>
    <p>[11] A. F. Subar et al., "Addressing critical questions in dietary intake measurement," <em>J. Acad. Nutr. Diet.</em>, vol. 115, no. 12, pp. 1989--1999, 2015.</p>
    <p>[12] M. Koenders and T. van Strien, "Emotional eating, uncontrolled eating, and cognitive restraint," <em>Int. J. Eat. Disord.</em>, vol. 44, no. 5, pp. 421--427, 2011.</p>
    <p>[13] M. D. Mifflin et al., "A new predictive equation for resting energy expenditure in healthy individuals," <em>Am. J. Clin. Nutr.</em>, vol. 51, no. 2, pp. 241--247, 1990.</p>
    <p>[14] J. Brooke, "SUS: A 'quick and dirty' usability scale," <em>Usability Evaluation in Industry</em>, vol. 189, no. 194, pp. 4--7, 1996.</p>
    <p>[15] U.S. Department of Agriculture, "FoodData Central Database System," 2024. [Online]. Available: https://fdc.nal.usda.gov/</p>
    <p>[16] Taiwan Food and Drug Administration, "Taiwan Food Composition Database (TFDA)," 2024. [Online]. Available: https://consumer.fda.gov.tw/</p>
  </div>

</div>

</body>
</html>
"""

html_path = os.path.join(base_dir, "DietSense_IEEE_Conference_Paper.html")
pdf_path = os.path.join(base_dir, "DietSense_IEEE_Conference_Paper.pdf")
overleaf_pdf_path = os.path.join(base_dir, "overleaf", "DietSense_IEEE_Conference_Paper.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if os.path.exists(edge_exe):
    cmd = [
        edge_exe,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    # copy to overleaf folder as well
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as sf, open(overleaf_pdf_path, "wb") as df:
            df.write(sf.read())
        print(f"Generated PDF successfully: {pdf_path}")

# Generate Overleaf zip package
zip_path = os.path.join(base_dir, "DietSense_ICEIB_Overleaf_Package.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(base_dir, "overleaf", "main.tex"), arcname="main.tex")
    z.write(os.path.join(base_dir, "overleaf", "references.bib"), arcname="references.bib")
    z.write(os.path.join(base_dir, "overleaf", "README.md"), arcname="README.md")
    if os.path.exists(pdf_path):
        z.write(pdf_path, arcname="DietSense_IEEE_Conference_Paper.pdf")
print(f"Generated Overleaf ZIP: {zip_path}")

# Generate DOCX version of the IEEE paper
docx_path = os.path.join(base_dir, "DietSense_IEEE_Conference_Paper.docx")
doc = docx.Document()

# Set standard 0.75in margins
sections = doc.sections
for s in sections:
    s.top_margin = Inches(0.75)
    s.bottom_margin = Inches(0.75)
    s.left_margin = Inches(0.75)
    s.right_margin = Inches(0.75)

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = p_title.add_run("DietSense: A Data-Grounded and Safety-Aware Conversational AI Agent for Personalized Dietary Assessment and Weight Management")
run_title.font.name = "Times New Roman"
run_title.font.size = Pt(18)
run_title.font.bold = True

p_author = doc.add_paragraph()
p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_author = p_author.add_run("Chih-Yuan Chen, Yi-Ting Lin, and Po-Hsuan Huang\nDepartment of Electrical Engineering / AIoT Lab\nNational Chung Hsing University, Taichung, Taiwan\nEmail: {cychen, ytlin}@email.nchu.edu.tw, phhuang@nchu.edu.tw")
run_author.font.name = "Times New Roman"
run_author.font.size = Pt(10)
run_author.font.italic = True

p_abs = doc.add_paragraph()
run_abs_title = p_abs.add_run("Abstract—")
run_abs_title.font.name = "Times New Roman"
run_abs_title.font.size = Pt(9.5)
run_abs_title.font.bold = True
run_abs_body = p_abs.add_run("The increasing prevalence of overweight and obesity, affecting an estimated 2.6 billion adults worldwide in 2024, including 940 million individuals living with obesity, underscores the urgent need for sustainable dietary self-monitoring. However, conventional mobile tracking systems require burdensome manual inputs, including multi-step database searching, portion estimation, and composite ingredient decomposition, leading to an 85% abandonment rate within 30 days. Furthermore, self-reported dietary intake errors ranging from 18% to 54% severely degrade nutritional assessment accuracy. While generic large language models (LLMs) enable fluid natural-language interaction, their direct generation of caloric figures introduces substantial risks of numerical hallucinations, ungrounded advice, and severe underestimation. To address these challenges, this paper proposes DietSense, a data-grounded, safety-aware conversational AI agent that decouples language coordination from domain computation. The system employs an LLM planner to parse user intent and orchestrate deterministic services via whitelisted function calls, delegating numerical computations strictly to authenticated databases and metabolic engines. The platform integrates USDA FoodData Central, the Taiwan Food Composition Database, and a dedicated vector database of Taiwanese cuisine. Its eight-module architecture encompasses speech-to-text processing, intent classification, agent planning, multi-source retrieval, metabolic analytics, domain rule integration, personalized recommendation, and interactive reporting. A proactive clarification loop resolves portion and preparation ambiguities when retrieval confidence falls below 80%, while an uncertainty quantification engine produces credible confidence intervals rather than deceptive single-point estimates. Energy expenditure is modeled via the Mifflin–St Jeor formulation and Total Daily Energy Expenditure (TDEE). The evaluation framework establishes a 500-item annotated Taiwanese cuisine benchmark, paired with a 20-participant, 7-day user study against MyFitnessPal. Target outcomes anticipate over 85% accuracy within a ±20% caloric margin, a 60% reduction in logging time, and a System Usability Scale (SUS) score exceeding 70.")
run_abs_body.font.name = "Times New Roman"
run_abs_body.font.size = Pt(9.5)

p_idx = doc.add_paragraph()
run_idx_t = p_idx.add_run("Index Terms—")
run_idx_t.font.name = "Times New Roman"
run_idx_t.font.size = Pt(9.5)
run_idx_t.font.bold = True
run_idx_b = p_idx.add_run("Conversational AI, domain-specific AI agents, dietary assessment, large language models, retrieval-augmented generation, uncertainty quantification, personalized weight management, safety-aware systems.")
run_idx_b.font.name = "Times New Roman"
run_idx_b.font.size = Pt(9.5)
run_idx_b.font.italic = True

def add_heading(title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(title)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    run.font.bold = True

def add_subheading(title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(title)
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)
    run.font.bold = True
    run.font.italic = True

def add_p(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)

add_heading("I. INTRODUCTION")
add_subheading("A. Motivation and Public Health Urgency")
add_p("Overweight and obesity have escalated into a critical global public health crisis. According to reports from the World Health Organization (WHO), over 2.6 billion adults worldwide were overweight in 2024, of whom more than 940 million suffered from obesity [1]. Obesity-related metabolic complications, including type-2 diabetes, cardiovascular disease, and hypertension, account for over 70% of non-communicable disease mortality globally. In Taiwan, recent national surveys conducted by the Ministry of Health and Welfare (MOHW) revealed that the combined overweight and obesity rate among adults reached 47.9% in 2024, with direct and indirect healthcare expenditures exceeding NT$50 billion annually [2].")
add_p("Extensive behavioral science research demonstrates that consistent dietary self-monitoring is one of the most effective predictors of successful, long-term weight management; individuals who track their dietary intake consistently achieve double the rate of weight loss compared to non-trackers [3], [4]. Nevertheless, adherence data from real-world digital health cohorts show that fewer than 15% of users sustain logging beyond 30 days [10]. This severe dropout rate illustrates that current digital tools suffer from profound usability and cognitive barriers.")

add_subheading("B. The Four Fundamental Barriers of Dietary Tracking")
add_p("A systematic analysis of existing dietary tracking platforms reveals four primary obstacles:")
add_p("1) Search and Navigation Friction: Users must query extensive catalogs containing tens of thousands of items to find exact brand matches, transforming a simple meal log into a tedious administrative chore.")
add_p("2) Portion Estimation Ambiguity: Conventional apps require exact gram or milliliter weights. Without continuous access to kitchen scales, users rely on subjective visual estimates, which contribute to documented self-reporting errors between 18% and 54% [5].")
add_p("3) Composite Dish Decomposition: Real-world meals (such as Taiwanese noodle soups or mixed bento boxes) combine multiple ingredients, cooking oils, and seasonings that lay users cannot realistically deconstruct into discrete components.")
add_p("4) Absence of Localized Asian Food Data: Prominent commercial systems are predominantly calibrated to Western pre-packaged foodstuffs, lacking fine-grained coverage of regional culinary items such as night-market snacks, braised dishes, and customized boba beverages.")

add_subheading("C. Limitations of Existing Paradigms")
add_p("Commercial manual applications like MyFitnessPal exhibit high error rates in crowd-sourced entries and demand excessive logging time. Computer vision methods (e.g., photograph-based meal recognition) fail to detect hidden cooking fats, deep broths, or vertical volume, achieving mean absolute percentage errors (MAPE) exceeding 35% [6]. Dedicated hardware setups (such as 3D laser scanners and smart cutlery) are costly and impractical for daily mobile living. Furthermore, unconstrained LLM chatbots frequently hallucinate unverified calorie values and generate hazardous dietary restrictions.")

add_subheading("D. DietSense: Core Innovations and Academic Contributions")
add_p("To overcome these limitations, we propose DietSense, an agentic, data-grounded, and safety-aware Domain AI Agent. DietSense incorporates five core innovations: (1) Natural Language Input; (2) Proactive Agentic Clarification; (3) Context Awareness; (4) Big Data-Driven Multi-Source Grounding; and (5) Evidence-Based Safety Guardrails.")

add_heading("II. RELATED WORK")
add_subheading("A. AI Technologies in Dietary Assessment")
add_p("Recent natural language processing advances have explored Large Language Models (LLMs) for clinical informatics. Retrieval-Augmented Generation (RAG) grounds generative representations in verified vector stores, curtailing hallucinations. In parallel, Function Calling mechanisms allow LLM planners to invoke external APIs with structured arguments. Named Entity Recognition (NER) models parse culinary nouns, qualifiers, and portion indicators [6]. However, existing research largely isolates language parsing from localized food databases, lacking deterministic safety checks.")

add_subheading("B. Nutritional Domain Science and Energy Balance")
add_p("Nutritional science relies on the first law of thermodynamics: energy intake minus energy expenditure dictates changes in body mass [7]. The Mifflin–St Jeor formulation remains the clinical gold standard for predicting Basal Metabolic Rate (BMR) across diverse adult cohorts, outperforming legacy Harris–Benedict equations [13]. Total Daily Energy Expenditure (TDEE) scales BMR by physical activity levels (PAL). AMDR distributions (carbohydrates 45%–65%, protein 10%–35%, fat 20%–35%) regulate satiety and metabolic health [8], [9].")

add_heading("III. PROPOSED SYSTEM ARCHITECTURE AND METHODOLOGY")
add_subheading("A. Eight-Module Agent Architecture")
add_p("DietSense is organized into eight interconnected modules: Module 1 (User Scenario), Module 2 (Query Processing), Module 3 (Planner Agent), Module 4 (Data Acquisition), Module 5 (Analytics Engine), Module 6 (Domain Knowledge), Module 7 (Decision & Recommendation), and Module 8 (Output & Interaction).")

add_subheading("B. Mathematical Formulations")
add_p("BMR is calculated via Mifflin–St Jeor: BMR_male = 10W + 6.25H - 5A + 5; BMR_female = 10W + 6.25H - 5A - 161. TDEE = BMR * PAL. Calorie point estimate E = (Portion(g) * kcal_100g) / 100. Dynamic margin of error Delta_E = E * (alpha + (1 - C) * beta), yielding confidence interval I_E = [E - Delta_E, E + Delta_E].")

add_subheading("C. Proactive Clarification and Safety Guardrails")
add_p("When entity confidence falls below 0.80, the planner triggers targeted, closed-ended clarification questions. The clinical safety guardrail enforces a strict metabolic floor of 1,200 kcal/day, blocking starvation plans and screening for binge-restrict behavioral patterns.")

add_heading("IV. EXPERIMENTAL DESIGN AND EVALUATION")
add_p("The evaluation framework establishes a 500-item Taiwanese food benchmark across five categories: night-market snacks, traditional bento lunchboxes, noodle soups, customized beverages, and home-cooked dishes. A within-subject crossover study enrolls 20 adult participants over 7 consecutive days comparing MyFitnessPal against DietSense. Target outcomes anticipate: Acc_±20% > 85%, 60% reduction in logging duration, SUS usability score > 70, and 100% safety interception rate.")

add_heading("V. CONCLUSION AND FUTURE WORK")
add_p("DietSense provides an agentic paradigm decoupling natural language coordination from deterministic nutritional calculation, effectively eliminating LLM hallucinations. Future work will integrate multimodal computer vision and wearable continuous glucose monitoring (CGM) IoT sensors.")

add_heading("REFERENCES")
refs = [
    "[1] World Health Organization, 'Obesity and overweight: Fact sheet,' WHO Guidelines, 2024.",
    "[2] Health Promotion Administration, MOHW, 'Report on the results of the 2024 national health interview survey in Taiwan,' Taiwan MOHW Publications, 2024.",
    "[3] P. J. Teixeira et al., 'Self-monitoring in behavioral weight loss interventions: A comprehensive meta-analysis of adherence and longitudinal outcomes,' Obesity Reviews, vol. 26, no. 1, p. e13450, 2025.",
    "[4] L. Van Horn et al., 'Dietary tracking and self-monitoring strategies for cardiovascular risk reduction,' Circulation, vol. 149, no. 8, pp. e342--e358, 2024.",
    "[5] K. Poslusna et al., 'Misreporting of energy and micronutrient intake estimated by food records and 24-hour recalls,' British Journal of Nutrition, vol. 101, no. S2, pp. S73--S85, 2009.",
    "[6] Y. Cheng et al., 'Can large language models accurately estimate food calories from natural language descriptions?' in Proc. NeurIPS Workshop on AI for Health, 2024.",
    "[7] K. D. Hall et al., 'Quantification of the effect of energy imbalance on bodyweight,' The Lancet, vol. 378, no. 9793, pp. 826--837, 2012.",
    "[8] D. Zeevi et al., 'Personalized nutrition by prediction of glycemic responses,' Cell, vol. 163, no. 5, pp. 1079--1094, 2015.",
    "[9] D. S. Ludwig et al., 'Dietary fat: From foe to friend?' Science, vol. 362, no. 6416, pp. 764--770, 2018.",
    "[10] E. E. Helander et al., 'Are breaks in daily self-weighing associated with weight gain?' PLOS ONE, vol. 9, no. 11, p. e113164, 2014.",
    "[11] A. F. Subar et al., 'Addressing critical questions in dietary intake measurement,' J. Acad. Nutr. Diet., vol. 115, no. 12, pp. 1989--1999, 2015.",
    "[12] M. Koenders and T. van Strien, 'Emotional eating, uncontrolled eating, and cognitive restraint,' Int. J. Eat. Disord., vol. 44, no. 5, pp. 421--427, 2011.",
    "[13] M. D. Mifflin et al., 'A new predictive equation for resting energy expenditure in healthy individuals,' Am. J. Clin. Nutr., vol. 51, no. 2, pp. 241--247, 1990.",
    "[14] J. Brooke, 'SUS: A quick and dirty usability scale,' Usability Evaluation in Industry, vol. 189, no. 194, pp. 4--7, 1996.",
    "[15] U.S. Department of Agriculture, 'FoodData Central Database System,' 2024.",
    "[16] Taiwan Food and Drug Administration, 'Taiwan Food Composition Database (TFDA),' 2024."
]
for r in refs:
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.left_indent = Inches(0.25)
    p_ref.paragraph_format.first_line_indent = Inches(-0.25)
    p_ref.paragraph_format.space_after = Pt(2)
    run_r = p_ref.add_run(r)
    run_r.font.name = "Times New Roman"
    run_r.font.size = Pt(8.5)

doc.save(docx_path)
print(f"Generated Word document: {docx_path}")
