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
    const botaoPesquisar = document.getElementById('botao-edit-patient');

    function disableAllFields() {
        searchID.disabled = true;
        searchCpfCnpj.disabled = true;
        searchName.disabled = true;
    }

    function enableAllFields() {
        const allFields = document.querySelectorAll('.form-control');
        allFields.forEach(field => field.disabled = false);
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

    botaoPesquisar.addEventListener('click', function () {
        enableAllFields();
    });

    disableAllFields();
});
