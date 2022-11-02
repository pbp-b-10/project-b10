async function getBlood() {
    return fetch("api/blood/").then((res) => res.json())
  }

  async function refreshBlood() {
        
        document.getElementById("data").innerHTML = ""
        const bloods = await getBlood()
        let htmlString = ''
        bloods.forEach((item) => {
          htmlString += `\n<tr><td> ${item.fields.user}
                          <td> ${item.fields.date} 
                          </td><td> ${item.fields.golongan} 
                          </td><td> ${item.fields.rhesus}
                          </td><td> ${item.fields.penyakit_bawaan} 
                          </td><td> ${item.fields.lokasi_donor}
                          </td><td>  <button id="delete-button" style="font-weight:bold;
                                                                        background-color:#F96666;
                                                                        border: none;
                                                                        text-decoration: none;
                                                                        display: inline-block;"
                                                                        onmouseover="this.style.backgroundColor='#E14D2A';"
                                                                        onmouseout="this.style.backgroundColor='#F96666';"
                                                                        onclick="cancelCloth(${item.pk})"
                                                                        >X</button>
                          </td></tr>`
        })
        document.getElementById("data").innerHTML = htmlString
  }
  
  async function successAfterCancel() {
      refreshClothes()
      document.getElementById("success").innerHTML = ""
      htmlString = `\n<div class="alert alert-primary" role="alert">\n
                      You have canceled a donation\n
                      </div>`
      document.getElementById("success").innerHTML = htmlString
      setInterval(exitSuccess, 2500)
  }

  async function exitSuccess() {
      document.getElementById("success").innerHTML = ""
      htmlString = ``
      document.getElementById("success").innerHTML = htmlString
  }

  async function cancelBlood(id) {
          $.ajax({
              url: `blood/${id}/delete`,
              type: "DELETE",
              success: function() {
                $(`#${id}`).remove();
              }
          }).then(successAfterCancel)
      }

  refreshBlood()