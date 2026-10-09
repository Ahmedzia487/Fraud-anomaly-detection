# Week 4 — Final Validation Findings

## 1. Dataset and Integrity Checks

- Total records: 5,000
- Suspicious records: 75 (1.50%)
- Training records: 3,500
- Validation records: 750
- Test records: 750
- Integrity audit: 29 checks passed, 0 failures
- Required project files: all checked files present
- Robustness validation: 20/20 tests passed

## 2. Final Test Evaluation — One-Class SVM

The One-Class SVM was selected based on validation performance.
Its threshold was chosen using the validation data and held fixed
during final test evaluation.

- Selected threshold: -0.221592
- Test records: 750
- Actual suspicious records: 12
- Average Precision: 0.4319
- Trapezoidal PR-AUC: 0.4286
- Precision@50: 10.00%
- Alerts generated: 52
- True positives: 5
- False alarms: 47
- Missed suspicious transactions: 7
- True negatives: 691
- Precision at selected threshold: 9.62%
- Recall at selected threshold: 41.67%
- F1-score: 0.1562

## 3. Illustrative Business Cost

Assumptions:
- Cost per missed suspicious transaction: PKR 25,000
- Cost per false alarm: PKR 500
- Review time per alert: 5 minutes

Test-period estimated cost:
- Missed-event cost: PKR 175,000
- False-alarm cost: PKR 23,500
- Total assumed cost: PKR 198,500

Estimated weekly workload:
- 13.36 alerts per week
- Approximately 1.11 review hours per week

These figures are estimates on synthetic data using assumed costs,
not actual financial outcomes from a real workshop.

## 4. Problems Found and Fixes Applied

### Issue 1: Immutable timestamp array
- Problem: Timestamp modification failed because pandas returned
  an immutable DatetimeIndex.
- Fix: Converted timestamps to a mutable NumPy array before
  modifying selected transaction times.

### Issue 2: Grouped feature engineering lost customer_id
- Problem: The groupby.apply approach removed the grouping column
  under the installed pandas behaviour.
- Fix: Replaced the approach with explicit per-customer processing
  and assignment back to the original dataframe indexes.

### Issue 3: Notebook kernel state was not available
- Problem: A notebook cell failed because NumPy was not imported
  in the active kernel.
- Fix: Made the Autoencoder training cell self-contained, loading
  the processed dataset and saved scaler and declaring imports
  explicitly.

## 5. Limitations and Follow-Up Improvements

- The data is synthetic; results do not establish performance on
  real workshop transactions.
- The predefined Precision@50 target of 25% was not achieved.
- Only 12 suspicious records occur in the test set, so metrics can
  vary substantially with a small number of cases.
- The time-of-day deviation feature uses a linear hour difference,
  which does not fully account for the circular nature of time.
- Transaction-note robustness was tested separately. Text is not
  a direct input to the three numerical anomaly detectors.
- A future iteration should improve circular time features,
  test on real or independently generated data, and investigate
  approaches to reduce false alarms.

## 6. Final Assessment

The integrity checks and unusual-input preprocessing tests passed.
One-Class SVM was the strongest model on the validation comparison,
but its fixed-threshold test Precision@50 was 10.00%, and seven
suspicious test transactions were missed. The system should be
treated as an experimental alert-prioritization prototype rather
than a production-ready fraud detector.
