# Shape-Detection

## Project Description:
- This is python project to detect shape, center and color of different shapes in images.
- Technologies used - OpenCV, Numpy
- This project was done as a Task for Eyantra - Robotics competition organized by IIT Bombay.

## Installation and Testing:
- Clone the repository using

    ```
    git clone https://github.com/Vaibhav-22-dm/Shape-Detection.git
    ```
- Install Python
- Install virtualenv packages using 

    ```
    pip install virtualenv
    ```
- Create a virtual environment with
    ```
    virtualenv <env_name>
    ```
- Activate the virtual environment using :

    For Windows

    ```
    .env_name/Scripts/activate
    ``` 
    For Linux
    
    ```
    source env_name/bin/activate
    ```
- Install the required packages using 
    
    ```
    pip install -r requirements.txt
    ```
- Run the task_1a.py using 

    ```
    python ./task_1a.py
    ```

## Future Work
- Develop Web UI where people can upload their images.
- Superimpose a grid over the images then label the shapes with color, center and shape name at the appropriate grid cell.
- Convert the project to handle dynamic (live image capturing using web cam) instead of static images.