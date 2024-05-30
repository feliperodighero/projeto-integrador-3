document.getElementById("botaoPesquisarOS").addEventListener("click", function() {
    var orderCode = document.getElementById("listaCodigoOS").value;
    var patientName = document.getElementById("ListaNomePacienteOS").value;
    var orderDate = document.getElementById("ListaDateOS").value;

    var data = {
        OrderCode: orderCode,
        PatientName: patientName,
        OrderDate: orderDate
    };

    fetch("/search_orders", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        var tableBody = document.getElementById("tabela-ordem-servico-info");
        tableBody.innerHTML = ""; // Limpar tabela

        if (data.orders && data.orders.length > 0) {
            data.orders.forEach(order => {
                var row = document.createElement("tr");

                var orderCodeCell = document.createElement("th");
                orderCodeCell.scope = "row";
                orderCodeCell.textContent = order.order_code;
                row.appendChild(orderCodeCell);

                var patientNameCell = document.createElement("td");
                patientNameCell.textContent = order.patient_name;
                row.appendChild(patientNameCell);

                var orderDateCell = document.createElement("td");
                orderDateCell.textContent = order.order_date;
                row.appendChild(orderDateCell);

                var actionsCell = document.createElement("td");
                var viewButton = document.createElement("button");
                viewButton.className = "btn btn-secondary";
                viewButton.textContent = "Visualizar";
                viewButton.setAttribute("data-bs-toggle", "modal");
                viewButton.setAttribute("data-bs-target", "#visualizarModal");
                actionsCell.appendChild(viewButton);
                row.appendChild(actionsCell);

                tableBody.appendChild(row);
            });
        } else {
            var row = document.createElement("tr");
            var noResultsCell = document.createElement("td");
            noResultsCell.colSpan = 4;
            noResultsCell.textContent = "Nenhum resultado encontrado.";
            row.appendChild(noResultsCell);
            tableBody.appendChild(row);
        }
    })
    .catch(error => {
        console.error("Error fetching orders:", error);
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.btn-visualizar').forEach(button => {
        button.addEventListener('click', function () {
            const orderCode = this.getAttribute('data-order-code');

            fetch(`/order_details/${orderCode}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert('Erro ao buscar os detalhes do pedido.');
                    } else {
                        document.getElementById('pedido-codigo').textContent = `Código do Pedido: ${data.order_code}`;
                        document.getElementById('laboratorio-codigo').textContent = `Código do Laboratório: ${data.lab_code}`;
                        document.getElementById('laboratorio-nome').textContent = `Nome do Laboratório: ${data.lab_name}`;
                        document.getElementById('usuario-codigo').textContent = `Código do Usuário: ${data.user_code}`;
                        document.getElementById('usuario-nome').textContent = `Nome do Usuário: ${data.user_name}`;
                        document.getElementById('cliente-codigo').textContent = `Código do Cliente: ${data.client_code}`;
                        document.getElementById('cliente-nome').textContent = `Nome do Cliente: ${data.client_name}`;
                        document.getElementById('data-solicitacao').textContent = `Data da Solicitação: ${data.order_date}`;
                        document.getElementById('itens-pedido').textContent = `Itens do Pedido: ${data.items.map(item => item.product_name).join(', ')}`;
                        document.getElementById('valor-total').textContent = `Valor Total R$: ${data.total_value}`;
                        document.getElementById('status-pedido').textContent = `Status do Pedido: ${data.order_status}`;
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Erro ao buscar os detalhes do pedido.');
                });
        });
    });
});
