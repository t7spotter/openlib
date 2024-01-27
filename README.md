# Open Library Flask API

This Flask application interacts with the Open Library API to retrieve information about books, authors, and works.

## Getting Started

### Prerequisites

- Python 3.x
- [Pip](https://pip.pypa.io/en/stable/installation/)
- (Optional) Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/t7spotter/openlib.git

2. Run it with Docker! (expose 5000 to appropriate Port)
3. The application will be accessible at http://127.0.0.1:5000/ (At the port that you chose.)

## API Endpoints

- **/ok**: If everything is okay it returns ypu "hello world!"

- **/title/<title>**: Fetches information about books based on the provided title.

- **/author/<author_id>**: Retrieves details about an author using the provided author ID.

- **/works/<path:next>**: Retrieves information about works based on the provided path and offset.

- **/authorworks/<author_id>**: Fetches information about works authored by a specific author identified by the provided author ID.

- **/isbn/<isbn>**: Fetches details about a book using the provided ISBN.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
