from pathlib import Path
import json,pandas as pd
from energy_auditor.audit import AuditConfig,audit_dataset
from energy_auditor.database import save_audit
ROOT=Path(__file__).resolve().parent; OUT=ROOT/"outputs"
def main():
    OUT.mkdir(exist_ok=True); df=pd.read_csv(ROOT/"data"/"demo_energy_records.csv"); summary,issues,groups,drift=audit_dataset(df,AuditConfig(min_group_rows=3)); issues.to_csv(OUT/"issue_register.csv",index=False); groups.to_csv(OUT/"representation.csv",index=False); drift.to_csv(OUT/"drift.csv",index=False); (OUT/"summary.json").write_text(json.dumps(summary,indent=2)); rid=save_audit(OUT/"audit_runs.sqlite","demo_energy_records",summary,issues); print(f"Audit {rid}: {summary}")
if __name__=="__main__": main()
