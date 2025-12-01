# Healthcare Patient Satisfaction – 2024 Performance Analysis

**Author:** 25ds1000231@ds.study.iitm.ac.in  

## Business Context

As a senior data analyst in a healthcare organization, I was asked to investigate a concerning trend in patient satisfaction. The executive team is particularly focused on patient experience and wait times, as these directly influence reputation, retention, and revenue. The industry benchmark for patient satisfaction is **4.5**, but internal feedback suggests we may be underperforming in some areas.

This analysis uses quarterly patient satisfaction data for 2024 to build a data-driven story and recommend actions for the next fiscal year.

---

## Dataset

**Patient Satisfaction Score – 2024 Quarterly Data**

| Quarter | Patient Satisfaction Score |
|---------|----------------------------|
| Q1      | 0.35                       |
| Q2      | 5.34                       |
| Q3      | 1.74                       |
| Q4      | 10.61                      |

- **Average (2024): 4.51**  
- **Industry Target:** 4.5  

Although the **overall average of 4.51 slightly exceeds the industry target of 4.5**, the quarterly breakdown shows extreme variability and inconsistent patient experience from quarter to quarter.

---

## Methodology

Tools and approach:

- Language model–assisted coding (e.g., Jules / ChatGPT Codex / LLM-based code generation)
- Python (Pandas + Matplotlib) for:
  - Loading and processing the quarterly data
  - Calculating descriptive statistics (mean, gap vs target, per-quarter flag)
  - Creating visualizations comparing quarterly performance against the benchmark
- Visual outputs:
  - Line chart of quarterly satisfaction vs. industry target
  - Bar chart of quarterly scores with benchmark overlay

The analysis code is in:  
`analysis/healthcare_analysis.py`  
The data is in:  
`data/patient_satisfaction_2024.csv`

---

## Key Findings

1. **Overall average is slightly above target, but misleading**  
   - The **average satisfaction score is 4.51**, narrowly above the **industry target of 4.5**.
   - However, this hides very large quarter-to-quarter swings.

2. **Extremely volatile quarterly performance**  
   - Q1: **0.35** – critically low experience level, far below target.  
   - Q2: **5.34** – notably above target; significant improvement.  
   - Q3: **1.74** – sharp drop again, suggesting issues re-emerged (e.g., operational disruptions, staffing, process gaps).  
   - Q4: **10.61** – exceptionally high score, suggesting either:
     - a period of very strong operational performance, or  
     - a potential scale or measurement issue that needs validation.

3. **Inconsistent patient experience**  
   - Patients visiting in Q1 and Q3 likely experienced significantly worse service quality and/or longer wait times when compared to Q2 and Q4.
   - This inconsistency is **strategically risky**: average numbers may look acceptable, but patient sentiment, reviews, and loyalty will be strongly influenced by when they visited.

4. **Gaps vs Industry Target**  
   - Q1 and Q3 fall dramatically short of the target, dragging down trust and satisfaction.  
   - Q2 and Q4 exceed the benchmark, proving that the organization *can* deliver high-quality care and experience when processes, staffing, and capacity are aligned.

---

## Business Implications

1. **Reputational Risk**  
   - Large fluctuations in patient satisfaction can lead to mixed or polarized reviews online.
   - Patients who visit during low-performing periods (Q1, Q3) may actively discourage others, impacting patient acquisition and retention.

2. **Operational Instability**  
   - The volatility hints at underlying operational issues:
     - Inconsistent staffing levels
     - Poorly managed peak loads
     - Unstandardized service protocols
   - Even if average performance meets or exceeds the benchmark, instability undermines long-term trust.

3. **Resource Allocation and Planning**  
   - Management decisions based purely on the annual average (4.51) would be **misleading**.
   - Instead, leadership must:
     - Investigate what went wrong in Q1 and Q3  
     - Replicate the practices and conditions that enabled strong performance in Q2 and Q4  
     - Allocate resources to ensure that success is repeatable and sustainable rather than sporadic.

---

## Recommendations to Reach and Sustain the Target (4.5+)

The clear solution direction is to **improve service quality and reduce wait times** in a consistent and systematic way.

### 1. Stabilize Operational Processes

- **Standardize patient flow protocols**  
  - Implement clear triage rules for walk-ins and emergencies.  
  - Define standard operating procedures (SOPs) for admission, consultation, diagnostics, and discharge.

- **Capacity planning using data**  
  - Use historical hourly/daily load data to forecast peak periods.  
  - Align staff schedules and room availability with expected demand to avoid bottlenecks.

### 2. Reduce Wait Times

- **Digital check-in and pre-registration**  
  - Introduce online pre-registration to reduce queueing and paperwork delays.
  - Provide estimated wait times through SMS or app notifications to manage patient expectations.

- **Fast-track pathways**  
  - Separate low-complexity cases into a fast-track lane to keep throughput high and reduce congestion for more complex cases.

- **Queue monitoring dashboards**  
  - Deploy real-time dashboards in nurse stations and admin areas to monitor wait times and intervene early.

### 3. Improve Service Quality Consistently

- **Staff training on patient communication**  
  - Provide training on empathy, clear communication, and expectation management.
  - Focus on frontline staff: reception, nurses, and primary treating physicians.

- **Patient feedback loops per quarter**  
  - Collect short, targeted feedback at point of service via tablets or SMS.
  - Tag feedback by quarter/department to identify where experience drops.

- **Cross-functional quality huddles**  
  - Hold quarterly (or monthly) “quality huddles” with representatives from operations, nursing, doctors, and admin to review satisfaction scores and feedback.

### 4. Investigate Outliers and Measurement Quality

- **Validate Q4 measurement (10.61)**  
  - Confirm that the scoring scale, survey design, and data capture process are correct.
  - If valid, identify what process improvements or pilots were in effect and **institutionalize** those.

- **Root cause analysis for Q1 and Q3**  
  - Investigate:
    - Staffing shortages
    - Infrastructure issues (e.g., system downtimes, renovations)
    - Policy or process changes
  - Implement corrective actions and monitor impact in subsequent quarters.

---

## Visualizations

The following figures are generated by `analysis/healthcare_analysis.py`:

1. **`figures/patient_satisfaction_trend.png`**  
   - Line plot showing:
     - Quarterly patient satisfaction scores
     - Horizontal line representing the industry target (4.5)  
   - Highlights volatility and when the benchmark is exceeded or missed.

2. **`figures/patient_satisfaction_bars.png`**  
   - Bar chart of quarterly scores with benchmark overlay.  
   - Makes it easy to see underperforming and overperforming periods at a glance.

---

## How to Reproduce

1. Clone the repository.
2. Ensure Python and required libraries are installed:
   ```bash
   pip install pandas matplotlib
This README is part of the PR submission.
This README is part of the PR submission.


