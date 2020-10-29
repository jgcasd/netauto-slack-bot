.PHONY: clean lint format deploy

clean:
	find . -type f -name '*.zip' -delete
	rm -rf build/
	find . -type f -name '*.pyc' -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".terraform" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

lint:
	flake8

format:
	black .

deploy:
	docker build -t netauto-slack-bot .
	docker run --env-file .env -t netauto-slack-bot