async function getGroceries() {
    return fetch("api/groceries").then((res) => res.json())
  }

  async function refreshGroceries() {
        
        document.getElementById("data").innerHTML = ""
        const groceries = await getGroceries()
        let htmlString = ''
        groceries.forEach((item) => {
          htmlString += `\n<tr>`
          if (user === 'staff') {
            htmlString += `<td> ${item.fields.username}`
          }
          htmlString += `<td> ${item.fields.donasi} 
                          </td><td> ${item.fields.sembako} 
                          </td><td> ${item.fields.amount}
                          </td><td> ${item.fields.date} 
                          </td><td>  <button id="delete-button" style="font-weight:bold;
                                                                        background-color:#F96666;
                                                                        border: none;
                                                                        text-decoration: none;
                                                                        display: inline-block;"
                                                                        onmouseover="this.style.backgroundColor='#E14D2A';"
                                                                        onmouseout="this.style.backgroundColor='#F96666';"
                                                                        onclick="cancelGroceries(${item.pk})"
                                                                        >X</button>
                          </td></tr>`
        })
        document.getElementById("data").innerHTML = htmlString
  }
  
  async function successAfterCancel() {
      refreshGroceries()
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

  async function cancelGroceries(id) {
          $.ajax({
              url: `groceries/${id}/delete`,
              type: "DELETE",
              success: function() {
                $(`#${id}`).remove();
              }
          }).then(successAfterCancel)
      }

  refreshGroceries()