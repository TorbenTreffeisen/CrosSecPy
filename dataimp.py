import pandas as pd


def file_path(listfiles, modelpath):
    respath = []
    for file in listfiles:
        respath.append(str(modelpath) + str(file))
    return respath

def ans_csvimp_f1(name, results, key):
    df = pd.read_csv(name, names=results[key], skiprows=1)
    df = df.apply(pd.to_numeric)
    return df


def ans_csvimp(name, results, key):
    df = pd.read_csv(name, names=results[key], skiprows=1)
    df = df.drop(columns=['node'])
    df = df.apply(pd.to_numeric)
    return df


def ans_csvdataimp_complete(listfiles, results, listkeys):
    df1 = ans_csvimp_f1(listfiles[0], results, listkeys[0])
    df2 = ans_csvimp(listfiles[1], results, listkeys[1])
    df3 = ans_csvimp(listfiles[2], results, listkeys[2])
    df4 = ans_csvimp(listfiles[3], results, listkeys[3])
    df5 = ans_csvimp(listfiles[4], results, listkeys[4])
    df6 = ans_csvimp(listfiles[5], results, listkeys[5])
    df7 = ans_csvimp(listfiles[6], results, listkeys[6])

    df_res = pd.concat([df1, df2, df3, df4, df5, df6, df7], axis=1, sort=False)

    return df_res


def ans_printcsv(listfiles, results, listkeys):
    printcsv = ans_csvdataimp_complete(listfiles, results, listkeys)
    return printcsv.to_csv('complete_results.csv')


def ans_calc(results, parameter, calc):
    df_calc = pd.concat([results['x'], results['y'], results[parameter]], axis=1)
    df_calc.columns = ['x', 'y', parameter]


    def calc_to_negmpa(row):
        return row[parameter] * ((-1) / 1000000)

    def calc_to_posmpa(row):
        return row[parameter] / 1000000

    def calc_toperc(row):
        return row[parameter] * 100

    if calc == 'neg_mpa':
        df_calc[parameter] = df_calc.apply(calc_to_negmpa, axis=1)
    elif calc == 'pos_mpa':
        df_calc[parameter] = df_calc.apply(calc_to_posmpa, axis=1)
    elif calc == 'perc':
        df_calc[parameter] = df_calc.apply(calc_toperc, axis=1)
    else:
        pass

    return df_calc