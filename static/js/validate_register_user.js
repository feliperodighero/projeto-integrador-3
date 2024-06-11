(() => {
  "use strict";

  const forms = document.querySelectorAll(".needs-validation");

  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();

function goBack() {
  window.location.href = "/select_user_patient";
}

function validateUsername() {
  var username = document.getElementById("UserName").value;
  var regex = /^[a-zA-Z\u00C0-\u00FF]+$/; // Regex para letras
  var usernameError = document.getElementById("usernameError");

  if (!regex.test(username)) {
    usernameError.style.display = "block";
    return false;
  } else {
    usernameError.style.display = "none";
    return true;
  }
}

function validatePassword() {
  var password = document.getElementById("UserPassword").value;
  var confirmPassword = document.getElementById("UserConfirmPassword").value;

  if (password != confirmPassword) {
    alert("As senhas não coincidem. Por favor, insira novamente.");
    return false;
  }
  return true;
}

function validateCPF() {
  var cpf = document.getElementById("UserCpf").value;
  var regex = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/; // Regex para o formato XXX.XXX.XXX-XX
  var cpfError = document.getElementById("CPFError");

  if (!regex.test(cpf)) {
    cpfError.style.display = "block";
    return false;
  } else {
    cpfError.style.display = "none";
    return true;
  }
}

function validatePhoneNumber() {
  var phoneNumber = document.getElementById("UserNumberPhone").value;
  var regex = /^\(\d{2}\)\d{5}-\d{4}$/; // Regex para o formato (XX)XXXXX-XXXX
  var phonenumberError = document.getElementById("NumberPhoneError");

  if (!regex.test(phoneNumber)) {
    phonenumberError.style.display = "block";
    return false;
  } else {
    phonenumberError.style.display = "none";
    return true;
  }
}

function validateBirthDate() {
  var birthDateInput = document.getElementById("UserDateBirth");
  var birthDateValue = birthDateInput.value;
  var datanascError = document.getElementById("DataNascError");

  if (!birthDateValue) {
    datanascError.style.display = "block";
    return false;
  }

  var birthDate = new Date(birthDateValue);
  var today = new Date();
  var age = today.getFullYear() - birthDate.getFullYear();
  var m = today.getMonth() - birthDate.getMonth();

  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }

  if (birthDate > today) {
    datanascError.style.display = "block";
    return false;
  } else if (age < 16) {
    alert("O usuário deve ter pelo menos 16 anos.");
    return false;
  } else {
    datanascError.style.display = "none";
    return true;
  }
}

function validateCRM() {
  var crm = document.getElementById("UserCrm").value;
  var cargo = document.getElementById("inlineFormCustomSelect").value;
  var crmError = document.getElementById("CRMError");

  // Verifica se o cargo é Secretário(a) e permite "N/A" para o CRM
  if (cargo == "2" && crm === "N/A") {
    crmError.style.display = "none";
    return true;
  }

  // Regex para exatamente 6 números
  var regex = /^\d{6}$/;

  if (!regex.test(crm)) {
    crmError.style.display = "block";
    return false;
  } else {
    crmError.style.display = "none";
    return true;
  }
}

function validateCargo() {
  var cargo = document.getElementById("inlineFormCustomSelect").value;
  var cargoError = document.getElementById("CargoError");

  if (cargo != "1" && cargo != "2") {
    cargoError.style.display = "block";
    return false;
  } else {
    cargoError.style.display = "none";
    return true;
  }
}

function validateStreet() {
  var street = document.getElementById("UserStreet").value;
  var regex = /^[a-zA-Z0-9\s]+$/; // Regex para letras e espaços
  var streetError = document.getElementById("StreetError");

  if (street === "" || !regex.test(street)) {
    streetError.style.display = "block";
    return false;
  } else {
    streetError.style.display = "none";
    return true;
  }
}

function validateHouseNumber() {
  var houseNumber = document.getElementById("UserNumberHouse").value;
  var regex = /^[a-zA-Z0-9]+$/; // Regex para letras e números
  var numberError = document.getElementById("NumberError");

  if (!regex.test(houseNumber)) {
    numberError.style.display = "block";
    return false;
  } else {
    numberError, (style.display = "none");
    return true;
  }
}

function validateNeighborhood() {
  var neighborhood = document.getElementById("UserNeighborhood").value;
  var regex = /^[a-zA-Z0-9\s\u00C0-\u017F]+$/; // Regex para letras (incluindo acentuadas), números e espaços
  var neighborhoodError = document.getElementById("NeighborhoodError");

  if (!neighborhood || !regex.test(neighborhood)) {
    neighborhoodError.style.display = "block";
    return false;
  } else {
    neighborhoodError.style.display = "none";
    return true;
  }
}
