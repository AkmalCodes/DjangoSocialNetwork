# DjangoSocialNetwork

This project entails a social networking app that has allowed me to implement a few features.

The features are:<br/>
-login<br/>
-logout<br/>
-password recovery<br/>
-Create Post<br/>
-view post 
--->comment on post<br/>
-delete post<br/>
-report post<br/>
-like post<br/>
-create chatroom
--->join chatroom<br/>
-delete chatroom<br/>
-view chatroom
---> create chat<br/>
-Create User 
---> Create User Profile (using django-admin)<br/>
-View User Profile<br/>
-update user profile <br/>
---> change password<br/>
---> change profile pict <br/>
---> update hobby (not implemented yet)<br/>
<br/>


INSTRUCTIONS ON HOW TO USE:(THIS PROJECT WAS MADE ON PYTHON VERSION 3+)<br/>
1.OPEN VS_CODE(SHOULD WORKS SAME ON OTHER IDEs),MOVE TO BASE DIRECTORY OF PROJECT FOLDER AND OPEN NEW CMD OR BASH TERMINAL
<br/>
<br/>
2.IF YOU HAVE VIRTUAL ENV INSTALLED RUN THE CODE BELOW:<br/>
-->python3 -m virtualenv venv OR python -m virtualenv venv <br/>
2.A)IF YOU DO NOT HAVE PYTHON VIRTUAL ENV INSTALLED, RUN THE CODE BELOW:<br/>
-->pip install virtualenv  <br/>
2.B)MOVE TO STEP 1.<br/>
<br/>
<br/>
3.AFTER INSTALLING VIRTUAL ENV, RUN THE FOLLOWING CODE: (if you named your virtual environment differently then use that name instead of venv)<br/>
-->venv\Scripts\activate<br/>
<br/>
<br/>
4.IN THE SAME TERMINAL, RUN THE FOLLOWING CODE:<br/>
-->pip3 install requirements.txt<br/>
<br/>
<br/>
5.IN THE SAME TERMINAL, RUN THE FOLLOWING CODE:<br/>
-->cd SocialNetwork<br/>
<br/>
<br/>
6.IN THE SAME TERMINAL, RUN THE FOLLOWING CODE: this is to create a superuser/admin account, fill in the output given by terminal, which is username followed by password(password is blank when typed for security reasons!).<br/>
-->python manage.py createsuperuser<br/>
<br/>
<br/>
7. AFTER CREATING SUPERUSER YOU CAN FINALLY RUN THE SERVER WITH THE FOLLOWING CODE:<br/>
-->python manage.py runserver<br/>
7.A) IF TERMINAL SAYS THERE ARE MIGRATIONS TO BE MADE:<br/>
-->python manage.py makemigrations<br/>
7.B) THEN RUN <br/>
-->python manage.py migrate<br/>
7.C) move to step 7.
<br/>
<br/>
8. COPY AND PASTE URL GIVEN BY TERMINAL AND PASTE IT ON WEBBROWSER<br/>
8.A) IF YOU WANT TO SEE DATABASE USE (URL/admin)<br/>
8.B) USE CREDENTIALS YOU MADE FOR SUPERUSER TO LOGIN THE SAME CAN BE DONE ON THE ACTUAL WEBAPP<br/>



