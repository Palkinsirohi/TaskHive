from flask import Flask, render_template, request, redirect, url_for
import quotes
import weather
import news
import todo

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/news')
def news_page():
    headlines = news.fetch_api_news()
    return render_template('news.html', headlines=headlines)

@app.route('/weather', methods=['GET', 'POST'])
def weather_page():
    city = request.form.get('city', 'London') if request.method == 'POST' else 'London'
    weather_info = weather.get_weather(city)
    return render_template('weather.html', weather=weather_info, city=city)

@app.route('/quote')
def quote_page():
    quote, author = quotes.get_quote()
    return render_template('quote.html', quote=quote, author=author)

@app.route('/todo', methods=['GET', 'POST'])
def todo_page():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            task = request.form.get('task')
            status = request.form.get('status', 'todo')
            todo.add_task(task, status)
        elif action == 'update':
            task_id = request.form.get('task_id')
            task = request.form.get('task')
            status = request.form.get('status')
            todo.update_task(task_id, task, status)
        elif action == 'delete':
            task_id = request.form.get('task_id')
            todo.delete_task(task_id)
        return redirect(url_for('todo_page'))
    tasks = todo.get_tasks()
    return render_template('todo.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
