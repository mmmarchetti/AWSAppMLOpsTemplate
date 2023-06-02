# MLOps Template

### Project Structure
```
project_name/
|
|__ data/ 
|    |
|    |__ raw/                           - Raw, unprocessed data
|    |   |__ dataset.csv
|    |
|    |__ interim/                       - Intermediate data after some preprocessing
|    |   |__ cleaned_data.csv
|    |
|    |__ processed/                     - Final data used for modeling
|    |   |__ preprocessed_data. csv
|    |
|    |__ external/                      - Data from external sources
|        |__ external_data. csv
|
|__ trained_models/                     - Trained and serialized models
|    |__model_v1.pk
|
|__ notebooks/                          - Jupyter notebooks for exploration and analysis
|    |__exploratory_analysis.ipynb
|
|__ src/ 
|    |                                  - Source code for the project 
|    |__ data/                          - Scripts to download, preprocess and generate data
|    |   |__ download_data.py                 
|    |   |__ preprocess_data.py
|    |
|    |__ features/                      - Scripts to turn raw data into features for modeling
|    |   |__ feature_engineering.py
|    |
|    |__ models/                        - Scripts to train models and make predictions
|    |   |__ train_model.py 
|    |   |__ predict_model.py
|    |
|    |__ visualization/                 - Scripts to create visualizations
|    |   |__ visualize_data.py
|    |
|    |__ reports/                       
|        |
|        |__ figures/                   - Generated graphics and figures  
|        |   |__ histogram.png
|        |  
|        |__ docs                       - Generated analysis as HTML, PDF, or other formats
|            |__ report.pdf            
|
|__ docker/                             - Docker files
|    |__ base.Dockerfile                 
|    |__ cloud.Dockerfile
|
|__ .gitignore                          - List of files and directories to ignore in version cont
|
|__ README.md                           - Project description and setup guide
|
|__ requirements.txt                    - Python dependencies for the project
|
|__ .env                                - Env secrets (KEYS, passwords, etc...) Obs. Listed in .gitignore
|
|__ Makefile                            - Make file for CI/CD
```
