import requests

from bs4 import BeautifulSoup


def get_net_salaries(salaries):
    """Takes the list of gross salaries and for each one
    fetches data (net salary) from a defined URL"""
    net_salaries = []
    url = 'https://zarobki.pracuj.pl/kalkulator-wynagrodzen/'
    try:
        for salary in salaries:
            try:
                html = requests.get(url=f'{url}{salary}-brutto').text
            except requests.exceptions.RequestException as exception:
                print('Sprawdź połączenie z siecią')
                raise SystemExit from exception

            soup = BeautifulSoup(html, features='html.parser')

            for script in soup(["script", "style"]):
                script.decompose()

            strips = list(soup.stripped_strings)
            for i, _ in enumerate(strips):
                if strips[i] == 'netto)':
                    net_salary = strips[i+1].split()
                    net_salary = ''.join(net_salary).replace('zł', '')
                    net_salaries.append(net_salary)
                    break
    except TypeError as exception:
        print('Nie podałeś żadnej kwoty brutto!')
        raise SystemExit from exception

    return net_salaries
