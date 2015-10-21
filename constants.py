'''
'''

uva_headers = {
    'Accept-Charset': 'utf-8,ISO-8859-1',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent' :  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) "+
                    "AppleWebKit/537.17 (KHTML, like Gecko) "+
                    "Chrome/24.0.1312.57 Safari/537.17",
    "Accept" : "text/html, application/xml, text/xml, */*",
}


udebug_headers = {
    'Accept-Charset': 'utf-8,ISO-8859-1',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent' :  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) "+
                    "AppleWebKit/537.17 (KHTML, like Gecko) "+
                    "Chrome/24.0.1312.57 Safari/537.17",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}

verdicts = {
    0  : "Pending",
    10 : "Submission error",
    15 : "Can't be judged",
    20 : "In queue",
    30 : "Compile error",
    35 : "Restricted function",
    40 : "Runtime error",
    45 : "Output limit",
    50 : "Time limit",
    60 : "Memory limit",
    70 : "Wrong answer",
    80 : "Presentation Error",
    90 : "Accepted",
}

language = {
    1 : "ANSI C",
    2 : "Java",
    3 : "C++",
    4 : "Pascal",
    5 : "C++11"
}
