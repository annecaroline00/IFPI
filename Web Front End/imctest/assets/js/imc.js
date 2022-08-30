function imc () {
    var alt_var_tmp = document.f_imc.f_alt.value;
    var pes_var_tmp = document.f_imc.f_pes.value;

    if ((alt_var == 0) || (pes_var == 0)) {
        alert ("Digite o peso ou altura");

    } else {
            var alt_var = alt_var_tmp.replace ("," , ".");
            var pes_var = pes_var_tmp.replace ("," , ".");

            var vimc = (pes_var_tmp/ Math.pow (alt_var_tmp,2)).toFixed (1);
            alert ("O IMC é" + vimc);
    }
}

imc ();