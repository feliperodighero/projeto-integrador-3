document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCpfCnpj = document.getElementById('SearchCpfCnpj');
    const searchName = document.getElementById('SearchName');

    function disableAllFields() {
        searchID.disabled = true;
        searchCpfCnpj.disabled = true;
        searchName.disabled = true;
    }

    document.getElementById('search-id').addEventListener('click', function () {
        disableAllFields();
        searchID.disabled = false;
    });

    document.getElementById('search-cpf').addEventListener('click', function () {
        disableAllFields();
        searchCpfCnpj.disabled = false;
    });

    document.getElementById('search-name').addEventListener('click', function () {
        disableAllFields();
        searchName.disabled = false;
    });

    disableAllFields();
});


document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCpfCnpj = document.getElementById('SearchCpfCnpj');
    const searchName = document.getElementById('SearchName');
    const botaoEditUser = document.getElementById('botao-edit-user');

    function disableAllFields() {
        [searchID, searchCpfCnpj, searchName].forEach(field => {
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

    document.getElementById('search-name').addEventListener('click', function () {
        disableAllFields();
        searchName.disabled = false;
    });

    botaoEditUser.addEventListener('click', function (event) {
        const isValid = searchID.value || searchCpfCnpj.value || searchName.value;
        if (!isValid) {
            event.preventDefault();
            alert('Por favor, preencha um dos campos de busca.');
        }
    });

    disableAllFields();
});