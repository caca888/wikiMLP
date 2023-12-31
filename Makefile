install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			python -m textblob.download_corpora

test:
	python -m pytest -vv --cov=src/. ./tests/.

format:
	black src/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' --ignore-patterns=tests/test_.*?py src/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

generate: 
	python setup.py install &&\
		python setup.py build

deploy:
	#deploy goes here

all: install lint test format deploy