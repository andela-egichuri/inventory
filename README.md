## Inventory

 - Add book categories
 - Add books to inventory
 - Search for books by title

### Local Application Setup:

* Download or clone the repo
* Install requirements.
`pip install -r requirements.txt`
* Setup environment variables
```
DATABASE_URL="postgres://<user>:<password>@localhost:5432/<db_name>"
SECRET=<SECRET>
APP_SETTINGS="inventory.settings.dev" (inventory.settings.dev for production)
```
* Perform database migrations.
```
python manage.py makemigrations
python manage.py migrate
```
### Running the application
`python manage.py runserver`


### Running Tests
Tests are run from the root folder
`python manage.py test`

To show Coverage results
`coverage report -m`