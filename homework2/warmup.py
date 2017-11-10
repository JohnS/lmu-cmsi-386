import math
from random import shuffle
import requests
from Crypto.Cipher import AES


def change(c):
    if c < 0:
        raise ValueError('amount cannot be negative')
    quarters = divmod(c, 25)
    dimes = divmod(quarters[1], 10)
    nickles = divmod(dimes[1], 5)
    return quarters[0], dimes[0], nickles[0], nickles[1]


def strip_quotes(quote):
    quote = quote.replace('\'', '')
    quote = quote.replace('"', '')
    return quote


def scramble(phrase):
    result = list(phrase)
    shuffle(result)
    return ''.join(result)


def say(firstWord=''):
    if firstWord == '':
        return firstWord

    def say_more(nextWord=''):
        if nextWord == '':
            return firstWord
        return say(firstWord + ' ' + nextWord)
    return say_more


def triples(limit):
    set_of_triples = []

    for a in range(3, limit):
        for c in range(a+1, limit + 1):
            if c > a:
                b = math.sqrt((c ** 2) - (a ** 2))
                if b == int(b) and b > a:
                    set_of_triples.append((a, int(b), c))
    return set_of_triples


def powers(base, limit):
    exponent = 0
    current = 1
    while current <= limit:
        yield current
        exponent = exponent + 1
        current = base ** exponent


def interleave(x, *y):
    result = []
    while x or y:
        if x:
            result.append(x.pop(0))
        if y:
            result.append(y[0])
            y = y[1:]
    return result


class Cylinder:
    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height
        self.volume = None
        self.surface_area = None
        self.get_measurements()

    def stretch(self, factor):
        self.height *= factor
        self.get_measurements()
        return self

    def widen(self, factor):
        self.radius *= factor
        self.get_measurements()
        return self

    def get_measurements(self):
        self.volume = math.pi * (self.radius ** 2) * self.height
        self.surface_area = 2 * math.pi * self.radius * (self.radius + self.height)
        return self


def make_crypto_functions(key, iv):

    def encrypt(plain_text):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.encrypt(plain_text)

    def decrypt(encrypted_text):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.decrypt(encrypted_text)
    return (encrypt, decrypt)


def random_name(**args):
    gender = args['gender']
    region = args['region']
    req = requests.get('https://uinames.com/api/',
                       params={'gender': gender, 'region': region, 'amount': 1})
    if 'error' in req.json():
        raise ValueError(req.text)
    return '{}, {}'.format(req.json()['surname'], req.json()['name'])
