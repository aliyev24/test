from bs4 import BeautifulSoup
from base_request import BaseRequest


def params_generator(
        hotel_id: int = None,
        from_date: str = '20240601',
        till_date: str = '20240601',
        nights_from: int = 3,
        nights_till: int = 3,
        adult: int = 1,
        child: int = 0,
        children_ages=[],
):
    params = {
        "TOWNFROMINC": '1930',
        "STATEINC": "9",
        "MEALS": "3",
        "FILTER": "1",
        "FREIGHT": "1",
        "TOWNS_ANY": "0",
        "TOWNS": "NaN,1959,1968,1962,1966,"
                 "1967,1960,1965,1963,1961,1964,NaN,1179,1432,1433,"
                 "NaN,1947,1948,NaN,1973,1970,1975,1974,1976,1979,"
                 "1977,1981,1978,1969,1980,NaN,1985,NaN,1972,NaN,"
                 "1438,1435,1437,1241,1436,1434,NaN,1971,NaN,1986,"
                 "2063,1987,1990,NaN,1951,1950,1957,1954,1956,1949,"
                 "1958,1952,1955",
        "DOLOAD": "1",
        "PRICEPAGE": "1",
    }
    params.update({
        "CHECKIN_BEG": from_date,
        "CHECKIN_END": till_date,
    })

    params.update({
        "NIGHTS_FROM": str(nights_from),
        "NIGHTS_TILL": str(nights_till),
    })

    params.update({
        "ADULT": str(adult),
        "CHILD": str(child),
        "AGES": '',
    })

    if child:
        for age in children_ages:
            params['AGES'] = params['AGES'] + f"{str(age)},"

    if hotel_id:
        params.update({
            'HOTELS': str(hotel_id),
        })

    return params


class SummerTour(BaseRequest):
    def __init__(self, url: str, params={}, proxy=None):
        super().__init__()
        if proxy:
            self.set_proxies(proxy)

        self.url = url
        self.params = params
        self.response = None
        self.soup = None
        self.page = 1

    def open_page(self):
        self.response = self.request.get(self.url,
                                         params=self.params,
                                         timeout=(60, 60))
        self.soup = BeautifulSoup(self.response.text, 'lxml')

        return self.response.status_code

    def get_content(self):
        tour_list = self.soup.find('tbody').find_all('tr')
        for tour in tour_list:
            tour_details = [x.text.strip() for x in tour.find_all('td')]
        return tour_details
