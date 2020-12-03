 # Software Requirements Specification (SRS)
 
> In the root of the repository create folder "documentation". Create there a document Software Requirements Specification (SRS) with a description of a software system to be developed with all applicable use cases. The specification document must include forms mockups too. SRS has to be created in Markdown format in English.

## Introduction
- ### Purpose:
  **Department Managment System** - simple web-application for managing **departments** and **employees**.

___

## Overall Description
- ### Product features:
  The web application should allow:
  - to display a list of **departments** and the average salary (calculated automatically) for these **departments**.
  - to display a list of **employees** in the **departments** with an indication of the salary for each **employee** and a search field to search for **employees** born on a certain date or in the period between dates.
  - to change (add / edit / delete) the above data (CRUD operations).

  The database should contain two entities: **department** and **employee**:
  - **Department** should store *name* and *description*
  - **Employee** should store the following data: *related department*, *employee name*, *date of birth*, *salary*.

- ### Design and implementation constraints:
  This project uses *Python* as main programming language, also *Flask* as a micro web-framework to build web-application and *PostgreSQL* as DB.
  
  On client side there is next technology stack: *HTML*, *CSS*, *JS*.
  
___

## System features
- ### Department functional:
  - #### Display *departments*:
    The page is accessible by clicking the "Departments" tab in the top of the screen. It displays the list of departments and looks like:
    
    <p align="center">
    <img src="/documentation/mockups/departments-main.png">
    </p>
    
    User can perform the following actions:
     - go to the "Employees" page.
     - update departments.
     - add a new department.
     - edit the existing department.
     - delete the department.
     
    User can see the following information about departments:
     - Department name: title of the department.
     - Description: description of the department.
     - Average salary: average salary of employees in the department.
     - Num of employees: number of employees in the department.
     
  - #### Add an *department*:
    The page is accessible by clicking the "Add" button in the "Departments" page. It allows to add a new department and looks like:
    
    <p align="center">
    <img src="/documentation/mockups/add-new-department.png">
    </p>
    
    User can perform the following actions:
     - Fill information about new department.
     - Save an information to new department. After this option information will be saved to a new department in DB.
     - Cancel action. After this option
     
  - #### Edit the *department*:
    The page is accessible by clicking the "Edit" button opposite needed department. It allows to edit the existing department and looks like:
    
    <p align="center">
    <img src="/documentation/mockups/edit-department.png">
    </p>
    
    User can perform the following actions:
     - Fill information about new department.
     - Save an information to new department. After this option information will be saved to a new department in DB.
     - Cancel action. After this option user will be returned to "Departments" page.
     
     
- ### Employee functional:
  - #### Display *employees*:
    The page is accessible by clicking the "Employees" tab in the top of the screen. It displays the list of employees and looks like:
    
    <p align="center">
    <img src="/documentation/mockups/employees-main.png">
    </p>
    
    User can perform the following actions:
     - go to the "Departments" page.
     - update employees.
     - add a new employee.
     - edit the existing employee.
     - delete the employee.
     - filter employees by birth date.
     - cancel the filtration.
     
    User can see the following information about employees:
     - First name: first name of the employee.
     - Last name: last name of the employee.
     - Date of birth: birth date of the employee.
     - Salary: salary of the employee.
     - Department: the related department to the employee.
     
  - #### Add an *employee*:
    The page is accessible by clicking the "Add" button in the "Employees" page. It allows to add a new employee and looks like:
    
    <p align="center">
    <img src="/documentation/mockups/add-new-employee.png">
    </p>
    
    User can perform the following actions:
     - Fill information about new employee.
     - Save an information to new employee. After this option information will be saved to a new employee in DB.
     - Cancel action. After this option user will be return to the "Employees" page.
     
  - #### Edit the *employee*:
    The page is accessible by clicking the "Edit" button opposite needed employee. It allows to edit the existing employee and looks like:
    
    <p align="center">
    <img src="/documentation/mockups/edit-employee.png">
    </p>
    
    User can perform the following actions:
     - Fill information about new department.
     - Save an information to new department. After this option information will be saved to a new department in DB.
     - Cancel action. After this option
     
  
