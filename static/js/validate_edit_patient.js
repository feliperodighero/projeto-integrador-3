document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCpfCnpj = document.getElementById('SearchCpfCnpj');


    function disableAllFields() {
        searchID.disabled = true;
        searchCpfCnpj.disabled = true;

    }

    document.getElementById('search-id').addEventListener('click', function () {
        disableAllFields();
        searchID.disabled = false;
    });

    document.getElementById('search-cpf').addEventListener('click', function () {
        disableAllFields();
        searchCpfCnpj.disabled = false;
    });


    disableAllFields();
});


document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCpfCnpj = document.getElementById('SearchCpfCnpj');
    const botaoEditUser = document.getElementById('botao-edit-user');

    function disableAllFields() {
        [searchID, searchCpfCnpj].forEach(field => {
            field.disabled = true;
            field.value = '';
        });
    }

    function enableFormFields() {
        document.querySelectorAll('#editForm input').forEach(input => input.disabled = false);
    }

    document.getElementById('search-id').addEventListener('click', function () {
        disableAllFields();
        searchID.disabled = false;
    });

    document.getElementById('search-cpf-cnpj').addEventListener('click', function () {
        disableAllFields();
        searchCpfCnpj.disabled = false;
    });


    botaoEditUser.addEventListener('click', function (event) {
        const isValid = searchID.value || searchCpfCnpj.value;
        if (!isValid) {
            event.preventDefault();
            alert('Por favor, preencha um dos campos de busca.');
        }
    });

    disableAllFields();
});