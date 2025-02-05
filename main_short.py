from qtpy import QtWidgets
from gui.mainwindow_short import Ui_MainWindow

from filepaths import *
from dic_def import *
from plotting import *

from scipy.interpolate import griddata
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pb_models.clicked.connect(self.models_changed)
        self.ui.pb_models_2.clicked.connect(self.models_predefined)
        self.ui.pb_plot.clicked.connect(self.plot_results)
        self.ui.pb_plot_diff.clicked.connect(self.plot_differences)

        self.ui.pb_models.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pb_models_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

        self.ui.pb_select.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pb_select_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        self.ui.pb_filepath_selec.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pb_selection.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        self.ui.cbx_cat_c1.currentTextChanged.connect(self.cat_c1_changed)
        self.ui.cbx_cat_c2.currentTextChanged.connect(self.cat_c2_changed)
        self.ui.cbx_cat_c3.currentTextChanged.connect(self.cat_c3_changed)
        self.ui.cbx_cat_c4.currentTextChanged.connect(self.cat_c4_changed)

        self.ui.cbx_inp_depth_m1.currentTextChanged.connect(self.model1_input_change)
        self.ui.cbx_inp_depth_m2.currentTextChanged.connect(self.model2_input_change)

    def models_changed(self):
        self.ui.cbx_mod1.clear()
        self.ui.cbx_mod2.clear()

        model1 = self.ui.input_model1.text()
        model2 = self.ui.input_model2.text()

        models = [str(model1), str(model2)]

        self.ui.cbx_mod1.addItems(models)
        self.ui.cbx_mod2.addItems(models)

        self.ui.radb_freesel.setChecked(True)

    def models_predefined(self):
        self.ui.cbx_mod1.clear()
        self.ui.cbx_mod2.clear()

        model1 = self.ui.cbx_inp_model_m1.currentText()
        model1_ls = self.ui.cbx_inp_loadstep_m1.currentText()
        model2 = self.ui.cbx_inp_model_m2.currentText()
        model1_2s = self.ui.cbx_inp_loadstep_m2.currentText()

        models = [str(model1 + '_' + model1_ls), str(model2 + '_' + model1_2s)]

        self.ui.cbx_mod1.addItems(models)
        self.ui.cbx_mod2.addItems(models)

        self.ui.radb_predsel.setChecked(True)

    def cat_c1_changed(self):
        self.ui.cbx_scat_c1.clear()

        cat1 = self.ui.cbx_cat_c1.currentText()
        res_pres = ['-']
        res_str = ['tot']

        if cat1 == "pressure":
            self.ui.cbx_scat_c1.addItems(res_pres)
        elif cat1 == "stress":
            self.ui.cbx_scat_c1.addItems(res_str)
        elif cat1 == "el. strain":
            self.ui.cbx_scat_c1.addItems(res_str)
        elif cat1 == "pl. strain":
            self.ui.cbx_scat_c1.addItems(res_str)
        elif cat1 == "tot. strain":
            self.ui.cbx_scat_c1.addItems(res_str)
        else:
            self.ui.cbx_scat_c1.addItems(" ")

    def cat_c2_changed(self):
        self.ui.cbx_scat_c2.clear()

        cat1 = self.ui.cbx_cat_c2.currentText()
        res_pres = ['-']
        res_str = ['tot']

        if cat1 == "pressure":
            self.ui.cbx_scat_c2.addItems(res_pres)
        elif cat1 == "stress":
            self.ui.cbx_scat_c2.addItems(res_str)
        elif cat1 == "el. strain":
            self.ui.cbx_scat_c2.addItems(res_str)
        elif cat1 == "pl. strain":
            self.ui.cbx_scat_c2.addItems(res_str)
        elif cat1 == "tot. strain":
            self.ui.cbx_scat_c2.addItems(res_str)
        else:
            self.ui.cbx_scat_c2.addItems(" ")

    def cat_c3_changed(self):
        self.ui.cbx_scat_c3.clear()

        cat1 = self.ui.cbx_cat_c3.currentText()
        res_pres = ['-']
        res_str = ['tot']

        if cat1 == "pressure":
            self.ui.cbx_scat_c3.addItems(res_pres)
        elif cat1 == "stress":
            self.ui.cbx_scat_c3.addItems(res_str)
        elif cat1 == "el. strain":
            self.ui.cbx_scat_c3.addItems(res_str)
        elif cat1 == "pl. strain":
            self.ui.cbx_scat_c3.addItems(res_str)
        elif cat1 == "tot. strain":
            self.ui.cbx_scat_c3.addItems(res_str)
        else:
            self.ui.cbx_scat_c3.addItems(" ")

    def cat_c4_changed(self):
        self.ui.cbx_scat_c4.clear()

        cat1 = self.ui.cbx_cat_c4.currentText()
        res_pres = ['-']
        res_str = ['tot']

        if cat1 == "pressure":
            self.ui.cbx_scat_c4.addItems(res_pres)
        elif cat1 == "stress":
            self.ui.cbx_scat_c4.addItems(res_str)
        elif cat1 == "el. strain":
            self.ui.cbx_scat_c4.addItems(res_str)
        elif cat1 == "pl. strain":
            self.ui.cbx_scat_c4.addItems(res_str)
        elif cat1 == "tot. strain":
            self.ui.cbx_scat_c4.addItems(res_str)
        else:
            self.ui.cbx_scat_c4.addItems(" ")

    def model1_input_change(self):

        self.ui.cbx_inp_model_m1.clear()

        depth1 = self.ui.cbx_inp_depth_m1.currentText()

        if depth1 == "Mod1":
            self.ui.cbx_inp_model_m1.addItems(mod1key)
        elif depth1 == "Mod2":
            self.ui.cbx_inp_model_m1.addItems(mod2key)
        else:
            self.ui.cbx_inp_model_m1.addItems(" ")

    def model2_input_change(self):

        self.ui.cbx_inp_model_m2.clear()

        depth2 = self.ui.cbx_inp_depth_m2.currentText()

        if depth2 == "Mod1":
            self.ui.cbx_inp_model_m2.addItems(mod1key)
        elif depth2 == "Mod2":
            self.ui.cbx_inp_model_m2.addItems(mod2key)
        else:
            self.ui.cbx_inp_model_m2.addItems(" ")

    def plot_results(self):
        user_cat_c1 = self.ui.cbx_cat_c1.currentText()
        user_cat_c2 = self.ui.cbx_cat_c2.currentText()
        user_cat_c3 = self.ui.cbx_cat_c3.currentText()
        user_cat_c4 = self.ui.cbx_cat_c4.currentText()

        user_subcat_c1 = self.ui.cbx_scat_c1.currentText()
        user_subcat_c2 = self.ui.cbx_scat_c2.currentText()
        user_subcat_c3 = self.ui.cbx_scat_c3.currentText()
        user_subcat_c4 = self.ui.cbx_scat_c4.currentText()

        user_cshades_c1 = int(self.ui.cshades_c1.value())
        user_cshades_c2 = int(self.ui.cshades_c2.value())
        user_cshades_c3 = int(self.ui.cshades_c3.value())
        user_cshades_c4 = int(self.ui.cshades_c4.value())

        user_colormap = str(self.ui.cbx_legend.currentText())
        user_resolution = int(self.ui.resolution.value())

        key_f1 = user_cat_c1 + '-' + user_subcat_c1
        key_f2 = user_cat_c2 + '-' + user_subcat_c2
        key_f3 = user_cat_c3 + '-' + user_subcat_c3
        key_f4 = user_cat_c4 + '-' + user_subcat_c4

        xi = np.linspace(-500, 500, user_resolution)
        yi = np.linspace(-500, 500, user_resolution)

        user_mod1 = self.ui.cbx_mod1.currentText()
        user_mod2 = self.ui.cbx_mod2.currentText()

        if self.ui.radb_freesel.isChecked():

            user_folderpath_m1 = self.ui.input_folder_m1.text()
            user_folderpath_m2 = self.ui.input_folder_m2.text()

            model1 = self.ui.input_model1.text()
            model2 = self.ui.input_model2.text()

            if self.ui.checkbox_folder_m1.isChecked():
                model_path_m1 = user_folderpath_m1 + '/' + model1 + '/'
            else:
                model_path_m1 = 'input_files/' + model1 + '/'

            if self.ui.checkbox_folder_m2.isChecked():
                model_path_m2 = user_folderpath_m2 + '/' + model2 + '/'
            else:
                model_path_m2 = 'input_files/' + model2 + '/'

            if user_mod1 == model1 and user_mod2 == model2:
                model_path1 = model_path_m1
                model_path2 = model_path_m2
            elif user_mod2 == model1 and user_mod1 == model2:
                model_path1 = model_path_m2
                model_path2 = model_path_m1
            elif user_mod1 == model1 and user_mod2 == model1:
                model_path1 = model_path_m1
                model_path2 = model_path_m1
            elif user_mod1 == model2 and user_mod2 == model2:
                model_path1 = model_path_m2
                model_path2 = model_path_m2

        elif self.ui.radb_predsel.isChecked():

            depth_m1 = self.ui.cbx_inp_depth_m1.currentText()
            depth_m2 = self.ui.cbx_inp_depth_m2.currentText()

            loadstep_m1 = self.ui.cbx_inp_loadstep_m1.currentText()
            loadstep_m2 = self.ui.cbx_inp_loadstep_m2.currentText()

            model1 = self.ui.cbx_inp_model_m1.currentText()
            model2 = self.ui.cbx_inp_model_m2.currentText()

            model_path_m1 = predef_paths(depth_m1, model1, loadstep_m1)
            model_path_m2 = predef_paths(depth_m2, model2, loadstep_m2)

            comp_m1 = model1 + '_' + loadstep_m1
            comp_m2 = model2 + '_' + loadstep_m2

            if user_mod1 == comp_m1 and user_mod2 == comp_m2:
                model_path1 = model_path_m1
                model_path2 = model_path_m2
            elif user_mod2 == comp_m1 and user_mod1 == comp_m2:
                model_path1 = model_path_m2
                model_path2 = model_path_m1
            elif user_mod1 == comp_m1 and user_mod2 == comp_m1:
                model_path1 = model_path_m1
                model_path2 = model_path_m1
            elif user_mod1 == comp_m2 and user_mod2 == comp_m2:
                model_path1 = model_path_m2
                model_path2 = model_path_m2

        # Calculations
        results_mod1 = ans_csvdataimp_complete(model_path1)
        results_mod2 = ans_csvdataimp_complete(model_path2)

        xval_f1_m1, yval_f1_m1, zval_f1_m1, chead_f1_m1, output_title_f1_m1 = plot_df(results_mod1, input_output, key_f1)
        xval_f2_m1, yval_f2_m1, zval_f2_m1, chead_f2_m1, output_title_f2_m1 = plot_df(results_mod1, input_output, key_f2)
        xval_f3_m1, yval_f3_m1, zval_f3_m1, chead_f3_m1, output_title_f3_m1 = plot_df(results_mod1, input_output, key_f3)
        xval_f4_m1, yval_f4_m1, zval_f4_m1, chead_f4_m1, output_title_f4_m1 = plot_df(results_mod1, input_output, key_f4)

        xval_f1_m2, yval_f1_m2, zval_f1_m2, chead_f1_m2, output_title_f1_m2 = plot_df(results_mod2, input_output, key_f1)
        xval_f2_m2, yval_f2_m2, zval_f2_m2, chead_f2_m2, output_title_f2_m2 = plot_df(results_mod2, input_output, key_f2)
        xval_f3_m2, yval_f3_m2, zval_f3_m2, chead_f3_m2, output_title_f3_m2 = plot_df(results_mod2, input_output, key_f3)
        xval_f4_m2, yval_f4_m2, zval_f4_m2, chead_f4_m2, output_title_f4_m2 = plot_df(results_mod2, input_output, key_f4)

        min_f1, max_f1 = graduation(results_mod1, results_mod2, input_output, key_f1)
        min_f2, max_f2 = graduation(results_mod1, results_mod2, input_output, key_f2)
        min_f3, max_f3 = graduation(results_mod1, results_mod2, input_output, key_f3)
        min_f4, max_f4 = graduation(results_mod1, results_mod2, input_output, key_f4)

        user_graduation_f1 = np.linspace(min_f1, max_f1, user_cshades_c1, endpoint=True)
        user_graduation_f2 = np.linspace(min_f2, max_f2, user_cshades_c2, endpoint=True)
        user_graduation_f3 = np.linspace(min_f3, max_f3, user_cshades_c3, endpoint=True)
        user_graduation_f4 = np.linspace(min_f4, max_f4, user_cshades_c4, endpoint=True)

        colm = colormap(user_colormap)

        fig = plt.figure(constrained_layout=True, figsize=(18, 9))

        spec = gridspec.GridSpec(ncols=4, nrows=2, figure=fig)

        # figure 1

        f1_ax1 = fig.add_subplot(spec[0, 0])
        # Contour plot
        zi = griddata((xval_f1_m1, yval_f1_m1), zval_f1_m1, (xi[None, :], yi[:, None]), method='linear')
        cf_f1_1 = plt.contourf(xi, yi, zi, user_graduation_f1, cmap=colm)

        f1_ax1.axes.get_xaxis().set_visible(False)

        plt.ylabel(user_mod1)

        plt.title(output_title_f1_m1)

        f1_ax2 = fig.add_subplot(spec[1, 0])
        # Contour plot
        zi = griddata((xval_f1_m2, yval_f1_m2), zval_f1_m2, (xi[None, :], yi[:, None]), method='linear')
        cf_f1_2 = plt.contourf(xi, yi, zi, user_graduation_f1, cmap=colm)

        plt.ylabel(user_mod2)

        fig.colorbar(cf_f1_1, location='bottom')

        # figure 2

        f2_ax1 = fig.add_subplot(spec[0, 1])
        zi = griddata((xval_f2_m1, yval_f2_m1), zval_f2_m1, (xi[None, :], yi[:, None]), method='linear')
        cf_f2_1 = plt.contourf(xi, yi, zi, user_graduation_f2, cmap=colm)

        f2_ax1.axes.get_xaxis().set_visible(False)
        f2_ax1.axes.get_yaxis().set_visible(False)

        plt.title(output_title_f2_m1)

        f2_ax2 = fig.add_subplot(spec[1, 1])
        # Contour plot
        zi = griddata((xval_f2_m2, yval_f2_m2), zval_f2_m2, (xi[None, :], yi[:, None]), method='linear')
        cf_f2_2 = plt.contourf(xi, yi, zi, user_graduation_f2, cmap=colm)

        f2_ax2.axes.get_yaxis().set_visible(False)

        fig.colorbar(cf_f2_1, location='bottom')

        # figure 3

        f3_ax1 = fig.add_subplot(spec[0, 2])
        zi = griddata((xval_f3_m1, yval_f3_m1), zval_f3_m1, (xi[None, :], yi[:, None]), method='linear')
        cf_f3_1 = plt.contourf(xi, yi, zi, user_graduation_f3, cmap=colm)

        f3_ax1.axes.get_xaxis().set_visible(False)
        f3_ax1.axes.get_yaxis().set_visible(False)

        plt.title(output_title_f3_m1)

        f3_ax2 = fig.add_subplot(spec[1, 2])
        zi = griddata((xval_f3_m2, yval_f3_m2), zval_f3_m2, (xi[None, :], yi[:, None]), method='linear')
        cf_f3_2 = plt.contourf(xi, yi, zi, user_graduation_f3, cmap=colm)

        f3_ax2.axes.get_yaxis().set_visible(False)

        fig.colorbar(cf_f3_1, location='bottom')

        # figure 4

        f4_ax1 = fig.add_subplot(spec[0, 3])
        # Contour plot
        zi = griddata((xval_f4_m1, yval_f4_m1), zval_f4_m1, (xi[None, :], yi[:, None]), method='linear')
        cf_f4_1 = plt.contourf(xi, yi, zi, user_graduation_f4, cmap=colm)

        f4_ax1.axes.get_xaxis().set_visible(False)
        f4_ax1.axes.get_yaxis().set_visible(False)

        plt.title(output_title_f4_m1)

        f4_ax2 = fig.add_subplot(spec[1, 3])
        zi = griddata((xval_f4_m2, yval_f4_m2), zval_f4_m2, (xi[None, :], yi[:, None]), method='linear')
        cf_f4_2 = plt.contourf(xi, yi, zi, user_graduation_f4, cmap=colm)

        f4_ax2.axes.get_yaxis().set_visible(False)

        fig.colorbar(cf_f4_1, location='bottom')

        plt.show()

    def plot_differences(self):
        user_cat_c1 = self.ui.cbx_cat_c1.currentText()
        user_cat_c2 = self.ui.cbx_cat_c2.currentText()
        user_cat_c3 = self.ui.cbx_cat_c3.currentText()
        user_cat_c4 = self.ui.cbx_cat_c4.currentText()

        user_subcat_c1 = self.ui.cbx_scat_c1.currentText()
        user_subcat_c2 = self.ui.cbx_scat_c2.currentText()
        user_subcat_c3 = self.ui.cbx_scat_c3.currentText()
        user_subcat_c4 = self.ui.cbx_scat_c4.currentText()

        user_cshades_c1 = int(self.ui.cshades_c1.value())
        user_cshades_c2 = int(self.ui.cshades_c2.value())
        user_cshades_c3 = int(self.ui.cshades_c3.value())
        user_cshades_c4 = int(self.ui.cshades_c4.value())

        user_colormap = str(self.ui.cbx_legend.currentText())
        user_resolution = int(self.ui.resolution.value())

        key_f1 = user_cat_c1 + '-' + user_subcat_c1
        key_f2 = user_cat_c2 + '-' + user_subcat_c2
        key_f3 = user_cat_c3 + '-' + user_subcat_c3
        key_f4 = user_cat_c4 + '-' + user_subcat_c4

        xi = np.linspace(-500, 500, user_resolution)
        yi = np.linspace(-500, 500, user_resolution)

        user_mod1 = self.ui.cbx_mod1.currentText()
        user_mod2 = self.ui.cbx_mod2.currentText()

        label_diff = 'Difference: ' + str(user_mod2) + ' - ' + str(user_mod1)

        if self.ui.radb_freesel.isChecked():

            user_folderpath_m1 = self.ui.input_folder_m1.text()
            user_folderpath_m2 = self.ui.input_folder_m2.text()

            model1 = self.ui.input_model1.text()
            model2 = self.ui.input_model2.text()

            if self.ui.checkbox_folder_m1.isChecked():
                model_path_m1 = user_folderpath_m1 + '/' + model1 + '/'
            else:
                model_path_m1 = 'input_files/' + model1 + '/'

            if self.ui.checkbox_folder_m2.isChecked():
                model_path_m2 = user_folderpath_m2 + '/' + model2 + '/'
            else:
                model_path_m2 = 'input_files/' + model2 + '/'

            if user_mod1 == model1 and user_mod2 == model2:
                model_path1 = model_path_m1
                model_path2 = model_path_m2
            elif user_mod2 == model1 and user_mod1 == model2:
                model_path1 = model_path_m2
                model_path2 = model_path_m1
            elif user_mod1 == model1 and user_mod2 == model1:
                model_path1 = model_path_m1
                model_path2 = model_path_m1
            elif user_mod1 == model2 and user_mod2 == model2:
                model_path1 = model_path_m2
                model_path2 = model_path_m2

        elif self.ui.radb_predsel.isChecked():

            depth_m1 = self.ui.cbx_inp_depth_m1.currentText()
            depth_m2 = self.ui.cbx_inp_depth_m2.currentText()

            loadstep_m1 = self.ui.cbx_inp_loadstep_m1.currentText()
            loadstep_m2 = self.ui.cbx_inp_loadstep_m2.currentText()

            model1 = self.ui.cbx_inp_model_m1.currentText()
            model2 = self.ui.cbx_inp_model_m2.currentText()

            model_path_m1 = predef_paths(depth_m1, model1, loadstep_m1)
            model_path_m2 = predef_paths(depth_m2, model2, loadstep_m2)

            comp_m1 = model1 + '_' + loadstep_m1
            comp_m2 = model2 + '_' + loadstep_m2

            if user_mod1 == comp_m1 and user_mod2 == comp_m2:
                model_path1 = model_path_m1
                model_path2 = model_path_m2
            elif user_mod2 == comp_m1 and user_mod1 == comp_m2:
                model_path1 = model_path_m2
                model_path2 = model_path_m1
            elif user_mod1 == comp_m1 and user_mod2 == comp_m1:
                model_path1 = model_path_m1
                model_path2 = model_path_m1
            elif user_mod1 == comp_m2 and user_mod2 == comp_m2:
                model_path1 = model_path_m2
                model_path2 = model_path_m2

        results_mod1 = ans_csvdataimp_complete(model_path1)
        results_mod2 = ans_csvdataimp_complete(model_path2)

        xval_f1_diff1, yval_f1_diff1, zval_f1_diff1, chead_f1_diff1, output_title_f1_diff1, min_diff_f1, max_diff_f1= plot_diff_df(results_mod1, results_mod2, input_output, key_f1)
        xval_f2_diff1, yval_f2_diff1, zval_f2_diff1, chead_f2_diff1, output_title_f2_diff1, min_diff_f2, max_diff_f2 = plot_diff_df(results_mod1, results_mod2, input_output, key_f2)
        xval_f3_diff1, yval_f3_diff1, zval_f3_diff1, chead_f3_diff1, output_title_f3_diff1, min_diff_f3, max_diff_f3 = plot_diff_df(results_mod1, results_mod2, input_output, key_f3)
        xval_f4_diff1, yval_f4_diff1, zval_f4_diff1, chead_f4_diff1, output_title_f4_diff1, min_diff_f4, max_diff_f4 = plot_diff_df(results_mod1, results_mod2, input_output, key_f4)


        user_graduation_diff_f1 = np.linspace(min_diff_f1, max_diff_f1, user_cshades_c1, endpoint=True)
        user_graduation_diff_f2 = np.linspace(min_diff_f2, max_diff_f2, user_cshades_c2, endpoint=True)
        user_graduation_diff_f3 = np.linspace(min_diff_f3, max_diff_f3, user_cshades_c3, endpoint=True)
        user_graduation_diff_f4 = np.linspace(min_diff_f4, max_diff_f4, user_cshades_c4, endpoint=True)


        colm = colormap(user_colormap)

        fig_diff = plt.figure(constrained_layout=True, figsize=(18, 4.5))

        spec_diff = gridspec.GridSpec(ncols=4, nrows=1, figure=fig_diff)
        fig_diff.suptitle(label_diff, fontsize=10)

        # figure 1

        f1_diff_ax1 = fig_diff.add_subplot(spec_diff[0, 0])
        # Contour plot
        zi = griddata((xval_f1_diff1, yval_f1_diff1), zval_f1_diff1, (xi[None, :], yi[:, None]), method='linear')
        cf_f1_1 = plt.contourf(xi, yi, zi, user_graduation_diff_f1, cmap=colm)

        plt.ylabel('differences')

        plt.title(output_title_f1_diff1)
        fig_diff.colorbar(cf_f1_1, location='bottom')

        # figure 2

        f2_diff_ax1 = fig_diff.add_subplot(spec_diff[0, 1])
        zi = griddata((xval_f2_diff1, yval_f2_diff1), zval_f2_diff1, (xi[None, :], yi[:, None]), method='linear')
        cf_f2_1 = plt.contourf(xi, yi, zi, user_graduation_diff_f2, cmap=colm)

        f2_diff_ax1.axes.get_yaxis().set_visible(False)

        plt.title(output_title_f2_diff1)

        fig_diff.colorbar(cf_f2_1, location='bottom')

        # figure 3

        f3_diff_ax1 = fig_diff.add_subplot(spec_diff[0, 2])
        zi = griddata((xval_f3_diff1, yval_f3_diff1), zval_f3_diff1, (xi[None, :], yi[:, None]), method='linear')
        cf_f3_1 = plt.contourf(xi, yi, zi, user_graduation_diff_f3, cmap=colm)

        f3_diff_ax1.axes.get_yaxis().set_visible(False)

        plt.title(output_title_f3_diff1)

        fig_diff.colorbar(cf_f3_1, location='bottom')

        # figure 4

        f4_diff_ax1 = fig_diff.add_subplot(spec_diff[0, 3])
        # Contour plot
        zi = griddata((xval_f4_diff1, yval_f4_diff1), zval_f4_diff1, (xi[None, :], yi[:, None]), method='linear')
        cf_f4_1 = plt.contourf(xi, yi, zi, user_graduation_diff_f4, cmap=colm)

        f4_diff_ax1.axes.get_yaxis().set_visible(False)

        plt.title(output_title_f4_diff1)

        fig_diff.colorbar(cf_f4_1, location='bottom')

        plt.show()


window = MainWindow()

window.show()

sys.exit(app.exec_())