import requests
import re
import logging
log = logging.getLogger(__name__)

def crawl(start, end):
    for i in range(start, end):
        try:
            url = f'https://gram.dins.ru/action.php?id={i}&part=e&download'
            r = requests.get(url, stream=True)
            if r.status_code != 200:
                log.info(f'{url} {r.status_code}')
                continue
            file_name = re.findall('filename="(.+)"', r.headers['content-disposition'])[0]
            log.info(f'{url} {r.status_code} {file_name}')
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
        except Exception as e:
            log.exception(f'Get exception for {url}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    crawl(6539, 10000)
