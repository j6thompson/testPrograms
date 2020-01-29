import ProductionCode


def test_good_data():
	test_data = ["Hi Hi Hi$#%!%, There",
				"There %$ Hi, No"]
	results = ProductionCode.count_words(test_data)
	assert "Hi" in results
	assert results["Hi"] == 4


def test_bad_data1():
	test_data = {}
	results = ProductionCode.count_words(test_data)
	assert len(results) == 0


def test_bad_data2():
	test_data = 234235
	results = ProductionCode.count_words(test_data)
	assert len(results) == 0
