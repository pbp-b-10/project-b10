async function getClothes() {
    return fetch("api/cloth").then((res) => res.json())
  }

  async function refreshClothes() {
        
        document.getElementById("data").innerHTML = ""
        const clothes = await getClothes()
        let htmlString = ''
        clothes.forEach((item) => {
          htmlString += `\n<tr><td> ${item.fields.username}
                          <td> ${item.fields.cloth_model} 
                          </td><td> ${item.fields.material} 
                          </td><td> ${item.fields.type}
                          </td><td> ${item.fields.date} 
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

  async function cancelCloth(id) {
          $.ajax({
              url: `cloth/${id}/delete`,
              type: "DELETE",
              success: function() {
                $(`#${id}`).remove();
              }
          }).then(successAfterCancel)
      }

  refreshClothes()