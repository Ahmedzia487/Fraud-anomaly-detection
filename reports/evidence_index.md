# Week 4 Evidence Index

## Main documentation
- `README.md` — project approach, tools, results, limitations, setup
- `reports/week4_summary.md` — standalone written project summary
- `reports/validation_findings.md` — validation findings, issues, fixes
- `CHANGELOG.md` — development history

## Model evaluation
- `reports/model_comparison_validation.csv`
- `reports/final_test_evaluation.csv`
- `reports/threshold_cost_analysis.csv`

## Charts
- `reports/figures/all_models_pr_curve.png`
- `reports/figures/isolation_forest_pr_curve.png`
- `reports/figures/one_class_svm_pr_curve.png`
- `reports/figures/autoencoder_pr_curve.png`
- `reports/figures/autoencoder_training_loss.png`
- `reports/figures/threshold_cost_curve.png`

## Robustness evidence
- `reports/robustness_test_results.csv`
- `src/robustness.py`

## Suggested screenshots for submission
1. Dataset preview and 1.5% suspicious class distribution
2. Dummy baseline with 98.5% accuracy and zero recall
3. Time-based split and temporal leakage checks
4. Autoencoder training-loss graph
5. Three-model comparison table
6. Combined Precision-Recall graph
7. Cost threshold table and cost graph
8. Robustness table showing 20/20 passed
9. Final test evaluation metrics

Capture screenshots from the real notebook or saved output files.
Do not present suggested screenshots as already captured.
