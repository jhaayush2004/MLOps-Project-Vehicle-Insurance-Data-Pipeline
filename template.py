import os
from pathlib import Path

project_name = "src"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")



# You've correctly identified a key pattern in Python projects, especially larger ones: the presence of __init__.py files in almost every directory within your src folder.

# This ubiquitous __init__.py file serves a crucial purpose in Python's module system: it designates a directory as a Python package.

# Let's break down what __init__.py means and its need:

# What __init__.py Means
# When Python encounters a directory that contains an __init__.py file, it treats that directory not just as a regular folder, but as a Python package. This has several implications:

# It's a Package: The directory (e.g., src/components/) can now be imported using dot notation (e.g., from src.components import data_ingestion).
# Initialization Code: The code inside __init__.py is executed only once when the package (or any module within it) is first imported. This makes it a perfect place for initialization tasks.
# Defines What's Public: You can control what names are exposed when someone does from package_name import *.
# Why __init__.py is Needed (and its purpose)
# 1. Enabling Package Imports
# This is the primary and most fundamental reason. Without an __init__.py file in a directory, Python simply doesn't know how to treat that directory as an importable package.

# Example:

# If src/components/ contains data_ingestion.py but no src/components/__init__.py:

# You cannot do: from src.components import data_ingestion
# Python would raise a ModuleNotFoundError because src.components is not recognized as a package.
# With src/components/__init__.py present:

# You can do: from src.components import data_ingestion
# You can also do: import src.components.data_ingestion
# 2. Package Initialization
# The code inside __init__.py is executed automatically the first time the package (or any of its submodules) is imported. This makes it a great place for:

# Setting up package-wide configurations.
# Importing commonly used classes/functions: You can import sub-modules or specific functions/classes from those sub-modules into the package's namespace, making them directly accessible from the package itself.
# Example: In src/components/__init__.py:
# Python

# from .data_ingestion import DataIngestion
# from .data_validation import DataValidation
# Then, in another file, you could do: from src.components import DataIngestion instead of from src.components.data_ingestion import DataIngestion. This can make imports cleaner, though it's a design choice.
# Defining __all__: This special variable is a list of strings that defines what modules/names are exposed when a user does from package_name import *. If __all__ is not defined, import * will import all non-underscored names defined in the __init__.py and its imported submodules.
# 3. Namespace Management
# __init__.py helps manage the package's namespace, preventing naming conflicts and organizing code logically. Each __init__.py contributes to the package's overall structure and how its contents are exposed.

# Why It's "Everywhere" in Your List
# Your list_of_files creates a well-structured Python project with multiple sub-packages:

# src/: Main package
# src/components/: Sub-package for modular steps of your MLOps pipeline.
# src/configuration/: Sub-package for configuration files.
# src/cloud_storage/: Sub-package for cloud storage interactions.
# src/data_access/: Sub-package for data access logic.
# src/constants/: Sub-package for constants.
# src/entity/: Sub-package for entity (data model) definitions.
# src/exception/: Sub-package for custom exceptions.
# src/logger/: Sub-package for logging setup.
# src/pipeline/: Sub-package for ML pipelines.
# src/utils/: Sub-package for utility functions.
# By placing __init__.py in each of these directories, you are telling Python: "Hey, treat these folders as Python packages, and allow me to import modules and sub-packages from within them using dot notation." This is standard practice for organizing larger Python applications.

# In Python 3.3+ (Implicit Namespace Packages)
# It's worth noting a nuance: Since Python 3.3, if a directory doesn't contain an __init__.py file, it can sometimes be treated as an implicit namespace package. This allows for splitting a single logical package across multiple physical directories, which is useful for very large projects or distributed development where different teams own different sub-packages.

# However, for most typical projects like yours, explicit __init__.py files are still widely used and recommended because they clearly define package boundaries, allow for explicit initialization code, and are compatible with all Python versions. They also make the package structure immediately clear to anyone looking at your codebase.
