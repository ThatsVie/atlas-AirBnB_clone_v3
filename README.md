# AirBnB Clone 

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

## Web Static

The `web_static` folder serves as a repository for static assets such as HTML, CSS, and images. It organizes the front-end resources used to create and style the web pages in the project. These assets are served to users directly by the web server without any processing, enhancing the performance and scalability of the web application.

To view a README file for the Atlas AirBnb Clone `web_static` folder, please visit [this link](https://github.com/ThatsVie/atlas-AirBnB_clone/blob/main/web_static/README.md).

## Web Flask/ Web Framewok

This project implements a web framework for an AirBnB clone using Flask, a lightweight WSGI web application framework. It includes various tasks that demonstrate the functionality of the web application, such as displaying different routes, rendering HTML templates, and interacting with a database.

To view a README file for the Atlas AirBnb Clone `web_flask` folder, please visit [this link](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/blob/master/web_flask/README.md).

## AirBnB Clone v3 API

This repository was originally forked from this [codebase](https://github.com/alexaorrico/AirBnB_clone_v2) It was built upon to provide endpoints to interact with various resources such as states, cities, users, places, reviews, and amenities.

### Storage Enhancement: DBStorage and FileStorage

The DBStorage and FileStorage modules have been updated in the storage_get_count branch to include two new methods:

**get(cls, id):** Retrieves an object based on the class and its ID, or returns None if not found.

**count(cls=None):** Returns the number of objects in storage matching the given class. If no class is passed, returns the count of all objects in storage.

New tests have been added to ensure the functionality of these methods.

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

### Cross-Origin Resource Sharing (CORS)
The API is configured to allow cross-origin requests from any origin (0.0.0.0) using the flask_cors module. This setup ensures that web clients can access the API data without encountering CORS-related issues.

### Installation

**Clone the repository:**
```bash
git clone https://github.com/ThatsVie/atlas-AirBnB_clone_v3.git
```
**Navigate to the project directort**
```bash
cd atlas-AirBnB_clone_v3
```
**Install the flask_cors module:**
```bash
pip3 install flask_cors
```

### Usage
Running the API Locally
To run the API locally, execute the following command:
```bash
(working on this)
```
The API will be available at http://0.0.0.0:5000/



## Authors:
Vie Paula - [Github](https://github.com/ThatsVie)

Ryan Donaldson - [Github](https://github.com/donaldrs01)
