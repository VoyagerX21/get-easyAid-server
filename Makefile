dev:
	docker compose up

stop:
	docker compose down

makei:
	docker build -t voyagerx21/geteasyserver .

tag:
	docker tag voyagerx21/geteasyserver voyagerx21/geteasyserver:latest

pushd:
	docker push voyagerx21/geteasyserver:latest

pushg:
	git push origin main