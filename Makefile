test:
	pytest tests/*.py

debug_test:
	pytest -s -vvvv tests/*.py

cleandist:
	rm dist/* || true

# version is in prologterms.py
# TODO: manually increment version in python, run . utils/bump.sh, then this
release: cleandist
	python setup.py sdist bdist_wheel
	twine upload dist/*

