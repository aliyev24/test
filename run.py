import time
import summertour_class

URL = "https://www.summertour.az/search_tour?"

CHILDREN_AGES = [
    [[2], [10]],
    [[2, 10], [4, 7]],
    [[2, 6, 10], [10, 7, 4]]
]


def run(
        day_of_month: int = 1,
        month: int = 6,
        nights: int = 7,
        adult: int = 2,
        child: int = 0,
        children_ages: list = [],
        proxies_in_work: list = None,
        proxies: list = None,
):
    start_time = time.time()

    day = str(day_of_month).zfill(2)  # for example -> 01,02,03
    month = str(month).zfill(2)

    params = summertour_class.params_generator(
        from_date=f'2024{month}{day}',
        till_date=f'2024{month}{day}',
        nights_from=nights,
        nights_till=nights,
        adult=adult,
        child=child,
        children_ages=children_ages,
    )

    bot = summertour_class.SummerTour(url=URL, params=params)
    bot.open_page()
    result = bot.get_content()

    return result


# Test üçün parametrlər.
print(run(
    day_of_month=3,
    month=6,
    nights=7,
    adult=2,
    child=0,
))
