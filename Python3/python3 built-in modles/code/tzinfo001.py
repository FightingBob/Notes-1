from datetime import tzinfo, datetime, timedelta


class UTC(tzinfo):

    def __init__(self, offset=0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +{}".format(self._offset)

    def dst(self, dt):
        return timedelta(hours=self._offset)


beijing = datetime(2018,1,13, tzinfo=UTC(8))
bangkok = datetime(2018,1,13, tzinfo=UTC(7))


print(beijing)
print(bangkok)
print(beijing.astimezone((UTC(7))))