
predefined_paths_mod1 = {'rect_60_f3_fa100c4e6_inj3': ['D:/Desktop_alt/PyAns_clean/PyPost/input_files/test_inp/Mod1/rect_60_f3_fa100c4e6_inj3'],}

predefined_paths_mod2 = {'curv_60_f3_fa100c4e6_inj3': ['D:/Desktop_alt/PyAns_clean/PyPost/input_files/test_inp/Mod4/curv_60_f3_fa100c4e6_inj3'], }


depth_keys = {
    'Mod1_RectGrid60_f3el_inj3': ['predefined_paths_mod1'],
    'Mod4_CurvGrid60_f3el_inj3': ['predefined_paths_mod4'],}

def list_keys(dic):
    li = []
    for key in dic:
        li.append(key)
    return li


def predef_paths(depth, model, loadstep):
    if depth == 'Mod1_RectGrid60_f3el_inj3':
        path = predefined_paths_mod1[model][0] + '/' + model + '_' + loadstep + '/'

    elif depth == "Mod4_CurvGrid60_f3el_inj3":
        path = predefined_paths_mod2[model][0] + '/' + model + '_' + loadstep + '/'

    else:
        pass

    return path


mod1key = list_keys(predefined_paths_mod1)

mod2key = list_keys(predefined_paths_mod2)
