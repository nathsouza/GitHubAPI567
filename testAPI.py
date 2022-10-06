#Stevens Institute of Technology - Fall 2022
# SSW 567 - Software Testing, Quality Assurance and Maintenance
# Nathalie Souza
#Homework Assignment #2


import unittest
import gitHubAPI

class TestAPI(unittest.TestCase):

    def testAPIs(self):
        """may not account for new repositories being made i believe but does for increasing commits"""
        # self.assertEqual(gitHubAPI.gitHubAPI.(''), [])
        self.assertGreaterEqual(gitHubAPI.gitHubAPI('richkempinski'), [['csp', 2], ['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], ['Project1', 2], ['richkempinski.github.io', 9], ['threads-of-life', 1], ['try_nbdev', 2], ['try_nbdev2', 5]])

if __name__ == '__main__':
    unittest.main()