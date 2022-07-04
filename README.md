# Processing Large Data
**Files**
- main.py = .py file in which the top-level code is executed
- tasks.py = development of asynchronous tasks
- utils.py = Functions and objects required to perform the main process
- conf_celery.py = Configuration for integrating Flask with Celery
- requirements.txt = Libraries installed in the development environment

To start the program you must first 
1. Activate venv: source/bin/activate
2. Installing requirements.txt
3. processing_large_data-main/: python3 main.py
4. In terminal: celery -A tasks.celery worker

5. APi "/upload/<name_file>":
   1. curl -X POST http://127.0.0.1:5000/upload/songs_normalize.csv
   On Post request, it processes the file storing it with the name: output-{date}.csv The task id is printed on the terminal screen.
   
6. API "/task/<task_id>"
   1. curl -X GET http://127.0.0.1:5000/task/5f16e1d5-d904-472a-b1f6-139c20591d22. In case the task is finished, it returns on the terminal screen the result of the processed csv.

Note: Include data in csv format in /data file