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