# FastAPI Example Application

This is an example FastAPI application that demonstrates basic CRUD operations with unit tests and CI/CD using GitHub Actions.

## Endpoints

- `POST /items/`: Create a new item.
- `GET /items/`: Retrieve all items.
- `GET /items/{item_id}`: Retrieve an item by ID.
- `PUT /items/{item_id}`: Update an existing item by ID.
- `DELETE /items/{item_id}`: Delete an item by ID.

## Running the Application

To run the application locally:

```bash
uvicorn app.main:app --reload
