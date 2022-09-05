function pulaLinha(){
    document.write("<br>");
}

function mostra(frase){

    document.write(frase);
    pulaLinha();
}


var numeroPensado = Math.round(Math.random()*10);
var tentativas = 1;
var acertou = false;

while (tentativas <= 3){

    var chute = parseInt(prompt("Qual seu chute? "));

    if (chute == numeroPensado){
        mostra("Acertou mizeravi, o número era "+ numeroPensado);
        acertou = true;

        break;
    }

    tentativas++;
}

if(acertou == false) {
    mostra("Errou, o número pensado era "+numeroPensado);
}

mostra("FIM");