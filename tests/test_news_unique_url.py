import unittest

from newsable.DB import MongoDB

class TestNewsUniqueUrl(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def bernama(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','bernama')
        db.setUnique('url')
        db.__del__()
    
    def borneoPost(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','theBorneoPost')
        db.setUnique('url')
        db.__del__()

    def freeMalaysiaToday(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','freeMalaysiaToday')
        db.setUnique('url')
        db.__del__()
    
    def ipohEcho(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','ipohEcho')
        db.setUnique('url')
        db.__del__()

    def malayMail(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','malayMail')
        db.setUnique('url')
        db.__del__()

    def malaysiaChronicle(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','malaysiaChronicle')
        db.setUnique('url')
        db.__del__()

    def theMalaysianInsider(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','theMalaysianInsider')
        db.setUnique('url')
        db.__del__()
    
    def theStar(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','theStar')
        db.setUnique('url')
        db.__del__()
           
    def theSunDaily(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('news','theSunDaily')
        db.setUnique('url')
        db.__del__()
    
if __name__ == '__main__':
    #unittest.main()
    tests = ['bernama', 'borneoPost', 'freeMalaysiaToday', 'ipohEcho', 'malayMail', 'malaysiaChronicle', 'theMalaysianInsider', 'theStar', 'theSunDaily']
    #tests = ['theSunDaily']
    testClass = TestNewsUniqueUrl
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)