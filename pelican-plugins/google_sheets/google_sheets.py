from pelican import signals
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTEpKuYan9Cyl_tCzY1RA366pxAlWZQ3l02TdgnxeqIvIujN5iZpMFiGsK_o8t5LzNUGZV7FQ5VCBnj/pub?output=csv'


df = pd.read_csv(url)
print(df)



#def register():
#    signals.article_generator_finalized.connect(get_csv)