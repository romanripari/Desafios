def total_cost(tupla):
    segundos = []
    for t in tupla: 
        segund = int(t.split(" ")[2])
        agrego = segund // 60 if segund // 60 == segund / 60 else segund // 60 + 1
        print(segund, agrego)
        segundos.append( agrego )

    return sum(segundos)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert total_cost(("2014-01-01 01:12:13 181",
                "2014-01-02 20:11:10 600",
                "2014-01-03 01:12:13 6009",
                "2014-01-03 12:13:55 200")) == 124


