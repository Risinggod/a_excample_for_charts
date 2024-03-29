from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt, QDateTime, pyqtSlot, QTimer
import random


# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class DateTime(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.series = QSplineSeries()
        self.series1 = QSplineSeries()

        self.timer = QTimer()




        chart = QChart()
        chart.setTitle("Die wunderbare Welt der Mathematik")
        chart.addSeries(self.series)
        chart.addSeries(self.series1)

        self.date_time_axis = QDateTimeAxis()
        self.date_time_axis.setFormat("d.MM hh:mm")

        start_date_time = QDateTime().currentDateTime()

        end_date_time = QDateTime().currentDateTime().addSecs(5 * 60)

        self.date_time_axis.setRange(start_date_time, end_date_time)

        axis_y = QValueAxis()
        axis_y.setRange(-5, 5)

        chart.addAxis(self.date_time_axis, Qt.AlignmentFlag.AlignTop)

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        self.series.attachAxis(self.date_time_axis)
        self.series.attachAxis(axis_y)

        self.series1.attachAxis(self.date_time_axis)
        self.series1.attachAxis(axis_y)

        self.series.setName("Values from Slider")

        self.series1.setName("Values from randome")

        self.setChart(chart)

    @pyqtSlot(int)
    def add_value(self, value):
        current_time = QDateTime.currentDateTime()
        start_time = current_time.addSecs(-30)

        self.series.append(current_time.toMSecsSinceEpoch(), value)

        self.date_time_axis.setRange(start_time, current_time)

    @pyqtSlot(int)
    def add_random_value(self, value):
        current_time = QDateTime.currentDateTime()
        start_time = current_time.addSecs(-30)

        self.series1.append(current_time.toMSecsSinceEpoch(), value)

        self.date_time_axis.setRange(start_time, current_time)

