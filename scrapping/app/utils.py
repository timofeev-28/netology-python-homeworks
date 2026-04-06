from typing import Dict
import requests
import bs4
from bs4 import Tag
from fake_headers import Headers


def get_headers() -> Dict[str, str]:
    """return headers for requests"""
    return Headers(browser="chrome", os="win").generate()


def get_article(url: str, article: Tag, session: requests.Session) -> str:
    """retrieves the article and returns its text or returns the preview text"""
    headers = get_headers()
    try:
        response = session.get(url, headers=headers, timeout=10)
        article_soup = bs4.BeautifulSoup(response.text, features="lxml")
        if article_soup:
            preview_text = article_soup.select_one(
                "article.tm-article-presenter__content"
            )
            return preview_text.text.strip() if preview_text else ""
        return ""
    except Exception as e:
        print(f"Ошибка при загрузке статьи: {e}, ищем совпадения по превью")
        preview_text = article.select_one("div.article-formatted-body")
        return preview_text.text.strip() if preview_text else ""
