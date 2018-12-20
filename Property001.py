class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be a integer!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0-100!')
        self._score = value


s = Student()
s.set_score(99)
print(s.get_score())
