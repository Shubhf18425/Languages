const insert = document.getElementById('insert')

window.addEventListener('keydown', (event) => {
    insert.innerHTML = 
    `
    <div class = 'color'>
    <table>
  <tr>
    <th>Key</th>
    <th>KeyCode</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>${event.key}</td>
    <td>${event.keycode}</td>
    <td>${event.code}</td>
  </tr>
  
</table>
    </div>
    `
})