py=python
cli_name=dvd_shop_cli


local_cli: main.py
	@ $(py) main.py

local_test: test_cart.py
	@pytest

container_cli: Dockerfile
	@docker image build -q -t $(cli_name) . 
	@docker container run -it $(cli_name) python main.py

container_test: test_cart.py
	@docker image build -q -t $(cli_name) . 
	@docker container run -it $(cli_name) pytest test_cart.py
