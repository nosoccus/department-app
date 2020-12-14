# Department Management System [![Coverage Status](https://coveralls.io/repos/github/nosoccus/department-app/badge.svg)](https://coveralls.io/github/nosoccus/department-app)
> A simple Flask web-application for managing departments and employees.

#### Software Requirements Specification (SRS) is located [here](https://github.com/nosoccus/department-app/blob/main/documentation/SPECIFICATION.md).

### How to install the project:
- #### Clone the project from Github into a fresh folder.
      git clone https://github.com/nosoccus/Tronion.git
    
- #### Create a Virtual Environment.
      $ virtualenv venv
    
  - Activate on **Linux**: 

        $ source venv/bin/activate

  - Activate on **Windows**:
    
        > .\venv\scripts\activate
    
- #### Install the project dependencies listed in [```requirements.txt```](https://github.com/nosoccus/department-app/blob/main/requirements.txt)
      (venv) $ pip install -r requirements.txt
      
- #### Make sure you have installed up to date version of [PostgreSQL](https://www.postgresql.org/download/).
Before launching project you also have to configure database access.

- #### Create DB and configure it.
  - Create it with this query:
    ```postgresql
    CREATE DATABASE IF NOT EXISTS departments
    ```
  - Configure it in [```config.py```](https://github.com/nosoccus/department-app/blob/main/config.py):
  ```python
  SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@server/database'
  ```

- #### Set environment variables:
  - For **Linux**:
  
        export FLASK_APP=run.py
  - For **Windows**:
  
        set FLASK_APP=run.py

- #### Run the project:
      flask run