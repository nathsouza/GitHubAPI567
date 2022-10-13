#Stevens Institute of Technology - Fall 2022
# SSW 567 - Software Testing, Quality Assurance and Maintenance
# Nathalie Souza
#Homework Assignment #2


import unittest
import gitHubAPI

class TestAPI(unittest.TestCase):

    def testAPIs(self):
        test =  gitHubAPI.gitHubAPI("nathsouza") 
        actual = {'GitHubAPI567':17, 'SSW567-HW2A-Triangle': 21, 'SSW567-HW1-Triangle': 3, 'stevens-ssw567-fall2022': 3, 'String-Calculator': 2, 'nathsouza.github.io': 8, 'Oenofiles': 6, 'Python': 1, 'python_project_week': 1, 'python_project_week-1': 1, 'mock_project' : 2}
        self.assertDictEqual(test, actual)
        self.assertEqual(len(test.values()), 12)

if __name__ == '__main__':
    unittest.main()
