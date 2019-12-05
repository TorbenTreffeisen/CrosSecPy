import pandas as pd


def ans_csvdataimp_complete(name):      # list_files, result_parameter, list_keys
    df = pd.read_csv(name)          # Einlesen CSV
    df = df.apply(pd.to_numeric)                               # Datatype to numeric ändern.

    return df


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
