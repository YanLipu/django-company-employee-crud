# API com Django

https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5
https://www.youtube.com/watch?v=diB38AvVkHw

Este é um guia para execução do projeto no Ubuntu.

## Passo 1: Instalar o Docker (caso já tenha instalado, pule para o passo 2)

### Docker e docker compose pré requisitos
```
sudo apt-get install curl
sudo apt-get install gnupg
sudo apt-get install ca-certificates
sudo apt-get install lsb-release
```
### Download do arquivo gpg para Ubuntu

```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### Adicionando Docker e Docker Compose para o gerenciador de pacotes do Ubuntu

```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-pluginsudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-pluginlinux/ubuntu   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```

### Instalar Docker e Docker Compose

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### Checar se a instalação ocorreu corretamente

```
sudo docker run hello-world
```

## Passo 2: Execução do servidor

Para executar o servidor navegue até o diretório onde o repositório foi clonado e digite o seguinte comando:

```
docker-compose up -d --build
```

Se tudo ocorrer bem o servidor estará rodando no endereço `localhost:8000`

## Passo 3: Teste das rotas

Faça o download e instalação do Postman [aqui.](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-linux)

Após instalado, importe o arquivo `Django_API.postman_collection.json` na raiz desse diretório.

Após isso basta testar as rotas.

# django-company-employee-crud
