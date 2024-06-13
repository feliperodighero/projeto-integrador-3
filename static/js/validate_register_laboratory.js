function goBack() {
  window.location.href = "/select_user_patient";
}

(function () {
  "use strict";

  const form = document.getElementById("complementos-cards");

  form.addEventListener(
    "submit",
    function (event) {
      // Chama as funções de validação aqui
      const isValidName = validadeLaboratoryName();
      const isValidStreet = validadelaboratoryrua();
      const isValidCnpj = ValidadeLaboratoryCPF();
      const isValidCep = ValidadeLaboratoryCEP();
      const isValidPhone = ValidadeLaboratoryTelefonerror();
      const isValidNumber = validateLaboratoryNumber();
      const isValidNeighborhood = validateLaboratoryNeighborhood();

      if (
        !form.checkValidity() ||
        !isValidName ||
        !isValidStreet ||
        !isValidCnpj ||
        !isValidCep ||
        !isValidPhone ||
        !isValidNumber ||
        !isValidNeighborhood
      ) {
        event.preventDefault();
        event.stopPropagation();
      } else {
        // Permitir o envio do formulário se tudo estiver válido
        form.classList.add("was-validated");
      }
    },
    false
  );
})();

function validadeLaboratoryName() {
  var laboratoryname = document.getElementById("LaboratoryName").value;
  var regex = /^[a-zA-Z\u00C0-\u00FF\s]+$/; // Regex para letras e espaços
  var validadelaboratorynameError = document.getElementById(
    "ValidadeLaboratoryNameError"
  );

  if (!regex.test(laboratoryname)) {
    validadelaboratorynameError.style.display = "block";
    return false;
  } else {
    validadelaboratorynameError.style.display = "none";
    return true;
  }
}

function validadelaboratoryrua() {
  var rua = document.getElementById("LaboratoryStreet").value;
  var regex = /^[a-zA-Z0-9\s]+$/; // Regex para letras e espaços
  var validadelaboratoryruaError = document.getElementById(
    "ValidadeLaboratoryRuaError"
  );

  if (rua === "" || !regex.test(rua)) {
    validadelaboratoryruaError.style.display = "block";
    return false;
  } else {
    validadelaboratoryruaError.style.display = "none";
    return true;
  }
}

function ValidadeLaboratoryCPF() {
  var cnpj = document.getElementById("LaboratoryCnpj").value;
  var regex = /^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/;
  var validadelaboratorycpf = document.getElementById(
    "ValidadeLaboratoryCPFError"
  );

  if (!regex.test(cnpj)) {
    validadelaboratorycpf.style.display = "block";
    return false;
  } else {
    validadelaboratorycpf.style.display = "none";
    return true;
  }
}

function ValidadeLaboratoryCEP() {
  var cep = document.getElementById("LaboratoryCep").value;
  var regex = /^\d{5}-\d{3}$/;
  var validadelaboratorycepError = document.getElementById(
    "ValidadeLaboratoryCEPError"
  );

  if (!regex.test(cep)) {
    validadelaboratorycepError.style.display = "block";
    return false;
  } else {
    validadelaboratorycepError.style.display = "none";
    return true;
  }
}

function ValidadeLaboratoryTelefonerror() {
  var laboratorynumber = document.getElementById("LaboratoryNumberPhone").value;
  var regex = /^\(\d{2}\)\d{5}-\d{4}$/; // Regex para o formato (XX)XXXXX-XXXX
  var laboratorynumberphoneError = document.getElementById(
    "ValidadeLaboratoryTelefoneError"
  );

  if (!regex.test(laboratorynumber)) {
    laboratorynumberphoneError.style.display = "block";
    return false;
  } else {
    laboratorynumberphoneError.style.display = "none";
    return true;
  }
}

function validateLaboratoryNumber() {
  var laboratoryNumber = document.getElementById(
    "LaboratoryNumberAddress"
  ).value;
  var regex = /^[a-zA-Z0-9]+$/; // Regex para letras e números
  var validadelaboratorynumeroError = document.getElementById(
    "ValidadeLaboratoryNumeroError"
  );

  if (!regex.test(laboratoryNumber)) {
    validadelaboratorynumeroError.style.display = "block";
    return false;
  } else {
    validadelaboratorynumeroError.style.display = "none";
    return true;
  }
}

function validateLaboratoryNeighborhood() {
  var laboratoryneighborhood = document.getElementById(
    "LaboratoryNeighborhood"
  ).value;
  var regex = /^[a-zA-Z0-9\s\u00C0-\u017F]+$/; // Regex para letras (incluindo acentuadas), números e espaços
  var validadelaboratoryneighborhoodError = document.getElementById(
    "ValidadeLaboratoryNeighborhoodError"
  );

  if (!laboratoryneighborhood || !regex.test(laboratoryneighborhood)) {
    validadelaboratoryneighborhoodError.style.display = "block";
    return false;
  } else {
    validadelaboratoryneighborhoodError.style.display = "none";
    return true;
  }
}
