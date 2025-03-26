function delete_conceito_fe(designacao) {
    $.ajax(`/conceitos/${designacao}`, {
        type: "DELETE",
        success: function(data) {
            console.log(data)
            if (data["success"]) {
                window.location.href = data["redirect_url"];
            }
        },
        error: function(error) {
            console.log(error);
        }
    })
}

$(document).ready(() => {
    $('#tabela_conceitos').DataTable({
        search: {
            regex: true
        },
        language: {
            "url": "https://cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Portuguese.json"
        }
    });
});
