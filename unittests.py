from most_active_cookie import createCookiesLog, getMostActiveCookies
import unittest

class TestMethods(unittest.TestCase):

    def testCreateCookiesLog(self):
        filename = "test_log.csv"

        date1 = "2018-12-09"
        cookies1 = createCookiesLog(filename, date1)
        test1 = {"AtY0laUfhglK3lC7": 2, "SAZuXPGUrfbcn5UA": 1, "5UAVanZf6UtGyKVS": 1}
        self.assertEqual(cookies1, test1)

        date2 = "2018-12-08"
        cookies2 = createCookiesLog(filename, date2)
        test2 = {"SAZuXPGUrfbcn5UA": 1, "4sMM2LxV07bPJzwf": 1, "fbcn5UAVanZf6UtG": 1}
        self.assertEqual(cookies2, test2)

    def testGetMostActiveCookies(self):
        cookies1 = {"AtY0laUfhglK3lC7": 2, "SAZuXPGUrfbcn5UA": 1, "5UAVanZf6UtGyKVS": 1}
        mostActive1 = getMostActiveCookies(cookies1)
        test1 = ["AtY0laUfhglK3lC7"]
        self.assertEqual(mostActive1, test1)

        cookies2 = {"SAZuXPGUrfbcn5UA": 1, "4sMM2LxV07bPJzwf": 1, "fbcn5UAVanZf6UtG": 1}
        mostActive2 = getMostActiveCookies(cookies2)
        test2 = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        self.assertEqual(mostActive2, test2)

if __name__ == "__main__":
    unittest.main()