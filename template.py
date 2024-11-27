import os
from pathlib import Path

# Define the project name
project_name = "loan-approval-gcp-vetexai-mlops"

# List of directories and files based on your expanded modular structure
list_of_files = [
    f"{project_name}/README.md",
    f"{project_name}/Makefile",
    f"{project_name}/.env",
    f"{project_name}/cloudbuild/pr-checks.yaml",
    f"{project_name}/cloudbuild/test.yaml",
    f"{project_name}/cloudbuild/release.yaml",
    f"{project_name}/cloudbuild/terraform-plan.yaml",
    f"{project_name}/cloudbuild/trigger-tests.yaml",
    f"{project_name}/cloudbuild/terraform-apply.yaml",
    f"{project_name}/components/bigquery-components/src/__init__.py",
    f"{project_name}/components/bigquery-components/src/bq_query_to_table.py",
    f"{project_name}/components/bigquery-components/src/extract_bq_to_dataset.py",
    f"{project_name}/components/bigquery-components/tests/conftest.py",
    f"{project_name}/components/bigquery-components/tests/test_dummy.py",
    f"{project_name}/components/bigquery-components/README.md",
    f"{project_name}/components/vertex-components/src/vertex_components/__init__.py",
    f"{project_name}/components/vertex-components/src/vertex_components/train_job.py",
    f"{project_name}/components/vertex-components/src/vertex_components/import_model_evaluation.py",
    f"{project_name}/components/vertex-components/src/vertex_components/lookup_model.py",
    f"{project_name}/components/vertex-components/src/vertex_components/model_batch_predict.py",
    f"{project_name}/components/vertex-components/src/vertex_components/update_best_model.py",
    f"{project_name}/components/vertex-components/tests/conftest.py",
    f"{project_name}/components/vertex-components/tests/test_lookup_model.py",
    f"{project_name}/components/vertex-components/tests/test_model_batch_predict.py",
    f"{project_name}/components/vertex-components/tests/test_update_best_model.py",
    f"{project_name}/components/vertex-components/README.md",
    f"{project_name}/components/Readme.md",
    f"{project_name}/docs/images",
    f"{project_name}/docs/PRODUCTION.md",
    f"{project_name}/docs/TESTING.md",
    f"{project_name}/infra/TROUBLESHOOTING.md",
    f"{project_name}/pipelines/src/pipelines/trigger/README.md",
    f"{project_name}/pipelines/src/pipelines/trigger/__main__.py",
    f"{project_name}/pipelines/src/pipelines/trigger/main.py",
    f"{project_name}/pipelines/src/pipelines/trigger/requirements.txt",
    f"{project_name}/pipelines/src/pipelines/xgboost/README.md",
    f"{project_name}/pipelines/src/pipelines/xgboost/__init__.py",
    f"{project_name}/pipelines/src/pipelines/xgboost/training/pipeline.py",
    f"{project_name}/pipelines/src/pipelines/xgboost/training/assets/train_xgb_model.py",
    f"{project_name}/pipelines/src/pipelines/xgboost/training/queries/engineer_features.sql",
    f"{project_name}/pipelines/src/pipelines/xgboost/training/queries/ingest.sql",
    f"{project_name}/pipelines/src/pipelines/xgboost/prediction/pipeline.py",
    f"{project_name}/pipelines/src/pipelines/xgboost/prediction/pipeline.py",
    f"{project_name}/pipelines/src/pipelines/xgboost/prediction/quries/ingest.sql",
    f"{project_name}/terraform/envs/dev/main.tf",
    f"{project_name}/terraform/envs/dev/variables.tf",
    f"{project_name}/terraform/envs/test/main.tf",
    f"{project_name}/terraform/envs/test/variables.tf",
    f"{project_name}/terraform/envs/prod/main.tf",
    f"{project_name}/terraform/envs/prod/variables.tf",
    f"{project_name}/terraform/modules/cloudfunction/function.tf",
    f"{project_name}/terraform/modules/cloudfunction/variables.tf",
    f"{project_name}/terraform/modules/cloudfunction/versions.tf",
    f"{project_name}/terraform/modules/scheduled_pipelines/main.tf",
    f"{project_name}/terraform/modules/scheduled_pipelines/variables.tf",
    f"{project_name}/terraform/modules/scheduled_pipelines/variables.tf",
    f"{project_name}/terraform/modules/vertex_deployment/main.tf",
    f"{project_name}/terraform/modules/vertex_deployment/iam.tf",
    f"{project_name}/terraform/modules/vertex_deployment/outputs.tf",
    f"{project_name}/terraform/modules/vertex_deployment/variables.tf",
    f"{project_name}/terraform/modules/vertex_deployment/versions.tf",
    f"{project_name}/terraform/modules/vpc/main.tf",
    f"{project_name}/terraform/modules/vpc/variables.tf",
    f"{project_name}/terraform/modules/vpc/versions.tf",
    f"{project_name}/tests/e2e/test_e2e.py",
    f"{project_name}/tests/trigger/test_main.py",
    f"{project_name}/tests/xgboost/prediction/test.py",
    f"{project_name}/tests/xgboost/training/test.py",
    f"{project_name}/frontend/README.md",
    f"{project_name}/frontend/src/App.js",
    f"{project_name}/frontend/src/index.js",
    f"{project_name}/src/components/README.md",
    f"{project_name}/frontend/src/App.css",
    f"{project_name}/frontend/public/index.html",
    f"{project_name}/frontend/package.json",
    f"{project_name}/.flake8",
    f"{project_name}/.gitignore",
    f"{project_name}/.pre-commit-config.yaml",
    f"{project_name}/.python-version",
    f"{project_name}/.yamllint",
    f"{project_name}/Dockerfile",


]

# Create the directories and files based on the list
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create the file if it does not exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File already exists: {filepath}")

print("Project structure created successfully!")
