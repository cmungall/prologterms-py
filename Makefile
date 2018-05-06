test:
	pytest tests/*.py

debug_test:
	pytest -s -vvvv tests/*.py

cleandist:
	rm dist/* || true

# TODO: manually increment version in python, run . bump.sh, then this
release: cleandist
	python setup.py sdist bdist_wheel
	twine upload dist/*

