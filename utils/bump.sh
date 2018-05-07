TAG=v`python setup.py --version`
git add prologterms.py
git commit --message="Upgrade to $TAG"
git push
git tag --annotate $TAG --message="Upgrade to $TAG"
git push --tags
