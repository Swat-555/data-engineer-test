# data-engineer-test
Monitor the pipeline in Azure Data Factory:
Go to the ADF portal.
Select Monitor from the left-hand menu.
Look for the failed pipeline in the Pipeline Runs tab.
Click on the failed pipeline to view detailed error logs.

The logs will usually provide useful information like:
Which activity failed (e.g., Copy Data, Data Flow).
A specific error message, which might tell you what field or data format caused the issue.

Prevent invalid data format issues:
Add a pre-validation step that verifies the data format and schema before loading it into the pipeline.
Dynamically check and handle different formats using parameters for dataset configurations (like delimiters, headers, etc.).