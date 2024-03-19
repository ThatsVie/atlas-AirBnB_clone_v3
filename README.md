# AirBnB Clone 

💻
## The Console
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

<details>
<summary>Functionalities of this command interpreter</summary>
<ul>
  <li>Create a new object (ex: a new User or a new Place)</li>
  <li>Retrieve an object from a file, a database etc...</li>
  <li>Do operations on objects (count, compute stats, etc...)</li>
  <li>Update attributes of an object</li>
  <li>Destroy an object</li>
</ul>
</details>
    
<details>
<summary>Table of Content</summary>
<ul>
  <li><a href="#environment">Environment</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#file-descriptions">File Descriptions</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#examples-of-use">Examples of use</a></li>
  <li><a href="#bugs">Bugs</a></li>
  <li><a href="#authors">Authors</a></li>
  <li><a href="#license">License</a></li>
</ul>
</details>

<details>
<summary> Environment</summary>
<ul>
  <li>This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3) </li>
</ul>
</details>

<details>
<summary>Installation</summary>
<ul>
  <li>Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`</li>
  <li>Access AirBnb directory: `cd AirBnB_clone`</li>
  <li>Run hbnb(interactively): `./console` and enter command</li>
  <li>Run hbnb(non-interactively): `echo "<command>" | ./console.py`</li>
</ul>
</details>

<details>
<summary>File Descriptions</summary>
<ul>
  <li>[console.py](console.py) - the console contains the entry point of the command interpreter.</li>
  <li>List of commands this console current supports:</li>
  <li>`EOF` - exits console</li>
  <li>`quit` - exits console</li>
  <li>`<emptyline>` - overwrites default emptyline method and does nothing</li>
  <li>`create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id</li>
  <li>`destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).</li>
  <li>`show` - Prints the string representation of an instance based on the class name and id.</li>
  <li>`all` - Prints all string representation of all instances based or not on the class name.</li>
  <li>`update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).</li>
</ul>

#### `models/` directory contains classes used for this project:
<ul>
  <li>[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived</li>
  <li>`def __init__(self, *args, **kwargs)` - Initialization of the base model</li>
  <li>`def __str__(self)` - String representation of the BaseModel class</li>
  <li>`def save(self)` - Updates the attribute `updated_at` with the current datetime</li>
  <li>`def to_dict(self)` - returns a dictionary containing all keys/values of the instance</li>
</ul>

Classes inherited from Base Model:
<ul>
  <li>[amenity.py](/models/amenity.py)</li>
  <li>[city.py](/models/city.py)</li>
  <li>[place.py](/models/place.py)</li>
  <li>[review.py](/models/review.py)</li>
  <li>[state.py](/models/state.py)</li>
  <li>[user.py](/models/user.py)</li>
</ul>

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
<ul>
  <li>[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances</li>
  <li>`def all(self)` - returns the dictionary __objects</li>
  <li>`def new(self, obj)` - sets in __objects the obj with key <obj class name>.id</li>
  <li>`def save(self)` - serializes __objects to the JSON file (path: __file_path)</li>
  <li>` def reload(self)` - deserializes the JSON file to __objects</li>
</ul>

#### `/tests` directory contains all unit test cases for this project:
<ul>
  <li>[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes</li>
  <li>TestBaseModelDocs class:</li>
  <li>`def setUpClass(cls)`- Set up for the doc tests</li>
  <li>`def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8</li>
  <li>`def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8</li>
  <li>`def test_bm_module_docstring(self)` - Test for the base_model.py module docstring</li>
  <li>`def test_bm_class_docstring(self)` - Test for the BaseModel class docstring</li>
  <li>`def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods</li>

TestBaseModel class:
<ul>
  <li>`def test_is_base_model(self)` - Test that the instantiation of a BaseModel works</li>
  <li>`def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime</li>
  <li>`def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime</li>
  <li>`def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects</li>
</ul>

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenityDocs class:
<ul>
  <li>`def setUpClass(cls)` - Set up for the doc tests</li>
  <li>`def test_pep8_conformance_amenity(self)` - Test that models/amenity.py conforms to PEP8</li>
  <li>`def test_pep8_conformance_test_amenity(self)` - Test that tests/test_models/test_amenity.py conforms to PEP8</li>
  <li>`def test_amenity_module_docstring(self)` - Test for the amenity.py module docstring</li>
  <li>`def test_amenity_class_docstring(self)` - Test for the Amenity class docstring</li>
</ul>

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
<ul>
  <li>`def setUpClass(cls)` - Set up for the doc tests</li>
  <li>`def test_pep8_conformance_city(self)` - Test that models/city.py conforms to PEP8</li>
  <li>`def test_pep8_conformance_test_city(self)` - Test that tests/test_models/test_city.py conforms to PEP8</li>
  <li>`def test_city_module_docstring(self)` - Test for the city.py module docstring</li>
  <li>`def test_city_class_docstring(self)` - Test for the City class docstring</li>
</ul>

[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorageDocs class:
<ul>
  <li>`def setUpClass(cls)` - Set up for the doc tests</li>
  <li>`def test_pep8_conformance_file_storage(self)` - Test that models/file_storage.py conforms to PEP8</li>
  <li>`def test_pep8_conformance_test_file_storage(self)` - Test that tests/test_models/test_file_storage.py conforms to PEP8</li>
  <li>`def test_file_storage_module_docstring(self)` - Test for the file_storage.py module docstring</li>
  <li>`def test_file_storage_class_docstring(self)` - Test for the FileStorage class docstring</li>
</ul>

[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the TestPlaceDoc class:
<ul>
  <li>`def setUpClass(cls)` - Set up for the doc tests</li>
  <li>`def test_pep8_conformance_place(self)` - Test that models/place.py conforms to PEP8.</li>
  <li>`def test_pep8_conformance_test_place(self)` - Test that tests/test_models/test_place.py conforms to PEP8.</li>
  <li>`def test_place_module_docstring(self)` - Test for the place.py module docstring</li>
  <li>`def test_place_class_docstring(self)` - Test for the Place class docstring</li>
</ul>

[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the TestReviewDocs class:
<ul>
  <li>`def setUpClass(cls)` - Set up for the doc tests</li>
  <li>`def test_pep8_conformance_review(self)` - Test that models/review.py conforms to PEP8</li>
  <li>`def test_pep8_conformance_test_review(self)` - Test that tests/test_models/test_review.py conforms to PEP8</li>
  <li>`def test_review_module_docstring(self)` - Test for the review.py module docstring</li>
  <li>`def test_review_class_docstring(self)` - Test for the Review class docstring</li>
</ul>

[/test_models/state.py](/tests/test_models/test_state.py) - Contains the TestStateDocs class:
<ul>
  <li>`def setUpClass(cls)` - Set up for the doc tests</li>
  <li>`def test_pep8_conformance_state(self)` - Test that models/state.py conforms to PEP8</li>
  <li>`def test_pep8_conformance_test_state(self)` - Test that tests/test_models/test_state.py conforms to PEP8</li>
  <li>`def test_state_module_docstring(self)` - Test for the state.py module docstring</li>
  <li>`def test_state_class_docstring(self)` - Test for the State class docstring</li>
</ul>

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
<ul>
  <li>`def setUpClass(cls)` - Set up for the doc tests</li>
  <li>`def test_pep8_conformance_user(self)` - Test that models/user.py conforms to PEP8</li>
  <li>`def test_pep8_conformance_test_user(self)` - Test that tests/test_models/test_user.py conforms to PEP8</li>
  <li>`def test_user_module_docstring(self)` - Test for the user.py module docstring</li>
  <li>`def test_user_class_docstring(self)` - Test for the User class docstring</li>
</ul>


</details>

<details>
<summary>Examples of use</summary>

```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```
</details>

<details>
<summary> Authors</summary>
<li>Alexa Orrico - [Github](https://github.com/alexaorrico) / [Twitter](https://twitter.com/alexa_orrico)  </li>
<li>Jennifer Huang - [Github](https://github.com/jhuang10123) / [Twitter](https://twitter.com/earthtojhuang)  </li>
<li>Second part of Airbnb: Joann Vuong</li>
</details>

To view a README file for the Atlas AirBnB Clone Console project, please visit [this link](https://github.com/ThatsVie/atlas-AirBnB_clone/blob/main/README.md).


💻
 ## Web Static

The `web_static` folder serves as a repository for static assets such as HTML, CSS, and images. It organizes the front-end resources used to create and style the web pages in the project. These assets are served to users directly by the web server without any processing, enhancing the performance and scalability of the web application.

To view a README file for the Atlas AirBnb Clone `web_static` folder, please visit [this link](https://github.com/ThatsVie/atlas-AirBnB_clone/blob/main/web_static/README.md).

💻
## Web Flask/ Web Framewok

This project implements a web framework for an AirBnB clone using Flask, a lightweight WSGI web application framework. It includes various tasks that demonstrate the functionality of the web application, such as displaying different routes, rendering HTML templates, and interacting with a database.

To view a README file for the Atlas AirBnb Clone `web_flask` folder, please visit [this link](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/blob/master/web_flask/README.md).

💻
## AirBnB Clone v3 API

This repository was originally forked from this [codebase](https://github.com/alexaorrico/AirBnB_clone_v2). It was built upon to provide endpoints to interact with various resources such as states, cities, users, places, reviews, and amenities.

💫💫💫
### Storage Enhancement: DBStorage and FileStorage

The DBStorage and FileStorage modules have been updated from the storage_get_count branch to include two new methods:

**get(cls, id):** Retrieves an object based on the class and its ID, or returns None if not found.

**count(cls=None):** Returns the number of objects in storage matching the given class. If no class is passed, returns the count of all objects in storage.

New tests have been added to ensure the functionality of these methods.

💫💫💫
### Endpoints

**/states:** Retrieves a list of all state objects.

**/states/<state_id>:** Retrieves a specific state object by ID.

**/cities/<city_id>/places:** Retrieves a list of all places in a city.

**/places/<place_id>:** Retrieves a specific place object by ID.

**/places/<place_id>/reviews:** Retrieves a list of all reviews for a place.

**/reviews/<review_id>:** Retrieves a specific review object by ID.

**/amenities:** Retrieves a list of all amenity objects.

**/amenities/<amenity_id>:** Retrieves a specific amenity object by ID.

**/users:** Retrieves a list of all user objects.

**/users/<user_id>:** Retrieves a specific user object by ID.

For each resource, the API supports GET, POST, PUT, and DELETE methods to perform CRUD operations.

💫💫💫
### Cross-Origin Resource Sharing (CORS)
The API is configured to allow cross-origin requests from any origin (0.0.0.0) using the flask_cors module. This setup ensures that web clients can access the API data without encountering CORS-related issues.

💫💫💫
### CRUD
**CRUD** stands for **Create**, **Read**, **Update**, and **Delete**. It represents the four basic operations that can be performed on data in a persistent storage system, such as a database.

**Create (POST):** This operation involves creating new data entries or resources in the system. It typically involves sending data to the server to be stored.

**Read (GET):** This operation involves retrieving existing data or resources from the system. It retrieves information without altering the data itself.

**Update (PUT or PATCH):** This operation involves modifying existing data or resources in the system. PUT is often used to completely replace a resource, while PATCH is used to make partial updates.

**Delete (DELETE):** This operation involves removing existing data or resources from the system.

**GET**, **POST**, **PUT**, and **DELETE** are **HTTP** methods used to perform these **CRUD** operations over the network:

**GET:** Retrieves data from the server. It is typically used for the Read operation in **CRUD**.

**POST:** Sends data to the server to create a new resource. It is used for the Create operation in **CRUD**.

**PUT:** Sends data to the server to update or replace an existing resource. It is used for the Update operation in **CRUD**.

**DELETE:** Sends a request to the server to delete an existing resource. It is used for the Delete operation in **CRUD**.

💫💫💫
### Installation
Before running the application, ensure you have the following installed:

Python 3.x

MySQL

SQLAlchemy

MySQLDB (Python MySQL client library)

Flask

**Clone the repository:**
```bash
git clone https://github.com/ThatsVie/atlas-AirBnB_clone_v3.git
```
**Navigate to the project directory**
```bash
cd atlas-AirBnB_clone_v3
```
**Install the flask_cors module:**
```bash
pip3 install flask_cors
```
💫💫💫
### Usage

<details>
<summary>
🌻🌻🌻Retrieving Objects (get Method) and Counting Objects (count Method) </summary>
<ul>
  <li>
    
Input this command:

```bash
cat test_get_count.py
```

The command cat test_get_count.py is used to display the contents of the file named test_get_count.py.
![Screenshot 2024-03-18 155039](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/14959e0c-c94b-43ea-bccf-efc9460cfecb)

Input this command:

```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./test_get_count.py
```

This command sets environment variables for MySQL connection parameters (HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB) and the storage type (HBNB_TYPE_STORAGE). Then, it executes the Python script test_get_count.py.

![Screenshot 2024-03-18 155447](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/870992bd-3496-43d3-a900-a354c6b6d222)

Input this command:

```bash
./test_get_count.py
```

This command executes the Python script named test_get_count.py in the current directory.

![Screenshot 2024-03-18 155722](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/33f6ebc4-a9d3-434b-8c56-ad31ad713e4a)

</ul> </li> </details>


<details>
<summary>
🌻🌻🌻Starting the API
</summary>
  <ul></li>
    
Input this command:

```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
```

This command initializes environment variables for MySQL configuration, storage type, API host, and port, then runs the API server using Python 3.

![Screenshot 2024-03-18 160252](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/e1bd81a7-04be-434a-9d5a-548266ae664a)

In another terminal window input this command:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/status
```

This command sends a **GET** request to the specified URL (http://0.0.0.0:5000/api/v1/status) to retrieve the status of the API.

![Screenshot 2024-03-18 160933](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/7243b816-3017-42cc-beb8-2ea01fb825bc)

Next, input this command:

```bash
curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type
```

This command sends a **GET** request to the URL http://0.0.0.0:5000/api/v1/status with verbose output enabled (-vvv) while suppressing the progress meter (-s). It then redirects the standard error stream (2>&1) to the standard output stream. Finally, it filters the output to display lines containing "Content-Type" using the grep command.

![Screenshot 2024-03-18 161236](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/7b3b8c22-476d-440e-a178-22fb2a432692)

</ul> </li> </details>

<details>
<summary>
🌻🌻🌻Getting Stats  </summary>
<ul>
  <li>
    
**Note: For this to work the API needs to be running.**

In your terminal input this command:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/stats
```

This command sends a **GET** request to the specified URL http://0.0.0.0:5000/api/v1/stats. It is querying an API endpoint to retrieve statistics about the number of each type of object. The response will contain a JSON object with the counts of various object types such as amenities, cities, places, reviews, states, and users.

![Screenshot 2024-03-18 164441](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/92765fc0-f35a-4d4d-8f00-593b96591e94)


Now, in your browser:

```bash
http://localhost:5000/api/v1/stats
```

![Screenshot 2024-03-18 164607](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/3b0cc174-5da5-4c4f-9698-5fe0acdb98e8)

</ul> </li> </details>

<details>
<summary>🌻🌻🌻404 errors  </summary>
<ul>
  <li>

**Note: Ensure the API is running**

This task ensures that when clients access invalid endpoints in the API, they receive a clear and standardized JSON response indicating that the requested resource was not found.

In your terminal input this command:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/nop
```

This command sends a **GET** request to http://0.0.0.0:5000/api/v1/nop, attempting to retrieve data from the specified URL.
![Screenshot 2024-03-18 170823](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/871248f0-ddf9-43ee-8fa7-7ca59ba7031a)

Then, input this command:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/nop -vvv
```

This command sends a verbose GET request to http://0.0.0.0:5000/api/v1/nop, providing detailed output about the request and response communication.

![Screenshot 2024-03-18 170844](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/c200ec65-5028-4353-a23c-7b42f84e3279)

Now, in your browser:

```bash
http://localhost:5000/api/v1/nop
```

![Screenshot 2024-03-18 170706](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/79c60134-4dd9-42dd-878a-3a15a49012d5)

</ul> </li> </details>

<details>
<summary>
🌻🌻🌻State CRUD   </summary>
<ul>
  <li>

**Ensure the API server is still running**
Input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/states/
```

This command retrieves a list of all State objects from the API.

![Screenshot 2024-03-18 171651](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/7b028171-a828-481a-98dd-da5cb339b237)


Now, in your browser:

```bash
http://localhost:5000/api/v1/states/
```

![Screenshot 2024-03-18 171812](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/46275bea-8ada-42e8-a47e-8a06f4fccfd2)


Next, in the terminal input this command:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/states/bbee73a7-2f71-47e6-938a-2d9e932d4ff9
```

This command retrieves a specific State object with the ID "bbee73a7-2f71-47e6-938a-2d9e932d4ff9" from the API.

![Screenshot 2024-03-18 172110](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/943d4a6f-ae5d-4cde-ad56-ce721c49b460)

In your browser:

```
http://localhost:5000/api/v1/states/bbee73a7-2f71-47e6-938a-2d9e932d4ff9
```

![Screenshot 2024-03-18 172323](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/fa91b52a-4d04-4765-a376-b9b035d637e2)

Next, in your terminal input this command:

```bash
curl -X POST http://0.0.0.0:5000/api/v1/states/ -H "Content-Type: application/json" -d '{"name": "California"}' -vvv
```

This command sends a **POST** request to create a new State object with the name "California" to the specified API endpoint. The request body is in JSON format, containing the name of the State. The -vvv flag is for verbose output, providing detailed information about the request and response.

![Screenshot 2024-03-18 172632](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/407f72c4-ac27-4dbc-9642-ee709521d547)

Next, in your terminal input this command:

```
curl -X PUT http://0.0.0.0:5000/api/v1/states/bbee73a7-2f71-47e6-938a-2d9e932d4ff9 -H "Content-Type: application/json" -d '{"name": "Mississippi is so cool"}'
```

This command is sending a **PUT** request to the endpoint http://0.0.0.0:5000/api/v1/states/bbee73a7-2f71-47e6-938a-2d9e932d4ff9 with the data {"name": "Mississippi is so cool"} in JSON format and specifying the header Content-Type: application/json. It's intended to update the name of the State object with the specified ID (bbee73a7-2f71-47e6-938a-2d9e932d4ff9) to "Mississippi is so cool".

![Screenshot 2024-03-18 173318](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/c71682f4-0bc5-4b61-be06-7238e6c6c240)

In your browser:

```bash
http://localhost:5000/api/v1/states/bbee73a7-2f71-47e6-938a-2d9e932d4ff9
```

![Screenshot 2024-03-18 173453](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/e51ff67a-b131-478c-9270-df9a8ef4c4a2)

Mississippi is so cool now!( And always, obvs!)

**Important Note about DELETE:
Currently, although the DELETE function for State exists, there are constraints related to the state_id column in the cities table. This constraint prevents the deletion of State objects if associated City objects still reference them. As a result, attempting to use the DELETE function for State while associated City objects still exist triggers an error. You must delete all associated Cities before deleting the State**

</ul> </li> </details>

<details>
<summary>
🌻🌻🌻Cities CRUD   </summary>
<ul>
  <li>

**Ensure the API server is still running**

Input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/states/not_an_id/cities/
```

The command curl -X GET http://0.0.0.0:5000/api/v1/states/not_an_id/cities/ sends a **GET** request to the specified URL, which is the endpoint for retrieving the list of cities associated with a particular state. However, in this case, the not_an_id part in the URL represents that the provided state_id is not a valid ID for any state object in the system. Therefore, the request will lresult in a 404 error indicating that the state with the provided ID was not found.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/c5d9fb34-6cf4-46b2-82d7-f5c521964363)

In your browser:

```bash
http://localhost:5000/api/v1/states/not_an_id/cities/
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/4752f391-a60a-4989-91b3-2f912010d86e)

Next, input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities
```

The command curl -X GET http://0.0.0.0:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities sends a **GET** request to the specified URL, which is the endpoint for retrieving the list of cities associated with the state identified by the UUID 2b9a4627-8a9e-4f32-a752-9a84fa7f4efd. This command fetches all cities that belong to the state with the provided ID.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/0a3203d7-c312-4745-9126-4af9366492ba)

In your browser:

```bash
http://localhost:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/4ece7f3f-2405-42cf-8873-3bb55d40eb3a)

Next, input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/cities/1da255c0-f023-4779-8134-2b1b40f87683
```

The command curl -X GET http://0.0.0.0:5000/api/v1/cities/1da255c0-f023-4779-8134-2b1b40f87683 sends a **GET** request to the specified URL, which is the endpoint for retrieving information about a specific city. The UUID 1da255c0-f023-4779-8134-2b1b40f87683 in the URL identifies the city whose information is being requested.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/907c843d-d311-4539-abe5-eeda86eeba58)

In your browser:

```bash
http://localhost:5000/api/v1/cities/1da255c0-f023-4779-8134-2b1b40f87683
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/fec5632a-c160-4b12-bc71-13de8082679f)

Next, input this command in your terminal:

```
curl -X POST http://0.0.0.0:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities -H "Content-Type: application/json" -d '{"name": "Alexandria"}' -vvv
```

This command CREATES city named "Alexandria" associated with the state identified by the UUID 2b9a4627-8a9e-4f32-a752-9a84fa7f4efd.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/38858ba6-5d7c-4f71-b737-1a16f8caa78e)

In your browser:

```bash
http://localhost:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/edb08564-223b-4e68-a8c2-310d45442d77)

Input this command in your terminal:

```bash
curl -X PUT http://0.0.0.0:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e -H "Content-Type: application/json" -d '{"name": "Bossier City"}'
```

The command curl -X PUT http://0.0.0.0:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e -H "Content-Type: application/json" -d '{"name": "Bossier City"}' sends an HTTP **PUT** request to update a City object with the ID 8b871e03-8103-40b0-b609-ad776960468e. It specifies that the data being sent is in JSON format and includes the new name "Bossier City" for the city being updated.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/9ed96d68-7dea-412d-8102-dcd5b26c0f9c)


Input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e
```

The command curl -X GET http://0.0.0.0:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e sends an HTTP GET request to retrieve information about the City object with the ID 8b871e03-8103-40b0-b609-ad776960468e from the specified API endpoint.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/04bb0e93-cc96-4839-bb38-47bade7b3b7c)

The response confirms that the City object's information has been updated, showing the new name "Bossier City" along with other details such as creation and update timestamps.

In your browser:

```bash
http://localhost:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e
```

![Screenshot 2024-03-18 194927](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/dba75d0e-0a6d-4b32-b97c-b13b0be89086)


Input this command in your terminal:

```bash
curl -X DELETE http://0.0.0.0:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e
```

This command sends an HTTP **DELETE** request to the specified endpoint http://0.0.0.0:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e, aiming to delete the City object with the ID 8b871e03-8103-40b0-b609-ad776960468e. It requests the server to remove the City resource associated with the provided ID. If successful, the server should respond with an appropriate confirmation or success message, indicating that the deletion was executed.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/b8cf1b58-4363-436d-b4d8-bfa9483b32dd)

Input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e
```

This command is used to verify whether the City with the ID 8b871e03-8103-40b0-b609-ad776960468e has been deleted. It sends an HTTP GET request to the specified endpoint http://0.0.0.0:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e to retrieve information about the City object. If the City has been successfully deleted, the server's response should indicate that the resource is not found.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/b81958c1-4ab6-40a9-b8a4-e01b39a10856)


In your browser:

```bash
http://localhost:5000/api/v1/cities/8b871e03-8103-40b0-b609-ad776960468e
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/48a14aa5-6f1f-4e29-9e20-a4fb3c5483ea)

</ul> </li> </details>

<details>
<summary>
🌻🌻🌻Amenities CRUD  </summary>
<ul>
  <li>

**Ensure the API server is still running**

Input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/amenities/
```

The command curl -X **GET** http://0.0.0.0:5000/api/v1/amenities/ fetches a list of all amenities from the specified API endpoint.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/36928225-9cad-4670-81ce-8d170125235c)

In your browser:

```bash
http://localhost:5000/api/v1/amenities/
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/b7706689-a244-4d25-831a-707e7d77443d)

Next, input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/amenities/017ec502-e84a-4a0f-92d6-d97e27bb6bdf
```

The command curl -X **GET** http://0.0.0.0:5000/api/v1/amenities/017ec502-e84a-4a0f-92d6-d97e27bb6bdf sends a GET request to the specified API endpoint, aiming to retrieve information about the amenity with the ID 017ec502-e84a-4a0f-92d6-d97e27bb6bdf.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/3eb73fa9-a8a0-4f17-97b1-f67d337df377)

In your browser:

```bash
http://localhost:5000/api/v1/amenities/017ec502-e84a-4a0f-92d6-d97e27bb6bdf
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/74768849-0279-4220-94db-8254e74289d4)

Next, input this command in your terminal:

```bash
curl -X POST http://0.0.0.0:5000/api/v1/amenities/ -H "Content-Type: application/json" -d '{"name": "Pugs"}' -vvv
```

This command is making a **POST** request to the endpoint http://0.0.0.0:5000/api/v1/amenities/ with the header Content-Type: application/json and the data {"name": "Pugs"} in JSON format. The -vvv flag is for verbose output, providing detailed information about the request and response. It is intended to create a new amenity with the name "Pugs" in the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/9ed081ac-aa46-4170-a1b3-c5f626974e04)

In your browser:

```bash
http://localhost:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/ff09942a-f74d-4d4a-8b92-3e7b984603ca)

Next, input this command in your terminal:

```bash
 curl -X PUT http://0.0.0.0:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a -H "Content-Type: application/json" -d '{"name": "Pugs are Love"}'
```

This command is sending a **PUT** request to the endpoint http://0.0.0.0:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a with the header Content-Type: application/json and the data {"name": "Pugs are Love"} in JSON format. It's intended to update the amenity with the ID a4efd896-0685-47d3-ab8b-daa06195951a to have the name "Pugs are Love" in the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/8efb23bb-fecf-4aea-9663-475e17ebd0d8)

Next, input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a
```

This command is sending a **GET** request to the endpoint http://0.0.0.0:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a. It is requesting information about the amenity with the ID a4efd896-0685-47d3-ab8b-daa06195951a from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/c1334449-52ab-40c8-bf37-24450e03b41f)


In your browser:

```bash
http://localhost:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/ba423bef-0d91-437f-9a03-90ff990f0967)


Next, input this command in your terminal:

```bash
curl -X DELETE http://0.0.0.0:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a
```

This command is sending a **DELETE** request to the endpoint http://0.0.0.0:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a. It is requesting the deletion of the amenity with the ID a4efd896-0685-47d3-ab8b-daa06195951a from the API.


Next, input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a
```

This command is being used to verify the deletion of an amenity. It sends a GET request to the endpoint http://0.0.0.0:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a to check whether the amenity with the ID a4efd896-0685-47d3-ab8b-daa06195951a has been successfully deleted from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/60008fe7-6617-4f14-b133-74e948401201)


In your browser:

```bash
http://localhost:5000/api/v1/amenities/a4efd896-0685-47d3-ab8b-daa06195951a
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/49498c76-ca8f-4ac9-9efb-3357f0f03cc6)


</ul> </li> </details>


<details>
<summary>
🌻🌻🌻Users CRUD  </summary>
<ul>
  <li>

**Ensure the API server is still running**

Input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/users/
```

This command is sending a **GET** request to the endpoint http://0.0.0.0:5000/api/v1/users/ to retrieve a list of all users from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/68a47151-70ba-4656-bf18-bf3187279cb3)


In your browser:

```bash
http://localhost:5000/api/v1/users/
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/a0973b6b-1ad7-4dca-b3c2-b9960c94a7db)

Next, input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/users/00a11245-12fa-436e-9ccc-967417f8c30a
```

This command is sending a **GET** request to the endpoint http://0.0.0.0:5000/api/v1/users/00a11245-12fa-436e-9ccc-967417f8c30a to retrieve information about a specific user identified by the UUID 00a11245-12fa-436e-9ccc-967417f8c30a.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/626db054-cbdb-45c5-85ff-c513a2531668)

In your browser:

```bash
http://localhost:5000/api/v1/users/00a11245-12fa-436e-9ccc-967417f8c30a
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/1116d966-2090-4d35-924e-d185b4bdcb14)

Next, in your terminal input this command:

```bash
curl -X POST http://0.0.0.0:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"first_name": "Puggy", "last_name": "Wuggy", "email": "puggy@pugsruletheworld.com", "password": "pugsnotdrugs"}' -vvv
```

This command is making a **POST** request to http://0.0.0.0:5000/api/v1/users/ to create a new user. It includes user data such as first name, last name, email, and password in JSON format. The server's response will be displayed with verbose output (-vvv).

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/e08b27d5-34d7-4f98-a5d3-dbab42b222d6)


In your browser:

```bash
http://localhost:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/7778558a-0cb9-43cf-add6-a9ab9948d57a)


Next, input this command in the terminal:

```bash
curl -X PUT http://0.0.0.0:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103 -H "Content-Type: application/json" -d '{"first_name": "Puggie", "last_name": "Wuggie", "email": "puggie@pugsruletheworld.com", "password": "puggiessnotdrugs"}' -vvv
```

This command is sending a **PUT** request to update the user data associated with the ID 250ef043-9742-4308-abc1-02726675b103 at http://0.0.0.0:5000/api/v1/users/. It includes updated user information such as first name, last name, email, and password in JSON format, and verbose output (-vvv) is enabled to display detailed information about the request and response.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/77575556-4c8a-4c71-975b-02499ec158d5)

Next, input this command in the terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103
```

This command is sending an HTTP **GET** request to the specified endpoint http://0.0.0.0:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103 to retrieve information about the user with the ID "250ef043-9742-4308-abc1-02726675b103" from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/50eca386-0dc9-49fe-8ddb-4a100900f41f)


In your browser:

```bash
http://localhost:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103
```
![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/3558246e-ea46-4007-8b94-e5b6afa98641)

You can see on the terminal and browser that the user's first name, last name, and password have been updated.

Next, input this command in the terminal:

```bash
curl -X DELETE http://0.0.0.0:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103
```

This command is sending an HTTP DELETE request to the specified endpoint http://0.0.0.0:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103, aiming to delete the user with the ID "250ef043-9742-4308-abc1-02726675b103" from the API.

Then, input this command:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103
```

This command is sending an HTTP GET request to the specified endpoint http://0.0.0.0:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103 to verify whether the user with the ID "250ef043-9742-4308-abc1-02726675b103" has been deleted.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/2911e59f-43b7-457b-9bae-404148825d05)

In your browser:

```bash
http://localhost:5000/api/v1/users/250ef043-9742-4308-abc1-02726675b103
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/96f9fe40-9de8-4f8e-a694-1664f377fe8b)



</ul> </li> </details>




<details>
<summary>
🌻🌻🌻Places CRUD  </summary>
<ul>
  <li>

**Ensure the API server is still running**

Input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/cities/45903748-fa39-4cd0-8a0b-c62bfe471702/places
```

This command is sending an HTTP **GET** request to the specified endpoint http://0.0.0.0:5000/api/v1/cities/45903748-fa39-4cd0-8a0b-c62bfe471702/places. It retrieves a list of places associated with the city having the ID "45903748-fa39-4cd0-8a0b-c62bfe471702" from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/6194c9fa-b10b-4856-97b7-f223741392f6)

In your browser:

```bash
http://localhost:5000/api/v1/cities/45903748-fa39-4cd0-8a0b-c62bfe471702/places
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/0621e897-9ec0-47f7-91c7-bfca4d6c851c)

In your terminal input this command:

```
curl -X GET http://0.0.0.0:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288
```

This command sends an HTTP **GET** request to the specified endpoint http://0.0.0.0:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288. It retrieves information about a specific place identified by the UUID "0b96262f-2c72-464c-a182-8f58afde4288" from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/171ce22c-5e90-4aa6-9424-acbd8c41d6fc)

In your browser:

```bash
http://localhost:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/45db6287-0344-4b07-92fd-98a0e6f7e1af)

In your terminal input this command:

```bash
curl -X POST http://0.0.0.0:5000/api/v1/cities/45903748-fa39-4cd0-8a0b-c62bfe471702/places -H "Content-Type: application/json" -d '{"user_id": "b6160096-c503-4909-a674-7bfbddc8cc45", "name": "Puglandia"}'
```

This command sends an HTTP **POST** request to the specified endpoint http://0.0.0.0:5000/api/v1/cities/45903748-fa39-4cd0-8a0b-c62bfe471702/places. It is creating a new Place object associated with the City identified by the UUID 45903748-fa39-4cd0-8a0b-c62bfe471702. The request body contains JSON data specifying the user_id and name attributes of the new Place.


![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/6fe9e5c1-15da-45c2-ad6d-933dffc33f76)

In your browser: 

```bash
http://localhost:5000/api/v1/cities/45903748-fa39-4cd0-8a0b-c62bfe471702/places
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/d3242b51-8a71-41a6-b4cd-bffb7a26a555)


In your terminal input this command:

```bash
 curl -X PUT http://0.0.0.0:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288 -H "Content-Type: application/json" -d '{"name": "Pug Palace"}'
```

This command sends an HTTP **PUT** request to the specified endpoint http://0.0.0.0:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288. It is updating the attributes of the Place object identified by the UUID 0b96262f-2c72-464c-a182-8f58afde4288. The request body contains JSON data specifying the updated value for the name attribute of the Place, which is being changed to "Pug Palace".

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/1cab5339-bdc1-4a7f-9087-301301e9a004)


In your browser:

```bash
http://localhost:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/5fee315e-34a9-4179-8936-5dc6cc14883c)


**Important Note about DELETE: Similar to the constraints observed with State and City associations, where the state_id column in the cities table prevents State deletion if associated Cities exist, constraints exist for Place and Review relationships.
In this case, a constraint is imposed on the place_id column in the reviews table, disallowing Place deletion if associated Reviews are present. Consequently, attempting to delete a Place with associated Reviews will result in errors. To resolve this, all associated Reviews must be deleted before a Place can be removed.**

</ul> </li> </details>


<details>
<summary>
🌻🌻🌻Reviews CRUD   </summary>
<ul>
  <li>

**Ensure the API server is still running**

Input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288/reviews
```

This command sends an HTTP **GET** request to the specified endpoint http://0.0.0.0:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288/reviews. It retrieves a list of reviews associated with the place identified by the UUID 0b96262f-2c72-464c-a182-8f58afde4288 from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/79db45e7-032a-40ae-a556-91d6e5d36e78)

In your browser:

```bash
http://localhost:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288/reviews
```

![Screenshot 2024-03-19 153123](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/c7a823e4-8a0b-4a34-b31e-724148f80ff8)

Next, input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/reviews/06af6da4-137d-4a3b-bc3e-0ae33d687b47
```

This command sends an HTTP GET request to the specified endpoint http://0.0.0.0:5000/api/v1/reviews/06af6da4-137d-4a3b-bc3e-0ae33d687b47. It retrieves information about a specific review identified by the UUID 06af6da4-137d-4a3b-bc3e-0ae33d687b47 from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/a4154b0b-8f1c-4a10-b7d4-5cb55a945117)

In your browser:

```bash
http://localhost:5000/api/v1/reviews/06af6da4-137d-4a3b-bc3e-0ae33d687b47
```

![Screenshot 2024-03-19 154009](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/4f7ef6e6-e900-4c36-83ab-1b70a42262fd)

In your terminal input this command:

```bash
curl -X DELETE http://0.0.0.0:5000/api/v1/reviews/06af6da4-137d-4a3b-bc3e-0ae33d687b47
```

This command sends an HTTP DELETE request to the specified endpoint http://0.0.0.0:5000/api/v1/reviews/06af6da4-137d-4a3b-bc3e-0ae33d687b47. It deletes the review associated with the UUID 06af6da4-137d-4a3b-bc3e-0ae33d687b47 from the API.

Input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/reviews/06af6da4-137d-4a3b-bc3e-0ae33d687b47
```

This command sends an HTTP GET request to the specified endpoint http://0.0.0.0:5000/api/v1/reviews/06af6da4-137d-4a3b-bc3e-0ae33d687b47 to verify the deletion of the review associated with the UUID 06af6da4-137d-4a3b-bc3e-0ae33d687b47 from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/439cc436-3dd6-4c61-81b1-52e718a4747f)


In your browser:

```bash
http://localhost:5000/api/v1/reviews/06af6da4-137d-4a3b-bc3e-0ae33d687b47
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/1a3f5594-27ce-4062-b3ed-277b04aceb47)


Next, in your terminal input this command:

```bash
 curl -X POST http://0.0.0.0:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288/reviews -H "Content-Type: application/json" -d '{"user_id": "00a11245-12fa-436e-9ccc-967417f8c30a", "text": "Not enough pugs!"}'
```

This command is sending an HTTP **POST** request to create a new review for the place with the ID 0b96262f-2c72-464c-a182-8f58afde4288. The request includes JSON data in the request body specifying the user_id as "00a11245-12fa-436e-9ccc-967417f8c30a" and the text of the review as "Not enough pugs!". The -H "Content-Type: application/json" header indicates that the content being sent is in JSON format.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/d743e10b-0aba-4f6c-b228-338cec825927)

In your browser:

```bash
http://localhost:5000/api/v1/places/0b96262f-2c72-464c-a182-8f58afde4288/reviews
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/1ca573d3-a17e-4501-91d1-de83b2c1394b)

Next, input this command in your terminal:

```bash
curl -X GET http://0.0.0.0:5000/api/v1/reviews/38d44b1a-6872-4c55-8332-38f88cbadc41
```

This command is sending an HTTP **GET** request to the specified endpoint http://0.0.0.0:5000/api/v1/reviews/38d44b1a-6872-4c55-8332-38f88cbadc41. It is retrieving information about a specific review identified by the UUID 38d44b1a-6872-4c55-8332-38f88cbadc41 from the API.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/c923d32b-114c-45cc-b3b4-c29697930d13)


In your browser:

```bash
http://localhost:5000/api/v1/reviews/38d44b1a-6872-4c55-8332-38f88cbadc41
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/a464e169-036a-4a86-9f8b-99ed6e73b646)


Next, input this command in your terminal:

```bash
curl -X PUT http://0.0.0.0:5000/api/v1/reviews/38d44b1a-6872-4c55-8332-38f88cbadc41 \ 
-H "Content-Type: application/json" \
-d '{"text": "We were promised pugs. No pugs in sight"}'
```

This command sends a **PUT** request to update the review with the ID 38d44b1a-6872-4c55-8332-38f88cbadc41 by changing its text to "We were promised pugs. No pugs in sight". It specifies the request's content type as JSON and includes the updated review text in the request body.

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/7c431f32-0da4-41bd-8b79-672425bf38f1)

In your browser:

```bash
http://localhost:5000/api/v1/reviews/38d44b1a-6872-4c55-8332-38f88cbadc41
```

![image](https://github.com/ThatsVie/atlas-AirBnB_clone_v3/assets/143755961/f002d1a0-69ab-4626-9a3d-b0e5b195c2a8)


</ul> </li> </details>

💻
## Authors:
Vie Paula - [Github](https://github.com/ThatsVie)

Ryan Donaldson - [Github](https://github.com/donaldrs01)
