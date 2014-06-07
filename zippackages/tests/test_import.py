from unittest import TestCase

class TestImport(TestCase):
	def test_can_import_django(self):
		import zippackages
		import zippackagefakemodule
		self.assertTrue(zippackagefakemodule.has_loaded())
