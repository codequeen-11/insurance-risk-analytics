# Insurance Risk Analytics

End-to-end insurance risk analytics and predictive modeling project for AlphaCare Insurance Solutions (ACIS).

## Objectives

- Perform exploratory data analysis
- Conduct hypothesis testing
- Build predictive models
- Implement risk-based pricing framework
- Use DVC for reproducible pipelines

## Project Structure


## Data Version Control (DVC)

This project uses DVC to manage dataset versions and ensure reproducibility.

### Initialize DVC

```bash
dvc init
```

### Pull Data

```bash
dvc pull
```

### Push Data

```bash
dvc push
```

### Reproduce Pipeline

```bash
dvc repro
```

Datasets are tracked using a local DVC remote storage.


## Project Workflow

1. Data Exploration (EDA)
2. Data Version Control with DVC
3. Hypothesis Testing
4. Predictive Modeling
5. Risk-Based Pricing

## Running Tests

```bash
pytest


# Environment Setup

## Clone Repository

```bash
git clone <repository-url>
cd insurance-risk-analytics
```

## Create Virtual Environment

### Using venv

```bash
python -m venv .venv
```

Activate environment:

#### Windows (Git Bash)

```bash
source .venv/Scripts/activate
```

#### Windows (CMD)

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Run DVC Pipeline

Pull tracked data:

```bash
dvc pull
```

Push tracked data:

```bash
dvc push
```

# Project Structure

```text
insurance-risk-analytics/
├── data/
├── notebooks/
├── reports/
├── src/
├── tests/
└── README.md
```