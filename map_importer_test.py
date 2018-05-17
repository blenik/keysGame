import unittest
import StringIO as io
from map_importer import MapImporter


class TestMapImoporter(unittest.TestCase):
    def test_readLinesFromFileStream(self):
        testStream = io.StringIO()  # utworzenie strumienia na potrzeby testu
        testStream.write('A')
        testStream.seek(0)  # ustawienie wskaznika na poczatek strumienia

        testList = list()
        returned2DList = self.importer.readLinesFromFileStream(testList, testStream)
        self.assertEqual('A', returned2DList[0][0])

    def setUp(self):
        self.importer = MapImporter()


if __name__ == '__main__':
    unittest.main()