# FastAPI CRUD Example

A simple REST API developed with **FastAPI** that demonstrates basic CRUD (Create, Read, Update, Delete) operations using an in-memory Python list. This project is designed for learning REST API development and FastAPI fundamentals.

## Features

- Get all items
- Get an item by index
- Add new items
- Update items by value
- Update items by index
- Delete items by value
- Delete items by index
- Get the last item
- Reverse the list
- Simple RESTful API design

## Technologies

- Python
- FastAPI
- FastAPI Offline

## Project Structure

```
fastapi-crud-example/
├── main.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/fastapi-crud-example.git
```

Go to the project directory:

```bash
cd fastapi-crud-example
```

Install dependencies:

```bash
pip install fastapi fastapi-offline uvicorn
```

Run the server:

```bash
uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/home` | Welcome endpoint |
| GET | `/getItem/` | Get all items |
| GET | `/get_item/{index}` | Get item by index |
| GET | `/lastItem` | Get last item |
| GET | `/reverse_list` | Reverse the list |
| POST | `/item/{new_item}` | Add a new item |
| PUT | `/update_item/` | Update item by value |
| PUT | `/update_item_byindex/` | Update item by index |
| DELETE | `/delete_item/` | Delete item by value |
| DELETE | `/delete_index/` | Delete item by index |

## Example

Initial list:

```python
[10, 20, 30, 40]
```

After adding a new item:

```python
POST /item/50
```

Result:

```python
[10, 20, 30, 40, 50]
```

## Learning Objectives

- REST API fundamentals
- CRUD operations
- HTTP methods
- Path parameters
- Query parameters
- FastAPI routing
- Python list manipulation

## Future Improvements

- SQLite database support
- SQLAlchemy ORM
- Pydantic models
- Request validation
- Error handling
- Swagger documentation
- User authentication
- Docker support

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

---

If you found this project useful, consider giving it a ⭐ on GitHub.
