import pandas as pd,streamlit as st
from energy_auditor.audit import AuditConfig,audit_dataset
st.set_page_config(page_title="Energy Data Auditor",layout="wide"); st.title("Responsible Energy Data & AI Auditor"); st.caption("Evidence-led quality, representation, drift and leakage screening")
upload=st.file_uploader("Upload CSV"); df=pd.read_csv(upload) if upload else pd.read_csv("data/demo_energy_records.csv"); summary,issues,groups,drift=audit_dataset(df,AuditConfig(min_group_rows=3)); cols=st.columns(4)
for col,(key,value) in zip(cols,summary.items()): col.metric(key.replace("_"," ").title(),value)
st.subheader("Issue register"); st.dataframe(issues,use_container_width=True); st.subheader("Representation"); st.dataframe(groups,use_container_width=True); st.subheader("Drift"); st.dataframe(drift,use_container_width=True); st.download_button("Download issue register",issues.to_csv(index=False),"issue_register.csv")
