import unittest

from .transform import Transform


class TransformTest(unittest.TestCase):
    def setUp(self) -> None:
        self.strict_data_dict = {
            "我捡了100块钱": "我捡了一百块钱",
            "用户增长最快的3个城市": "用户增长最快的三个城市"
        }

        self.t = Transform()

    def test_transform(self) -> None:
        for strict_item in self.strict_data_dict.keys():
            self.assertEqual(self.t.transform(strict_item, "an2cn"), self.strict_data_dict[strict_item])
            self.assertEqual(self.t.transform(self.strict_data_dict[strict_item], "cn2an"), strict_item)


if __name__ == '__main__':
    unittest.main()
