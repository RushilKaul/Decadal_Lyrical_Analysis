import regex as re
import pandas as pd

# re.sub(r'(.{2,}?)([aeiougyn]+$)',r'\1', word)

path = 'lyrics.csv'
data = pd.read_csv(path)

df = data[(data['Year'] >= 1930) & (data['Year'] <= 1939)]
print(df.shape)
df.to_csv('1930-39.csv', index=False)

df = data[(data['Year'] >= 1940) & (data['Year'] <= 1949)]
print(df.shape)
df.to_csv('1940-49.csv', index=False)

df = data[(data['Year'] >= 1950) & (data['Year'] <= 1959)]
print(df.shape)
df.to_csv('1950-59.csv', index=False)

df = data[(data['Year'] >= 1960) & (data['Year'] <= 1969)]
print(df.shape)
df.to_csv('1960-69.csv', index=False)

df = data[(data['Year'] >= 1970) & (data['Year'] <= 1979)]
print(df.shape)
df.to_csv('1970-79.csv', index=False)

df = data[(data['Year'] >= 1980) & (data['Year'] <= 1989)]
print(df.shape)
df.to_csv('1980-89.csv', index=False)

df = data[(data['Year'] >= 1990) & (data['Year'] <= 1999)]
print(df.shape)
df.to_csv('1990-99.csv', index=False)

df = data[(data['Year'] >= 2000) & (data['Year'] <= 2009)]
print(df.shape)
df.to_csv('2000-09.csv', index=False)

df = data[(data['Year'] == 0) | (data['Year'] == -1) | (data['Year'] == 197)]
print(df.shape)
df.to_csv('others.csv', index=False)

# print(set(data['Year']))

# threedots
# extra spaces and punctuations
# numbers