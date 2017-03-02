import unittest

class SimplisticTest(unittest.TestCase):

	def test(self):
		self.assertTrue(True)


class OutcomesTest(unittest.TestCase):
	def test_pass(self):
		self.assertTrue(True, 'This could be true')

	def test_fail(self):
		self.assertTrue(False, 'This could be true')

	def test_error(self):
		raise RuntimeError('Test error!')

class FixtureTest(unittest.TestCase):

	def setUp(self):
		print ('In setUp()')
		self.fixture = range(1, 10)

	def tearDown(self):
		print('In tearDown()')
		del self.fixture

	def test(self):
		print ('in test()')
		self.assertEqual(self.fixture, range(1, 10))

if __name__ == '__main__':
	unittest.main()