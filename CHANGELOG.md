\# Changelog



\## Week 4 — Initial Setup

\- Created the Week 4 project workspace.

\- Created separate data, model, notebook, source, report, figure, and test directories.

\- Created a dedicated Conda environment named `week4\_ai`.

\- Installed and verified scikit-learn, PyTorch, pandas, NumPy, Matplotlib, Jupyter, and pytest.

\- Defined the project scope before dataset and model development.



## Phase 12 — Robustness Testing
- Tested 20 unusual transaction-note inputs.
- Achieved 20/20 passing tests with zero failures.
- Added reusable text preprocessing to `src/robustness.py`.
- Saved robustness evidence to `reports/robustness_test_results.csv`.
- Documented the limitation that transaction notes are not direct model inputs.



## Phase 13 — Final Validation
- Passed the 29-check project integrity audit with zero failures.
- Evaluated One-Class SVM on the reserved test set using the
  validation-selected threshold (-0.221592).
- Recorded test Average Precision, PR-AUC, Precision@50,
  confusion-matrix counts, assumed cost, and workload estimates.
- Documented encountered implementation issues and their fixes.
- Documented limitations involving synthetic data, limited test
  positives, circular time-of-day distance, and text input scope.
- Saved the findings to `reports/validation_findings.md`.

