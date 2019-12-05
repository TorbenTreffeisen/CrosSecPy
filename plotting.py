from dataimp import *


def plot_df(results, dic, key):
    df_res = ans_calc(results, dic[key][0], dic[key][1])
    xval = df_res['x']
    yval = df_res['y']
    zval = df_res[dic[key][0]]
    chead = dic[key][0]
    output = dic[key][2]
    return xval, yval, zval, chead, output


def graduation(resultmod1, resultmod2, dic, key):
    df_mod1 = ans_calc(resultmod1, dic[key][0], dic[key][1])
    df_mod2 = ans_calc(resultmod2, dic[key][0], dic[key][1])
    max_mod1 = df_mod1[dic[key][0]].max()
    max_mod2 = df_mod2[dic[key][0]].max()
    if max_mod1 >= max_mod2:
        maxm = max_mod1
    else:
        maxm = max_mod2

    min_mod1 = df_mod1[dic[key][0]].min()
    min_mod2 = df_mod2[dic[key][0]].min()
    if min_mod1 <= min_mod2:
        minm = min_mod1
    else:
        minm = min_mod2

    return minm, maxm


def colormap(col):
    if col == 'RdYlBu':
        col = col + '_r'
    elif col == 'RdYlGn':
        col = col + '_r'
    elif col == 'RdBu':
        col = col + '_r'
    elif col == 'spectral':
        col = col + '_r'
    else:
        col = col
    return col


def plot_diff_df(results1, results2, dic, key):
    df_res1 = ans_calc(results1, dic[key][0], dic[key][1])
    df_res2 = ans_calc(results2, dic[key][0], dic[key][1])
    diff = 'difference ' + dic[key][0]
    df_res1[diff] = df_res2[dic[key][0]] - df_res1[dic[key][0]]

    df_res = pd.concat([df_res1['x'], df_res1['y'], df_res1[diff]], axis=1)
    df_res.columns = ['x', 'y', diff]

    xval = df_res['x']
    yval = df_res['y']
    zval = df_res[diff]
    chead = dic[key][0]
    output = dic[key][2]

    maxval = df_res[diff].max()
    minval = df_res[diff].min()

    return xval, yval, zval, chead, output, minval, maxval
