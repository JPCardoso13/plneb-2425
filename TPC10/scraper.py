import json
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://revista.spmi.pt/index.php/rpmi/issue/archive"
NUM_ARCHIVES = 6


def get_html_content(url):
    html_content = requests.get(url).text

    if html_content:
        print(f"Fetched HTML content from {url}")
    else:
        print(f"Failed to fetch HTML content from {url}")

    return html_content


def fetch_article_data(url):
    html_content = get_html_content(url)
    soup = BeautifulSoup(html_content, "html.parser")
    article_data = {"URL": url}

    # Título
    article_data["titulo"] = soup.find("h1", class_="page_title").text.strip().replace("  ", " ")

    # Título traduzido
    subtitle = soup.find("h2", class_="subtitle")
    if subtitle:
        article_data["titulo_pt"] = subtitle.text.strip().replace("  ", " ")

    # Data de publicação
    article_data["data_publicacao"] = (soup.find("div", class_="item published").
                                       find("div", class_="value").text.strip().replace("  ", " "))

    # Autores
    author_list = soup.find("ul", class_="authors")
    author_values = []
    for li in author_list.find_all("li"):
        author_info = {}
        author_info["nome"] = li.find("span", class_="name").text.strip().replace("  ", " ")

        affiliation = li.find("span", class_="affiliation")
        if affiliation:
            author_info["afiliacao"] = affiliation.text.strip().replace("  ", " ")

        orcid = li.find("span", class_="orcid")
        if orcid:
            author_info["orcid"] = orcid.text.strip().replace("  ", " ")

        author_values.append(author_info)

    article_data["autores"] = author_values

    # DOI
    doi_section = soup.find("section", class_="item doi")
    if doi_section:
        article_data["DOI"] = doi_section.a.text.strip().replace("  ", " ")

    # Keywords
    kwd_section = soup.find("section", class_="item keywords")
    if kwd_section:
        article_data["keywords"] = [kwd.strip().replace("  ", " ") for kwd in kwd_section.span.text.split(",")]

    # Abstract
    abstract_section = soup.find("section", class_="item abstract")
    if abstract_section:
        abstract_data = []
        for p in abstract_section.find_all("p"):
            abstract_data.append(p.text.strip().replace("  ", " "))
        article_data["abstract"] = abstract_data

    return article_data


def fetch_newsletter_data(url):
    articles = []

    html_content = get_html_content(url)
    soup = BeautifulSoup(html_content, "html.parser")

    main_content = soup.find("div", class_="sections")
    for h3 in main_content.find_all("h3"):
        article_url = h3.a["href"]
        articles.append(fetch_article_data(article_url))

    pub_date_div = soup.find("div", class_="published")
    pub_date = pub_date_div.find("span", class_="value").text.strip()

    return {
        "URL": url,
        "data_publicacao": pub_date,
        "artigos": articles,
    }


def fetch_archive_data(soup):
    archive_data = {}

    for list_item in soup.find_all("li"):
        title = list_item.h2.a.text.strip()
        sub_title_div = list_item.h2.div
        url = list_item.h2.a["href"]

        if sub_title_div:
            title += (" - " + sub_title_div.text.strip())

        archive_data[title] = fetch_newsletter_data(url)

    return archive_data


def scrape_data(num_archives=NUM_ARCHIVES):
    scraped_data = {}

    for i in range(1, num_archives + 1):
        url = f"{BASE_URL}/{i}"
        html_content = get_html_content(url)
        soup = BeautifulSoup(html_content, "html.parser")

        content_div = soup.find("ul", class_="issues_archive")
        scraped_data.update(fetch_archive_data(content_div))

    return scraped_data


if __name__ == "__main__":
    data = scrape_data()
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
