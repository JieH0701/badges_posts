# Badge_Posts

### STEPS:
1. create two tables in database with sqlite3: bagdes & posts. 
2. inital load with this two tables use run.py
3. create get functions for all bagdes
4. create get functions for all posts
5. create get_total_answers for the assigment:

### RESULTS URL:
1. http://localhost:5000 --> hello message, docker is running!
2. http://localhost:5000/posts --> all posts
3. http://localhost:5000/badges --> all bagdes
4. http://localhost:5000/totalanswers/Autobiographer --> total answers with bagde Autobiographer: 4597
5. http://localhost:5000/posts/_int:user_id_ --> posts with certain user_id
6. http://localhost:5000/badge/_string:name_ --> all badges with certain name, for example "Autobiographer"

### HOW TO:
1. How to build docker image: 
    docker build -t "badges_posts" .
2. How to run docker:
docker run -p 5000:80 --volume=./badges_post:/app badges_posts

