import requests
sess = requests.session()
url = 'http://192.168.0.10:5000'


def register_user(name, password):
    """
    this function will register users in the database.
    :param name:
    :param password:
    :return: if the status code is 200 then it will return this message: "Registration successful..!"
            if the status code id 400 then it will return this message: "Name or password is missing"
            if the status code is 409 then it will return this message: "Name already exist.."
    """
    response = requests.post(url+'/user/register', json={'name': name, 'password': password})
    if response.status_code == 200:
        return 'Registration successful..!'
    if response.status_code == 400:
        return "Name or password is missing"
    if response.status_code == 409:
        return "Name already exist.."


def login(name, password):
    """
    This function will only login register users.
    :param name:
    :param password:
    :return: if the status code is 200 it will return the user name and this message:
                " is logged in." (e.g: ali is logged in. )
            if the status code is 400 return this function will return the message: "Name or password is missing"
            if the status code is 401 it will return this message: "invalid name or password...!"
    """
    response = sess.post(url+'/user/login', json={'name': name, 'password': password})
    if response.status_code == 200:
        return ' %s is logged in.' % name
    if response.status_code == 400:
        return "Name or password is missing"
    if response.status_code == 401:
        return "invalid name or password...!"


def logout():
    """
    If the user is logged in then this function will logout the user.
    :return: if the status code is 200 then it will return this message: 'Log out successfully...!.'
            if the status code is 401 then this function will return this message: "unauthorized access...!
    """
    response = sess.get(url+'/user/logout')
    if response.status_code == 200:
        return 'Log out successfully...!.'
    if response.status_code == 401:
        return "unauthorized access...!"
    if response.status_code == 405:
        return "you are not logged in"


def delete_user():
    """
    This function will delete the user who is logged in
    :return: if the status code is 200 then it will return the message: ' Delete'
            if the status code is 401 then it will return this message: "unauthorized access...!"
    """
    response = sess.delete(url+'/user/delete')
    if response.status_code == 200:
        return ' Delete'
    if response.status_code == 401:
        return "unauthorized access...!"
    if response.status_code == 405:
        return "you are not logged in"


def add_course(cr_name):
    """
    This function will register user in courses.
    :param cr_name:
    :return: if the status code is 200 then it will return this message: "Registered successfully..!"
            if the status code is 400 then it will return this message: "please enter the course name you want to register"
    if the status code is 409 then it will return this message: "you are already register to this course"
    if the status code is  401 then it will return this message "Unauthorized access...!"
    """
    response = sess.post(url+'/course/add', json={"cr_name": cr_name})
    if response.status_code == 200:
        return "Registered successfully..!"
    if response.status_code == 400:
        return "please enter the course name you want to register"
    if response.status_code == 409:
        return "you are already register to this course"
    if response.status_code == 401:
        return "Unauthorized access...!"
    if response.status_code == 405:
        return "you are not logged in"


def all_courses():
    """
    This function will show all the courses in which the user is registered
    :return: if the status code is 200 the function will return all the courses in which the user is registered
    if the status code is 404, it will return this message: "Not Found...!"
    if the status code is 401, it will return this message: "Unauthorized access...!"

    {"status": SUCCESS/FAILURE, "output": list}
    """
    response = sess.get(url+'/course/all')
    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return "Not Found...!"
    if response.status_code == 401:
        return "Unauthorized access...!"
    if response.status_code == 405:
        return "you are not logged in"


def find_course(id_):
    """
    This function will find a specific course in the courses in which user is registered
    :param id_:
    :return: if the status code is 200, it will show you the name of the course
    if the status code is 404, it will return this message: "Not Found...!"
    if the status code is 401,it will  return this message: "Unauthorized access...!"
    if the status code is 405, it will return this message "Unauthorized access...!"
    """
    response = sess.get(url+'/course/find/'+id_)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return "Not Found...!"
    if response.status_code == 401:
        return "Unauthorized access...!"
    if response.status_code == 405:
        return "Unauthorized access...!"
    if response.status_code == 405:
        return "you are not logged in"


def delete_course(id_):
    """
    This function will delete a course from the user registered courses
    :param id_:
    :return: if the status code is 200, it will return this message'deleted'
    if the status code is 404, it will return this message: "Not Found...!"
    if the status code is 401, it will return this message"Unauthorized access...!"
    """
    response = sess.delete(url+'/course/delete/'+id_)
    if response.status_code == 200:
        return 'deleted'
    if response.status_code == 404:
        return "Not Found...!"
    if response.status_code == 401:
        return "Unauthorized access...!"
    if response.status_code == 405:
        return "you are not logged in"


def update_course(id_, cr_name):
    """
    This function wil to update the course(user can change course)
    :param id_:
    :param cr_name:
    :return: if the status code is 200, it will return the message: 'updated successfully...'
            if the status code is 404, it will return this message: "Not Found...!"
            if the status code is 401,it will return this message: "Unauthorized access...!"
            if the status code is 405, it will return this message: "you are not logged in"
    """
    response = sess.put(url+'/course/update/'+id_, json={"cr_name": cr_name})
    if response.status_code == 200:
        return 'updated successfully...'
    if response.status_code == 404:
        return "Not Found...!"
    if response.status_code == 401:
        return "Unauthorized access...!"
    if response.status_code == 405:
        return "you are not logged in"
