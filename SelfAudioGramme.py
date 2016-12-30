from math import pi, sin
import struct, sys

from PyQt5.QtCore import QBuffer, QByteArray, QIODevice, Qt, QAbstractTableModel
from PyQt5.QtWidgets  import QApplication, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, QSlider, QVBoxLayout, QWidget
from PyQt5.QtChart import  QChart,QChartView, QLineSeries, QVXYModelMapper
from PyQt5.QtMultimedia import QAudio, QAudioDeviceInfo, QAudioFormat, QAudioOutput




class dataOreille(QAbstractTableModel):
    def __init__(self, parent = None):
        super(dataOreille, self).__init__(parent)

        self.m_columnCount = 1
        self.m_rowCount = 11

        self.m_data = []
        self.m_mapping = {}


        self.dictFreqence = {125:0, 250 : 0, 500: 0, 750:0, 1000:0, 1500:0, 2000:0, 3000:0, 4000:0, 6000:0, 8000:0}



class Window(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        self.deviceLineEdit = QLineEdit()
        self.deviceLineEdit.setReadOnly(True)
        self.deviceLineEdit.insert(QAudioDeviceInfo.defaultOutputDevice().deviceName())

        deviceLayout = QFormLayout()
        deviceLayout.addRow(self.tr("Device output :"), self.deviceLineEdit)



        chartOreilleDroite = QChart()
        chartOreilleDroite.setAnimationOptions(QChart.AllAnimations)

        seriesOreilleDroite = QLineSeries()
        seriesOreilleDroite.setName("Oreille droite")

        mapper = QVXYModelMapper(self)
        mapper.setXColumn(0)
        mapper.setYColumn(1)
        mapper.setSeries(seriesOreilleDroite)
        mapper.setModel(model)
        chartOreilleDroite.addSeries(seriesOreilleDroite)





        principalLayout = QVBoxLayout(self)

        principalLayout.addLayout(deviceLayout)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
