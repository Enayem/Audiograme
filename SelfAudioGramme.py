from math import pi, sin
import struct, sys

from PyQt5.QtCore import QBuffer, QByteArray, QIODevice, Qt, QAbstractTableModel, QModelIndex, QRect
from PyQt5.QtWidgets  import QApplication, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, QSlider, QVBoxLayout, QWidget, QComboBox, QLabel, QGroupBox, QRadioButton, QGridLayout
from PyQt5.QtChart import  QChart,QChartView, QLineSeries, QVXYModelMapper , QAbstractSeries, QLogValueAxis, QValueAxis
from PyQt5.QtMultimedia import QAudio, QAudioDeviceInfo, QAudioFormat, QAudioOutput
from PyQt5.QtGui import QColor, QPainter


class serieOreille(QLineSeries):
    def __init__(self, parent = None):
        QLineSeries.__init__(self, parent)
        self.append(125, 0)
        self.append(250, 0)
        self.append(500, 0)
        self.append(750, 0)
        self.append(1000, 0)
        self.append(2000, 0)
        self.append(3000, 0)
        self.append(4000, 0)
        self.append(6000, 0)
        self.append(8000, 0)




class fenPrincipale(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        principalLayout = QGridLayout(self)


        #######################################################################
        # Layout nom du Device
        #######################################################################

        self.deviceLineEdit = QLineEdit()
        self.deviceLineEdit.setReadOnly(True)
        self.deviceLineEdit.insert(QAudioDeviceInfo.defaultOutputDevice().deviceName())

        deviceLayout = QFormLayout()
        deviceLayout.addRow(self.tr("Device output :"), self.deviceLineEdit)

        #######################################################################
        #Layout Chart Graphique fréquence volume
        #######################################################################


        chartOreilleDroite = QChart()
        chartOreilleDroite.setAnimationOptions(QChart.SeriesAnimations)
        seriesOreilleDroite = serieOreille()
        seriesOreilleDroite.setName("Oreille droite")




        chartOreilleGauche = QChart()
        chartOreilleGauche.setAnimationOptions(QChart.SeriesAnimations)
        seriesOreilleGauche = serieOreille()
        seriesOreilleGauche.setName("Oreille Gauche")




        chartOreilleDroite.addSeries(seriesOreilleDroite)
        chartOreilleGauche.addSeries(seriesOreilleGauche)


        axeDX = QLogValueAxis()
        axeDX.setTitleText("Fréquences")
        axeDX.setBase(10)
        axeDX.setRange(125,8000)


        axeDY = QValueAxis()
        axeDY.setTitleText("Volume")
        axeDY.setTickCount(10)
        axeDY.setRange(0,10)

        axeGX = QLogValueAxis()
        axeGX.setTitleText("Fréquences")
        axeGX.setBase(10)
        axeGX.setRange(125,8000)


        axeGY = QValueAxis()
        axeGY.setTitleText("Volume")
        axeGY.setTickCount(10)
        axeGY.setRange(0,10)


        chartOreilleDroite.addAxis(axeDX, Qt.AlignBottom)
        seriesOreilleDroite.attachAxis(axeDX)
        chartOreilleGauche.addAxis(axeGX, Qt.AlignBottom)
        seriesOreilleGauche.attachAxis(axeGX)

        chartOreilleDroite.addAxis(axeDY, Qt.AlignLeft)
        seriesOreilleDroite.attachAxis(axeDY)
        chartOreilleGauche.addAxis(axeGY, Qt.AlignLeft)
        seriesOreilleGauche.attachAxis(axeGY)

        chartViewOreilleDroite = QChartView(chartOreilleDroite)
        chartViewOreilleDroite.setRenderHint(QPainter.Antialiasing)
        chartViewOreilleDroite.setMinimumSize(400,300)

        chartViewOreilleGauche = QChartView(chartOreilleGauche)
        chartViewOreilleGauche.setRenderHint(QPainter.Antialiasing)
        chartViewOreilleGauche.setMinimumSize(400,300)


        chartOreilleLayout = QHBoxLayout(self)
        chartOreilleLayout.addWidget(chartViewOreilleDroite)
        chartOreilleLayout.addWidget(chartViewOreilleGauche)



        #######################################################################
        # Layout Lancement de test
        #######################################################################


        actionAutomatiqueLayout = QHBoxLayout(self)

        boutonVerifierInstallation = QPushButton("Vérifier l'installation",self)
        boutonLancementTest = QPushButton("Lancer le test",self)

        actionAutomatiqueLayout.addWidget(boutonVerifierInstallation)
        actionAutomatiqueLayout.addWidget(boutonLancementTest)


        #######################################################################
        # Layout GroupBox A
        # Action une fréquence
        #######################################################################
        actionUneFrequenceLayout = QHBoxLayout(self)
        groupActionUnefrequence = QGroupBox("tester une seule fréquence")

        freqLabel = QLabel("Fréquence", self)
        actionUneFrequenceLayout.addWidget(freqLabel)
        listeFrequence = QComboBox(self)
        listeFrequence.addItems(["125","250","500","750","1000","2000","3000","4000","6000","8000"])
        actionUneFrequenceLayout.addWidget(listeFrequence)

        groupGD = QGroupBox("Oreille" ,self)
        radioD = QRadioButton("droite", groupGD)
        radioG = QRadioButton("gauche", groupGD)
        groupGDLayout = QVBoxLayout(self)
        groupGDLayout.addWidget(radioD)
        groupGDLayout.addWidget(radioG)
        groupGDLayout.addStretch(1)
        groupGD.setLayout(groupGDLayout)

        actionUneFrequenceLayout.addWidget(groupGD)

        lancerUneFrequence = QPushButton("Tester la fréquence", self)
        actionUneFrequenceLayout.addWidget(lancerUneFrequence)

        #lancerUneFrequence.clicked.connect(self.lancerTestAudio)

        groupActionUnefrequence.setLayout(actionUneFrequenceLayout)


        ##############################################################################
        # Layout Déroulement du test
        ##############################################################################

        deroulementTestLayout = QVBoxLayout(self)
        groupDeroulementTest = QGroupBox("Test ...")
        labelVol = QLabel("...", self)
        labelVol.setAlignment(Qt.AlignCenter)











        principalLayout.addLayout(deviceLayout, 0, 0, Qt.AlignCenter)
        principalLayout.addLayout(chartOreilleLayout, 1, 0, Qt.AlignCenter)
        principalLayout.addLayout(actionAutomatiqueLayout, 2,0, Qt.AlignLeft)
        principalLayout.addWidget(groupActionUnefrequence,3,0,Qt.AlignLeft)





    #def lancerTestAudio(self):





if __name__ == "__main__":

    app = QApplication(sys.argv)
    fenPrincipale = fenPrincipale()
    fenPrincipale.show()
    sys.exit(app.exec_())
