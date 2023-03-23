# WAVE - Gerador de cargas múltiplas para experimentação em redes de computadores

## Configurator WAVE 


## 1 Verificando os Requisitos Necessários

1.1 Verificando a se o Python3 [7] está instalado e qual versão:

![wave-version-python3](https://user-images.githubusercontent.com/79940823/227387336-5cf0f04e-d74d-4107-b1c2-121accc85cf9.png)


1.2 Adicionalmente, é necessário o ambiente virtual VirtualEnv:

![wave-version-venv](https://user-images.githubusercontent.com/79940823/227387419-f8e7fa75-5c76-43f3-be66-4af4b83c5b2e.png)


1.3 Verificando os componentes Docker [3] e docker-compose:

![wave-version-docker](https://user-images.githubusercontent.com/79940823/227387459-b2ac5df2-aa2a-4a2e-9487-dac1e23f2dad.png)


![wave-version-docker-compose](https://user-images.githubusercontent.com/79940823/227387519-fb43dd4b-1826-4065-931e-4088bc64f132.png)


1.4 Verificando qual versão do VirtualBox [10] está instalada:

![wave-version-virtualbox](https://user-images.githubusercontent.com/79940823/227387550-05df777e-e121-4f49-b1ff-753dd32b4489.png)


1.5 Verificando qual versão do Vagrant [9] está instalada:

![wave-version-vagrant](https://user-images.githubusercontent.com/79940823/227387581-f5448336-2242-438f-b70c-8aa410fefca3.png)


As versões apresentadas nas figuras dos passos 1.1-1.5 foram aquelas
testadas no momento de elaboração deste manual.

## 2 Baixando o Código e Iniciando o Ambiente

2.1 Clonando o repositório oficial e iniciando o sistema:

![image](https://user-images.githubusercontent.com/79940823/227388516-955400f2-7055-450b-84d5-913a3e205836.png)


2.2 Verificando a execução em ambiente Docker:

![wave-cli-docker](https://user-images.githubusercontent.com/79940823/227387624-3d84cb78-2fe4-4b6d-8c37-09f71cf9eb9d.png)


Como pode ser observado na figura acima, o módulo de Inicialização
do WAVE utiliza dois contêineres para sua execução: wave_app e
grafana-oss. Ao lado esquerdo da figura temos a saída do comando
de inicialização do WAVE, ou seja, saída da linha 3 do código exibido
na seção 2.1.
2.3 O módulo WAVE Web pode ser acessado via navegador:

![wave-web-deprovisioned](https://user-images.githubusercontent.com/79940823/227387686-634fc6ee-bb3c-4bb4-9ef0-28e8e0459175.png)

O formulário contém campos para inserir dados de rede tanto da
origem da carga de tráfego quanto do destino. Além do endereço IP
e gateway (caso origem e destino estiverem em redes separadas), é possível selecionar o provisionamento do ambiente através de máquina
virtual com configuração de tamanho de memória e quantidade
de CPUs virtuais. A opção de provisionamento por contêiner e a
comunicação via gateway são funcionalidades futuras, ainda não implementadas. Por fim, o usuário pode escolher qual modelo de carga
de trabalho ele deseja aplicar, seja sinusoid ou flashcrowd.

## 4 Encerrando a Execução do WAVE
4.1 Finalizando e removendo o ambiente de contêineres:

![image](https://user-images.githubusercontent.com/79940823/227384855-c8aad12e-42c7-464a-ae8d-ff6e1ab004e2.png)

Ao executar o comando acima, o usuário finaliza o módulo WAVE
WEB e remove os contêineres responsáveis pelos demais módulos
iniciados. Para reiniciar todo o sistema basta executar o mesmo
comando, porém, substituindo o argumento –destroy por –start,
como indicado na linha 3 do código na seção 2.1.
