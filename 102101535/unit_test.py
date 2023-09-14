import unittest
import text

list_bvid = ["BV1yF411C7ZJ", "BV1Ym4y1K7rg", "BV1Ap4y1E718", "BV1zh4y127Ur", "BV1NG411d7H5", "BV1t94y147Fk", "BV1wu4y1C7bY","BV1Sm4y1T7VL"]
list_cid = ["1245133831", "1264099708", "1245630731", "1248718090", "1250757149", "1253529510","1265320906","1253980657"]


class Mytest(unittest.TestCase):

    def test_bvid(self):
        for i in range(8):
            bvid = text.get_bvid(i, 0)
            self.assertIsNotNone(bvid)

    def test_get_cid(self):
        cid_num = []
        for i in list_bvid:
            cid_num.append(str(text.get_cid(i)))
        self.assertEqual(list_cid, cid_num)

if __name__ == '__main__':
    unittest.main()