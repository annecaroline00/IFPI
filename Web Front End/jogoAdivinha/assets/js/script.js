function app() {

    let numero_secreto = Math.trunc(Math.random() * 100) + 1;
    const campo_palpite = document.getElementById('campo_numero');
    const btn_palpite = document.getElementById('btn_palpite');

    const palpites = document.getElementById('palpites');
    const erro = document.getElementById('erro');
    const acerto = document.getElementById('acerto');

    const dica = document.getElementById('dica');

    esconder(erro);
    esconder(acerto);
    esconder(dica);
    esconder(palpites);

    btn_palpite.addEventListener('click', (event) => {

        event.preventDefault()

        const palpite = Number(campo_palpite.value)
        palpites++
        
        esconder(dica)
        esconder(erro)
        esconder(acerto)

        if (palpite === 1) {
            mostrar(palpite)
            
        }

        palpites.innerText += " " + palpites

        if (palpite == numero_secreto) {
            mostrar(acerto)
        } else {
            mostrar(erro)

            if (palpites == 10){
                erro.innerText = "!!FIM DE JOGO!!"
            } else {
                if (palpites < numero_secreto) {
                    dica.innerText = 'Seu palpite está muito baixo!'
                } else {
                    dica.innerText = 'Seu palpite está muito alto!'
                }

                mostrar(dica)
            }
        }
        
    })
}

function mostrar(elemento) {
    elemento.classList.add('visivel');
    elemento.classList.remove('invisivel');
}

function esconder(elemento) {
    elemento.classList.remove('visivel');
    elemento.classList.add('invisivel');
}