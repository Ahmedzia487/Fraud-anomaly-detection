# Week 4 Project Summary

## Fraud / Anomaly Detection for a Regional Furniture Workshop

This project developed an experimental anomaly-detection pipeline to prioritize unusual transactions for human review. A synthetic dataset of 5,000 records was created, with 75 suspicious transactions (1.5%). Five behavioural features were engineered from historical customer activity. The dataset was divided chronologically into training, validation, and test periods.

Three anomaly detectors were compared: Isolation Forest and One-Class SVM using scikit-learn, and a PyTorch Autoencoder based on reconstruction error. On the validation set, One-Class SVM achieved the best ranking results, with Average Precision of 0.2701, trapezoidal PR-AUC of 0.2523, and Precision@50 of 14%. No model achieved the predefined 25% Precision@50 target.

A threshold of -0.221592 was selected for One-Class SVM using illustrative assumptions of PKR 25,000 per missed suspicious transaction and PKR 500 per false alarm. Validation analysis estimated PKR 99,000 in total cost and 1.20 hours of manual review per week.

On the reserved test set, the fixed threshold produced Average Precision of 0.4319, PR-AUC of 0.4286, and Precision@50 of 10%. The detector identified 5 of 12 suspicious test transactions and missed 7. Estimated test-period cost was PKR 198,500, with a projected review workload of 1.11 hours per week. These figures depend on synthetic data and assumed business costs.

Twenty unusual transaction-note inputs were tested, and all 20 passed preprocessing checks. Key limitations include synthetic data, the small number of suspicious test cases, failure to meet the Precision@50 target, and the fact that text notes are not direct inputs to the anomaly models. The project demonstrates an end-to-end rare-event detection workflow while identifying specific areas requiring improvement before real-world use.
