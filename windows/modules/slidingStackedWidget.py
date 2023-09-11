from PySide6 import QtWidgets, QtCore


class SlidingStackedWidget(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super(SlidingStackedWidget, self).__init__(parent)

        self.movingDirection = QtCore.Qt.Orientation.Horizontal
        self.movingSpeed = 500
        self.movingAnimationType = QtCore.QEasingCurve.Type.OutCubic
        self.movingNow = 0
        self.movingNext = 0
        self.movingWrap = False
        self.currentPosition = QtCore.QPoint(0, 0)
        self.movingActive = False

    def set_direction(self, direction):
        self.movingDirection = direction

    def set_speed(self, speed):
        self.movingSpeed = speed

    def set_animation(self, animation_type):
        self.movingAnimationType = animation_type

    def set_wrap(self, wrap):
        self.movingWrap = wrap

    @QtCore.Slot()
    def slide_backward(self):
        now = self.currentIndex()
        if self.movingWrap or now > 0:
            self.slide_by_the_index(now - 1)

    @QtCore.Slot()
    def slide_forward(self):
        now = self.currentIndex()
        if self.movingWrap or now < (self.count() - 1):
            self.slide_by_the_index(now + 1)

    def slide_by_the_index(self, index):
        if index > (self.count() - 1):
            index = index % self.count()
        elif index < 0:
            index = (index + self.count()) % self.count()
        self.slideInWgt(self.widget(index))

    def slideInWgt(self, new_widget):
        if self.movingActive:
            return

        self.movingActive = True

        _now = self.currentIndex()
        _next = self.indexOf(new_widget)

        if _now == _next:
            self.movingActive = False
            return

        offsetX, offsetY = self.frameRect().width(), self.frameRect().height()
        self.widget(_next).setGeometry(self.frameRect())

        if not self.movingDirection == QtCore.Qt.Orientation.Horizontal:
            if _now < _next:
                offsetX, offsetY = 0, -offsetY
            else:
                offsetX = 0
        else:
            if _now < _next:
                offsetX, offsetY = -offsetX, 0
            else:
                offsetY = 0

        nextPosition = self.widget(_next).pos()
        currentPosition = self.widget(_now).pos()
        self.currentPosition = currentPosition

        offset = QtCore.QPoint(offsetX, offsetY)
        self.widget(_next).move(nextPosition - offset)
        self.widget(_next).show()
        self.widget(_next).raise_()

        animationGroup = QtCore.QParallelAnimationGroup(self)
        animationGroup.finished.connect(self.animationDoneSlot)

        for index, start, end in zip(
            (_now, _next), (currentPosition, nextPosition - offset), (currentPosition + offset, nextPosition)
        ):
            animation = QtCore.QPropertyAnimation(self.widget(index), b"pos")
            animation.setDuration(self.movingSpeed)
            animation.setEasingCurve(self.movingAnimationType)
            animation.setStartValue(start)
            animation.setEndValue(end)
            animationGroup.addAnimation(animation)

        self.movingNext = _next
        self.movingNow = _now
        self.movingActive = True
        animationGroup.start(QtCore.QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)

    @QtCore.Slot()
    def animationDoneSlot(self):
        self.setCurrentIndex(self.movingNext)
        self.widget(self.movingNow).hide()
        self.widget(self.movingNow).move(self.currentPosition)
        self.movingActive = False
