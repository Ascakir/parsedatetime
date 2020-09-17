# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import *  # noqa

# don't use an unicode string
localeID = 'tr_TR'
dateSep = ['.']
timeSep = [':']
meridian = []
usesMeridian = False
uses24 = True
decimal_mark = ','

Weekdays = [
    'pazartesi', 'salı', 'çarşamba',
    'perşembe', 'cuma', 'cumartesi', 'pazar',
]
shortWeekdays = ['ptesi', 'salı', 'çarş', 'perş', 'cuma', 'ctesi', 'pazar']
Months = [
    'ocak', 'şubat', 'mart',
    'nisan', 'mayıs', 'haziran',
    'temmuz', 'ağustos', 'eylül',
    'ekim', 'kasım', 'aralık',
]
shortMonths = [
    'ocak', 'şub', 'mart', 'nisan', 'may', 'haz',
    'temz', 'ağus', 'eyl', 'ekim', 'kas', 'aralık',
]

dateFormats = {
    'full': 'EEEE, d. MMMM yyyy',
    'long': 'd. MMMM yyyy',
    'medium': 'dd.MM.yyyy',
    'short': 'dd.MM.yy',
}

timeFormats = {
    'full': 'HH:mm:ss v',
    'long': 'HH:mm:ss z',
    'medium': 'HH:mm:ss',
    'short': 'HH:mm',
}

dp_order = ['d', 'm', 'y']


# Used to parse expressions like "in 5 hours"
numbers = {
    'sıfır': 0,
    'bir': 1,
    'tek': 1,
    'iki': 2,
    'üç': 3,
    'dört': 4,
    'beş': 5,
    'altı': 6,
    'yedi': 7,
    'sekiz': 8,
    'dokuz': 9,
    'on': 10,
    'on bir': 11,
    'on iki': 12,
    'on üç': 13,
    'on dört': 14,
    'on beş': 15,
    'on altı': 16,
    'on yedi': 17,
    'on sekiz': 18,
    'on dokuz': 19,
    'yirmi': 20,
    'yirmi bir': 21,
    'yirmi iki': 22,
    'yirmi üç': 23,
    'yirmi dört': 24,
}
# the short version would be a capital M,
# as I understand it we can't distinguish
# between m for minutes and M for months.

# this will be added to re_values later
units = {
    'seconds': ['saniye', 'saniyeler', 'sn', 'sn'],
    'minutes': ['dakika', 'dakikalar', 'dk', 'd'],
    'hours': ['saat', 'saatler', 's', 's'],
    'days': ['gün', 'günler', 'g', 'g'],
    'weeks': ['hafta', 'haftalar', 'h', 'h'],
    'months': ['ay', 'aylar', 'a'],
    'years': ['yıl', 'yıllar', 'yıl', 'y'],
}

re_values = re_values.copy()
re_values.update({
    'specials': 'içinde|den|dan',
    'timeseparator': ':',
    'rangeseparator': '-',
    'daysuffix': 'inci|üncü|ıncı|uncu',
    'qunits': 's|d|sn|g|h|a|y',
    'now': ['şimdi'],
})

# Used to adjust the returned date before/after the source
# still looking for insight on how to translate all of them to german.
Modifiers = {
    'itibaren': 1,
    'önce': -1,
    'sonra': 1,
    'önceki': -1,
    'sonraki': -1,
    'geçen': -1,
    'bu': 0,
    'sonu': 0,
    'en son': -1,
    'bir sonraki': 1,
}

# morgen/abermorgen does not work, see
# http://code.google.com/p/parsedatetime/issues/detail?id=19
dayOffsets = {
    'yarın': 1,
    'bugün': 0,
    'dün': -1,
    'önceki gün': -2,
    'sonraki gün': 2,
}

# special day and/or times, i.e. lunch, noon, evening
# each element in the dictionary is a dictionary that is used
# to fill in any value to be replace - the current date/time will
# already have been populated by the method buildSources
re_sources = {
    'öğlen': {'hr': 12, 'mn': 0, 'sec': 0},

}
