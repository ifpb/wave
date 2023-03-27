# WAVE - Gerador de cargas múltiplas para experimentação em redes de computadores

[Manual do Usuário do WAVE](Manual_do_Usuario_do_WAVE.pdf)

[Vídeo Explicativo](https://www.youtube.com/watch?v=AOsvDJgxGQ8&ab_channel=JeffersonLucasFerreiradaSilva)

## Verificando os Requisitos Necessários

### Verificando a se o Python3 está instalado e qual versão:

![wave-version-python3](https://user-images.githubusercontent.com/79940823/227387336-5cf0f04e-d74d-4107-b1c2-121accc85cf9.png)

### Adicionalmente, é necessário o ambiente virtual VirtualEnv:

![wave-version-venv](https://user-images.githubusercontent.com/79940823/227387419-f8e7fa75-5c76-43f3-be66-4af4b83c5b2e.png)


### Verificando os componentes Docker e docker-compose:

![wave-version-docker](https://user-images.githubusercontent.com/79940823/227387459-b2ac5df2-aa2a-4a2e-9487-dac1e23f2dad.png)

![wave-version-docker-compose](https://user-images.githubusercontent.com/79940823/227387519-fb43dd4b-1826-4065-931e-4088bc64f132.png)

### Verificando qual versão do VirtualBox está instalada:

![wave-version-virtualbox](https://user-images.githubusercontent.com/79940823/227387550-05df777e-e121-4f49-b1ff-753dd32b4489.png)

### Verificando qual versão do Vagrant está instalada:

![wave-version-vagrant](https://user-images.githubusercontent.com/79940823/227387581-f5448336-2242-438f-b70c-8aa410fefca3.png)

As versões apresentadas nas figuras foram aquelas testadas no momento de elaboração deste manual.

## Baixando o Código e Iniciando o Ambiente

### Clonando o repositório oficial e iniciando o sistema:

```
$ git clone https://github.com/ifpb/wave.git
$ cd wave
$ ./app-compose.sh --start
```

### Verificando a execução em ambiente Docker:

![wave-cli-docker](https://user-images.githubusercontent.com/79940823/227387624-3d84cb78-2fe4-4b6d-8c37-09f71cf9eb9d.png)

Como pode ser observado na figura acima, o módulo de Inicialização do WAVE utiliza dois contêineres para sua execução: wave_app e grafana-oss. Ao lado esquerdo da figura temos a saída do comando de inicialização do WAVE.

### O módulo WAVE Web pode ser acessado via navegador:

![wave-web-home](https://user-images.githubusercontent.com/79940823/227392316-1a45422c-8d38-4562-9094-6a39302bae98.png)

O formulário contém campos para inserir dados de rede tanto da origem da carga de tráfego quanto do destino. Além do endereço IP e gateway (caso origem e destino estiverem em redes separadas), é possível selecionar o provisionamento do ambiente através de máquina virtual com configuração de tamanho de memória e quantidade de CPUs virtuais. A opção de provisionamento por contêiner e a comunicação via gateway são funcionalidades futuras, ainda não implementadas. Por fim, o usuário pode escolher qual modelo de carga de trabalho ele deseja aplicar, seja sinusoid ou flashcrowd.

## Encerrando a Execução do WAVE

### Finalizando e removendo o ambiente de contêineres:

```
$ ./app-compose.sh --destroy
```

Ao executar o comando acima, o usuário finaliza o módulo WAVE WEB e remove os contêineres responsáveis pelos demais módulos iniciados. Para reiniciar todo o sistema basta executar o mesmo comando, porém, substituindo o argumento "--destroy" por "--start".
