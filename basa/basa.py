l1 = '05:30'
l2 = '07:20'
l3 = '09:10'
l4 = '11:15'
l5 = '13:00'

monday = 'monday'
tuesday = 'tuesday'
wednesday = 'wednesday'
thursday = 'thursday'
friday = 'friday'
saturday = 'saturday'
sunday = 'sunday'

TIME = 'time'
DAY = 'day'
NAME = 'name'
URL = 'url'
WEEK = 'week'
WEEK_A = 'a'
WEEK_B = 'b'
WEEK_ALL = 'all'
DESCRIPTION = 'description'

base = [
    {
        TIME: l2,
        DAY: monday,
        WEEK: WEEK_B,
        NAME: 'Аналогова мікросхемотехніка',
        URL: 'https://us04web.zoom.us/j/75903696710?pwd=xz1AIywYOSgG24-5Loz5EPlG1PNy_r.1',
        DESCRIPTION: f'Лабораторна\n'
                     f'I/II підгрупа\n'
                     f'Викладач: Вітер О.С.\n'
    },
    {
        TIME: l3,
        DAY: monday,
        WEEK: WEEK_B,
        NAME: 'Аналогова мікросхемотехніка',
        URL: 'https://us04web.zoom.us/j/75903696710?pwd=xz1AIywYOSgG24-5Loz5EPlG1PNy_r.1',
        DESCRIPTION: f'Лабораторна\n'
                     f'I/II підгрупа\n'
                     f'Викладач: Вітер О.С.\n'
    },
    {
        TIME: l3,
        DAY: monday,
        WEEK: WEEK_A,
        NAME: 'Мікроконтролери, частина 2',
        URL: 'https://teams.microsoft.com/l/meetup-join/19%3Ameeting_MTMzOTQ0OTQtM2NmNC00NTI1LWJjNjUtNjc2OTkwM2RkNDU5%40thread.v2/0?context=%7B%22Tid%22%3A%227631cd62-5187-4e15-8b8e-ef653e366e7a%22%2C%22Oid%22%3A%2249826ca3-7714-41f8-8dcc-61bd605bb161%22%7D',
        DESCRIPTION: f'Лабораторна\n'
                     f'II підгрупа\n'
                     f'Викладач: Татарин В.Я.\n'
    },
    {
        TIME: l4,
        DAY: monday,
        WEEK: WEEK_A,
        NAME: 'Мікроконтролери, частина 2',
        URL: 'https://teams.microsoft.com/l/meetup-join/19%3Ameeting_MTMzOTQ0OTQtM2NmNC00NTI1LWJjNjUtNjc2OTkwM2RkNDU5%40thread.v2/0?context=%7B%22Tid%22%3A%227631cd62-5187-4e15-8b8e-ef653e366e7a%22%2C%22Oid%22%3A%2249826ca3-7714-41f8-8dcc-61bd605bb161%22%7D',
        DESCRIPTION: f'Лабораторна\n'
                     f'II підгрупа\n'
                     f'Викладач: Татарин В.Я.\n'
    },

    {
        TIME: l2,
        DAY: tuesday,
        WEEK: WEEK_B,
        NAME: 'Аналогова мікросхемотехніка',
        URL: 'https://us04web.zoom.us/j/75903696710?pwd=xz1AIywYOSgG24-5Loz5EPlG1PNy_r.1',
        DESCRIPTION: f'Практична\n'
                     f'Викладач: Вітер О.С.\n'
                     f'Відмічає\n'
    },
    {
        TIME: l3,
        DAY: tuesday,
        WEEK: WEEK_ALL,
        NAME: 'Теорія інформації',
        URL: 'https://us04web.zoom.us/j/79824756085?pwd=Xsd5WKZ5MHjyr2w1vXQKtprvwsM_rO.1%20#Passcode:%2012345',
        DESCRIPTION: f'Лекція\n'
                     f'Викладач: Стахів Р.І.\n'
    },
    {
        TIME: l4,
        DAY: tuesday,
        WEEK: WEEK_ALL,
        NAME: 'Мікроконтролери, частина 2',
        URL: 'https://teams.microsoft.com/l/meetup-join/19%3Ameeting_MTMzOTQ0OTQtM2NmNC00NTI1LWJjNjUtNjc2OTkwM2RkNDU5%40thread.v2/0?context=%7B%22Tid%22%3A%227631cd62-5187-4e15-8b8e-ef653e366e7a%22%2C%22Oid%22%3A%2249826ca3-7714-41f8-8dcc-61bd605bb161%22%7D',
        DESCRIPTION: f'Лекція\n'
                     f'Викладач: Татарин В.Я.\n'

    },
    {
        TIME: l5,
        DAY: tuesday,
        WEEK: WEEK_A,
        NAME: 'Мікроконтролери, частина 2',
        URL: 'https://teams.microsoft.com/l/meetup-join/19%3Ameeting_MTMzOTQ0OTQtM2NmNC00NTI1LWJjNjUtNjc2OTkwM2RkNDU5%40thread.v2/0?context=%7B%22Tid%22%3A%227631cd62-5187-4e15-8b8e-ef653e366e7a%22%2C%22Oid%22%3A%2249826ca3-7714-41f8-8dcc-61bd605bb161%22%7D',
        DESCRIPTION: f'Лекція\n'
                     f'Викладач: Татарин В.Я.\n'

    },
    {
        TIME: l1,
        DAY: wednesday,
        WEEK: WEEK_ALL,
        NAME: 'Чисельні методи',
        URL: 'https://us04web.zoom.us/j/2169406971?pwd=NGwzVy9tK1lUL3pCVjQxY3ZHR04vUT09%20%20Meeting%20ID:%20216%20940%206971%20Passcode:%204t49Hn',
        DESCRIPTION: f'Лабораторна\n'
                     f'I підгрупа\n'
                     f'Викладач: Дзелендзяк У.Ю.\n'
    },

    {
        TIME: l1,
        DAY: wednesday,
        WEEK: WEEK_A,
        NAME: 'Теорія інформації',
        URL: 'https://us04web.zoom.us/j/79824756085?pwd=Xsd5WKZ5MHjyr2w1vXQKtprvwsM_rO.1%20#Passcode:%2012345',
        DESCRIPTION: f'Лабораторна\n'
                     f'ІI підгрупа\n'
                     f'Викладач: Стахів Р.І.\n'
    },
    {
        TIME: l2,
        DAY: wednesday,
        WEEK: WEEK_ALL,
        NAME: 'Чисельні методи',
        URL: 'https://us04web.zoom.us/j/2169406971?pwd=NGwzVy9tK1lUL3pCVjQxY3ZHR04vUT09%20%20Meeting%20ID:%20216%20940%206971%20Passcode:%204t49Hn',
        DESCRIPTION: f'Лабораторна\n'
                     f'II підгрупа\n'
                     f'Викладач: Дзелендзяк У.Ю.\n'
    },
    {
        TIME: l2,
        DAY: wednesday,
        WEEK: WEEK_A,
        NAME: 'Теорія інформації',
        URL: 'https://us04web.zoom.us/j/79824756085?pwd=Xsd5WKZ5MHjyr2w1vXQKtprvwsM_rO.1%20#Passcode:%2012345',
        DESCRIPTION: f'Лабораторна\n'
                     f'І підгрупа\n'
                     f'Викладач: Стахів Р.І.\n'
    },
    {
        TIME: l1,
        DAY: thursday,
        WEEK: WEEK_A,
        NAME: 'Мікроконтролери, частина 2',
        URL: 'https://teams.microsoft.com/l/meetup-join/19%3Ameeting_MTMzOTQ0OTQtM2NmNC00NTI1LWJjNjUtNjc2OTkwM2RkNDU5%40thread.v2/0?context=%7B%22Tid%22%3A%227631cd62-5187-4e15-8b8e-ef653e366e7a%22%2C%22Oid%22%3A%2249826ca3-7714-41f8-8dcc-61bd605bb161%22%7D',
        DESCRIPTION: f'Лабораторна\n'
                     f'І підгрупа\n'
                     f'Викладач: Татарин В.Я.\n'
    },
    {
        TIME: l2,
        DAY: thursday,
        WEEK: WEEK_A,
        NAME: 'Мікроконтролери, частина 2',
        URL: 'https://teams.microsoft.com/l/meetup-join/19%3Ameeting_MTMzOTQ0OTQtM2NmNC00NTI1LWJjNjUtNjc2OTkwM2RkNDU5%40thread.v2/0?context=%7B%22Tid%22%3A%227631cd62-5187-4e15-8b8e-ef653e366e7a%22%2C%22Oid%22%3A%2249826ca3-7714-41f8-8dcc-61bd605bb161%22%7D',
        DESCRIPTION: f'Лабораторна\n'
                     f'І підгрупа\n'
                     f'Викладач: Татарин В.Я.\n'

    },
    {
        TIME: l2,
        DAY: thursday,
        WEEK: WEEK_B,
        NAME: 'Системний аналіз',
        URL: 'https://us04web.zoom.us/j/3493308408',
        DESCRIPTION: f'Лабораторна\n'
                     f'ІІ підгрупа\n'
                     f'Викладач: Шпак О.І.\n'
                     f'pass: ```1Gcaiw```'
    },
    {
        TIME: l3,
        DAY: thursday,
        WEEK: WEEK_B,
        NAME: 'Системний аналіз',
        URL: 'https://us04web.zoom.us/j/3493308408',
        DESCRIPTION: f'Лабораторна\n'
                     f'І підгрупа\n'
                     f'Викладач: Шпак О.І.\n'
                     f'pass: ```1Gcaiw```'
    },
    {
        TIME: l1,
        DAY: friday,
        WEEK: WEEK_ALL,
        NAME: 'Хмарні технології',
        URL: 'https://softserveinc.zoom.us/j/99979302138?pwd=dzlMdjgyUXpjcUtSc05oWDd1c3Z6Zz09',
        DESCRIPTION: f'Лекція\n'
                     f'Викладач: Верес\n'
    },
    {
        TIME: l2,
        DAY: friday,
        WEEK: WEEK_ALL,
        NAME: 'Системний аналіз',
        URL: 'https://us04web.zoom.us/j/3493308408',
        DESCRIPTION: f'Лекція\n'
                     f'Викладач: Шпак О.І.\n'
                     f'pass: ```1Gcaiw```'

    },
{
        TIME: l3,
        DAY: friday,
        WEEK: WEEK_ALL,
        NAME: 'Аналогова мікросхемотехніка',
        URL: 'https://us04web.zoom.us/j/75903696710?pwd=xz1AIywYOSgG24-5Loz5EPlG1PNy_r.1',
        DESCRIPTION: f'Лекція\n'
                     f'Викладач: Вітер О.С.\n'
                     f'Відмічає\n'
    },
{
        TIME: l4,
        DAY: friday,
        WEEK: WEEK_ALL,
        NAME: 'Чисельні методи',
        URL: 'https://us04web.zoom.us/j/2169406971?pwd=NGwzVy9tK1lUL3pCVjQxY3ZHR04vUT09%20%20Meeting%20ID:%20216%20940%206971%20Passcode:%204t49Hn',
        DESCRIPTION: f'Лекція\n'
                     f'Викладач: Дзелендзяк У.Ю.\n'
    },
]
