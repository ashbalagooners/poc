import unittest
from pageobjects.base import selenium_driver
from pageobjects.login.loginpageobject import LoginPageObject
from pageobjects.page.statisticscommentpageobject import StatisticsCommentPageObject
from pageobjects.page.statisticsfollowingpageobject import StatisticsFollowingPageObject
from pageobjects.page.statisticsplaypageobject import StatisticsPlayPageObject
from pageobjects.page.statisticssharingpageobject import StatisticsSharingPageObject
from pageobjects.page.statisticsviewpageobject import StatisticsViewPageObject


class StatisticsPageTests(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.driver.implicitly_wait(10)

        self.base_url = selenium_driver.base_url

    def test_look_extended_statistics(self):
        self.login()

        stat = StatisticsViewPageObject(self.driver, self.base_url)
        stat.view_day_statistic()
        stat.view_week_statistic()
        stat.view_month_statistic()

        stat2 = StatisticsPlayPageObject(self.driver, self.base_url)
        stat2.view_day_statistic()
        stat2.view_week_statistic()
        stat2.view_month_statistic()

        stat3 = StatisticsCommentPageObject(self.driver, self.base_url)
        stat3.view_day_statistic()
        stat3.view_week_statistic()
        stat3.view_month_statistic()

        stat4 = StatisticsFollowingPageObject(self.driver, self.base_url)
        stat4.view_day_statistic()
        stat4.view_week_statistic()
        stat4.view_month_statistic()

        stat5 = StatisticsSharingPageObject(self.driver, self.base_url)
        stat5.view_day_statistic()
        stat5.view_week_statistic()
        stat5.view_month_statistic()

    #TODO: move to general utils
    def login(self):
        lpo = LoginPageObject(self.driver, self.base_url)

        lpo.username = "tjlee@inbox.ru"
        lpo.password = "Welcome01@"
        lpo.submit()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()