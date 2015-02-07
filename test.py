from tests import quadtree_test
tests = [quadtree_test]
if __name__=="__main__":
	for test in tests:
		test.run()
		test.print_results()
