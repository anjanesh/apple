from datetime import datetime
import os.path
from apple.settings import BASE_DIR
import decimal

# https://codereview.stackexchange.com/questions/148853/convert-an-amount-to-indian-notation
def currency_in_indian_format(n):
    """ Convert a number (int / float) into indian formatting style """
    d = decimal.Decimal(str(n))

    if d.as_tuple().exponent < -2:
        s = str(n)
    else:
        s = '{0:.2f}'.format(n)

    l = len(s)
    i = l - 1

    res, flag, k = '', 0, 0
    while i >= 0:
        if flag == 0:
            res += s[i]
            if s[i] == '.':
                flag = 1
        elif flag == 1:
            k += 1
            res += s[i]
            if k == 3 and i - 1 >= 0:
                res += ','
                flag = 2
                k = 0
        else:
            k += 1
            res += s[i]
            if k == 2 and i - 1 >= 0:
                res += ','
                flag = 2
                k = 0
        i -= 1

    return res[::-1]


# n = 1200000
# print("INR {}".format(currency_in_indian_format(n)))  # INR 12,00,000.00

def date_last_modified_static(request, app, template_name):        
    template_file_path = os.path.join(str(BASE_DIR) + '/' + app + '/templates/', template_name)
    # https://thispointer.com/python-get-last-modification-date-time-of-a-file-os-stat-os-path-getmtime/
    mtime = os.path.getmtime(template_file_path)    
    dt = datetime.fromtimestamp(mtime)
    return dt