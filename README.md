# Servidores

Programa para rotinas automatizadas e de alta escalabilidade para auxílio de 
implementações e manutenções de servidores clientes

## Para começar

Essas instruções fornecerão uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste. Consulte implantação para obter notas sobre como implantar o projeto em um sistema ativo.

### Pré-requisitos

Inicie instalando as dependencias necessárias

```
cd documentation/
python setup.py install
```

## Exemploes de utilização

* [Sh3ScriptExecutarComandos](http://192.168.0.193/jonathanscheibel/servidores/blob/master/examples/Sh3ScriptExecutarComandos.py) - Executar comandos com retorno em servidores


### Executar comandos com retorno em servidores:

Para execução de diversos comandos e capturar o retorno dos mesmos você poderá
utilizar o exemplo abaixo:

```
cd examples/
python Sh3ScriptExecutarComandos.py 'uname -a' 
```