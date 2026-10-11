# Responsible Energy Data & AI Auditor

A reusable Python application for auditing energy datasets before analysis or machine-learning use. It converts responsible-AI principles into an explainable issue register rather than a vague checklist.

## Capabilities

- completeness, duplicate and physical-range checks;
- IQR outlier screening with a “validate, do not automatically delete” policy;
- asset-group representation diagnostics;
- temporal drift detection;
- explicit target-leakage warnings;
- model error-parity reporting when predictions are supplied;
- auditable SQLite run history, CSV exports and Streamlit dashboard;
- automated unit tests and GitHub Actions CI.

The bundled data are synthetic and deliberately contain defects. A flag is evidence for review—not proof that a record, model or group is wrong.

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
python run_audit.py
streamlit run dashboard.py
python -m unittest discover -s tests -v
```

## Author

**Dr Khaldoun Shaker**  
Petroleum & Reservoir Engineer | Energy Data Analytics  
Edinburgh, United Kingdom · [GitHub](https://github.com/drK89)

## Licence

Copyright (c) 2026 Khaldoun Shaker. All rights reserved. See [LICENSE](LICENSE).
