
$(document).ready(function () {
    var person = "<i class='fa fa-cat'></i>";
    var wall = "<i class='fa fa-chess-board'></i>";
    var door = "<i class='fa fa-archway'></i>";
    var start = "<i class='fa fa-align-justify'></i>";
    var tamanhoMuro = 51;
    var arrayMuro = [];
    var posicaoPessoa = 0;
    var posicaoPorta = 0;
    var contador = 0;
    var inicioExecucao = null;

    gerarTelaAutomática();

    $("#reset").click(
        function () {
            location.reload();
        }
    );

    $("#executarQua").click(
        function () {
            resetar();
            var posicao = encontrarPortaQuadratico(posicaoPessoa, posicaoPessoa + 1, 1);
            mensagemPosicao(posicao);
        }
    );

    $("#executarLin").click(
        function () {
            resetar();
            var posicao = encontrarPortaLinear(posicaoPessoa, posicaoPessoa + 1, 1);
            mensagemPosicao(posicao);
        }
    );

    function resetar() {
        posicaoPessoa = Math.floor(tamanhoMuro / 2);
        contador = 0;
        $("#movements").html('');
        inicioExecucao = new Date();
    }

    function mensagemPosicao(posicao) {
        if (posicao == null) {
            alert("Porta não encontrada");
        } else {
            alert("Porta encontrada em: posição: " + posicao + ", passos: " + contador + ", distancia: " + Math.abs(Math.floor(tamanhoMuro / 2) - posicao) + ", tempo de execução: " + obterTempoExecucao() + "ms");
        }
    }

    function obterTempoExecucao() {
        return difference = (new Date() - inicioExecucao);
    }

    function gerarTelaAutomática() {
        posicaoPessoa = Math.floor(tamanhoMuro / 2);
        posicaoPorta = posicaoPessoa;

        while (posicaoPorta == posicaoPessoa) {
            posicaoPorta = Math.floor(Math.random() * (tamanhoMuro - 1));;
        }

        for (let index = 0; index < tamanhoMuro; index++) {
            if (posicaoPorta == index) {
                arrayMuro.push(1);
            } else {
                arrayMuro.push(0);
            }
        }

        var stringMuro = obterTelaAtual();

        $("#screen").html(stringMuro);
    }

    function obterTelaAtual() {
        let stringMuro = '';
        for (let index = 0; index < arrayMuro.length; index++) {
            const element = arrayMuro[index];
            if (index == posicaoPessoa) {
                stringMuro += person;
            } else if (element == 1) {
                stringMuro += door;
            } else if (index == Math.floor(tamanhoMuro / 2)) {
                stringMuro += start;
            } else {
                stringMuro += wall;
            }
        }
        return stringMuro;
    }

    function imprimirPosicaoAtual() {
        $("#movements").html($("#movements").html() + "<div class='padding-muro'></div>" + obterTelaAtual() + contador++);
    }

    function encontrarPortaQuadratico(inicio, reach, distancia) {
        posicaoPessoa = inicio;
        imprimirPosicaoAtual();
        if (arrayMuro[inicio] == 1) { // sucesso
            return inicio;
        } else if (inicio == 0) { // simular limite infinito do muro
            reach = arrayMuro.length;
        } else if (inicio == arrayMuro.length) {
            reach = 0;
        }

        if (inicio == reach) {
            distancia += 1;
            if (reach > Math.floor(tamanhoMuro / 2)) {
                reach -= distancia;
            } else {
                reach += distancia;
            }
        }

        var n = reach > inicio ? 1 : -1;

        return encontrarPortaQuadratico(inicio + n, reach, distancia);
    }

    function encontrarPortaLinear(inicio, reach, distancia) {
        posicaoPessoa = inicio;
        imprimirPosicaoAtual();
        if (arrayMuro[inicio] == 1) { // sucesso
            return inicio;
        } else if (inicio == 0) { // simular limite infinito do muro
            reach = arrayMuro.length;
        } else if (inicio == arrayMuro.length) {
            reach = 0;
        }

        if (inicio == reach) {
            distancia *= 2;
            if (reach > Math.floor(tamanhoMuro / 2)) {
                reach -= distancia;
            } else {
                reach += distancia;
            }
        }

        var n = reach > inicio ? 1 : -1;

        return encontrarPortaLinear(inicio + n, reach, distancia);
    }
})