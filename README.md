# Badge_Posts

###STEPS:
1. create two tables in database with sqlite3: bagdes & posts. 
2. inital load with this two tables use run.py
3. create get functions for all bagdes
4. create get functions for all posts
5. create get_total_answers for the assigment:

###RESULTS:
URL in Docker for tests:
http://localhost:5000 --> hello message, docker is running!
http://localhost:5000/posts --> all posts
http://localhost:5000/badges --> all bagdes
http://localhost:5000/totalanswers/Autobiographer --> total answers with bagde Autobiographer: 4597
http://localhost:5000/posts/<int:user_id> --> posts with certain user_id
http://localhost:5000/badge/<string:name> --> all badges with certain name, for example "Autobiographer"

###HOW TO:
How to build docker image: 
    docker build -t "badges_posts" .
How to run docker:
docker run -p 5000:80 --volume=./badges_post:/app badges_posts

