
file1 = "results_all_presseqv.csv"
file2 = "results_all_stress.csv"
file3 = "results_all_elstr.csv"
file4 = "results_all_plstr.csv"
file5 = "results_all_tstr.csv"
file6 = "results_all_addvalues.csv"
file7 = "results_all_estress.csv"

list_files = [file1, file2, file3, file4, file5, file6, file7]
list_filestring = ['file1', 'file2', 'file3', 'file4', 'file5', 'file6', 'file7']

result_parameters = {
    'file1': ['node', 'x', 'y', 'z', 'pres', 'stress', 'el. strain', 'pl. strain', 'tot. strain'],
    'file2': ['node', 'S1', 'S2', 'S3', 'SXX', 'SYY', 'SZZ', 'SXY', 'SYZ', 'SXZ'],
    'file3': ['node', 'el. Str1', 'el. Str2', 'el. Str3', 'el. StrXX', 'el. StrYY', 'el. StrZZ',
              'el. StrXY', 'el. StrYZ', 'el. StrXZ'],
    'file4': ['node', 'pl. Str1', 'pl. Str2', 'pl. Str3', 'pl. StrXX', 'pl. StrYY', 'pl. StrZZ',
              'pl. StrXY', 'pl. StrYZ', 'pl. StrXZ'],
    'file5': ['node', 'tot. Str1', 'tot. Str2', 'tot. Str3', 'tot. StrXX', 'tot. StrYY', 'tot. StrZZ',
              'tot. StrXY', 'tot. StrYZ', 'tot. StrXZ'],
    'file6': ['node', 'UX', 'UY', 'UZ', 'estress'],
    'file7': ['node', 'ES1', 'ES2', 'ES3', 'ESXX', 'ESYY', 'ESZZ', 'ESXY', 'ESYZ', 'ESXZ']}

input_output = {'pressure--': ['pres', 'pos_mpa', 'Pressure in MPa'],
                'u-x': ['UX', 'false', 'X-Displacement in m'],
                'u-y': ['UY', 'false', 'Y-Displacement in m'],
                'u-z': ['UZ', 'false', 'Z-Displacement in m'],

                'stress-tot': ['stress', 'pos_mpa', 'total Stress in MPa'],
                'stress-s3': ['S1', 'neg_mpa', 'S3 in MPa'],
                'stress-s2': ['S2', 'neg_mpa', 'S2 in MPa'],
                'stress-s1': ['S3', 'neg_mpa', 'S1 in MPa'],
                'stress-sxx': ['SXX', 'neg_mpa', 'SXX in MPa'],
                'stress-syy': ['SYY', 'neg_mpa', 'SYY in MPa'],
                'stress-szz': ['SZZ', 'neg_mpa', 'SZZ in MPa'],
                'stress-sxy': ['SXY', 'false', 'SXY in MPa'],
                'stress-syz': ['SYZ', 'false', 'SYZ in MPa'],
                'stress-sxz': ['SXZ', 'false', 'SXZ in MPa'],

                'estress-tot': ['estress', 'pos_mpa', 'total E-Stress in MPa'],
                'estress-s3': ['ES1', 'neg_mpa', 'E-S3 in MPa'],
                'estress-s2': ['ES2', 'neg_mpa', 'E-S2 in MPa'],
                'estress-s1': ['ES3', 'neg_mpa', 'E-S1 in MPa'],
                'estress-sxx': ['ESXX', 'neg_mpa', 'E-SXX in MPa'],
                'estress-syy': ['ESYY', 'neg_mpa', 'E-SYY in MPa'],
                'estress-szz': ['ESZZ', 'neg_mpa', 'E-SZZ in MPa'],
                'estress-sxy': ['ESXY', 'false', 'E-SXY in MPa'],
                'estress-syz': ['ESYZ', 'false', 'E-SYZ in MPa'],
                'estress-sxz': ['ESXZ', 'false', 'E-SXZ in MPa'],

                'el. strain-tot': ['el. strain', 'perc', 'total elastic Strain in %'],
                'el. strain-s1': ['el. Str1', 'perc', 'S1 elastic Strain in %'],
                'el. strain-s2': ['el. Str2', 'perc', 'S2 elastic Strain in %'],
                'el. strain-s3': ['el. Str3', 'perc', 'S3 elastic Strain in %'],
                'el. strain-sxx': ['el. StrXX', 'perc', 'SXX elastic Strain in %'],
                'el. strain-syy': ['el. StrYY', 'perc', 'SYY elastic Strain in %'],
                'el. strain-szz': ['el. StrZZ', 'perc', 'SZZ elastic Strain in %'],
                'el. strain-sxy': ['el. StrXY', 'perc', 'SXY elastic Strain in %'],
                'el. strain-syz': ['el. StrYZ', 'perc', 'SYZ elastic Strain in %'],
                'el. strain-sxz': ['el. StrXZ', 'perc', 'SXZ elastic Strain in %'],

                'pl. strain-tot': ['pl. strain', 'perc', 'total plastic Strain in %'],
                'pl. strain-s1': ['pl. Str1', 'perc', 'S1 plastic Strain in %'],
                'pl. strain-s2': ['pl. Str2', 'perc', 'S2 plastic Strain in %'],
                'pl. strain-s3': ['pl. Str3', 'perc', 'S3 plastic Strain in %'],
                'pl. strain-sxx': ['pl. StrXX', 'perc', 'SXX plastic Strain in %'],
                'pl. strain-syy': ['pl. StrYY', 'perc', 'SYY plastic Strain in %'],
                'pl. strain-szz': ['pl. StrZZ', 'perc', 'SZZ plastic Strain in %'],
                'pl. strain-sxy': ['pl. StrXY', 'perc', 'SXY plastic Strain in %'],
                'pl. strain-syz': ['pl. StrYZ', 'perc', 'SYZ plastic Strain in %'],
                'pl. strain-sxz': ['pl. StrXZ', 'perc', 'SXZ plastic Strain in %'],

                'tot. strain-tot': ['tot. strain', 'perc', 'total total Strain in %'],
                'tot. strain-s1': ['tot. Str1', 'perc', 'S1 total Strain in %'],
                'tot. strain-s2': ['tot. Str2', 'perc', 'S2 total Strain in %'],
                'tot. strain-s3': ['tot. Str3', 'perc', 'S3 total Strain in %'],
                'tot. strain-sxx': ['tot. StrXX', 'perc', 'SXX total Strain in %'],
                'tot. strain-syy': ['tot. StrYY', 'perc', 'SYY total Strain in %'],
                'tot. strain-szz': ['tot. StrZZ', 'perc', 'SZZ total Strain in %'],
                'tot. strain-sxy': ['tot. StrXY', 'perc', 'SXY total Strain in %'],
                'tot. strain-syz': ['tot. StrYZ', 'perc', 'SYZ total Strain in %'],
                'tot. strain-sxz': ['tot. StrXZ', 'perc', 'SXZ total Strain in %'],
                }

