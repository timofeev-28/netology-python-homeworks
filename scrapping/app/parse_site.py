import sys
import requests
import bs4
from app.data import KEYWORDS
from app.utils import get_article, get_headers


def parse_site(url: str) -> None:
    """
    collects data from the site page, selects articles by keywords,
    and outputs the date, title, and link to the article to the console.
    """
    print("Происходит загрузка и обработка данных...")

    with requests.Session() as session:
        headers = get_headers()
        try:
            response = session.get(url, headers=headers, timeout=10)
            soup = bs4.BeautifulSoup(response.text, features="lxml")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")
            sys.exit(1)

        articles = soup.select("article.tm-articles-list__item")
        if not articles:
            print(
                "Информация не найдена, проверьте искомую страницу на изменения"
            )
            sys.exit(1)

        parsed_data = []
        for article in articles:
            # == title ==
            title_elem = article.select_one("a.tm-title__link")
            title = title_elem.text.strip() if title_elem else ""

            # == link ==
            href = (
                title_elem["href"]
                if title_elem and "href" in title_elem.attrs
                else ""
            )
            link = "https://habr.com" + href  # type: ignore

            # == date ==
            date_elem = article.select_one("time")
            date_title = date_elem["title"] if date_elem else None
            if date_title:
                date = date_title
            else:
                date = "Дата публикации неизвестна"

            # == text ==
            text = get_article(link, article, session)

            # == search text ==
            search_text = f"{title} {text}".lower()

            # == check ==
            if any(keyword.lower() in search_text for keyword in KEYWORDS):
                parsed_data.append((date, title, link))

    if parsed_data:
        words = ", ".join(KEYWORDS)
        print(
            f"По ключевым словам {words} найдено статей:  {len(parsed_data)}"
        )
        for date, title, link in parsed_data:
            print(f"{date} – {title} – {link}")
    else:
        print("Статей по ключевым словам не найдено.")
