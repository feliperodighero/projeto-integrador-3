document.addEventListener('DOMContentLoaded', function () {
    const searchID = document.getElementById('SearchID');
    const searchCnpj = document.getElementById('SearchCnpj');
    const searchName = document.getElementById('SearchName');
    const botaoPesquisar = document.getElementById('botao-edit-laboratory');

    function disableAllFields() {
        searchID.disabled = true;
        searchCnpj.disabled = true;
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

    document.getElementById('search-cnpj').addEventListener('click', function () {
        disableAllFields();
        searchCnpj.disabled = false;
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
