def time_to_words(hours,minutes):

    minute_dict = {
        "00": "o' clock",
        "01": "one",
        "02": "two",
        "03": "three",
        "04": "four",
        "05": "five",
        "06": "six",
        "07": "seven",
        "08": "eight",
        "09": "nine",
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "quarter",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",
        "20": "twenty",
        "21": "twenty one",
        "22": "twenty two",
        "23": "twenty three",
        "24": "twenty four",
        "25": "twenty five",
        "26": "twenty six",
        "27": "twenty seven",
        "28": "twenty eight",
        "29": "twenty nine",
        "30": "half",
    }
    hours_str = ""
    if hours < 10:
        hours_str = "0"+str(hours)
    else:
        hours_str = str(hours)
    minutes_str = ""
    if minutes < 10:
        minutes_str = "0"+str(minutes)
    else:
        minutes_str = str(minutes)
    if minutes <= 30:
        if minutes_str == "00":
            print(minute_dict[hours_str]+" "+minute_dict[minutes_str])
        elif minutes_str == "15" or minutes_str == "30":
            print(minute_dict[minutes_str]+" past "+minute_dict[hours_str])
        elif minutes_str == "01":
            print(minute_dict[minutes_str]+" minute past "+minute_dict[hours_str])
        else:
            print(minute_dict[minutes_str]+" minutes past "+minute_dict[hours_str])

    else:
        minutes = 60 - minutes
        minutes_str = str(minutes)
        hours_decode = int(hours_str)
        hours_decode = hours_decode + 1
        hours_str = ""
        if hours_decode < 10:
            hours_str = "0"+str(hours_decode)
        else:
            hours_str = str(hours_decode)
        minutes_str = ""
        if minutes < 10:
            minutes_str = "0"+str(minutes)
        else:
            minutes_str = str(minutes)

        if minutes_str == "15":
            print(minute_dict[minutes_str]+" to "+minute_dict[hours_str])
        elif minutes_str == "01":
            print(minute_dict[minutes_str]+" minute to "+minute_dict[hours_str])
        else:
            print(minute_dict[minutes_str]+" minutes to "+minute_dict[hours_str])

hours = int(input())
minutes = int(input())
time_to_words(hours,minutes)