Ok....
As usually you have to create a database of postgresql
After that,change my values in line 8 and line 20 of the config.py file .

This application requires a database to run..we have created a database now we add values to the database:
    


    Step 1 on Terminal run   this code  python3.6 manage.py db init

    A folder will be created called 

    Step 2  on Terminal run   this code  python3.6 manage.py db migrate


    Step 3  on terminal run this code   python3.6 manage.py db upgrade


   What these above codes does is create and add tables into the database you have created


   Now you can run your app by simply running the code ./start.sh


   PS:The ony change you need to make is in the config.py files ..only that




