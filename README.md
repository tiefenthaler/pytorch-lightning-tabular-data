# README table of contents
- [ml_packaging_classification](#ml-packaging-classification)
- [Use case description:](#use-case-description-)
- [Structure of the showcase](#structure-of-the-showcase)


# ml_packaging_classification
This repo is meant as a showcase to demonstrate a data science workflow for a multi-class classification (see use case description below) use case in business context. Data science use cases may have very different nature in terms of how the result/solution is used by the business. This use case has the characteristic of providing one-time insights and a inference solution to be reused manually to get the classification outputs further continues usage by the business. Therefore the repo focuses on analytics and limits operational aspects for analytical reusability. Still the repo contains proper data engineering and data science best practices for data preparation, pre-processing, modeling and evaluation. Many different frameworks for modeling with their specific integrations are used. Each of the different frameworks is used to demonstrate the reusability of the code and the data science workflow and contains a **pre-processing pipeline**, **modeling pipeline** and **evaluation pipeline**. A description of each solution for a given framework as given in the related notebook. For the data science pipeline with best performance, the best performing model is used to create a **prediction pipeline** and **deeper analysis** of the model and the related results in respect to performance and the business goal.


The repo focuses on the following aspects:
- Build a simple ETL pipeline to prepare the raw data for analysis and classification.
- Conduct general data analysis for data quality investigation under consideration of the business goal.
- Conduct data analysis to get an understanding how to handle the data for multi-class classification, including a naive benchmark model using sklearn (DummyClassifier & a custom classifier).
- Build multiple machine learning pipelines to evaluate best classification performance. The following aspects are considered within those pipelines:
  - Benchmarking pipelines to compare performance of multiple different types of models:
    - A basic benchmarking pipeline using naive classifiers as a base line.
    - A AutoML (automated machine learning) pipeline using PyCaret to compare a "large" variety of machine learning algorithms, considering:
      - including and excluding custom data pre-processing
      - pre-defined hyper-parameter set for each algorithm by PyCaret
      - using random search for HPO (hyper-parameter optimization) with a pre-defined hyper-parameter search space for each algorithm by PyCaret
    - A AutoML (automated machine learning) pipeline using AutoGluon.Tablular, considering:
      - including and excluding custom data pre-processing
      - including auto pre-processing by AutoGluon.Tabular
      - including auto feature engineering by AutoGluon.Tabular
      - including multiple classifiers by using:
        - multiple ml algorithms
        - "standard" HPO for each algorithm defined by AutoGluon.Tabular
        - ensambles of algorithms (bagging and stacking with possible multiple layers)
    - A benchmarking pipeline for multiple tree-based algorithms, considering:  
    (since AutoML indicates a good performance of tree-based algorithms for the given use case; as well as showing that no single tree-based algorithm significantly outperforms others)
      - Tree-based classifiers: DecisionTree, RandomForest, LightGBM.
      - Model hyper-parameter optimization.
      - Class imbalance.
    - A benchmarking pipeline for Neural Network using Pytorch/Lightning, considering:  
    (AutoML shows relative low performance of NN with defined time constrains for the given use case. Double-check the AutoML-NN results with individual constrains)
      - MLP and Embedding-MLP.
      - Custom classes to handle tabular data for Pytorch/Lightning Dataset, DataLoaders, LightningDataModule, LightningModule, Trainer, and Models.
      - Model hyper-parameter optimization.
      - Class imbalance.
  - A custom pipeline for the best performing model based on benchmarking, considering:
    - Model hyper-parameter optimization.
    - Class imbalance.
    - Oversampling.
  - Business decision optimization for best model.
    - Threshold analysis (since best model provides probabilistic forecasts).
    - Consideration of class values from a business perspective using profit curves and under consideration of thresholds.
- Build a production pipeline (training & inference) excluding infrastructure aspects for best model to provide final results.

**Python:** [sklearn](https://scikit-learn.org/stable/) | [PyCaret](https://pycaret.gitbook.io/docs) | [AutoGluon.Tabular](https://auto.gluon.ai/stable/tutorials/tabular/index.html) | [LightGBM](https://lightgbm.readthedocs.io/en/stable/) | [PyTorch/Lightning](https://lightning.ai/pytorch-lightning) | [MLflow](https://mlflow.org/) | [Optuna](https://optuna.org/) | [Docker](https://www.docker.com/)

# Use case description:
To reach sustainability goals for the packaging of products, the company needs to know to which packaging categories the single items belong to. Since this information is not given for 45.058 items of the total 137.035 items, the goal is to provide the categories for the items with missing ones based on a data-driven approach. The solution should be applied for comparable data sets from multiple origins.

First analysis has shown that simple 1:1 relationships and rule-based approaches do not lead to proper results. Therefore, a machine learning approach was used. The goal is to build a solution that is capable of doing a highly accurate prediction for as many packaging categories as possible. Meaning that on the one side predictions need to meet a certain threshold for accuracy to be useful for the business (a small amount of wrong classifications can be tolerated but low classification accuracy does not help the business). On the other hand, a threshold for a minimum number of products needs to be covered (it is not mandatory to provide good predictions for all items, but providing good predictions for only a small amount of items also does not help the business a lot). Finally the machine learning solution should consider business decision optimization (cost optimization) based on different individual packaging categories (class).


# Structure of the showcase
As the showcase is intended to reflect the data science process to tackle the use case, the structure builds up on this.

**Code structure**
Directory-tree structure: