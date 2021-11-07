$(document).ready(function () {
        $('#btn1').click(function () {
            if ($('#dep1').get(0).value === $('#dep2').get(0).value) {
                alert('Выберите разные департаменты!')
                return false
            }
        });
    }
);
$(document).ready(function () {
        table = document.getElementById('tb1')
        for (let i = 2; i < table.rows.length; i++) {
            if (+table.rows[i].cells[1].innerText > +table.rows[i].cells[2].innerText) {
                table.rows[i].cells[1].style = 'background-color: greenyellow;'
            } else if (+table.rows[i].cells[1].innerText < +table.rows[i].cells[2].innerText) {
                table.rows[i].cells[2].style = 'background-color: greenyellow;'
            }
        }
    }
);