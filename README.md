# TaskHive Flask Web Application

TaskHive is a Flask-based web application that provides multiple useful features including news headlines, weather information, inspirational quotes, and a todo list manager. The app integrates with external APIs for news, weather, and quotes, and uses a local SQLite database for managing todo tasks.

## Features

- **Home Page**: A landing page for the app.
- **News**: Displays top news headlines fetched from the BBC News source using the NewsAPI.
- **Weather**: Shows current weather information for a specified city using the WeatherAPI.
- **Quotes**: Displays a random inspirational quote fetched from multiple quote APIs with a local fallback.
- **Todo List**: A simple todo list manager backed by a SQLite database, supporting adding, updating, and deleting tasks with status tracking.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone <repository-url>
cd TaskHive
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install the following packages manually:

```bash
pip install flask requests aiohttp python-dotenv rich
```

### API Keys Configuration

The app requires API keys for the NewsAPI and WeatherAPI.

1. **NewsAPI Key**  
   The NewsAPI key is currently hardcoded in `news.py`. You can replace the existing key with your own key from [https://newsapi.org](https://newsapi.org).

2. **WeatherAPI Key**  
   The WeatherAPI key should be stored in an environment variable named `WEATHER_API_KEY`.  
   - Get a free API key from [https://www.weatherapi.com/](https://www.weatherapi.com/).  
   - Create a `.env` file in the project root with the following content:  
     ```
     WEATHER_API_KEY=your_api_key_here
     ```

### Database

The todo list uses a SQLite database file `todos.db` which will be created automatically when you run the app.

## Running the Application

Run the Flask app using:

```bash
python app.py
```

The app will be accessible at `http://localhost:5000/`.

## Project Structure

```
TaskHive/
│
├── app.py              # Main Flask application
├── news.py             # News fetching module
├── weather.py          # Weather fetching module
├── quotes.py           # Quotes fetching module
├── todo.py             # Todo list management module
├── todos.db            # SQLite database for todo tasks
├── templates/          # HTML templates for the web pages
│   ├── home.html
│   ├── news.html
│   ├── quote.html
│   ├── todo.html
│   └── weather.html
└── README.md           # This file
```

## Notes

- The app runs in debug mode by default.
- The news feature fetches top headlines from BBC News.
- The quotes feature tries multiple APIs and falls back to local quotes if all fail.
- The todo list supports task statuses: todo, doing, done.

## License

This project is open source and free to use.
