import unittest
import sys
import importlib

def run_all():
  tests = unittest.defaultTestLoader.discover('./test')
  results = unittest.TestResult()
  tests.run(results)
  print_results(results)

def run_suite(ty, test_case_class_name):
  module = importlib.import_module('test.{}'.format(ty))
  test_class = getattr(module, test_case_class_name)
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
  results = unittest.TestResult()
  suite.run(results)
  print_results(results)

def run_case(ty, test_case_class_name, test_to_run):
  """ Not fully implemented yet """
  module = importlib.import_module('test.{}'.format(ty))
  test_class = getattr(module, test_case_class_name)
  tests = unittest.defaultTestLoader.getTestCaseNames(test_class)
  if test_to_run not in tests:
    print('Test case not found')
    return
  suite = unittest.TestSuite()
  suite.addTest(getattr(test_class(), test_to_run))
  results = unittest.TestResult()
  suite.run(results)
  print_results(results)
  
def print_results(results):
  print('############## RESULTS ##############')
  print('Failures: {}'.format(results.failures or 0))
  print('Errors: {}'.format(results.errors or 0))
  print('Skipped: {}'.format(results.skipped or 0))
  print('Total Run: {}'.format(results.testsRun))
  
if __name__ == '__main__':
  if (len(sys.argv) == 1):
    run_all()
  elif sys.argv[1] == 'suite':
    run_suite(sys.argv[2], sys.argv[3])
  elif sys.argv[1] == 'case':
    print('Not implemented yet.  Use the suite argument instead')
    #run_case(sys.argv[2], sys.argv[3], sys.argv[4])