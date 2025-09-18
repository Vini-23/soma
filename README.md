# Soma
Esse projeto é pra ser algo simples, apenas com uma interface que possui 3 campos onde a pessoa coloca dois números e a operação. A ideia aqui é explorar melhor pacotes em python, como logging, tratamento de erros, utilização do flask, criação de testes CI/CD e volumes do Docker.

## Funcionalidades
O projeto vai ser baseado em flask, contando com uma página em HTML que vai possuir 3 campos. Dois que estão abertos para o usuário digitar um número e um que é de seleção, onde o usuário deve escolher qual operação matemática ele deseja.
O projeto contará com um arquivo de validação das funções, garantindo que, para cada alteração que for feita, esse arquivo irá validar todas as funções antes do deploy.
Ele também contará com um arquivo de logging que vai salvar as informações, permitindo a rastreabilidade das ações executadas e auxílio no debbug do código.
O código vai ser executado via docker, então também terá que ser mapeado os volumes para os dados do logging serem salvos localmente.