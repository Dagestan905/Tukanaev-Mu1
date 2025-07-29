from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang=\"ru\">
<head>
    <meta charset=\"UTF-8\">
    <title>Туканаев | Манчестер Юнайтед</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #e6e6e6;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #da291c;
            color: white;
            padding: 20px;
            text-align: center;
        }
        nav {
            background: #b22222;
            padding: 10px;
            text-align: center;
        }
        nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }
        main {
            padding: 30px;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 15px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Туканаев | Манчестер Юнайтед</h1>
    </header>
    <nav>
        <a href="#home">Главная</a>
        <a href="#matches">Расписание</a>
        <a href="#players">Игроки</a>
        <a href="#catalog">Каталог</a>
    </nav>
    <main>
        <div class=\"card\" id=\"home\">
            <h2>Добро пожаловать на фан-сайт Манчестер Юнайтед!</h2>
            <p>Здесь вы найдете последние новости, фотографии и интересные факты о легендарном футбольном клубе Манчестер Юнайтед.</p>
            <img src=\"https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg\" alt=\"Manchester United Logo\">
        </div>
        <div class=\"card\" id=\"matches\">
            <h2>Расписание матчей</h2>
            <ul>
                <li>21 июля: Манчестер Юнайтед vs Ливерпуль</li>
                <li>28 июля: Манчестер Юнайтед vs Манчестер Сити</li>
                <li>4 августа: Манчестер Юнайтед vs Арсенал</li>
            </ul>
        </div>
        <div class=\"card\" id=\"players\">
            <h2>Галерея игроков</h2>
            <div class=\"gallery\">
                <img src=\"https://upload.wikimedia.org/wikipedia/commons/8/87/Cristiano_Ronaldo_2018.jpg\" alt=\"Cristiano Ronaldo\">
                <img src=\"https://upload.wikimedia.org/wikipedia/commons/7/74/Marcus_Rashford_2018.jpg\" alt=\"Marcus Rashford\">
                <img src=\"https://upload.wikimedia.org/wikipedia/commons/b/b7/Bruno_Fernandes_2021.jpg\" alt=\"Bruno Fernandes\">
            </div>
        </div>
        <div class=\"card\" id=\"catalog\">
            <h2>Каталог товаров</h2>
            <ul>
                <li>Футболка с логотипом МЮ — 2990₽</li>
                <li>Шарф болельщика — 1490₽</li>
                <li>Кружка с эмблемой — 890₽</li>
            </ul>
        </div>
    </main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)

