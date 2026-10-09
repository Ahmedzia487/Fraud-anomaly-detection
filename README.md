# Fraud / Anomaly Detection on Imbalanced Data

## Isolation Forest vs One-Class SVM vs PyTorch Autoencoder

**Business scenario:** Regional Furniture Workshop  
**Project:** Week 4 — Specialist Advanced Build  
**Role:** Member 5 — Individual Contributor

## 1. Project Overview

This project investigates how anomaly-detection methods can help a regional furniture workshop prioritize unusual transactions for human review.

A synthetic dataset of 5,000 transactions was created, containing 75 suspicious transactions (1.5%). Three detectors were developed and compared: Isolation Forest, One-Class SVM, and a PyTorch Autoencoder.

The models were evaluated using Average Precision, trapezoidal PR-AUC, and Precision@50. A cost-based threshold was also selected using explicit assumptions about missed suspicious events and false alarms.

This is an experimental decision-support prototype, not an autonomous fraud adjudication system.

## 2. Dataset

| Property | Value |
|---|---:|
| Total records | 5,000 |
| Normal records | 4,925 |
| Suspicious records | 75 |
| Suspicious rate | 1.50% |
| Original columns | 15 |
| Engineered behavioural features | 5 |
| Final columns | 20 |

The synthetic transactions span January to June 2026 and represent furniture purchases, discounts, delivery activity, returns, customer history, and unusual transaction patterns.

### Behavioural features

1. `transaction_velocity_24h` — previous transactions by the same customer within 24 hours.
2. `amount_deviation_from_history` — relative difference between the transaction amount and the customer's historical average.
3. `time_of_day_deviation` — difference between the current transaction hour and the customer's historical average hour.
4. `discount_deviation_from_history` — difference from the customer's historical average discount.
5. `return_frequency_30d` — previous returns by the same customer within 30 days.

Historical features use past transactions rather than future observations. The suspicious label is excluded from the detector input features.

### Why accuracy is misleading

A dummy system predicting every transaction as normal achieves 98.50% accuracy but detects none of the 75 suspicious records. Therefore, accuracy alone is unsuitable for judging this rare-event task.

## 3. Time-Based Data Split

| Split | Records | Suspicious | Suspicious rate |
|---|---:|---:|---:|
| Training | 3,500 | 52 | 1.486% |
| Validation | 750 | 11 | 1.467% |
| Test | 750 | 12 | 1.600% |

The dataset was split chronologically without random shuffling. Validation data was used for model comparison and threshold selection. The test period was held out for final evaluation.

## 4. Models and Validation Results

| Model | Average Precision | Trapezoidal PR-AUC | Precision@50 |
|---|---:|---:|---:|
| Isolation Forest | 0.1727 | 0.1621 | 8.00% |
| One-Class SVM | 0.2701 | 0.2523 | 14.00% |
| PyTorch Autoencoder | 0.1124 | 0.0805 | 10.00% |

One-Class SVM achieved the strongest validation performance on Average Precision and Precision@50. However, the predefined Precision@50 target of 25% was not achieved by any model.

## 5. Cost-Based Threshold

One-Class SVM was selected for cost-based threshold analysis.

Illustrative assumptions:

- Missed suspicious transaction: PKR 25,000
- False alarm: PKR 500
- Manual review time: 5 minutes per alert

The validation-selected threshold was **-0.221592**.

| Validation result | Value |
|---|---:|
| Alerts | 56 |
| True positives | 8 |
| False alarms | 48 |
| Missed suspicious transactions | 3 |
| Estimated total cost | PKR 99,000 |
| Estimated weekly alerts | 14.44 |
| Estimated weekly review workload | 1.20 hours |

These amounts are estimates based on synthetic data and assumed costs, not verified financial outcomes from a real workshop.

## 6. Final Test Results

The validation-selected threshold was applied unchanged to the reserved test set.

| Metric | Test result |
|---|---:|
| Average Precision | 0.4319 |
| Trapezoidal PR-AUC | 0.4286 |
| Precision@50 | 10.00% |
| Alerts generated | 52 |
| True positives | 5 |
| False alarms | 47 |
| Missed suspicious transactions | 7 |
| Precision at the selected threshold | 9.62% |
| Recall at the selected threshold | 41.67% |
| F1-score | 0.1562 |
| Estimated test-period cost | PKR 198,500 |
| Estimated weekly review workload | 1.11 hours |

Test Average Precision was higher than validation Average Precision, but Precision@50 was lower. The test set contains only 12 suspicious records, so individual cases can materially affect the metrics.

## 7. Robustness Testing

Twenty unusual transaction-note inputs were tested, including typos, slang, empty values, missing values, long text, whitespace, Unicode, emojis, control characters, and HTML-like or SQL-like strings.

**Result: 20/20 tests passed, with zero failures.**

Reusable preprocessing is implemented in `src/robustness.py`. The evidence is saved in `reports/robustness_test_results.csv`.

Scope limitation: the anomaly detectors use numerical transaction and behavioural features. Transaction-note text is not directly used for anomaly scoring. The tests validate input preprocessing rather than text-based fraud detection.

## 8. Tools

- Python 3.11
- pandas and NumPy
- scikit-learn
- PyTorch
- Matplotlib
- Jupyter Notebook
- pytest
- Git and GitHub

## 9. Main Project Files

- `notebooks/week4_fraud_anomaly_detection.ipynb` — main implementation notebook
- `data/raw/furniture_workshop_transactions.csv` — synthetic raw dataset
- `data/processed/` — engineered data and model scores
- `models/` — saved detectors and scaler
- `src/robustness.py` — reusable input preprocessing
- `reports/model_comparison_validation.csv` — validation model comparison
- `reports/threshold_cost_analysis.csv` — threshold and cost analysis
- `reports/final_test_evaluation.csv` — final test metrics
- `reports/validation_findings.md` — validation findings and limitations
- `reports/robustness_test_results.csv` — robustness evidence
- `reports/week4_summary.md` — written project summary
- `reports/figures/` — evaluation charts

## 10. Environment Setup

Run these commands from the project root in Anaconda Prompt:

    conda create -n week4_ai python=3.11 -y
    conda activate week4_ai
    python -m pip install -r requirements.txt
    jupyter notebook

Open `notebooks/week4_fraud_anomaly_detection.ipynb` and run the notebook cells in order. The notebook uses variables created by earlier cells, so execute it sequentially from a fresh kernel when reproducing the experiment.

## 11. Limitations

1. The dataset is synthetic and cannot establish performance on real workshop transactions.
2. Only 12 suspicious records occur in the test set.
3. The 25% Precision@50 target was not achieved.
4. The time-of-day feature uses a linear hour difference and does not fully model circular time.
5. Transaction notes are not direct inputs to the anomaly detectors.
6. The business-cost assumptions require validation with actual workshop stakeholders.
7. The prototype requires further independent evaluation before operational deployment.

## 12. Future Improvements

- Validate with real or independently generated transaction data.
- Improve time-of-day features using circular encoding or circular distance.
- Investigate methods to reduce false alarms while controlling missed events.
- Expand automated tests for data validation and model scoring.
- Confirm cost assumptions with workshop stakeholders.

## Conclusion

This project demonstrates a complete experimental workflow for rare-event anomaly detection: synthetic data generation, behavioural feature engineering, chronological evaluation, comparison of three detectors, cost-based threshold selection, and robustness testing.

One-Class SVM was the strongest validation candidate, but its final test Precision@50 was 10%. The system is therefore a portfolio-grade experimental prototype rather than a production-ready fraud detector.
