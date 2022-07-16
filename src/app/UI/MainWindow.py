import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from PyQt5 import QtCore


class MainWindow(BaseWidget):

    def __init__(self):
        super(MainWindow, self).__init__('MainWindow')

        MainWindow.setWindowTitle(self, 'mathsYNX Classic Calculator')
        MainWindow.setFixedHeight(self, 400)
        MainWindow.setFixedWidth(self, 320)
        MainWindow.set_margin(self, 10)

        self._input = ControlText('')
        self._input.value = '0'
        self.processed_input = ''

        # Controls buttons
        self._AC = ControlButton('AC')
        self._AC.value = self._allClear
        self._equals = ControlButton('=')

        # Numeric buttons
        self._zero = ControlButton('0')
        self._zero.value = lambda: self._numericAction(self._zero)
        self._one = ControlButton('1')
        self._one.value = lambda: self._numericAction(self._one)
        self._two = ControlButton('2')
        self._two.value = lambda: self._numericAction(self._two)
        self._three = ControlButton('3')
        self._three.value = lambda: self._numericAction(self._three)
        self._four = ControlButton('4')
        self._four.value = lambda: self._numericAction(self._four)
        self._five = ControlButton('5')
        self._five.value = lambda: self._numericAction(self._five)
        self._six = ControlButton('6')
        self._six.value = lambda: self._numericAction(self._six)
        self._seven = ControlButton('7')
        self._seven.value = lambda: self._numericAction(self._seven)
        self._eight = ControlButton('8')
        self._eight.value = lambda: self._numericAction(self._eight)
        self._nine = ControlButton('9')
        self._nine.value = lambda: self._numericAction(self._nine)

        # Operators buttons
        self._plus = ControlButton('+')
        self._minus = ControlButton('-')
        self._multiply = ControlButton('*')
        self._divide = ControlButton('/')
        self._squared = ControlButton('^2')
        self._power = ControlButton('^')

        self.formset = [
            '_input',
            '=',
            (
                [
                    ('_plus', '_minus', '_multiply'),
                    ('_divide', '_squared', '_power'),
                    ('_seven', '_eight', '_nine'),
                    ('_four', '_five', '_six'),
                    ('_one', '_two', '_three'),
                    ('_AC', '_zero', '_equals'),
                ]
            ),
            '='
        ]

    def _numericAction(self, button):
        """Numeric button action event"""
        if self._input.value[0] == '0':
            new_str = button.label
        else:
            new_str = self._input.value + button.label
        self._input.value = new_str

    def _allClear(self):
        self._input.value = '0'
        self.processed_input = ''


# Execute the application
if __name__ == "__main__":
    pyforms.start_app(MainWindow)
