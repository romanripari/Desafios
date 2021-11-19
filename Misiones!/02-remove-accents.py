def checkio(in_string):
    import unicodedata
    return ''.join(st for st in unicodedata.normalize('NFD', in_string)\
            if unicodedata.category(st) != 'Mn')





    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
