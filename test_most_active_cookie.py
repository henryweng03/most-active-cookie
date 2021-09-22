import datetime
import unittest
import most_active_cookie

class Test(unittest.TestCase):
    
    # this validation happens before findMostActive is called and thus must be tested seperately
    def test_date_validation(self):
        self.assertEqual(most_active_cookie.isValidDate("2020-10-01"), True)
        self.assertEqual(most_active_cookie.isValidDate("2010-01-01"), True)
        self.assertEqual(most_active_cookie.isValidDate("202000-10-01"), False)
        self.assertEqual(most_active_cookie.isValidDate("ABCD-10-01"), False)
        self.assertEqual(most_active_cookie.isValidDate("2020-50-01"), False)
        self.assertEqual(most_active_cookie.isValidDate("2020-01-90"), False)
    
    # this validation happens before findMostActive is called and thus must be tested seperately
    def test_file_validation(self):
        self.assertEqual(most_active_cookie.isValidFile("asdf.csv"), True)
        self.assertEqual(most_active_cookie.isValidFile("asdasdasdf.csv"), True)
        self.assertEqual(most_active_cookie.isValidFile("asdf.pdf"), False)
        self.assertEqual(most_active_cookie.isValidFile("asdf.pdfcsv"), False)

    def test_integration(self):
        testCookieLog = [most_active_cookie.Cookie("1", datetime.date(2020, 1, 1)),
        most_active_cookie.Cookie("1", datetime.date(2020, 1, 1)),
        most_active_cookie.Cookie("2", datetime.date(2020, 1, 1)),
        most_active_cookie.Cookie("2", datetime.date(2020, 1, 1)),
        most_active_cookie.Cookie("1", datetime.date(2019, 1, 1)),
        most_active_cookie.Cookie("2", datetime.date(2019, 1, 1)),
        most_active_cookie.Cookie("3", datetime.date(2019, 1, 1)),
        most_active_cookie.Cookie("1", datetime.date(2018, 1, 1)),
        most_active_cookie.Cookie("1", datetime.date(2018, 1, 1)),
        most_active_cookie.Cookie("0", datetime.date(2018, 1, 1)),
        most_active_cookie.Cookie("2", datetime.date(2018, 1, 1)),
        most_active_cookie.Cookie("3", datetime.date(2018, 1, 1)),]

        answer1 = {"1", "2"}
        self.assertEqual(most_active_cookie.findMostActive(most_active_cookie.stringToDateTime("2020-01-01"), testCookieLog), answer1)
        answer2 = {"1", "2", "3"}
        self.assertEqual(most_active_cookie.findMostActive(most_active_cookie.stringToDateTime("2019-01-01"), testCookieLog), answer2)
        answer3 = {"1"}
        self.assertEqual(most_active_cookie.findMostActive(most_active_cookie.stringToDateTime("2018-01-01"), testCookieLog), answer3)
        
        # date not in cookie log
        answer4 = None
        self.assertEqual(most_active_cookie.findMostActive(most_active_cookie.stringToDateTime("2017-01-01"), testCookieLog), answer4)


if __name__ == '__main__':
    unittest.main()