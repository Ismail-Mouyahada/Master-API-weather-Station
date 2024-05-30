# Weather Station API

This project is a weather station application that uses a Flask backend to manage data related to temperature, humidity, and sensors, and a MySQL database to store the data. The API provides endpoints to add, read, update, and delete records in the database.

## Features

- **Add Data**: Insert new records into the database.
- **Fetch Data**: Retrieve all records or specific records by ID.
- **Update Data**: Modify existing records.
- **Delete Data**: Remove records from the database.
- **Error Handling**: Return appropriate error messages for invalid requests.

## Prerequisites

- Python 3.x
- Flask
- Flask-MySQL
- PyMySQL

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ismail-Mouyahada/Master-csharp-vuejs-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Master-csharp-vuejs-app
   ```

3. Set up a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure the MySQL database connection in `config.py`:

   ```python
   MYSQL_DATABASE_USER = 'your_mysql_username'
   MYSQL_DATABASE_PASSWORD = 'your_mysql_password'
   MYSQL_DATABASE_DB = 'your_database_name'
   MYSQL_DATABASE_HOST = 'localhost'
   ```

## Running the Application

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. The API will be available at `http://192.168.43.60:5000`.

## API Endpoints

### Add Data

- **Endpoint**: `/api/v1/ajouter/`
- **Method**: `POST`
- **Description**: Add a new record to the `donnees` table.
- **Request Body**:
  ```json
  {
    "farenheit": "value",
    "temperature": "value",
    "humidite": "value",
    "capture": "value"
  }
  ```
- **Response**:
  ```json
  {
    "message": "les données ont été enregistrées avec succès !"
  }
  ```

### Fetch All Data

- **Endpoint**: `/api/v1/donnees/`
- **Method**: `GET`
- **Description**: Retrieve all records from the `donnees` table.
- **Response**: Array of records.

### Fetch Data by ID (Humidity)

- **Endpoint**: `/api/v1/donnees/humidite/<int:id>`
- **Method**: `GET`
- **Description**: Retrieve a specific record by ID from the `donnees` table.
- **Response**: Record details.

### Fetch Data by ID (Temperature)

- **Endpoint**: `/api/v1/donnees/temperature/<int:id>`
- **Method**: `GET`
- **Description**: Retrieve a specific record by ID from the `donnees` table.
- **Response**: Record details.

### Update Data

- **Endpoint**: `/api/v1/modifier/`
- **Method**: `PUT`
- **Description**: Update an existing record in the `donnees` table.
- **Request Body**:
  ```json
  {
    "id": "value",
    "farenheit": "value",
    "temperature": "value",
    "humidite": "value",
    "date": "value",
    "capture": "value"
  }
  ```
- **Response**:
  ```json
  {
    "message": "les données ont été modifié avec succès"
  }
  ```

### Delete Data

- **Endpoint**: `/api/v1/supprimer/<int:id>`
- **Method**: `DELETE`
- **Description**: Delete a record from the `donnees` table by ID.
- **Response**:
  ```json
  {
    "message": "Données ont été supprimées avec succès!"
  }
  ```

## Error Handling

- **404 Error**:
  - **Description**: Returns a message when a requested resource is not found.
  - **Response**:
    ```json
    {
      "status": 404,
      "message": "Enregistrement introuvable mais l'api marche : <requested_url>"
    }
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any inquiries or feedback, please contact Ismail Mouyahada at [your-email@example.com](mailto:your-email@example.com).
 
