
predefined_paths_mod1 = {'mod1_sub1_complete': ['D:/PyDev/CrosSecPy/input_files/Mod1/submod1'],}

predefined_paths_mod2 = {'mod2_sub1_complete': ['D:/PyDev/CrosSecPy/input_files/Mod2/submod1'], }


depth_keys = {
    'Mod1': ['predefined_paths_mod1'],
    'Mod2': ['predefined_paths_mod2'],}

def list_keys(dic):
    li = []
    for key in dic:
        li.append(key)
    return li


def predef_paths(depth, model, loadstep):
    if depth == 'Mod1':
        path = predefined_paths_mod1[model][0] + '/' + model + '_' + loadstep + '.csv'

    elif depth == "Mod2":
        path = predefined_paths_mod2[model][0] + '/' + model + '_' + loadstep + '.csv'

    else:
        pass

    return path


mod1key = list_keys(predefined_paths_mod1)

mod2key = list_keys(predefined_paths_mod2)
