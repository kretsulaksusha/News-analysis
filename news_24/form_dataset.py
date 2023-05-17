"""
Forming dataset from politics.json.
"""
import json
import re
from datetime import datetime


def find_string(pattern: str, string: str, data_type: str = None):
    """
    Scan through string looking for a match to the pattern.

    Parameters
    ----------
    pattern : str
        regex pattern
    string : str
        string that will be scanned
    data_type : str
        url or date

    Returns
    -------
    str
        matching substring
    """
    if not isinstance(pattern, str) or not isinstance(string, str):
        raise TypeError('invalid type, str expected')

    try:
        result = re.search(pattern, string).group(1)
    except AttributeError:
        result = None

    if data_type == 'url' and result:
        # forming url
        return "https://www.news24.com" + result

    if data_type == 'date' and not re.fullmatch(r"^\d{1,2} \w* \d{4}$", result):
        # adding year to the date
        result = result + ' ' + str(datetime.now().year)

    return result


def forming_dataset():
    """
    Return an object that produces a sequence of dict objects with information about news articles.
    Information: title, date, url.
    """
    with open('politics.json', 'r', encoding='utf-8') as file:
        data = json.load(file)['htmlContent']
        art_pat = re.compile(r"<div class=\"article-item--container\">(.*?)</p>.*?</span>.*?</div>",
                             re.DOTALL)
        all_articles = re.findall(art_pat, data)

        # patterns for different types of information
        title_pat = r'<div class=\"article-item__title\">\n *<span>\s*([^\n]*)\n *</span>\n *</div>'
        date_pat = r"<p class=\"article-item__date\">(.*)"
        url_pat = r"<a href=\"([^\n ]*)\" class=\"article-item--url (live)?\""

        # retrieving information from every article
        for article in all_articles:
            yield {
                'title': find_string(title_pat, article),
                'date': find_string(date_pat, article, 'date'),
                'url': find_string(url_pat, article, 'url')
            }

if __name__ == "__main__":
    with open('news_24_dataset.json', 'w', encoding='utf-8') as dataset_file:
        json.dump(list(forming_dataset()), dataset_file, indent=4)
