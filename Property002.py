class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be a integer!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0-100')
        self._score = value


s = Student()
s.score = 90
print(s.score)
