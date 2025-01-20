import re
import pandas as pd

def preprocess(data):
    pattern = r'(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}\s?[APM]{2}) - ([^:]+): (.*)'
    matches = re.findall(pattern, data)
    for match in matches:
        dates = match[0]
        user = match[1]
        Message = match[2]
    df = pd.DataFrame(matches,columns=['dates','user','Message'])
    df['dates'] = pd.to_datetime(df['dates'])
    df['user'] = pd.Categorical(df['user'])
    df['Message'] = pd.Categorical(df['Message'])
    df['date'] = df['dates'].dt.date
    df['year'] = df['dates'].dt.year
    df['month_num'] = df['dates'].dt.month
    df['month'] = df['dates'].dt.month_name()
    df['day'] = df['dates'].dt.day
    df['day_name'] = df['dates'].dt.day_name()
    df['hour'] = df['dates'].dt.hour
    df['minute'] = df['dates'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df