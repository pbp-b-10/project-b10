
$(document).ready(function(){
    $('#id_project').on('change', function() {
        const project = projects.find( o => o.pk == this.value )
        const today = new Date();
        const end_date = new Date(project.fields.akhir_waktu);
        const difference = end_date.getTime() - today.getTime();
        $('#durasi').val(Math.ceil(difference * (1000 * 3600 * 24)))
    });
})
async function successAfterSubmit() {
    document.getElementById("success").innerHTML = ""
    htmlString = `\n<div class="alert alert-success" role="alert">\n
                    {% csrf_token %}
                    \nThank you for your volunteer! <!-- See your donation history <a href="{% url 'pedulee:clothes_history' %}" class="alert-link">here</a> -->\n
                    </div>`
    document.getElementById("success").innerHTML = htmlString
    setInterval(exitSuccess, 3500)
}

function exitSuccess() {
    document.getElementById("success").innerHTML = ""
    htmlString = ``
    document.getElementById("success").innerHTML = htmlString
}

function submitVolunteer() {
    fetch("{% url 'pedulee:create_volunteer' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(successAfterSubmit)
    return false
}

document.getElementById("button-submit").onclick = submitVolunteer
