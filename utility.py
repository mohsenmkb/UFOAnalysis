import re
import numpy as np

# Utility
def extract_numbers(input_string):
    # Use regular expression to find all numbers in the input string
    numbers = re.findall(r'\d+', input_string)
    
    # Join the extracted numbers into a single string
    result = ''.join(numbers)
    
    return result


def transform_duration(x):
    try:
        x = x.lower()
        if 'hours' in x or 'hour' in x:
            x = float(extract_numbers(x)) * 3600

        elif 'minutes' in x or 'minute' in x or 'min' in x:
            x = float(extract_numbers(x)) * 60

        elif 'seconds' in x or 'second' in x or 'sec' in x:
            x = float(extract_numbers(x))

        else:
            x = np.nan

        if x > 3600*5:
            x = np.nan

    except:
        x = np.nan

    return x


def parse_duration(duration_str):
    try:
        # Define regular expressions to extract hours, minutes, and seconds
        hours = re.search(r'(\d+)\s*hour', duration_str)
        minutes = re.search(r'(\d+)\s*min', duration_str)
        seconds = re.search(r'(\d+)\s*second', duration_str)

        total_seconds = 0

        # Convert hours, minutes, and seconds to seconds and add to total_seconds
        if hours:
            total_seconds += int(hours.group(1)) * 3600
        if minutes:
            total_seconds += int(minutes.group(1)) * 60
        if seconds:
            total_seconds += int(seconds.group(1))

        if total_seconds > 3600*6:
            total_seconds = np.nan
    except:
        total_seconds = np.nan

    return total_seconds

def get_keyword_per_state(state,data,extractor):
    text_df = data[data['state']==state]
    text_data = ' '.join(text_df['text'])
    text_data = text_data.replace("\n", " ")
    keyphrases = extractor(text_data)
    return list(keyphrases)