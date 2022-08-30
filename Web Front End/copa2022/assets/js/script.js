function app(){

    const cx_texto_nome = document.getElementById('input_nome');

    const btn_button = document.getElementById('btn_saudacao');

    btn_button.onclick = () => alert('oi');

    cx_texto_nome.placeholder = 'Digite seu nome';

    botao_saudacao.addEventListener('click', () => {

        const texto_digitado = cx_texto_nome.value



        texto_saudacao.innerText  = texto_digitado
    })

}

app()