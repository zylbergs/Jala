# Jala
Project Documentation
[Structure]
1. devs
> development notebook that is temporarily used
2. feature
> folder containing feature store and versioning
3. jala
> folder containing python virtual environment used for this project
4. ml_prediction
> folder containing microservice predtiction function
    a. biomass.py
        script used to predict from choosed model from model repository. script used in streamlit service
5. model_repo
> folder containing best model from ML main notebook and folder for model versioning 
6. Report
> report output of feature importance generated from ML main notebook
> SR & ADG report generated from streamlit service
7. Source
> folder containing data source
8. transform
> containing main scripts that transform data source and feature versioning
    a. cycle.py
        main script that transform raw data source of cycle.csv
    b. fasting.py
        main script that transform raw data source of fasting.csv
    c. feature_store.py
        main script of feature store feature
    d. feed.py
        main script that transform raw data source of feed.csv
    e. measurement.py
        main script that transform raw data source of measurement.csv
    f. pond_farm.py
        main script that transform raw data source of pond.csv and farm.csv
    g. sampling_harverst.py
        main script that transform raw data source of sampling.csv and harvest.csv

9. vali_tools
> folder of internal tooling for advanced features inspection
    a. valitoos.py
        main script of internal tooling module, containing check_health function that perform advanced feature inspection
19. analytics_main.ipynb
> main EDA notebook used for features inspection
20. ML.ipynb
> main ML development and research notebook, this notebook will yield pickle model for ML prediction features
21. prediction.xlsx
> cache file/temporary file generated from ML prediction features in streamlit service
22. report_sr.py
> main script of SR & ADG report generation features
23. requirements.txt
> list of dependencies used in this project
24. streamlit_app.py
> simple python web app that is intended for end users.
> streamlit service
    a. Generate Features
        generate feature store if there is another feature version for further ML develoment
    b. Generate Report
        Generate report SR & ADG each Cycle
    C. ML Model Prediction
        Generate ML prediction of biomass, selling price, Survival rate, average weight harvest
