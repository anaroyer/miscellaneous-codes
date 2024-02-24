def is_valid(isbn):
    isbn_str = str(isbn)
    isbn_lenght = len(isbn)
    format_isbn = ''
    if isbn_str.isalnum() is False:
        if isbn_lenght == 13:
            for digit in isbn_str:
                if digit.isalnum() is True:
                    format_isbn += digit
                    continue
                continue
        if isbn_lenght != 13:
            return False
    
    if isbn_str.isalnum() is True and isbn_lenght != 10:
        return False
    
    if format_isbn[0:9].isalnum() is True and format_isbn[0:9].isnumeric() is False:
        return False
    
    if isbn_str.isalnum() is True and isbn_lenght == 10:
        format_isbn = isbn_str
    if format_isbn[0:9].isnumeric() is True:
        if format_isbn[9] in 'xX':
            calculus = (int(format_isbn[0]) * 10) + (int(format_isbn[1]) * 9) + (int(format_isbn[2]) * 8) + (int(format_isbn[3]) * 7) + (int(format_isbn[4]) * 6) + (int(format_isbn[5]) * 5) + (int(format_isbn[6]) * 4) + (int(format_isbn[7]) * 3) + (int(format_isbn[8]) * 2) + 10
            mod_eleven = calculus % 11
            if mod_eleven == 0:
                return True
            return False
            
        if format_isbn[9].isdigit() is True:
            calculus = (int(format_isbn[0]) * 10) + (int(format_isbn[1]) * 9) + (int(format_isbn[2]) * 8) + (int(format_isbn[3]) * 7) + (int(format_isbn[4]) * 6) + (int(format_isbn[5]) * 5) + (int(format_isbn[6]) * 4) + (int(format_isbn[7]) * 3) + (int(format_isbn[8]) * 2) + (int(format_isbn[9]))
            mod_eleven = calculus % 11
            if mod_eleven == 0:
                return True
            return False
    return False


