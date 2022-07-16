from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlButton
from pyforms.controls import ControlText


class MainWindow(BaseWidget):

    def __init__(self):
        super(MainWindow, self).__init__('MainWindow')
        self.setWindowTitle('mathsYNX Classic Calculator')
        self.setFixedHeight(400)
        self.setFixedWidth(320)
        self.set_margin(10)

        # Text input handling
        self._input = ControlText('')
        self._input.value = '0'
        self.processed_input = ''
        self.previous_calculation = None

        # Controls buttons
        self._AC = ControlButton('AC')
        self._AC.value = self._allClear
        self._equals = ControlButton('=')
        self._equals.value = self._result

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
        self._plus.value = lambda: self._operatorAction(self._plus)
        self._minus = ControlButton('-')
        self._minus.value = lambda: self._operatorAction(self._minus)
        self._multiply = ControlButton('*')
        self._multiply.value = lambda: self._operatorAction(self._multiply)
        self._divide = ControlButton('/')
        self._divide.value = lambda: self._operatorAction(self._divide)
        self._squared = ControlButton('^2')
        self._squared.value = lambda: self._operatorAction(self._squared)
        self._power = ControlButton('^')
        self._power.value = lambda: self._operatorAction(self._power)

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
        """Numeric buttons action event"""
        if self._input.value[0] == '0':
            new_str = button.label
        else:
            new_str = self._input.value + button.label
        self._input.value = new_str

    def _operatorAction(self, button):
        """Operator buttons action event"""
        if self._input.value[0] == '0':
            new_str = self._input.value
        else:
            new_str = self._input.value + ' ' + button.label + ' '
        self._input.value = new_str

    def _allClear(self):
        """Clear all inputs"""
        self._input.value = '0'
        self.processed_input = ''
        self.previous_calculation = None

    def _result(self):
        """Calculation result of the input"""
        self.processed_input = self._input.value.replace('^', '**')
        try:
            self._input.value = str(eval(self.processed_input))
        except SyntaxError as se:
            print(se.msg)
